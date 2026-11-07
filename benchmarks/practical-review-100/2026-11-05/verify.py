"""Offline public export verification: no network, subprocess or model calls."""
import collections
import hashlib
import json
import sys
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT/'replay'))
from protocol import equal, check_schema
from policy import apply_patch
from reference import solve

def read(rel): return json.loads((ROOT/rel).read_text(encoding='utf-8'))
manifest=read('PACKAGE_MANIFEST.json')
for name,record in manifest['files'].items():
    p=ROOT/name
    assert p.is_file(),name
    assert p.stat().st_size==record['bytes'],name
    assert hashlib.sha256(p.read_bytes()).hexdigest()==record['sha256'],name
rows=[]; patches=0; same=0; gemma_initial=0; families=collections.Counter(); profiles=collections.Counter()
for item in read('CASE_INDEX.json'):
    case=read(item['file']); j=case['public_job']; tid=case['task_id']; methods=case['methods']
    assert len(case['public_dialogue'])==5
    assert case['public_dialogue'][0]['content']==j['initial']
    assert case['public_dialogue'][2]['content']==j['owner_reply']
    assert case['public_dialogue'][4]['content']==j['continuation']
    expected=solve(case['metadata']['family'], j['attachments'])
    assert equal(expected,case['expected_data_after_routing_sealed']),tid
    families[case['metadata']['family']]+=1; profiles[j['profile']]+=1
    for arm,r in methods.items():
        final=r['final_artifact']; initial=r['initial_artifact']
        check_schema(final,j['output_schema'])
        assert final['report_md'].strip()
        assert equal({k:v for k,v in final.items() if k!='report_md'},expected), (tid,arm)
        score=next(x for x in case['scores'] if x['arm']==arm)
        assert score['data_exact'] and score['data_correct_adoption'] and not score['data_false_green']
        assert score['initial_data_exact']==equal({k:v for k,v in initial.items() if k!='report_md'},expected)
        rows.append(score)
    b=methods['PRACTICAL']
    if j['profile']=='small':
        same+=1; assert equal(b['final_artifact'],methods['SOL_CONTINUE']['final_artifact'])
    else:
        gemma_initial+=next(x for x in case['scores'] if x['arm']=='PRACTICAL')['initial_data_exact']
        assert len(b['visible_review_responses'])==1
    if b.get('patch_changes'):
        patches+=1
        assert equal(apply_patch(b['initial_artifact'],b['patch_changes'],j['output_schema']),b['final_artifact'])
assert len(rows)==200 and len(families)==10 and set(families.values())=={10}
assert dict(profiles)=={'normal':56,'complex':30,'small':14}
assert same==14 and patches==12 and gemma_initial==76
comp=read('analysis-001/COMPARISON.json')
for arm in ['SOL_CONTINUE','PRACTICAL']:
    rr=[r for r in rows if r['arm']==arm]; m=comp['methods'][arm]
    assert sum(Decimal(r['operating_reported_usage_credits']) for r in rr)==Decimal(m['operating_reported_usage_Credits'])
    assert abs(sum(r['total_active_seconds'] for r in rr)-m['active_seconds'])<0.00001
    assert collections.Counter(r['category'] for r in rr)==m['categories']
ledger=read('accounting/INCREMENTAL_USAGE.json'); assert len(ledger)==386
fields=['input_tokens','cached_input_tokens','output_tokens','reasoning_output_tokens']
sessions=collections.defaultdict(list)
for l in ledger:
    sessions[l['session_id']].append(l)
    assert l['raw_cumulative_usage']['cache_write_input_tokens']==0
    for k in fields:
        assert l['raw_cumulative_usage'][k]-l['previous_cumulative_usage'].get(k,0)==l['incremental_usage'][k]
for sid,ll in sessions.items():
    tail=max(ll,key=lambda l:sum(l['raw_cumulative_usage'][k] for k in fields))
    for k in fields: assert sum(l['incremental_usage'][k] for l in ll)==tail['raw_cumulative_usage'][k],(sid,k)
assert sum(Decimal(l['incremental_Credits']) for l in ledger)==Decimal('219.55402')
assert Decimal(comp['comparison_sum_not_actual'])==Decimal(comp['reported_usage_subtotal_Credits'])+Decimal(comp['shared_source_reported_Credits_once'])+Decimal(comp['shared_small_execution_reported_Credits_once'])
assert comp['study_total_Credits'] is None and comp['actual_credit_reduction_percent'] is None
assert comp['independent_narrative_equivalence_proven'] is False and comp['research_model_calls']==0
print(json.dumps({'passed':True,'cases':100,'method_results':200,'data_exact':200,'patches':patches,'physically_shared_small':same,'gemma_initial_correct':gemma_initial,'gemma_cases':86,'completed_usage_ledgers':len(ledger),'sessions':len(sessions),'public_file_hashes':len(manifest['files']),'new_model_calls':0,'independent_narrative_audit':False},ensure_ascii=False))
