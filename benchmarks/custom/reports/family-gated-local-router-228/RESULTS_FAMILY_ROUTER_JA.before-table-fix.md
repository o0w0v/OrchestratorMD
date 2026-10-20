> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/family-gated-local-router-228.md). This report alone does not establish a task result.

# Family-Gated Local Router Validation

集計: 2026-10-06T05:03:31.202755+00:00 / 判定: **FAMILY_ROUTER_CONFIRMED**

## 1. Task / family

未使用36 business behavior、6 family各6件。既存8crate型を使う小さいreporting/observation fixtureで、実顧客ticketそのものではない。1file/80LOC、low（DISCOVERYのみnormal）。全initial acceptanceはcompile正常・実テストFAILを確認。Task詳細はplanning/source-plans.json、tasks/、task-results.json。

## 2. Frozen routing

bounded2.2.8/Qwen14/各Codex role GPT-6 Sol xhigh Standard、prompt/options/ReferencePlan抽出/formatter/全mandatory validationは既存と同一。COLLECTION/NUMERIC/ADAPTER候補、RECEIPT exploratory、BORROW/DISCOVERYは全件direct。SPLITとsource/spec/acceptance/hashをAPI前freeze、結果によるroute変更なし。Local repair0。production Router設定は変更していない。

## 3. Controls

seed=20261006でeligible family内2control/4shadowを事前抽選。8direct controls/16Local shadows/12policy-direct、実行順もseeded shuffle。controlはLocal inferenceなし。同じcontract/checks/独立review。shadowのCodex-only二重実装はしていない。

## 4. Local adoption

採用 13/16 (81.25%)。Host PASS + 独立ACCEPT_NO_CHANGEのみ。FirstFAIL/REJECTは初期sourceのclean copyへhandoff。Local候補/diff/diagnosticsをExecutorへ渡していない。採用は実験copy内のみ。

## 5. Raw PASS

RAW 9、能力FirstFAIL 3。Direct-onlyはLocal未測定でFAIL扱いしない。INFRA別分類。

## 6. LF rescue

LF rescue 4。LF_APPLIED/VALIDATION_PASS/REVIEW_PASSをfamily表に分離。exact1byte LF以外の修正なし。実測個別LF_CREDITS_SAVED=null（未実行counterfactual）。同familycontrol平均によるLF採用group推定saved=7.58200 credits、LF自体の因果効果とは断定しない。

## 7. Family economics

下表は同family内unpaired randomized group比較。全Planner/Executor/Reviewer/own-path retry費用を含む。各control n=2で分散推定は不安定。DIFFERENCEはshadow minus control。

|family|Local attempts/adopt|RAW|LF applied/validation/review|FirstFAIL|shadow mean credits|control mean credits|reduction|gate/workflow/control mean s|提案|
|---|---|---:|---|---:|---:|---:|---:|---|---|
|RECEIPT|4/3|2|1/1/1|1|2.04605|2.92847|30.13%|54.782/135.730/153.148|EXPERIMENTAL_MORE_DATA|
|BORROW|0/0|0|0/0/0|0|null|null|null|null/null/null|DIRECT_UNMEASURED_LOCAL|
|COLLECTION|4/4|1|3/3/3|0|1.54581|3.32608|53.52%|57.554/104.070/155.788|LOCAL_CANDIDATE_MORE_DATA|
|NUMERIC|4/3|3|0/0/0|1|1.43437|3.88104|63.04%|59.039/125.547/146.078|LOCAL_CANDIDATE_MORE_DATA|
|DISCOVERY|0/0|0|0/0/0|0|null|null|null|null/null/null|DIRECT_UNMEASURED_LOCAL|
|ADAPTER|4/3|3|0/0/0|1|1.71476|2.51801|31.90%|54.258/121.293/130.515|LOCAL_CANDIDATE_MORE_DATA|

## 8. Router economics

TOTAL_ACTUAL_CODEX_CREDITS=86.89726、平均=2.41381。全directの群推定=110.54763、推定saved=23.65037、推定reduction=21.39%。計算はeligible family別control mean×shadow数 + 実controls/direct-only費用。実usageと推定baselineを分離。LES228の86.66370/30はhistorical referenceだけで因果比較しない。

Exploratory family-stratified bootstrap: {"contrast": "family-stratified total estimated credits saved", "lower_95": 16.984280000000005, "upper_95": 30.097109999999997, "resamples": 10000, "seed": 20261006, "exploratory": true}

公式Standard rate（1M uncached/cached/output）=[50.0, 5.0, 250.0] credits。raw URL/time/SHA rates/、actual turn.completed input/cached/outputから計算。請求balanceの実差ではない。取得不能usageはnullで代替しない。

## 9. Latency

実workflow interval合計=4,919.465秒、Local gate平均=56.408秒、Host validation=1,856.770秒。family gate/workflow/control wallをJSONと表で分離。wallはactive作業時間ではない。未実行個別directの差はnull。Host formatter秒はvalidationに含まれるため重複加算しない。

## 10. Local calls avoided

BORROW/DISCOVERYのLocal候補dispatchをpolicyで12件除外し、実Local GPU callは0。そのTaskへLocalを送っていないので反実仮想HTTP turn数・実savedwallは取得不能。LOCAL_GPU_CALLS_AVOIDED=null、LOCAL_GATE_WALL_AVOIDED=null。過去平均からの捏造なし。

## 11. Review quality

36最終候補はacceptance/regression/fmt/clippy/workspace test/check/build/scope/hashと独立ACCEPT_NO_CHANGE。独立CLI sessions=95、unique threads=95、usage欠測=0、順次/role-copy/inputhash/clean-handoff監査済み。Reviewerはcompact packetだけ、Local全会話なし。

## 12. False greens

LOCAL_VALIDATION_FALSE_GREEN=0 / FINAL_PIPELINE_FALSE_GREEN=0。観測checks+reviewでの指標で、未知欠陥なしの証明ではない。regression全checks PASS=True。

## 13. GPU / CUDA

Ollama=0.35.1 / fresh metadata=False / RTX3080 driver591.86。開始時psが停止frontendを自動起動した経緯をINITIAL_OBSERVATION.jsonに保存。Qwen14のみ・generation probeなし。CUDA=0、infra=0、backendcrash=0、GPUquerytimeout=0。peakGPU=9401.0MiB、telemetry=840、residencyMismatch=0。各Localcall前中後ログ/PID/Event保存。GPU fault1回でpause/no retry/no automaticrestart。

## 14. Rolling metrics

10/20/30/36完了時点をrolling/へ保存。採用・family採用・credit/Task・LF・FG・GPU・wall、未測定値を区別。

## 15. Family promotion / demotion

promotion参考はadoption>=40%・finalFG0・同family推定saving>0・stableinfra。ただし4shadow/2controlで自動採用せず。repeatedFirstFAIL/negativecredits/latencyoverhead/reviewREJECTはdirect候補。RECEIPTはexploratoryを維持またはdirect候補。下表は今回証拠に基づく提案のみ。

## 16. Decision

**FAMILY_ROUTER_CONFIRMED**。複数主要familyで採用再現＋router群推定saved>0がPROMISING条件。CONFIRMEDにはさらにexploratory saving95%区間下限>0を要求する事前の慎重な基準。production採用/Router変更/次cohort自動実行なし。

## 17. Limitations

各eligiblefamily control2/shadow4の小標本で、難易度・cache・provider・実行順変動の影響が残る。Host初期準備 593script/docs LOC/1773frozen files/redcheck398.484秒、coordinator actual tokens/active timeはnull。全workflowのnet費用削減には準備費欠測が残る。privatecopyはOS完全隔離ではない。一般モデル能力rankingではなく、このfixture/domain/policyのquality-constrained economic比較。旧artifact/STOP/runtimeはbyte保持。

料金根拠: 公式Codex pricing（元資料: http[LOCAL_PATH]）。

### Task results

|Task|family|route|adopt|raw|LF rescue|credits|workflow s|

|---|---|---|---|---|---|---:|---:|

|FGR228-001|RECEIPT|control|False|None|None|3.53130|167.062|

|FGR228-002|RECEIPT|shadow|True|True|False|2.30625|101.344|

|FGR228-003|RECEIPT|shadow|False|False|False|3.22556|241.515|

|FGR228-004|RECEIPT|control|False|None|None|2.32563|139.235|

|FGR228-005|RECEIPT|shadow|True|True|False|1.18516|101.360|

|FGR228-006|RECEIPT|shadow|True|False|True|1.46724|98.703|

|FGR228-007|BORROW|direct|False|None|None|3.82104|157.531|

|FGR228-008|BORROW|direct|False|None|None|2.48811|158.562|

|FGR228-009|BORROW|direct|False|None|None|2.37226|135.328|

|FGR228-010|BORROW|direct|False|None|None|3.17413|149.875|

|FGR228-011|BORROW|direct|False|None|None|2.34745|148.359|

|FGR228-012|BORROW|direct|False|None|None|2.47745|161.563|

|FGR228-013|COLLECTION|shadow|True|False|True|1.32360|101.797|

|FGR228-014|COLLECTION|shadow|True|False|True|1.22566|108.297|

|FGR228-015|COLLECTION|control|False|None|None|3.32302|150.046|

|FGR228-016|COLLECTION|shadow|True|False|True|1.30819|104.890|

|FGR228-017|COLLECTION|shadow|True|True|False|2.32578|101.297|

|FGR228-018|COLLECTION|control|False|None|None|3.32913|161.531|

|FGR228-019|NUMERIC|shadow|True|True|False|1.11946|98.812|

|FGR228-020|NUMERIC|shadow|True|True|False|1.16126|100.859|

|FGR228-021|NUMERIC|control|False|None|None|4.28698|151.594|

|FGR228-022|NUMERIC|shadow|False|False|False|2.19143|204.281|

|FGR228-023|NUMERIC|control|False|None|None|3.47510|140.562|

|FGR228-024|NUMERIC|shadow|True|True|False|1.26534|98.235|

|FGR228-025|DISCOVERY|direct|False|None|None|3.04589|164.672|

|FGR228-026|DISCOVERY|direct|False|None|None|3.03945|149.235|

|FGR228-027|DISCOVERY|direct|False|None|None|3.85749|162.391|

|FGR228-028|DISCOVERY|direct|False|None|None|3.11166|142.765|

|FGR228-029|DISCOVERY|direct|False|None|None|2.31524|131.203|

|FGR228-030|DISCOVERY|direct|False|None|None|2.57595|140.360|

|FGR228-031|ADAPTER|shadow|True|True|False|1.70985|93.281|

|FGR228-032|ADAPTER|control|False|None|None|2.85692|137.016|

|FGR228-033|ADAPTER|shadow|True|True|False|1.17361|98.171|

|FGR228-034|ADAPTER|shadow|False|False|False|2.78202|194.953|

|FGR228-035|ADAPTER|control|False|None|None|2.17909|124.015|

|FGR228-036|ADAPTER|shadow|True|True|False|1.19356|98.765|


### 完了時audit / latencyの補足

独立CLI 95 sessions、unique 95、missing usage 0。実Local /api/chat 16件、Qwen14のみ、全candidate1回・repair0。runtime Host STOP=[]。API前の保全snapshot処理停止=['initialize-STOP-001.json']は、Gitが未追跡埋込み作業コピーをdirectoryとして返したケース。source/evidenceのファイルhashを収集する処理へ対応し、部分snapshot/STOPを残してfreeze前に完了した。fixture準備のdependency/helper-call/helper-signature修正もPRE_FREEZE_*.jsonに保存、モデル結果を使った変更は0。

実usage合計（CLI）：`{"input_tokens": 5512035, "cached_input_tokens": 4617472, "uncached_input_tokens": 894563, "output_tokens": 76327, "total_tokens": 5588362}`。Local reported：`{"ollama_input_tokens_reported": 19394, "ollama_output_tokens_reported": 739, "ollama_cache_tokens_reported": 811}`。

|family|gate mean/median s|shadow workflow mean/median s|control mean/median s|direct-only mean/median s|

|---|---:|---:|---:|---:|

|RECEIPT|54.782/55.149|135.730/101.352|153.148/153.148|null/null|

|BORROW|null/null|null/null|null/null|151.870/153.703|

|COLLECTION|57.554/57.758|104.070/103.343|155.788/155.788|null/null|

|NUMERIC|59.039/56.718|125.547/99.836|146.078/146.078|null/null|

|DISCOVERY|null/null|null/null|null/null|148.438/146.000|

|ADAPTER|54.258/53.312|121.293/98.468|130.515/130.515|null/null|

eligible4familyはいずれもshadow群の平均workflow wallがcontrol群より低かった。一方、FirstFAIL Taskの実workflow wallはFGR228-003=241.515秒、022=204.281秒、034=194.953秒。群比較はunpaired、これらTaskの未実行direct wallはnullで、個別saved wallを作らない。

RECEIPTは3/4採用でも、family bootstrapのshadow-minus-control区間は0を含む。experimentalを維持し、広いpromotionを提案しない。ADAPTERの区間上限も0に近く、control2件の不確実性が大きい。COLLECTION/NUMERIC/ADAPTERはLocal candidate維持と追加の業務域確認を提案する。今回コード/ルールのproduction反映はしない。

終了解析health PASS。environment-after.jsonにGPU/API/モデルresidency/PIDを保存。最終旧artifact/未追跡source-evidence hash保全もPASS。記録した「CONFIRMED」は今回の固定cohort判定であり、未知顧客Taskへの一般化や準備費込みの厳密なnet節約の確定ではない。
