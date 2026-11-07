"""Public routing and atomic before/after patches. No private scoring imports."""
import copy,json
from protocol import equal,check_schema,parse

ARMS=['SOL_CONTINUE','PRACTICAL']
PROMPT='依頼と元資料に照らし、使えるならACCEPTだけ返す。利用に支障のある誤りがあれば、箇所と影響を短く示し、直せるなら差分だけ返す。依頼にない要件・表現改善・採点表は追加しない。'
FORMATS={
 'ACCEPT':{'decision':'ACCEPT'},
 'PATCH':{'decision':'PATCH','changes':[{'path':'JSON Pointer','before':'変更前のJSON値','after':'変更後のJSON値'}],'impact':'利用への影響'},
 'REWORK':{'decision':'REWORK','scope':'再計算等が必要な範囲','impact':'利用への影響'},
 'NEED_INPUT':{'decision':'NEED_INPUT','question':'不足している重要情報'}
}

def profile_for(family,a):
 if family in ['dependency_schedule','procurement']:return 'complex','high'
 if family=='allocation' and (any(x['lot']>1 for x in a['orders']) or any(x['reserve'] for x in a['stocks'])):return 'complex','high'
 if family=='availability':
  if a['buffer'] or a['blackouts'] or any(x['utc_offset'] for x in a['people']):return 'complex','high'
  return 'small','low'
 rows=max([len(v) for v in a.values() if isinstance(v,list)]+[0])
 if rows<=2 or family=='document_edits' and len(a['updates'])<=5:return 'small','low'
 return 'normal','medium'

def review_packet(t,candidate,feedback=None):
 p={'instruction':PROMPT,'public_conversation_verbatim':t,'candidate':candidate,'response_format':'指定例の該当する1種類のJSONだけ。PATCHのbefore/afterは実際のJSON値。関連する集計・報告文の修正も含める。','formats':FORMATS}
 if feedback is not None:p['targeted_resolution']={'issue':feedback,'limit':'今回の修正1回だけ。必要範囲を元条件で再計算し、PATCHまたはACCEPT。未解決ならREWORK/NEED_INPUT。'}
 return p

def valid_review(v):
 if not isinstance(v,dict):return False
 d=v.get('decision');required={
  'ACCEPT':{'decision'},'PATCH':{'decision','changes','impact'},
  'REWORK':{'decision','scope','impact'},'NEED_INPUT':{'decision','question'}}
 if d not in required or set(v)!=required[d]:return False
 for k in ['impact','scope','question']:
  if k in v and (not isinstance(v[k],str) or not v[k].strip()):return False
 if d=='PATCH':
  if not isinstance(v['changes'],list) or not 1<=len(v['changes'])<=100:return False
  for x in v['changes']:
   if not isinstance(x,dict) or set(x)!={'path','before','after'} or not isinstance(x['path'],str) or not x['path'].startswith('/'):return False
 return True

def apply_patch(candidate,changes,schema):
 # Atomic application; failed before-values never modify the candidate.
 v=copy.deepcopy(candidate);seen=set()
 for c in changes:
  path=c['path'];assert path.startswith('/') and path not in seen,'Invalid or duplicate patch target'
  assert all(not path.startswith(x+'/') and not x.startswith(path+'/') for x in seen),'Overlapping patch targets'
  seen.add(path)
  parts=path[1:].split('/');parts=[x.replace('~1','/').replace('~0','~') for x in parts]
  parent=v
  for key in parts[:-1]:
   assert not isinstance(parent,list) or key.isdigit() and str(int(key))==key,'Invalid array index'
   parent=parent[int(key)] if isinstance(parent,list) else parent[key]
  key=parts[-1]
  if isinstance(parent,list):
   assert key.isdigit() and str(int(key))==key,'Invalid array index';key=int(key)
  assert equal(parent[key],c['before']),'Patch before-value mismatch'
  parent[key]=copy.deepcopy(c['after'])
 check_schema(v,schema);assert v.get('report_md','').strip(),'Empty report'
 return v

def public_errors(j,v):
 try:check_schema(v,j['output_schema']);assert v['report_md'].strip();return []
 except (AssertionError,TypeError,ValueError,KeyError):return ['PUBLIC_SHAPE_OR_EMPTY_REPORT']

def parse_review(text):
 try:
  v=parse(text);assert valid_review(v);return v,None
 except (ValueError,TypeError,AssertionError):return None,'REVIEW_CONTRACT_FAILURE'
