> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/gemma26-production-like-soak-228--run-001.md). This report alone does not establish a task result.

# Gemma26 Production-Like Soak Shadow — 最終結果

判定: **INCONCLUSIVE / STOPPED_HOST_FIXTURE_VALIDATION_ERROR**。Local attempts 46/52、最終品質完了Local 45/52＋direct control 12/12。残り6 LocalはNOT_RUNのまま保持した。
Local採用は **36/46（78.26%）**。CUDA/backend crash/GPU query timeoutはそれぞれ 0/0/0。FINAL_PIPELINE_FALSE_GREEN=0。

Host reporting障害の中断中にbackend/residencyが消失し、未実行Taskの再開時に再ロードされた。frontendは継続し、Hostによるrestart/unload/keep_alive変更はないが、同一backendで50件以上連続稼働という主目的の証拠は不足した。品質・費用の観測を保存し、無中断soak成功とは判定しない。
最終停止はcall46 / GSOAK228-031の凍結Host testにあるClippyエラー。pristine sourceでも再現し、モデルが編集できない領域であることを確認した。Local/Codexのcoding能力FAILには混ぜずINVALID_HOST_FIXTUREとして分離する。Codex direct4 episodesの既存上限を超えてretryせず、凍結fixtureも変更しない。

本報告の会計は、元collectorの欠測usageをnative runtimeの実token記録で補完した `EFFECTIVE_FINAL_SUMMARY.json` に基づく。元collector判定=INCONCLUSIVE、元集計・CLI END・失敗記録は変更しない。

## 1. Environment

RTX 3080 10GB / driver 591.86 / Ollama 0.35.1。OS boot timeは 2026-10-04T07:04:49.0982690Z。
Gemma `gemma4:26b` / Q4_K_M / digest `08ae7ec1744bd7f451c4a530afb39d2673ad9d07a8369b8a33a3613b41212a68`。
固定条件: bounded 2.2.8、num_ctx=8192、num_predict=2048、temperature=0、seed=20260926、Flash Attention=1、KV=f16、stream=false、think=false。モデル・runtime・quantization・offload設定・production Routerは変更していない。
ユーザーtray Quit後のfrontend/backend/API/port/residency不在とGPU正常応答を確認してfresh開始した。models=[]、最初のbusiness Taskが最初のgeneration。health generationとpreloadなし。
開始証跡: fresh-exit.json（元資料: fresh-exit.json）、launch.json（元資料: launch.json）、environment.json（元資料: environment.json）、FREEZE.json（元資料: FREEZE.json）。raw日時はUTCと+09:00の両方を含み、各offsetを保持する。

## 2. Task selection

承認済み64 fresh business Task: COLLECTION / NUMERIC / ADAPTER / RECEIPT各16件。事前seed=20261007で各family13件Local＋3件direct controlに固定した。凍結後の再割当・仕様変更なし。
既知編集位置の単一責務・小さなreporting backlogをisolated fixtureで実装した。過去評価Taskの実装・resultは再利用しないが、collection/count/text等のprimitiveの類似はあり、一般的なapplication全体へ外挿しない。
全64件のinitial acceptanceはred、初期compileは正常。BORROW / DISCOVERY / high risk / architecture / security / ambiguous / large multi-file refactorはLocal対象外。
SPLIT.json（元資料: SPLIT.json）、tasks/（元資料: tasks/）、preparation/（元資料: preparation/）、OFFLINE_CHECKS_002.json（元資料: OFFLINE_CHECKS_002.json）に仕様・source hash・境界smokeを保存した。

## 3. Routing

52件はGemma26 one-shot、Local repair=0。Host PASSにのみ独立GPT-6 Sol compact reviewを実施し、ACCEPT_NO_CHANGEだけを採用する。
Local FAILまたはreview REJECTでは、clean initial source＋frozen contract＋planから独立GPT-6 Sol direct実装へhandoffした。Local candidate/diff/diagnosticsをexecutorへ供給しない。Qwen等へのcross-model fallbackなし。
全Codex roleはgpt-6-sol / xhigh / Standard、Taskごとの独立context、resume/forkなし。Planner64件とdirect control12件をLocalより先にfreezeした。

## 4. Local attempts

Local attempts=46、raw generation request=46、Local repair=0、terminal quality完了=45/52。
完了Local Task workflowの最初/最後の境界: `2026-10-07T15:32:07.916641+00:00` → `2026-10-07T17:30:51.203879+00:00`。追加のcall46の停止・未完了費用は別記録。cohort wall intervalにはvalidation/review/handoffとHost reporting中断を含む。
raw wire request bytes/SHAとoptionsの照合は FINAL_AUDIT.json（元資料: FINAL_AUDIT.json）。request/response、結果、diagnostics、GPU/logのpathは run-history.json（元資料: run-history.json） から辿れる。

## 5. Raw First PASS

RAW_FIRST_PASS=37/46（80.43%）。これはHost checksの初回通過であり、review採用とは別指標。

## 6. Exact final-LF rescue

LF_RESCUE=2。既存exact final-LF canonicalizationのみを使用し、model regenerationやsemantic修正はしていない。

## 7. Adoption

HOST_PASS=39、REVIEW_ACCEPT / LOCAL_ADOPTED=36、採用率=78.26%。過去20/24（83.33%）と混合せずhistorical referenceに留める。
全46 dispatch分母の採用率とは別に、Host fixture不成立1件を除いたcoding有効Task=45、有効分母採用率=80.00%。旧Local resultは改変せず、除外根拠はHOST_FIXTURE_FAILURE.jsonに保存する。

## 8. Validation false greens

LOCAL_VALIDATION_FALSE_GREEN=3。Host PASSでも契約違反を独立reviewが見つけた候補は採用しない。
- GSOAK228-048 (call 7): When execution is None, map_or(0, ...) returns zero without calling soak_line_count. The contract requires supplying an empty string to the protected helper and returning its result.
- GSOAK228-044 (call 31): load_presence_caption classifies load_one inline with is_finite(), although the contract forbids inline classification.; It calls soak_load_class(state.load_one) only for finite values; NaN and infinities bypass the protected classifier.
- GSOAK228-033 (call 43): When state.warnings is empty, warning_preview returns String::new() directly instead of passing "" and limit to soak_char_preview.

両経路の検証基準を緩めず、clean Codex direct結果もmandatory checksと独立reviewを要求した。

## 9. Final quality

最終品質完了=57/64。判定内訳: `{'MANDATORY_PASS_AND_ACCEPT_NO_CHANGE': 57, None: 7}`。FINAL_PIPELINE_FALSE_GREEN=0（承認済み必須条件は=0）。
acceptance / targeted regression / fmt / clippy / workspace test / check / build / scope/hash/freezeを維持した。Local不採用結果やSTOPを後からPASSへ置換しない。
raw Local non-PASS=7（うちHost fixture invalid1）、review REJECT=3、clean Codex handoff開始=10。call46は最終品質未完了でPASSとは呼ばない。

|Task|family|path|Local|raw|LF rescue|adopted|final quality|Codex credits|
|---|---|---|---|---|---|---|---|---:|
|GSOAK228-001|COLLECTION|shadow|PASS|True|False|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|2.286190|
|GSOAK228-002|COLLECTION|shadow|PASS|True|False|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|1.738390|
|GSOAK228-003|COLLECTION|shadow|PASS|True|False|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|1.187140|
|GSOAK228-004|COLLECTION|shadow|PASS|True|False|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|1.184640|
|GSOAK228-005|COLLECTION|shadow|PASS|True|False|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|1.823640|
|GSOAK228-006|COLLECTION|shadow|PASS|False|True|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|1.757600|
|GSOAK228-007|COLLECTION|shadow|PASS|True|False|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|1.172700|
|GSOAK228-008|COLLECTION|control|None|None|None|None|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|3.285610|
|GSOAK228-009|COLLECTION|shadow|PASS|True|False|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|2.300590|
|GSOAK228-010|COLLECTION|shadow|PASS|True|False|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|2.384780|
|GSOAK228-011|COLLECTION|shadow|PASS|True|False|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|1.728640|
|GSOAK228-012|COLLECTION|shadow|PASS|True|False|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|1.675800|
|GSOAK228-013|COLLECTION|shadow|PASS|True|False|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|1.301320|
|GSOAK228-014|COLLECTION|control|None|None|None|None|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|2.872130|
|GSOAK228-015|COLLECTION|control|None|None|None|None|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|3.029800|
|GSOAK228-016|COLLECTION|shadow|None|None|None|None|None|null|
|GSOAK228-017|NUMERIC|shadow|PASS|True|False|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|1.170500|
|GSOAK228-018|NUMERIC|control|None|None|None|None|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|2.563120|
|GSOAK228-019|NUMERIC|shadow|PASS|True|False|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|1.146850|
|GSOAK228-020|NUMERIC|shadow|PASS|True|False|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|1.701940|
|GSOAK228-021|NUMERIC|control|None|None|None|None|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|6.356620|
|GSOAK228-022|NUMERIC|shadow|ESCALATE|False|False|False|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|5.241480|
|GSOAK228-023|NUMERIC|shadow|PASS|True|False|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|1.129950|
|GSOAK228-024|NUMERIC|shadow|None|None|None|None|None|null|
|GSOAK228-025|NUMERIC|shadow|ESCALATE|False|False|False|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|2.697540|
|GSOAK228-026|NUMERIC|shadow|PASS|True|False|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|1.169700|
|GSOAK228-027|NUMERIC|shadow|PASS|True|False|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|2.324280|
|GSOAK228-028|NUMERIC|control|None|None|None|None|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|3.278810|
|GSOAK228-029|NUMERIC|shadow|PASS|True|False|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|1.105100|
|GSOAK228-030|NUMERIC|shadow|PASS|True|False|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|1.288630|
|GSOAK228-031|NUMERIC|shadow|ESCALATE|False|False|None|None|null|
|GSOAK228-032|NUMERIC|shadow|PASS|True|False|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|1.125400|
|GSOAK228-033|ADAPTER|shadow|PASS|True|False|False|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|3.503650|
|GSOAK228-034|ADAPTER|shadow|PASS|True|False|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|1.816780|
|GSOAK228-035|ADAPTER|shadow|PASS|True|False|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|1.204050|
|GSOAK228-036|ADAPTER|control|None|None|None|None|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|2.880400|
|GSOAK228-037|ADAPTER|control|None|None|None|None|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|3.233590|
|GSOAK228-038|ADAPTER|shadow|None|None|None|None|None|null|
|GSOAK228-039|ADAPTER|shadow|PASS|True|False|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|1.719790|
|GSOAK228-040|ADAPTER|shadow|PASS|True|False|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|1.689090|
|GSOAK228-041|ADAPTER|shadow|PASS|True|False|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|2.190240|
|GSOAK228-042|ADAPTER|shadow|PASS|True|False|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|1.879320|
|GSOAK228-043|ADAPTER|shadow|None|None|None|None|None|null|
|GSOAK228-044|ADAPTER|shadow|PASS|True|False|False|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|3.367610|
|GSOAK228-045|ADAPTER|shadow|PASS|True|False|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|1.156300|
|GSOAK228-046|ADAPTER|control|None|None|None|None|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|2.839720|
|GSOAK228-047|ADAPTER|shadow|PASS|True|False|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|1.289630|
|GSOAK228-048|ADAPTER|shadow|PASS|False|True|False|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|3.515260|
|GSOAK228-049|RECEIPT|shadow|PASS|True|False|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|1.251330|
|GSOAK228-050|RECEIPT|shadow|PASS|True|False|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|1.702200|
|GSOAK228-051|RECEIPT|shadow|PASS|True|False|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|1.124750|
|GSOAK228-052|RECEIPT|shadow|ESCALATE|False|False|False|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|2.909330|
|GSOAK228-053|RECEIPT|control|None|None|None|None|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|4.428300|
|GSOAK228-054|RECEIPT|shadow|None|None|None|None|None|null|
|GSOAK228-055|RECEIPT|shadow|PASS|True|False|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|1.213600|
|GSOAK228-056|RECEIPT|shadow|ESCALATE|False|False|False|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|2.280840|
|GSOAK228-057|RECEIPT|control|None|None|None|None|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|4.042440|
|GSOAK228-058|RECEIPT|shadow|PASS|True|False|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|1.745040|
|GSOAK228-059|RECEIPT|shadow|PASS|True|False|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|1.162350|
|GSOAK228-060|RECEIPT|shadow|PASS|True|False|True|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|1.710840|
|GSOAK228-061|RECEIPT|shadow|None|None|None|None|None|null|
|GSOAK228-062|RECEIPT|shadow|ESCALATE|False|False|False|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|4.515560|
|GSOAK228-063|RECEIPT|control|None|None|None|None|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|2.694040|
|GSOAK228-064|RECEIPT|shadow|ESCALATE|False|False|False|MANDATORY_PASS_AND_ACCEPT_NO_CHANGE|4.545100|

## 10. GPU lifecycle

frontend/server PIDs=[27584, 60444]。backend observed PIDs=[58080, 61628, 62056]、同一backend continuity=False。開始時のfit/load trial PIDと実inference backendは区別する。
10件完了後にHost reporting module名衝突で停止し、no-generation reporting復旧でSTART/ENDのrole重複指定も検出した。Host reporting error=2。旧STOP・完了10件・Planner・controlsを保持した新Host wrapperで未実行11–52だけを継続した。
中断前のbackend PID61628はhealthy snapshotで存在し、resume snapshotではbackend=[] / models=[]。既定expires_atが中断時間内にあり、keep_alive expirationと整合するが、明示的なunload logがない限り原因は断定しない。次business TaskでPID62056がロードされた。sampling gapを補間しない。
Host restart/unload/keep_alive延長・Task retryは行っていない。これは同一backend連続soakの制約であり、CUDAやmodel coding failureへ算入しない。
execute-STOP-001.json（元資料: execute-STOP-001.json）、HOST_REPORTING_FAULT_SNAPSHOT.json（元資料: HOST_REPORTING_FAULT_SNAPSHOT.json）、HOST_REPORTING_RECOVERY_002.json（元資料: HOST_REPORTING_RECOVERY_002.json）、HOST_REPORTING_REAL_RECORD_SMOKE.json（元資料: HOST_REPORTING_REAL_RECORD_SMOKE.json）、HOST_REPORTING_RECOVERY_PRESERVATION_002.json（元資料: HOST_REPORTING_RECOVERY_PRESERVATION_002.json）。
call index / frontend age / backend age / PID / GPU / /api/psは gpu-telemetry.csv（元資料: gpu-telemetry.csv） と ollama-residency.csv（元資料: ollama-residency.csv）、連続segment rawに保存。

|backend PID|observed call count|first sample|last sample|max age sec|
|---|---:|---|---|---:|
|58080|1|2026-10-07T15:32:25.786137+00:00|2026-10-07T15:32:25.786137+00:00|null|
|61628|10|2026-10-07T15:32:26.875872+00:00|2026-10-07T16:00:08.939138+00:00|1,662.608|
|62056|36|2026-10-07T16:09:08.325112+00:00|2026-10-07T17:36:03.068648+00:00|5,214.987|

このcountはcall phaseとの観測重複数で、全callを当該PIDでgenerationした直接証明ではない。startupのfit/load trialと長寿命inference backendを別扱いする。

## 11. VRAM drift

loaded GPU peak=10,005.000 MiB、minimum free=47.000 MiB。window means=[9742.546190155092, 9684.152121697358, 9683.834112149532, 9666.860095389507]、late-first=-75.686 MiB。事前drift screen=False。
screenは4 complete windows以上・非減少mean・late-first >=256MiBの記述的判定。backend変更・pause・background・温度・Task負荷が交絡するため、memory leak不存在の証明とはしない。
peak snapshot: `{'timestamp': '2026-10-07T17:13:46.024834+00:00', 'call_index': 37, 'task_id': 'GSOAK228-009', 'phase': 'Local_gate', 'gpu_used_mib': 10005.0, 'gpu_free_mib': 47.0, 'backend_pids': [62056], 'backend_age_seconds': 3877.943062067032, 'utilization_pct': 30.0, 'temperature_c': 55.0, 'power_w': 101.68, 'ollama_reported_vram_bytes': 990348573}`。total GPU値だけからmodel allocationやbackground変動の原因を断定しない。
residency_mismatch samples=0。API報告VRAMとnvidia-smiのphysical GPU totalは別値として保存した。固定detectorはAPI報告が実GPU totalを1GiB超上回るstale residencyを検出する。逆方向の過少報告や他processのメモリは検出対象ではなく、0件は値の完全一致を意味しない。WDDMで取得不能のper-process VRAMはnull。

## 12. CUDA / backend / Windows events

CUDA=0、backend crash=0、GPU query timeout=0、sampler GPU timeouts=0、INFRA_ERROR=0、Worker Host/scope failure=0。
Host fixture validation error=1、Host reporting error=2を上記Worker integrity/infraとは別計上する。『Host failure全体が0』とは表現しない。
Windows関連event deduplicated=0、Task log取得不能窓=0。Host reporting pauseのEvent Logもread-only保存した。取得不能を「該当なし」と表現しない。nvlddmkm 153単独をDisplay4101 driver resetと同一視しない。
backend command、FA/KV/context、GPU/CPU offload、buffer/loadの実ログは FINAL_AUDIT.json（元資料: FINAL_AUDIT.json） と各Task infrastructure/logs。推定原因や単純OOMの断定なし。

## 13. Latency

|metric|n|mean sec|median sec|p95 sec|max sec|
|---|---:|---:|---:|---:|---:|
|Ollama API|46|3.825|2.740|6.505|25.971|
|Local gate|46|97.783|104.336|109.360|130.672|
|workflow|45|145.822|128.344|248.578|285.344|
|Host First PASS workflow|39|131.843|127.407|259.422|285.344|
|Host First FAIL workflow|6|236.690|236.109|248.578|248.578|

Host validation累計=3,101.238 sec。active timeは未取得/null。GPU sampling、validation、Codex推論を含むwallと人間/agentのactive timeを混同しない。cold loadとwarm APIも分離可能なraw durationを保存した。

## 14. Codex usage

独立native CLI sessions実測=152、欠測=0。元CLI END欠測=1件のうちruntime実token補完=1件。
capacity failureしたPlanner GSOAK228-048の元ENDはnullのまま保持する。補完値は一致するthread/turn/cwdのtoken_usage_record、unique response ID、cumulative token_countと成功session cross-checkで検証した。推計や0-charge仮定なし。
|phase|sessions|input tokens|cached input|output tokens|total tokens|credits|
|---|---:|---:|---:|---:|---:|---:|
|planner|65|3049740|2506752|50435|3100175|52.291910|
|implementation|27|3026538|2495616|38756|3065294|48.713180|
|review|60|1983338|1380864|19078|2002416|41.797520|

inputはcachedを含む。uncached=input-cached。raw usage・phase・request metadataは各Codex START/END、ACCOUNTING_RUNTIME_RECOVERY.json（元資料: ACCOUNTING_RUNTIME_RECOVERY.json）、EFFECTIVE_FINAL_SUMMARY.json（元資料: EFFECTIVE_FINAL_SUMMARY.json）。Coordinator/Host preparationのtokens・credits・active timeはnullで、測定したCLI費用に加算推定しない。
Local Ollama reported usage: `{'ollama_input_tokens_reported': 57218, 'ollama_output_tokens_reported': 2578, 'ollama_cache_tokens_reported': 0, 'ollama_duration_seconds_reported': 175.42733769999998}`。Local tokensをCodex savingsへ換算しない。
実output token分布: `{'n': 46, 'mean': 56.04347826086956, 'median': 51.5, 'minimum': 21, 'maximum': 259, 'p95': 98}`。budgetは2048固定だが、各business実装の実出力量はこの分布であり、2048-token長文生成負荷試験とは別の観測である。

## 15. Codex credits

開始時にfreezeした公式GPT-6 Sol Standard rateは1M tokens当たりuncached=50 / cached=5 / output=250 credits。公式 Codex Pricing（元資料: http[LOCAL_PATH]）、取得raw/time/SHA/rowは rates/rate-card.json（元資料: rates/rate-card.json）。
実usageの公式rate換算: 完了Local shadow合計=88.135460、完了direct controls合計=41.504580、cohortの全CLI実支出=142.802610 credits（未完了Taskの既支出=13.162570を含む）。invoice実額ではない。失敗provider sessionの実測分も含める。
ACTUAL_CODEX_CREDITS_PER_TASK (shadow mean)=1.958566。全workflow NET savingsはHost/coordinator/electricity費用が未測定のためnull。

## 16. Direct control comparison

Task-specific Codex-only baselineは作らない。各family3 controlのmeanと同family13 shadowの群比較だけを行う。
|family|shadow n|control n|adopted|shadow mean credits|direct mean credits|group estimate saved|
|---|---:|---:|---:|---:|---:|---:|
|COLLECTION|12|3|12|1.711786|3.062513|16.208730|
|NUMERIC|11|3|9|1.827397|4.066183|24.626647|
|ADAPTER|11|3|8|2.121065|2.984570|9.498550|
|RECEIPT|11|3|7|2.196449|3.721593|16.776587|

family-matched group estimated credits saved=67.110513、estimated reduction=43.23%。この値は非paired estimateであり、個別Task反実仮想や純workflow savingsではない。controlがLocalより先に実行されたcache/order交絡も残る。

## 17. Rolling windows

10 Local attemptsごとの元rolling記録は変更せず、rolling/（元資料: rolling/）に保存した。元rollingの欠測creditsはnullのまま。以下は最終runtime usage補完後の窓別記述値。

## 18. Stability windows

|calls|attempts|adoption|API mean sec|gate mean sec|workflow mean sec|loaded mean MiB|peak MiB|min free MiB|Codex credits|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|1–10|10|70.00%|5.002|106.483|167.383|9,742.546|9,751.000|301.000|21.237060|
|11–20|10|90.00%|4.337|107.230|141.117|9,684.152|9,691.000|361.000|16.112780|
|21–30|10|90.00%|2.930|106.398|141.160|9,683.834|9,691.000|361.000|17.605830|
|31–40|10|80.00%|3.087|94.119|137.933|9,666.860|10,005.000|47.000|20.143620|
|41–52|6|50.00%|3.734|59.287|137.216|9,646.356|9,721.000|331.000|13.036170|

窓1–10と11以降はHost pauseとbackend変更をまたぐ。windowの改善/悪化を長寿命backendの因果効果と解釈しない。各Task / windowのCUDA、PIDセット、frontend/backend ageはFINAL_SUMMARYおよびCSVに保存した。

## 19. Circuit breaker / preservation

LOCAL_INFRA_STOP=None。CUDA/backend crash/timeout/residency mismatch時は停止・raw証跡保存・Local retryなしという固定policyを維持した。Ollama/OS自動restartなし。
Host reporting STOPとinfra circuit breakerは別記録。完了Task・controls・Planner・旧STOP・旧telemetryはhashで保持し、報告復旧は未実行Taskのみ対象とした。
最終STOPは report-recovery-STOP-002.json（元資料: report-recovery-STOP-002.json）。原因分類は HOST_FIXTURE_FAILURE.json（元資料: HOST_FIXTURE_FAILURE.json）、pristine Clippy stderrは host-fixture-audit/stderr.txt（元資料: host-fixture-audit/stderr.txt）。pristine source line99のbudget field代入はallowed body markers（line89–92）の外にある。candidate整形後のdiagnostic line番号とは分離する。source/hashはfreezeと一致し、診断copyのsourceも変更していない。
修正案は PROPOSED_FIXTURE_CORRECTION.patch（元資料: host-fixture-audit/PROPOSED_FIXTURE_CORRECTION.patch） に未適用で保存した。max_latency_ms=7とacceptanceの意味を維持するstruct initializer案である。現runのTask/source/validationを変更して再開しない。
offline regressionはWorker suite275件＋Rust fmt/clippy/test/check/build PASS。全generationのmodel/options/one-shot、全独立CLIの固定モデル/effort/speed、source/Task/runtime/旧artifact hashをFINAL_AUDITで再確認した。

## 20. Limitations

- 同一backendの無中断50件soakを満たしていない。Host reporting errorとsampling gapが主な制約。
- call46の凍結Host fixture validation errorでSTOPし、minimum50 attemptsを満たせず、6 Local NOT_RUN・1 Task最終品質未完了。完了済み57件の品質/economicsだけを群比較し、未完了分の既支出も別に全実費へ含める。
- 小さく固定したreporting fixtureの4 familyのみ。production applicationの全負荷、一般model順位、一般故障率、CUDA root causeには外挿しない。
- Host validation false greenはreviewで検出して不採用にした。final false green=0は観測範囲であり、未知欠陥がない証明ではない。
- controlsはfamily matchedでTask pairedではない。sample3/family・cache/order/background・共有prompt等の交絡がある。
- official-rate creditsはinvoiceではない。Host/coordinatorの未計測費用や電力を含む純economicsはnull。
- DESIGN_JA.mdの「section24–29欠落」記述は誤り。原依頼は全sectionを含み、凍結設計を変更せずDESIGN_ERRATUM_JA.mdで訂正した。該当契約は実行に含まれる。
- 原生成reportはRESULTS_GEMMA26_SOAK_JA.generated-original.mdにbyte-exact保存した。会計補完前の元FINAL_SUMMARY/CLI ENDも保持する。

## 21. Decision / production candidate

**INCONCLUSIVE**。46 attempts、採用78.26%、CUDA/infra/scope/final false greenの観測値と完了subsetのgroup economicsは保存したが、minimum50 attempts・全Task最終品質・無中断backend lifecycleを確認できなかった。Host fixture問題をModel/Router能力のFAILへ算入しない。
8192/f16/FA1は品質・経済性を示すproduction候補として保持する。ただし本runをGEMMA26_SOAK_SUCCESSやstrong continuous-stability evidenceと呼ばない。Router/production設定・memory/protocolは変更せず、追加Pilot/新cohortも自動開始しない。
次の候補は、未適用fixture correctionを新しいcopyで検証し、全Taskのpristine Clippyと実記録reporting smokeをfreeze前に通した新cohortの無中断soakである。既定keep_aliveを維持し、backend寿命・default expiryとworkflow間隔を分離して記録する。今回得た結果の再実行・再課金や新cohortの自動開始は行わない。

詳細監査: ANALYSIS_GEMMA26_SOAK_JA.md（元資料: ANALYSIS_GEMMA26_SOAK_JA.md）、FINAL_ANALYSIS.json（元資料: FINAL_ANALYSIS.json）、EFFECTIVE_FINAL_SUMMARY.json（元資料: EFFECTIVE_FINAL_SUMMARY.json）。

未完了GSOAK228-031の既支出は8.770050 credits。未実行6件のPlanner既支出は4.392520 credits。いずれもcohort実支出に含め、完了45 shadowの群削減率43.23%には含まれないことを明示する。全workflow純savingsはnull。
