> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/economic-accounting-recovery-228.md). This report alone does not establish a task result.

# bounded 2.2.8 Economic Accounting Recovery

集計: 2026-10-05T17:41:50.674961+00:00（UTC。開始日は2026-10-06 JST）

**判定: ECONOMIC_EVIDENCE_COMPLETE**

## 1. Old missing pairs

旧runはquality14/14、complete accounting11/14のまま保持。002/009の旧Planner capacity欠測、005の旧A implementation中断欠測を新usageで埋めない。対象はこの3件だけ。

## 2. Freeze verification

Task JSON、初期source、allowed scope、acceptance/regression/validation、Planner prompt/source/schema、旧Local evidenceをbyte/hash一致で固定。TASK_IDENTITY.json、FREEZE.json、pre-send/、audit.json参照。Runtime35と旧成果物を再検証。Protocol、prompt、routing、formatter、repair、予算変更なし。Local inference/API呼出し0。

Blinding metadata補足: pre-sendの汎用Local_candidate_exposed=falseはraw Local artifactがrole rootにないことを指す。009のA review packetには依頼どおり自身の保存済みLocal候補diff/summaryを含む。他armのimplementationは含まない。BLINDING_FIELD_CLARIFICATION.jsonに入力を変更せず区別を追記。

## 3. Recovery sessions

codex-cli0.160.0 / gpt-6-sol / xhigh / Standard。全role独立context、resume/forkなし、全CLI逐次。B3件をfreezeしてからA。Plannerは各Taskで新規実行一つをA/B共用し、対称比較上は両armに同じcostを含む。実際のunique spendは一度だけ数える。

## 4. Provider capacity

新規provider failure 0件。候補生成前capacityだけ同一条件retry最大1回。originalの欠測はnull、失敗callも会計対象。

## 5. Quality

A 3/3、B 3/3。全mandatory validationと独立ACCEPT_NO_CHANGEを要求。final pipeline false green観測値=0。Worker/Rust regression PASS=True。

|Task|Group|A quality|B quality|A Codex LOC|B Codex LOC|
|---|---|---|---|---:|---:|
|ECR228-002|FIRST_FAIL|True|True|9|11|
|ECR228-005|FIRST_FAIL|True|True|5|5|
|ECR228-009|RAW_PASS|True|True|0|2|

009のAは旧formatted candidate/final.diffとbyte一致、再生成・コード修正なし。002/005のAはclean initial sourceから実装し、Local candidate/diagnosticsやB implementationを見せない。各reviewは自身のcompact packetのみ。

## 6. Raw usage

実CLI session 16件。events.jsonlのturn.completedからinput/cached/outputを取得し、uncached=input−cached。session-usage.csvとrun-history.jsonからrawへ追跡可能。推定なし。Coordinator/preparation tokens=null。未実行phaseはusage=null・skipped=true（論理追加費用0）；欠測callはusage/cost=null。

|Session|Input|Cached|Uncached|Output|Total|
|---|---:|---:|---:|---:|---:|
|codex/planner/ECR228-002/plan|46607|29696|16911|807|47414|
|codex/B/ECR228-002/implementation-01|137475|99200|38275|1946|139421|
|codex/B/ECR228-002/reviews/01|33246|26496|6750|336|33582|
|codex/A-clean/ECR228-002/implementation-01|146442|123648|22794|3326|149768|
|codex/A-clean/ECR228-002/reviews/01|32755|26496|6259|294|33049|
|codex/planner/ECR228-005/plan|46462|29696|16766|818|47280|
|codex/B/ECR228-005/implementation-01|117091|104192|12899|1327|118418|
|codex/B/ECR228-005/implementation-02|203549|166656|36893|1292|204841|
|codex/B/ECR228-005/reviews/02|32435|14464|17971|257|32692|
|codex/A-clean/ECR228-005/implementation-01|119439|110720|8719|1768|121207|
|codex/A-clean/ECR228-005/implementation-02|147362|128256|19106|1822|149184|
|codex/A-clean/ECR228-005/reviews/02|32476|26496|5980|361|32837|
|codex/planner/ECR228-009/plan|46508|14464|32044|696|47204|
|codex/B/ECR228-009/implementation-01|100209|93056|7153|1010|101219|
|codex/B/ECR228-009/reviews/01|32663|14464|18199|243|32906|
|codex/A-local/ECR228-009/reviews/01|32601|14464|18137|278|32879|

## 7. Recovery credits

開始時の公式rateを新取得: [50.0, 5.0, 250.0] credits/1M（uncached/cached/output）。公式Codex pricing（元資料: http[LOCAL_PATH]）。URL/time/raw/SHA256はrates/に保存。

|Task|Complete|A credits|B credits|Saved|Reduction|
|---|---|---:|---:|---:|---:|
|ECR228-002|True|4.30415|4.64601|0.34186|7.36%|
|ECR228-005|True|5.19664|6.72499|1.52835|22.73%|
|ECR228-009|True|2.89719|3.96697|1.06978|26.97%|

## 8. Original aggregate unchanged

旧Primary（11 complete）: B39.06378 → A36.53867 credits、saved2.52511、6.46%。旧11/14を14/14へ書換えない。

## 9. Recovery aggregate

3 independent replications: B 15.33797 → A 12.39798、saved 2.93999、19.17%。complete 3/3。

新規unique CLI actual credits=23.50037。A+Bの論理比較合計とはPlanner共用分だけ異なる。旧Localのtokens/wallは過去観測値で、今回の実行費用へ再計上しない。

## 10. Composite coverage

COMPOSITE_TASK_COVERAGE=14/14。旧11件と新3件のTask coverageであり、旧run自体のaccounting completionではない。

## 11. Composite economics

COMPOSITE: B 54.40175 → A 48.93665 credits、saved 5.46510、10.05%。異なるrunのmeasurementを含み、単一cohortのactual spendではない。

## 12. Group economics

|Group|Tasks|B credits|A credits|Saved|Reduction|
|---|---:|---:|---:|---:|---:|
|RAW_PASS|1|3.96697|2.89719|1.06978|26.97%|
|FIRST_FAIL|2|11.37100|9.50079|1.87021|16.45%|
|LF_PASS|0|null|null|null|null|

参考COMPOSITE group（旧11＋新3の混在measurement）:

|Group|Tasks|B credits|A credits|Saved|Reduction|
|---|---:|---:|---:|---:|---:|
|RAW_PASS|2|7.03158|4.45815|2.57343|36.60%|
|FIRST_FAIL|7|30.51197|33.57808|-3.06611|-10.05%|
|LF_PASS|4|14.52070|7.95228|6.56842|45.23%|
|LOCAL_VALIDATION_FALSE_GREEN|1|2.33750|2.94814|-0.61064|-26.12%|

009 RAW_PASSではCodex implementation省略・coding LOC0のまま、saved 1.06978 credits、26.97%。この1件で費用削減が再現した。

002/005 FIRST_FAILの合計差は16.45%（正値はA節約）。両armとも同じclean direct workflowであり、Local候補を読ませていない。自己修正・review・cacheの実測差を含む2件だけの比較なので「概ね同等」の一般的証明にはしない。

RAW_PASSは009だけでimplementation省略の再現を見る。FIRST_FAILは002/005だけで同じclean direct workflowを比較する。異なる生成・自己修正回数・review costが費用差になり得るため、Local候補を読むoverheadとは解釈しない。LF_PASSは今回対象0件。

## 13. Limitations

3件の独立反復、小標本、TaskとLocal候補を再利用。新Planner/implementation/reviewの出力は変動し得る。実行順序は固定B→Aでcounterbalanceなし。Private contextとtrace auditは絶対的なOS containmentではない。tests/reviewで観測された範囲の品質であり完全正当性証明ではない。Coordinator、準備、電力、Local tokenの料金は未計測。Compositeはrunと測定時点を混在させる。モデル一般ランキングやproduction economicsへ外挿しない。

## 14. Decision

**ECONOMIC_EVIDENCE_COMPLETE**。旧証跡を保全した独立測定として判定。Local/Pilot/productionへ自動採用・再開せずここで停止。
