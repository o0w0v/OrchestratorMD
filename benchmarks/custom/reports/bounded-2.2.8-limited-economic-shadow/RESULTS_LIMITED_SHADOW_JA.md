> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/bounded-2.2.8-limited-economic-shadow.md). This report alone does not establish a task result.

# bounded 2.2.8 Limited Economic Shadow

集計: 2026-10-06T02:48:35.037155+00:00

判定: **LOCAL_LIMITED_SHADOW_SUCCESS**

## 1. Task selection

未使用の30単一責務をRECEIPT/BORROW/COLLECTION/NUMERIC/DISCOVERY/ADAPTERから各5件選定。既存8crateの型を用いたrepositoryに沿うobservational/reporting fixtureで、実顧客ticketそのものではない。low/normal、1file、80 LOC。dependency/schema/architecture/security/authority変更は対象外。全initial acceptanceは実行前にFAIL、static gatesはPASS。source/spec/acceptance/hash/risk/validationを両workflowの前にfreezeした。

## 2. Control/shadow split

seed=20260926、各familyからcontrol1件を事前抽選。control: LES228-001/006/011/020/022/030。残り24件はshadow。結果を見た再割当なし、shadowのCodex-only二重実装なし。SPLIT.json / FREEZE.jsonを参照。

## 3. Local adoption

採用 10/24 (41.67%)。Localを実行したTask 24。Host全checks PASSかつ独立Reviewer ACCEPT_NO_CHANGEの場合だけ採用し、それ以外はclean初期sourceからGPT-6 Solへhandoffした。Local候補/diff/diagnosticsはclean Executorへ渡していない。

## 4. Raw First PASS

RAW_LOCAL_FIRST_PASS 5/24 (20.83%)。分母は実Local試行。Local First FAIL 14。INFRAはmodel能力FAILと分離。

## 5. LF rescue

LF_LOCAL_FIRST_PASS 5/24 (20.83%)。LF追加があってもvalidation FAILならrescue成功に含めない。LF適用 11Task、Host追加bytes合計 11。既存exact-final-LFのみ、canonicalization/formatter/protocol変更なし。

## 6. Local false green

LOCAL_VALIDATION_FALSE_GREEN 0、Host PASS候補に対する率 0.00%。Reviewer REJECT候補は採用せずclean Codexへ。

## 7. Final quality

Terminal 30/30、全最終候補は同じmandatory acceptance/regression/fmt/clippy/workspace test/check/build/scope/hash checksと独立contract reviewを通過。観測FINAL_PIPELINE_FALSE_GREEN 0。未知欠陥の不存在は証明しない。Worker/Rust regression True。

## 8. Codex usage

独立CLI sessions 81、unique threads 81、Task accounting complete 30/30。GPT-6 Sol/xhigh/Standard固定、task/roleごとnew context、逐次実行。raw turn.completed input/cached/outputとuncached差分を保存。欠測sessions 0 はnull、他run usageで補完しない。Coordinatorの実usageはnull。phase_usage / session-usage.csvを参照。

## 9. Credits

実incurred Codex credits合計 86.66370、Task平均 2.88879。実役割call（reject/retryを含む）を合計。開始時公式Standard料金uncached/cached/output=[50.0, 5.0, 250.0] credits/1M tokens。raw URL/time/SHAはrates/。creditsはusageから固定公式rateで計算したtoken-based相当、請求画面のbalance差ではない。

## 10. Control credits

control n=6、mean 3.30510、median 3.41488、range 2.39592–3.74843。shadow mean 2.78471。controlはLocal inferenceなし。

## 11. Economic estimate

群レベル推定: control mean × measured shadow数 = 79.32236 credits。実shadow支出 66.83311。推定saved 12.48925、推定reduction 15.74%。個別Taskの仮想Codex-only usage/costはすべてnull。これはunpaired control比較で、難易度差を完全には制御しない。historical14Task composite10.05%は参考のみ、今回へ合算しない。

Exploratory bootstrap shadow-minus-control mean 95%区間: {"seed": 20260926, "resamples": 10000, "contrast": "shadow_mean_minus_control_mean", "lower_95": -1.0995654166666666, "upper_95": 0.11137958333333309, "exploratory": true, "unpaired_Task_difficulty_not_controlled": true}。有意な因果効果の断定には用いない。

## 12. Wall overhead

実workflow wall合計 4,686.032秒、Local gate mean/median 53.699/54.539秒。Host validation合計 1,835.475秒。失敗時Local前段のwallは増えるが、存在しないshadow Codex-only時間との差は作らない。wall intervalはactive作業時間ではない。

観測workflow wall: control mean/median 134.107/134.610秒、shadow mean/median 161.725/186.391秒。unpaired群差であり、個別Taskのlatency増減ではない。Host_validation_wallはLocal check command elapsed + Codex full validation intervalで、Codex側intervalはformatter/guardを含む。Formatter秒は重複する部分があるため加算しない。

## 13. GPU/CUDA

開始はfresh Ollama 0.35.1、loaded models=[]、RTX3080 10GB/driver591.86。Qwen14のみ、Gemma12/Gemma26/CoderNext生成なし。CUDA 0、backend crash 0、GPU query timeout 0、INFRA 0。telemetry 1202 samples、peak GPU 9,491 MiB、residency mismatch 0。各Task前/中/後GPU/API/process/log/Event Logを保存。generation health probeなし。

## 14. Host workload

準備 1770 frozen files、Host preparation script/docs 587 LOC、red-check preparation 301.107秒。Coverage Matrix合計 69591bytes、ReferencePlan合計 24526bytes、実Local reference packet合計 37899bytes。Formatter wall 64.634秒/changed LOC 86。これらは測定用fixture/harnessの初期準備で、料金節約から隠さない。Coordinator prep/review active timeと実Codex tokensは取得不能でnull、LOC/bytesをtokensへ換算しない。

## 15. Rolling metrics

10/20/30Taskの累積rolling JSONを保存。Local adoption、raw、LF rescue、validation false green、credits/task、gate wall、CUDAを含む。

|累積Task|shadow採用|RAW rate|LF rescue rate|validation FG|credits/Task|Local gate mean秒|CUDA|
|---:|---:|---:|---:|---:|---:|---:|---:|
|10|1/8|12.50%|0.00%|0|3.60551|49.730|0|
|20|7/16|31.25%|12.50%|0|2.99701|51.885|0|
|30|10/24|20.83%|20.83%|0|2.88879|53.699|0|

## 16. Circuit breakers

GPU_PAUSED=False、ECONOMIC_PAUSED=False、clear negative evidence=False。CUDA1回でTaskINFRA/GPU pause/no retry、Host/scope safety/finalFGでcohort停止の固定条件を維持。自動reboot/restart/Local再開なし。trace audit flags=0。

Host/cohort STOP records: []。model candidate rejectionとHost integrity failureを混同しない。

## 17. Decision

**LOCAL_LIMITED_SHADOW_SUCCESS**。今回の限定sampleに対する判定であり、production自動採用、Router/Operational Policy変更、次cohort開始は行わない。

## 18. Limitations

control6/shadow24はunpairedでTask難易度、順序、cached tokens、provider変動の影響が残る。balanced family抽選でも完全なcounterfactualではない。観測品質はprotected checks+独立reviewの範囲。private copy/trace/hash監査をOS完全隔離とは表現しない。Host初期準備・Coordinator usageは欠測で、net全体作業量の厳密な削減は未確定。料金とwall、model能力とinfra、Local validation false greenとfinal pipeline false greenを分離した。

### Task results

|Task|family|arm|Local|RAW|LF rescue|adopted|credits actual|Codex LOC|workflow seconds|
|---|---|---|---|---|---|---|---:|---:|---:|
|LES228-001|RECEIPT|control|NOT_APPLICABLE/None|None|None|False|3.74843|6|135.344|
|LES228-002|RECEIPT|shadow|ESCALATE/CODE_FAILURE|False|False|False|4.76850|3|204.688|
|LES228-003|RECEIPT|shadow|ESCALATE/CODE_FAILURE|False|False|False|3.35663|7|205.890|
|LES228-004|RECEIPT|shadow|ESCALATE/CODE_FAILURE|False|False|False|3.88932|7|189.031|
|LES228-005|RECEIPT|shadow|PASS/TARGETED_CHECKS_PASSED|True|False|True|2.23760|0|101.375|
|LES228-006|BORROW|control|NOT_APPLICABLE/None|None|None|False|3.30880|6|135.188|
|LES228-007|BORROW|shadow|ESCALATE/CODE_FAILURE|False|False|False|4.57328|7|209.000|
|LES228-008|BORROW|shadow|ESCALATE/CODE_FAILURE|False|False|False|3.88520|7|183.750|
|LES228-009|BORROW|shadow|ESCALATE/CODE_FAILURE|False|False|False|2.77878|8|191.687|
|LES228-010|BORROW|shadow|ESCALATE/CODE_FAILURE|False|False|False|3.50855|8|193.453|
|LES228-011|COLLECTION|control|NOT_APPLICABLE/None|None|None|False|3.52097|8|127.484|
|LES228-012|COLLECTION|shadow|ESCALATE/CODE_FAILURE|False|False|False|4.63755|9|197.485|
|LES228-013|COLLECTION|shadow|PASS/TARGETED_CHECKS_PASSED|False|True|True|1.27065|0|100.469|
|LES228-014|COLLECTION|shadow|PASS/TARGETED_CHECKS_PASSED|False|True|True|1.79837|0|100.516|
|LES228-015|COLLECTION|shadow|PASS/TARGETED_CHECKS_PASSED|True|False|True|2.53853|0|104.453|
|LES228-016|NUMERIC|shadow|ESCALATE/CODE_FAILURE|False|False|False|3.40444|3|176.078|
|LES228-017|NUMERIC|shadow|PASS/TARGETED_CHECKS_PASSED|True|False|True|1.18436|0|94.390|
|LES228-018|NUMERIC|shadow|PASS/TARGETED_CHECKS_PASSED|True|False|True|1.92029|0|100.750|
|LES228-019|NUMERIC|shadow|PASS/TARGETED_CHECKS_PASSED|True|False|True|1.21401|0|108.266|
|LES228-020|NUMERIC|control|NOT_APPLICABLE/None|None|None|False|2.39592|3|134.032|
|LES228-021|DISCOVERY|shadow|ESCALATE/CODE_FAILURE|False|False|False|2.88658|5|197.157|
|LES228-022|DISCOVERY|control|NOT_APPLICABLE/None|None|None|False|3.30081|5|142.610|
|LES228-023|DISCOVERY|shadow|ESCALATE/CODE_FAILURE|False|False|False|2.41256|6|200.906|
|LES228-024|DISCOVERY|shadow|ESCALATE/CODE_FAILURE|False|False|False|3.11440|9|210.484|
|LES228-025|DISCOVERY|shadow|ESCALATE/CODE_FAILURE|False|False|False|2.25850|5|246.953|
|LES228-026|ADAPTER|shadow|PASS/TARGETED_CHECKS_PASSED|False|True|True|1.18992|0|102.469|
|LES228-027|ADAPTER|shadow|PASS/TARGETED_CHECKS_PASSED|False|True|True|1.19351|0|101.031|
|LES228-028|ADAPTER|shadow|PASS/TARGETED_CHECKS_PASSED|False|True|True|1.76320|0|105.734|
|LES228-029|ADAPTER|shadow|ESCALATE/CODE_FAILURE|False|False|False|5.04838|8|255.375|
|LES228-030|ADAPTER|control|NOT_APPLICABLE/None|None|None|False|3.55566|5|129.984|

表のCodex LOCはdirect経路のinitial→final source diff（Host formattingを含む）で、厳密なCodex authored LOCではない。Local採用時のCodex code editsは0。内部contextはworkflow固有で、Localにはbounded typed packet、Codexには宣言済み初期sourceを与える。同じcontract/checksを用いたworkflow比較であり、モデルの一般能力比較ではない。

### Family observation

```json
[
  {
    "family": "RECEIPT",
    "control_cost": [
      3.74843
    ],
    "shadow_adopted": 1,
    "shadow_tasks": 4,
    "shadow_actual_credits": 14.252049999999999
  },
  {
    "family": "BORROW",
    "control_cost": [
      3.3088000000000006
    ],
    "shadow_adopted": 0,
    "shadow_tasks": 4,
    "shadow_actual_credits": 14.745809999999999
  },
  {
    "family": "COLLECTION",
    "control_cost": [
      3.5209699999999997
    ],
    "shadow_adopted": 3,
    "shadow_tasks": 4,
    "shadow_actual_credits": 10.2451
  },
  {
    "family": "NUMERIC",
    "control_cost": [
      2.3959200000000003
    ],
    "shadow_adopted": 3,
    "shadow_tasks": 4,
    "shadow_actual_credits": 7.7231000000000005
  },
  {
    "family": "DISCOVERY",
    "control_cost": [
      3.3008100000000002
    ],
    "shadow_adopted": 0,
    "shadow_tasks": 4,
    "shadow_actual_credits": 10.67204
  },
  {
    "family": "ADAPTER",
    "control_cost": [
      3.55566
    ],
    "shadow_adopted": 3,
    "shadow_tasks": 4,
    "shadow_actual_credits": 9.19501
  }
]
```

Local実reported usage合計: {"ollama_input_tokens_reported": 33966, "ollama_output_tokens_reported": 1605, "ollama_cache_tokens_reported": 3891}。欠測はnull、Local tokenはCodex節約tokenへ換算しない。

料金根拠: 公式Codex pricing（元資料: http[LOCAL_PATH]）。開始時rawをrates/raw/へ保存し、cohort中のrateは変更していない。
