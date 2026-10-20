> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/bounded-2.2.7-economic-confirmation.md). This report alone does not establish a task result.

# bounded 2.2.7 Economic Confirmation Cohort

集計: 2026-10-05T08:29:34.951448+00:00
判定: **SAFETY_REGRESSION**

## 1. Environment

Codex CLI: codex-cli 0.160.0 / gpt-6-sol / xhigh / Standard、全session independent・sequential。Qwen14 digest 9ec8897f747e246e970bc5cfdda85d22f1123dc2e3d34978a010a75968716849。fresh Ollama実証: True。API/version/GPU/driver/PID/ageはenvironment.jsonとtask boundary telemetryへ保存。generation probeなし。
Ollama API version: 0.35.1。fresh frontend/server PID: [16332, 20880]。GPU query (index / name / driver / total / used / free MiB / utilization / temperature / power): `0, NVIDIA GeForce RTX 3080, 591.86, 10240, 1103, 8949, 5, 58, 109.25`。固定generation options: `{"temperature": 0, "seed": 20260926, "num_ctx": 8192, "num_predict": 2048}`。num_ctx/output/context-char gateの引上げなし。

## 2. Task / category

14件の未使用business Taskを結果を見る前に7カテゴリ各2件へfreeze。REASONING categoryは小さい決定関数のcoding比較であり、read-only REASONING protocolへ変更したものではない。stateful 2件、他はfixed_slot。Routerは既存、Qwen14のみ既存experiment bindingで指定。Task/source/validation/typed referencesの変更はモデル実行前だけ。

| Task | category | business goal |
|---|---|---|
| ECC227-001 | STRICT_OUTPUT | Render exact two-line memory CSV sample |
| ECC227-002 | STRICT_OUTPUT | Render exact audit identity UTF-8 size receipt |
| ECC227-003 | COMPILE_SENSITIVE | Borrow nonempty warning slices without cloning |
| ECC227-004 | COMPILE_SENSITIVE | Split recorded reservations and call counts into typed columns |
| ECC227-005 | SEMANTIC_EDIT | Aggregate TCP samples while preserving unknown input |
| ECC227-006 | SEMANTIC_EDIT | Detect audit source payload allowance overflow |
| ECC227-007 | STATEFUL | Locate first audit row reporting an execution change |
| ECC227-008 | STATEFUL | Count exact source occurrences in sampled audit rows |
| ECC227-009 | DEBUGGING | Fix warning tail selection while preserving original order |
| ECC227-010 | DEBUGGING | Reject equal timestamps in strict audit chronology |
| ECC227-011 | REASONING | Classify verification set completeness with failure priority |
| ECC227-012 | REASONING | Detect duplicate positive PIDs in a process sample |
| ECC227-013 | SMALL_REFACTOR | Delegate warning count caption to existing count renderer |
| ECC227-014 | SMALL_REFACTOR | Delegate audit source width caption to existing byte renderer |

## 3. Baseline

全14件の独立Planner→blind clean Executor→7 mandatory checks＋scope/hash/freeze→独立reviewをLocal前に完成しBASELINE_FROZEN.jsonへ保存。Baseline実装をLocal/clean handoffへ渡していない。Task別baseline_componentsにPLANNER/EXECUTOR/REVIEWER/RETRYをdisjointに保存。追加call費用は必ず含める。

## 4. Raw Local First PASS

RAW_LOCAL_FIRST_PASS 2/6有効coding Task（Local実行 7件、freeze 14件）。raw body自身が契約と全validationを通った件だけ。Host/scope/infraで検証できなかったTaskと未実行TaskをモデルFAILへ加算しない。

## 5. LF canonicalization

LF_ELIGIBLE 1 / LF_APPLIED 1 / LF_VALIDATION_PASS 0 / LF_REVIEW_PASS 0。native 2.2.7のeligibility/+1 byteだけを使用。raw応答は不変、raw/normalized bodyのhashとbytesを別保存。

## 6. Workflow First PASS

CANONICALIZED_LOCAL_FIRST_PASS 0/6、WORKFLOW_FIRST_PASS 2/6。raw/canonicalizedは排他的。Local採用ACCEPT_NO_CHANGE 1件。モデルraw能力へHost救済を加算しない。

## 7. Local failures

LF_SEMANTIC_FAIL 1 / LF_LINT_FAIL 0。後者は実際のclippy::診断がある失敗で、Clippy実行中のcompile errorをlintと重複計上しない。実行済みLocal code generationは各Task1回、syntax/semantic/lint repair 0。coding failure・formatter unsupported・schema/output contract・INFRAを分離する。STOP以前のFirst FAIL/Local review rejectはclean initialからblind Codex direct。Local candidate/diagnostics/diff再利用なし。

| Task | Local status / reason | raw | LF applied | canonical PASS | review |
|---|---|---:|---:|---:|---|
| ECC227-001 | ESCALATE / CODE_FAILURE | False | False | False | clean handoff / N/A |
| ECC227-002 | PASS / TARGETED_CHECKS_PASSED | True | False | False | REJECT |
| ECC227-003 | ESCALATE / CODE_FAILURE | False | True | False | clean handoff / N/A |
| ECC227-004 | PASS / TARGETED_CHECKS_PASSED | True | False | False | ACCEPT_NO_CHANGE |
| ECC227-005 | ESCALATE / FORMAT_UNSUPPORTED_NORMALIZATION | False | False | False | clean handoff / N/A |
| ECC227-006 | ESCALATE / CODE_FAILURE | False | False | False | clean handoff / N/A |
| ECC227-007 | ESCALATE / HOST_FORMAT_ERROR | False | False | False | clean handoff / N/A |
| ECC227-008 | NOT_RUN / None | None | False | None | clean handoff / N/A |
| ECC227-009 | NOT_RUN / None | None | False | None | clean handoff / N/A |
| ECC227-010 | NOT_RUN / None | None | False | None | clean handoff / N/A |
| ECC227-011 | NOT_RUN / None | None | False | None | clean handoff / N/A |
| ECC227-012 | NOT_RUN / None | None | False | None | clean handoff / N/A |
| ECC227-013 | NOT_RUN / None | None | False | None | clean handoff / N/A |
| ECC227-014 | NOT_RUN / None | None | False | None | clean handoff / N/A |

## 8. Review quality

最終quality pair 6/14、FALSE_GREEN 1。両経路は同じfull checksと独立contract/diff review。Local PASS reviewはcompact packetのみ。raw conversationはreview/clean implementationへ渡さない。
Task002は全validation PASS後に独立reviewがREJECT。byte lengthをu32へcastしており、64bitで4,294,967,295 bytesを超える文字列の表示値を切り詰める。小さいacceptance fixtureはこの全入力域の欠陥を検出できなかった。候補は採用せず、clean initial sourceから独立Codexが直接実装した。既存acceptance/Task Spec/Local結果は変更していない。

## 9. Complete accounting coverage

COMPLETE_ECONOMIC_PAIR **3/14 (21.43%)**、目標90%。STARTがある全callを数え、turn.completed欠測はnull。成功retry usageで元失敗callを埋めない。partial source completionのquality PASSもeconomic completenessとは別。Primaryはcomplete pairだけ。
PROVIDER_CAPACITY_ERROR 6件、source編集後completion欠測 1件。usage欠測session: `["codex/B/ECC227-001/reviews/01", "codex/B/ECC227-003/implementation-01", "codex/planner/ECC227-005/plan", "codex/B/ECC227-007/reviews/02", "codex/B/ECC227-008/reviews/01", "codex/B/ECC227-010/implementation-01"]`。候補生成前のcapacityには同一入力のfresh exact retryを最大1回だけ使用。追加Taskで欠測を置換していない。

## 10. Raw Codex usage

各callのevents.jsonlとEND.jsonにraw turn.completed、input/cached/uncached/output/totalを保存。task-results.jsonのphase_usageへ全call合算・call数・skipped・missing_usageを保存。0 callの論理費用0と0 measured tokensを区別（skipped phase usage=null）。

## 11. Credits

公式Codex pricing（元資料: http[LOCAL_PATH]）を 2026-10-05T07:04:34.291689+00:00 にfreeze。uncached/cached/output: [50.0, 5.0, 250.0] credits / 1M。raw source/URL/timestamp/SHA256付き。uncached=input−cached、3種token rateで算出。実請求やsubscription debitの確認ではない。

| Task | accounting | B credits | A credits | saved | reduction |
|---|---|---:|---:|---:|---:|
| ECC227-001 | INCOMPLETE_ACCOUNTING | null | 4.52331 | null | null% |
| ECC227-002 | COMPLETE_ECONOMIC_PAIR | 2.94579 | 3.02470 | -0.07891 | -2.68% |
| ECC227-003 | INCOMPLETE_ACCOUNTING | null | 2.69112 | null | null% |
| ECC227-004 | COMPLETE_ECONOMIC_PAIR | 3.38248 | 1.72151 | 1.66097 | 49.11% |
| ECC227-005 | INCOMPLETE_ACCOUNTING | null | null | null | null% |
| ECC227-006 | COMPLETE_ECONOMIC_PAIR | 2.30985 | 3.14737 | -0.83752 | -36.26% |
| ECC227-007 | NOT_PAIRED | null | null | null | null% |
| ECC227-008 | NOT_PAIRED | null | null | null | null% |
| ECC227-009 | NOT_PAIRED | 4.62207 | null | null | null% |
| ECC227-010 | NOT_PAIRED | null | null | null | null% |
| ECC227-011 | NOT_PAIRED | 5.41712 | null | null | null% |
| ECC227-012 | NOT_PAIRED | 2.40847 | null | null | null% |
| ECC227-013 | NOT_PAIRED | 4.27782 | null | null | null% |
| ECC227-014 | NOT_PAIRED | 2.70745 | null | null | null% |

Primary complete pair: **8.63812 → 7.89358 credits**、saved **0.74454**、reduction **8.62%**。欠測pairは分母/合計から除外し、全14件の総額を推定しない。

## 12. LF-specific credits

Complete pair内 RAW_PASS_CREDITS_SAVED=1.66097、LF_CANONICALIZED_CREDITS_SAVED=null（0件）、FIRST_FAIL_CREDIT_DELTA=A−B=0.83752。LF採用でskipしたCodex implementationと独立Local reviewをmatched baselineへ比較。局所的counterfactualであり一般因果へ外挿しない。

## 13. Planner-inclusive economics

上記Primaryは共通Plannerを両側へ含む。Executor＋Reviewerのみでは 6.19242 → 5.44788、saved 0.74454 / 12.02%。共通Plannerはabsolute savingsで相殺、rateの分母には含める。Local native contract promptは改変せず、共有PlannerはHostのplanning artifactとして保存・費用算入し、Codex Executorへ同じplanを供給。

## 14. USD equivalent

公式GPT-6 Sol（元資料: http[LOCAL_PATH]）のinput/cached/output rate [2.0, 0.2, 10.0] USD/1MでCLI usageのread/output換算。Primary USD_EQUIVALENT_USED={'Codex_only': 0.34552479999999997, 'Local_routed': 0.3157432}, USD_EQUIVALENT_SAVED=0.02978。raw eventにcache_write_input_tokens等の追加fieldがある場合もそのまま保存している。今回の換算はfreezeした3種rateのみであり、別途cache-write課金を含むAPI invoiceの再現ではない。

## 15. JPY status

JPY_PER_CREDIT=null、JPY_SAVED=null。user accountのJPY換算を確認できていないため為替・USD・一般credit購入価格から推定しない。

## 16. Host workload

Host準備checks 30件 / 160.763秒（freeze前のfixture/static準備失敗も保存）。Task別mandatory validation count/wall、LF count/bytes、formatter LOC、Coverage/ReferencePlan/issued packet bytesをtask-results.jsonへ記録。合計: `{"Local_validation_count": 35, "Local_validation_seconds": 166.48399999999998, "Codex_only_validation_count": 105, "Codex_only_validation_seconds": 785.1739999999845, "Clean_handoff_validation_count": 35, "Clean_handoff_validation_seconds": 270.00000000001455, "LF_canonicalization_count": 1, "LF_bytes_added": 1, "Host_formatting_LOC": 20, "Coverage_bytes": 33746, "ReferencePlan_bytes": 8747, "Reference_packet_bytes_total": 8216}`。
Local Worker合計 283.108秒。Local実usage `{"ollama_input_tokens": 8712, "ollama_output_tokens": 478, "ollama_cache_tokens": 1036}`。全実行分のCodex source LOC: baseline 14件 98、routed 6件 33（母数が異なるため削減率として比較しない）。quality pairの同一6件ではbaseline 43、routed 33 LOC。validationはWorker wallへ内包、二重加算しない。Codex phase wallと実intervalはTask別JSON。token savingsとlatencyを別評価。

## 17. GPU / CUDA

Local INFRA 0 / CUDA 0 / cohort STOP True。fresh終了/startとTask before/during/afterにVRAM used/free、backend PID、API residency、frontend creation/age、Event Logをread-only保存。generation probe/Gemma12/別model/fallback/driver update等なし。provider capacityをLocal coding/infra失敗へ混ぜない。
STOP: `{"timestamp": "2026-10-05T08:11:02.404688+00:00", "task_id": "ECC227-007", "reason": "HOST_FORMAT_ERROR", "cuda": false, "backend_crash": false, "gpu_query_hang": false, "issues": [], "unstarted": ["ECC227-008", "ECC227-009", "ECC227-010", "ECC227-011", "ECC227-012", "ECC227-013", "ECC227-014"]}`。実行済みLocal 7/14、review/clean directが完了したquality pair 6/14。STOP後のLocal未実行 `["ECC227-008", "ECC227-009", "ECC227-010", "ECC227-011", "ECC227-012", "ECC227-013", "ECC227-014"]` はNOT_RUNのまま保存。

## 18. Safety

Host failure 1 / scope failure 0 / FALSE_GREEN 1。全旧tracked/untracked hash、native raw HTTPとexact body byte、session trace/blinding、runtime/source/registry/Router freezeはaudit.json。private copyは完全なOS sandboxではない。production反映なし。
STOP_ANALYSIS.jsonにTask007のraw診断とdiffを保存。モデルが初期bodyのlet行だけを置換してNoneを残し、rustfmtはexpected semicolon / found Noneを返した。Hostはunsupported/unbound診断としてHOST_FORMAT_ERRORを維持し、fail closedで停止。native分類の書換え・STOP解除・追加Local実行は行わない。Host readiness gateは未達だが、この停止だけからLF byte改変、scope escape、安全性regressionが起きたとは断定しない。
必須production regressionはregression/summary.jsonへ保存。Worker suite、Rust fmt/clippy/test/check/buildを実行し、固定runtimeを維持した。

## 19. Limitations

14件の小さいpure helper/display/refactorに対するheld-out標本。一般model能力ランキングではない。新規businessでもHostがsignatureとacceptanceを準備しており、Host coordinatorの設計/調査/validation準備/audit/集計tokens・credits・active timeはnull。したがって全労働コストのnet削減は主張しない。C: Codex copies / D: Local copiesのstorage/cache差、generationばらつき、capacityによる欠測選択の影響がある。

## 20. Decision

**SAFETY_REGRESSION**。READYはaccounting>=90%、品質・safety・INFRA条件と新Task LF再現、Primary/ LF-specific credits正の全条件を要求。未達条件があればREADYとしない。Protocol/router/prompt/formatter/repair/budgetを途中で変えず、production adoption/追加cohortは自動実行しない。
SAFETY_REGRESSIONは本cohortのFALSE_GREEN=0条件違反を示す採用判定。Task002の欠陥はLF補完を使用していないraw候補で起きており、LF canonicalization自身がbyte/scopeを破壊したという意味ではない。Host STOP、会計欠測、LF救済PASS未再現も独立したREADY未達要因として保持する。
