> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/gemma26-continuous-backend-soak-v2--run-002.md). This report alone does not establish a task result.

# Gemma26 Continuous Backend Soak v2
判定: **GEMMA26_CONTINUOUS_SOAK_STRONG**
集計: 2026-10-08T17:19:41.690440+00:00

## 目的と固定条件
同一frontend/healthy backendで50以上のbusiness generationを確認。52 green-pristine refactor、controlなし。新Task変更要件は独立contract review。旧Soakはimmutable。bounded2.2.8、Gemma26 same digest、8192/2048、FA1/f16、temperature0/seed20260926、one-shot/repair0/default keep_alive。Production変更なし。

## Pristine・reporting preflight
全52 fixtureのfmt/clippy/test/check/build、実serialized reporting records・import identity・signature・no-generation Worker boundaryを保存。失敗copy run-001はgeneration0 PREPARATION_STOPとして保全。

## Primary infrastructure
{
  "Local_attempts": 52,
  "business_generations": 52,
  "quality_completed": 52,
  "adopted": 51,
  "adoption_rate": 0.9807692307692307,
  "RAW_PASS": 51,
  "LF_RESCUE": 0,
  "HOST_PASS": 51,
  "VALIDATION_FALSE_GREEN": 0,
  "FINAL_PIPELINE_FALSE_GREEN": 0,
  "CUDA": 0,
  "backend_crash": 0,
  "GPU_query_timeout": 0,
  "sample_GPU_timeouts": 0,
  "Host_reporting_failure": 0,
  "Host_harness_failure": 0,
  "invalid_pristine_fixture": 0,
  "total_actual_Codex_credits_incurred": 87.46288,
  "coordinator_usage": null,
  "individual_savings": null,
  "group_savings": null,
  "control_tasks": 0,
  "one_backend_segment_ge50": true,
  "primary_backend_PIDs": [
    63296
  ],
  "residency_mismatch_samples": 0
}

## Quality secondary
|Task|Local|raw|LF|adopted|final|credits|
|---|---|---|---|---|---|---|
|GCB228-011|PASS|True|False|True|COMPLETE|1.9604|
|GCB228-017|PASS|True|False|True|COMPLETE|1.9123199999999998|
|GCB228-029|PASS|True|False|True|COMPLETE|1.73787|
|GCB228-049|PASS|True|False|True|COMPLETE|1.76327|
|GCB228-007|PASS|True|False|True|COMPLETE|1.7281300000000002|
|GCB228-022|PASS|True|False|True|COMPLETE|1.8450199999999999|
|GCB228-032|PASS|True|False|True|COMPLETE|2.3733500000000003|
|GCB228-044|PASS|True|False|True|COMPLETE|1.19483|
|GCB228-010|PASS|True|False|True|COMPLETE|1.7704300000000002|
|GCB228-018|PASS|True|False|True|COMPLETE|1.41188|
|GCB228-038|PASS|True|False|True|COMPLETE|2.58289|
|GCB228-043|PASS|True|False|True|COMPLETE|1.86371|
|GCB228-009|PASS|True|False|True|COMPLETE|1.73238|
|GCB228-024|PASS|True|False|True|COMPLETE|1.4238300000000002|
|GCB228-036|PASS|True|False|True|COMPLETE|1.88233|
|GCB228-040|PASS|True|False|True|COMPLETE|1.45475|
|GCB228-002|PASS|True|False|True|COMPLETE|2.25812|
|GCB228-019|PASS|True|False|True|COMPLETE|1.7442699999999998|
|GCB228-027|PASS|True|False|True|COMPLETE|1.95831|
|GCB228-046|PASS|True|False|True|COMPLETE|1.44626|
|GCB228-006|PASS|True|False|True|COMPLETE|1.33853|
|GCB228-025|PASS|True|False|True|COMPLETE|1.5034299999999998|
|GCB228-037|PASS|True|False|True|COMPLETE|1.19253|
|GCB228-051|PASS|True|False|True|COMPLETE|1.18533|
|GCB228-012|PASS|True|False|True|COMPLETE|1.2140300000000002|
|GCB228-016|PASS|True|False|True|COMPLETE|1.8614|
|GCB228-039|ESCALATE|False|False|False|COMPLETE|2.98782|
|GCB228-042|PASS|True|False|True|COMPLETE|1.16168|
|GCB228-013|PASS|True|False|True|COMPLETE|1.91053|
|GCB228-026|PASS|True|False|True|COMPLETE|1.96991|
|GCB228-034|PASS|True|False|True|COMPLETE|1.19348|
|GCB228-050|PASS|True|False|True|COMPLETE|1.22938|
|GCB228-003|PASS|True|False|True|COMPLETE|1.97452|
|GCB228-014|PASS|True|False|True|COMPLETE|1.53131|
|GCB228-033|PASS|True|False|True|COMPLETE|1.35583|
|GCB228-048|PASS|True|False|True|COMPLETE|1.41137|
|GCB228-004|PASS|True|False|True|COMPLETE|1.72328|
|GCB228-021|PASS|True|False|True|COMPLETE|1.71513|
|GCB228-031|PASS|True|False|True|COMPLETE|1.25697|
|GCB228-045|PASS|True|False|True|COMPLETE|1.8074599999999998|
|GCB228-008|PASS|True|False|True|COMPLETE|2.0356199999999998|
|GCB228-023|PASS|True|False|True|COMPLETE|1.7356800000000001|
|GCB228-035|PASS|True|False|True|COMPLETE|1.35174|
|GCB228-041|PASS|True|False|True|COMPLETE|1.8793000000000002|
|GCB228-001|PASS|True|False|True|COMPLETE|2.43147|
|GCB228-015|PASS|True|False|True|COMPLETE|1.78518|
|GCB228-028|PASS|True|False|True|COMPLETE|1.20148|
|GCB228-047|PASS|True|False|True|COMPLETE|1.4243999999999999|
|GCB228-005|PASS|True|False|True|COMPLETE|1.7521300000000002|
|GCB228-020|PASS|True|False|True|COMPLETE|1.35399|
|GCB228-030|PASS|True|False|True|COMPLETE|1.3822800000000002|
|GCB228-052|PASS|True|False|True|COMPLETE|1.56134|

## GPU/lifecycle/drift
{"means": [9920.879150066401, 9899.912985274432, 9914.899159663866, 9912.598382749326, 9832.928876244665], "progressive_drift_screen": false, "predeclared_rule": ">=4 complete windows, nondecreasing mean, late-first >=256 MiB"}
{"lifecycle": null, "infra": null}

## Usage/credits
独立GPT-6 Sol/xhigh/Standardの実usageのみ。公式レートのcredits換算、invoiceではない。欠測null。coordinator/Host準備usageはnull。今回savings推定なし。公式pricing（元資料: http[LOCAL_PATH]）をratesへ保存。旧3-way42.72%、旧Soak完了subset43.23%はhistorical参考のみ。

## 限界と運用候補
当該PC・固定digest/条件・green refactor負荷のInfrastructure確認。モデル能力/一般故障率/driver root causeへ外挿しない。成功時もProduction Routerへ自動反映しない。

## Terminal evidence audit / 日本語補足
同一frontend（app PID62668 / server PID59856）と同一backend PID63296を維持して52/52 business generationが正常に返った。backendのkernel作成時刻と各snapshotのageを照合し、PID再利用による見かけの継続も認めなかった。backend稼働時間は終了時約72.3分、cohort wallは約72.5分。一次条件の50連続callを達成した。
実行開始は2026-10-09 01:00:51 JST、quality終了は02:13:21 JST。ユーザーtray Quit後、frontend/backend/port/API不在と正常GPU queryを保存し、Ollama 0.35.1を同じbinaryでfresh起動。models=[]から開始し、最初のbusinessを最初のgenerationとした。generation probe/preload/unload/restart/keep_alive上書きなし。

|Call window|Loaded mean used MiB|Peak used MiB|Min free MiB|Backend|
|---|---:|---:|---:|---|
|1–10|9920.88|9955|97|63296|
|11–20|9899.91|9931|121|63296|
|21–30|9914.90|9926|126|63296|
|31–40|9912.60|10019|33|63296|
|41–50|9832.93|9862|190|63296|
|51–52|9849.67|9861|191|63296|

dispatch間gap（前API終了→次API開始）は平均80.32秒、中央値78.72秒、最大165.00秒。rolling writerは各window約0.03–0.05秒。後から閾値を変更せず、事前drift screenはfalse。
CUDA/backend crash/GPU query timeout/Host STOP/reporting failure/scope failure/invalid pristine fixtureは0。sampler errors=[]、Windowsの対象期間System/Application照会は取得可能で、関連eventなし。詳細とraw queryはenvironment-after.jsonおよび各Task events.jsonへ保存した。
GPU peak 10019 MiB / min free 33 MiBと、headroomが小さい瞬間もあった。Ollama-reported residencyと実GPU使用量は別CSVへ保存した。既存mismatch detectorは「API報告が実GPU使用量を1GiB以上上回る」方向のみであり、flag=falseを両値の一致とは解釈しない。VRAM不足やdriver/Ollamaの原因を断定しない。

### Quality safetyと唯一のclean handoff
RAW/HOST PASS 51/52、LF rescue 0、independent ACCEPT_NO_CHANGE / Local adopted 51/52（98.08%）。GCB228-039のみLINT_REPAIR_NOT_ELIGIBLE。Local候補は再利用せず、clean initial sourceとfrozen contractから独立GPT-6 Sol実装1回→全mandatory checks→独立reviewで完了。Local repairは52件すべて0。最終pipelineは52/52 PASS、validation/final false greenは0。
全Taskはユーザー承認済みのgreen-pristine refactor。behavioral testsは最初からPASSするため、direct helper forwardingとinline computation除去は独立contract/diff reviewで確認した。今回の98.08%を通常coding Taskの能力や経済性に外挿しない。

### 実usage・creditsのみ
独立Codex sessionは105件、raw turn.completed usage取得105/105。実usageをfreeze済みrateで換算したincurred creditsは87.46288。請求書の実課金額ではない。coordinator/Host準備usageはnull。controls=0なのでTask-specific/group savingsを計算しない。
|Role|Sessions|Incurred credits|
|---|---:|---:|
|planner|52|49.64004|
|implementation|1|1.61864|
|review|52|36.20420|
Local input/output tokensは78,834/1,179。API合計wall 174.86秒、Local gate合計wall 3505.30秒。同時実行のtelemetryやCodex処理を単純加算してcohort wallへ重ねない。

### 保全・結論
旧Soak v1、run-001 PREPARATION_STOP、run-002 preparation checkpointおよびfrozen contracts/plans/runtimeは変更していない。native summary/raw requests/responses/checks/usageを保持し、監査は別TERMINAL_EVIDENCE_AUDIT.json。native日本語reportはNATIVE_RESULTS_JA.mdへbyte-preserving copyとして保全した。
判定はGEMMA26_CONTINUOUS_SOAK_STRONG。このPC・digest・8192/f16/FA1・今回の短いrefactor生成とvalidation/review間隔で、Host interruptionなしの52-call backend継続を確認した。num_predict=2048は上限であり、2048 tokensを毎回生成するstress testではない。長いoutput、異なるpayload、background負荷、一般故障率や根本原因については未証明。
既存条件のGemma26をproduction候補として維持する根拠にできる。Router/model/protocol/application/driver/runtime/恒久設定の変更とPilot自動開始は行わず、本cohortの報告で停止する。
