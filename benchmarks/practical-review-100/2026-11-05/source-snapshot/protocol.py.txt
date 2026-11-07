"""Public schema and strict JSON helpers only; no expected outputs."""
import json
def parse(text):
 def unique(pairs):
  d={}
  for k,v in pairs:
   if k in d:raise ValueError('Duplicate JSON key')
   d[k]=v
  return d
 return json.loads(text,object_pairs_hook=unique,parse_constant=lambda _:(_ for _ in ()).throw(ValueError('Nonfinite')))
def equal(a,b):
 if type(a)!=type(b):return False
 if isinstance(a,dict):return set(a)==set(b) and all(equal(a[k],b[k]) for k in a)
 if isinstance(a,list):return len(a)==len(b) and all(equal(x,y) for x,y in zip(a,b))
 return a==b
def check_schema(v,s):
 t=s['type'];actual='boolean' if type(v)==bool else 'integer' if type(v)==int else 'string' if type(v)==str else 'array' if type(v)==list else 'object' if type(v)==dict else 'invalid'
 if actual!=t:raise ValueError('Wrong type')
 if 'enum' in s and v not in s['enum']:raise ValueError('Enum')
 if t=='object':
  if set(v)!=set(s['properties']):raise ValueError('Missing/extra keys')
  for k,x in v.items():check_schema(x,s['properties'][k])
 if t=='array':
  if len(v)>1000:raise ValueError('Array bound')
  for x in v:check_schema(x,s['items'])
