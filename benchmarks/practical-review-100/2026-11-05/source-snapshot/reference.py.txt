"""Trusted offline oracle. Never imported during actor execution."""
import copy,itertools
def solve(f,a):
 if f=='receivables':
  paid={x['id']:sum(p['amount'] for p in a['payments'] if p['invoice_id']==x['id'] and p['status']=='SETTLED') for x in a['invoices']};details=[]
  for x in sorted(a['invoices'],key=lambda x:x['id']):
   p=paid[x['id']];b=0 if x['cancelled'] else max(x['amount']-p,0);c=0 if x['cancelled'] else max(p-x['amount'],0)
   s='CANCELLED' if x['cancelled'] else 'PAID' if not b else 'OVERDUE' if x['due_day']<a['as_of_day'] else 'OPEN';d=a['as_of_day']-x['due_day'] if s=='OVERDUE' else 0
   act=('ESCALATE' if b>=a['threshold_balance'] or d>=a['threshold_days'] else 'REMIND') if s=='OVERDUE' else 'NONE'
   details.append({'id':x['id'],'paid':p,'balance':b,'credit':c,'state':s,'days_overdue':d,'action':act})
  def sums(rr):return {'balance':sum(x['balance'] for x in rr),'credit':sum(x['credit'] for x in rr),'overdue_count':sum(x['state']=='OVERDUE' for x in rr)}
  by={x['id']:x['team'] for x in a['invoices']};teams=[{'team':t,**sums([x for x in details if by[x['id']]==t])} for t in ['T1','T2','T3']]
  return {'details':details,'teams':teams,'queue':[x['id'] for x in sorted([x for x in details if x['state']=='OVERDUE'],key=lambda x:(-x['days_overdue'],-x['balance'],x['id']))],'totals':sums(details)}
 if f=='allocation':
  remaining={x['sku']:x['units'] for x in a['stocks']};reserve={x['sku']:x['reserve'] for x in a['stocks']};dd={x['id']:{'id':x['id'],'allocated':0,'backorder':0,'value':0,'state':'EXCLUDED'} for x in a['orders']}
  active=sorted([x for x in a['orders'] if not x['cancelled'] and x['due_day']<=a['as_of_day']],key=lambda x:(x['priority'],x['due_day'],x['id']))
  for x in active:
   q=min(x['units'],max(remaining[x['sku']]-reserve[x['sku']],0))//x['lot']*x['lot'];b=x['units']-q;remaining[x['sku']]-=q;dd[x['id']]={'id':x['id'],'allocated':q,'backorder':b,'value':q*100,'state':'FULFILLED' if not b else 'BACKORDER' if not q else 'PARTIAL'}
  d=[dd[k] for k in sorted(dd)];return {'details':d,'processing_order':[x['id'] for x in active],'stocks':[{'sku':k,'remaining':remaining[k]} for k in sorted(remaining)],'totals':{k:sum(x[k] for x in d) for k in ['allocated','backorder','value']}}
 if f=='service_queue':
  d=[];by={x['id']:x['team'] for x in a['tickets']}
  for x in sorted(a['tickets'],key=lambda x:x['id']):
   end=x['opened']+a['sla'][x['priority']]+x['paused'];s='EXCLUDED' if x['status']!='OPEN' or x['opened']>a['as_of_minute'] else 'BREACHED' if end<a['as_of_minute'] else 'DUE_SOON' if end-a['as_of_minute']<=a['window'] else 'ON_TRACK';o=a['as_of_minute']-end if s=='BREACHED' else 0;act='ESCALATE' if s=='BREACHED' and (x['priority']=='P1' or o>=480) else 'CONTACT' if s in ['BREACHED','DUE_SOON'] else 'NONE';d.append({'id':x['id'],'deadline':end,'state':s,'overdue':o,'action':act})
  teams=[]
  for t in ['T1','T2','T3']:
   rr=[x for x in d if by[x['id']]==t];teams.append({'team':t,'active':sum(x['state']!='EXCLUDED' for x in rr),'breached':sum(x['state']=='BREACHED' for x in rr),'due_soon':sum(x['state']=='DUE_SOON' for x in rr),'escalated':sum(x['action']=='ESCALATE' for x in rr)})
  return {'details':d,'teams':teams,'queue':[x['id'] for x in sorted([x for x in d if x['action']!='NONE'],key=lambda x:(0 if x['action']=='ESCALATE' else 1,x['deadline'],x['id']))]}
 if f=='expenses':
  budgets={x['employee']:x['remaining'] for x in a['budgets']};seen=set();d=[];order=sorted(a['claims'],key=lambda x:(x['day'],x['id']))
  for x in order:
   q=0
   if x['receipt_id'] in seen:s='DUPLICATE'
   elif x['cancelled']:s='CANCELLED'
   elif not x['receipt_ok']:s='NO_RECEIPT'
   else:q=min(x['amount'],a['category_caps'][x['category']],budgets[x['employee']]);budgets[x['employee']]-=q;s='FULL' if q==x['amount'] else 'NO_BUDGET' if not q else 'PARTIAL'
   seen.add(x['receipt_id']);d.append({'id':x['id'],'approved':q,'state':s})
  return {'details':sorted(d,key=lambda x:x['id']),'processing_order':[x['id'] for x in order],'budgets':[{'employee':k,'remaining':budgets[k]} for k in sorted(budgets)],'total_approved':sum(x['approved'] for x in d)}
 if f=='sales':
  d=[];by={x['id']:x['team'] for x in a['sales']}
  for x in sorted(a['sales'],key=lambda x:x['id']):
   ex=x['cancelled'] or x['day']>a['as_of_day'];net=0 if ex else max(x['qty']*x['price']-x['discount']-x['refund'],0);tax=(net*x['tax_bps']+5000)//10000;d.append({'id':x['id'],'net':net,'tax':tax,'gross':net+tax,'state':'EXCLUDED' if ex else 'INCLUDED'})
  teams=[]
  for t in sorted(a['targets'],key=lambda x:x['team']):
   sums={k:sum(x[k] for x in d if by[x['id']]==t['team']) for k in ['net','tax','gross']};teams.append({'team':t['team'],**sums,'gap':max(t['target']-sums['net'],0)})
  return {'details':d,'teams':teams,'unmet':[x['team'] for x in sorted([x for x in teams if x['gap']>0],key=lambda x:(-x['gap'],x['team']))],'totals':{k:sum(x[k] for x in d) for k in ['net','tax','gross']}}
 if f=='deduplication':
  groups={}
  for x in a['records']:
   key=x['email'].strip().lower();seen=set()
   while key in a['aliases']:assert key not in seen;seen.add(key);key=a['aliases'][key]
   groups.setdefault(key,[]).append(x)
  d=[]
  for key,rr in sorted(groups.items()):
   winner=sorted(rr,key=lambda x:(not x['active'],-x['updated'],x['id']))[0];d.append({'email':key,'representative_id':winner['id'],'name':winner['name'],'source_ids':sorted(x['id'] for x in rr),'balance':sum(x['balance'] for x in rr if x['active'])})
  return {'customers':d,'total_active_balance':sum(x['balance'] for x in d)}
 if f=='document_edits':
  texts={x['id']:x['text'] for x in a['sections']};protected={x['id']:x['protected'] for x in a['sections']};outcomes=[]
  for x in sorted(a['updates'],key=lambda x:x['id']):
   key=x['section_id'];state='UNKNOWN_SECTION' if key not in texts else 'PROTECTED' if protected[key] else 'OLD_NOT_UNIQUE' if texts[key].count(x['old'])!=1 else 'APPLIED'
   if state=='APPLIED':texts[key]=texts[key].replace(x['old'],x['new'],1)
   outcomes.append({'id':x['id'],'state':state})
  return {'sections':[{'id':x['id'],'text':texts[x['id']]} for x in a['sections']],'outcomes':outcomes,'applied_ids':[x['id'] for x in outcomes if x['state']=='APPLIED']}
 if f=='dependency_schedule':
  tasks={x['id']:x for x in a['tasks']};done={};teams={};order=[]
  while len(done)<len(tasks):
   ready=[x for x in tasks.values() if x['id'] not in done and all(p in done for p in x['deps'])];assert ready
   x=min(ready,key=lambda x:(x['priority'],x['due'],x['id']));start=max([x['release'],teams.get(x['team'],0)]+[done[p]['end'] for p in x['deps']]);end=start+x['duration'];done[x['id']]={'id':x['id'],'start':start,'end':end,'late':max(end-x['due'],0)};teams[x['team']]=end;order.append(x['id'])
  d=[done[k] for k in sorted(done)];return {'details':d,'processing_order':order,'makespan':max(x['end'] for x in d),'total_late':sum(x['late'] for x in d)}
 if f=='procurement':
  items=sorted(a['items'],key=lambda x:x['id']);best=None;bestq=None
  for q in itertools.product(*(range(x['max_qty']+1) for x in items)):
   used={x['vendor'] for x,v in zip(items,q) if v};cost=sum(x['price']*v for x,v in zip(items,q))+sum(a['vendor_fees'][v] for v in used)
   if cost>a['budget']:continue
   utility=sum(x['utility']*v for x,v in zip(items,q));key=(utility,-cost,q)
   if best is None or key>best:best=key;bestq=q
  assert best is not None
  used={x['vendor'] for x,v in zip(items,bestq) if v};return {'quantities':[{'id':x['id'],'qty':v} for x,v in zip(items,bestq)],'vendors':[{'vendor':v,'fee':fee if v in used else 0} for v,fee in sorted(a['vendor_fees'].items())],'totals':{'cost':-best[1],'utility':best[0],'remaining_budget':a['budget']+best[1]}}
 if f=='availability':
  # Discrete integer-minute occupancy is an independent representation of interval arithmetic.
  free=set(range(1440))
  for person in a['people']:
   occupied=set()
   for start,end in person['local_windows']:occupied.update(range(max(0,start-person['utc_offset']),min(1440,end-person['utc_offset'])))
   free.intersection_update(occupied)
  for start,end in a['blackouts']:free.difference_update(range(start,end))
  windows=[];k=0
  while k<1440:
   if k not in free:k+=1;continue
   end=k+1
   while end in free:end+=1
   if k+a['buffer']<end-a['buffer']:windows.append({'start':k+a['buffer'],'end':end-a['buffer']})
   k=end
  starts=[k for k in range(0,1440,a['grid']) if any(x['start']<=k and k+a['duration']<=x['end'] for x in windows)]
  return {'free_windows':windows,'eligible_starts':starts,'selected_start':starts[0] if starts else -1}
 raise ValueError(f)
def corrupt(f,gold):
 v=copy.deepcopy(gold)
 if f=='receivables':v['details'][-1]['paid']+=100
 elif f=='allocation':
  if len(v['processing_order'])>1:v['processing_order'][0],v['processing_order'][1]=v['processing_order'][1],v['processing_order'][0]
  else:v['details'][-1]['allocated']+=1
 elif f=='service_queue':v['details'][-1]['deadline']+=1
 elif f=='expenses':v['total_approved']+=100
 elif f=='sales':v['totals']['net']+=100
 elif f=='deduplication':v['customers'][0]['representative_id']='R999'
 elif f=='document_edits':v['sections'][0]['text']+='（誤更新）'
 elif f=='dependency_schedule':v['details'][-1]['start']+=1
 elif f=='procurement':
  for x in v['quantities']:x['qty']=0
  for x in v['vendors']:x['fee']=0
  v['totals']={'cost':0,'utility':0,'remaining_budget':gold['totals']['cost']+gold['totals']['remaining_budget']}
 elif f=='availability':
  if v['eligible_starts']:v['eligible_starts']=v['eligible_starts'][1:];v['selected_start']=v['eligible_starts'][0] if v['eligible_starts'] else -1
  else:v['selected_start']=0
 assert v!=gold
 return v
