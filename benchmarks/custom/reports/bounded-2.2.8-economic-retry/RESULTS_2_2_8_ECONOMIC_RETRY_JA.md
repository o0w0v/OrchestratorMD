> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/bounded-2.2.8-economic-retry.md). This report alone does not establish a task result.

# bounded 2.2.8 Economic Retry

集計: 2026-10-05T16:45:29.116291+00:00
判定: **INCONCLUSIVE**

両経路の最終品質は14/14、Local採用は6/14。完全会計は11/14 (78.57%)で90%目標未達のため、READYにはしない。
完全会計ペア内のPlanner込みcredits削減は6.46%。Host準備のCodex費用は未測定で、workflow全体のnet削減は未確定。

## 1. preflight/review availability

送信はユーザーが本cohort範囲で明示承認。独立GPT-6 Sol reviewは初回capacity error（回答/usageなし）を保存後、同条件exact retry1回でACCEPT_NO_CHANGE。原packet 8,372 bytes、source hash/trace/usage保存。preflightは評価Task/Primary pairへ含めず共通開始コストとして別記。初回MANUAL_ACTION_REQUIRED STOPとPREFLIGHT_RELEASEを両方保持。

## 2. environment

codex-cli 0.160.0 / gpt-6-sol / xhigh / Standard。全role independent、sequential、resume/forkなし。Qwen14 digest `9ec8897f747e246e970bc5cfdda85d22f1123dc2e3d34978a010a75968716849`。Ollama環境: `{"version": "0.35.1"}`、fresh PID `[46564, 43428]`。固定generation options `{"temperature": 0, "seed": 20260926, "num_ctx": 8192, "num_predict": 2048}`、context char gate24000。詳細environment.json/quit-confirmed.json。

## 3. task/category

14未使用business Task、7カテゴリ各2件を両経路開始前にfreeze。初期acceptanceは14件すべてcompile-clean FAIL。13/14のpre-freeze helper scaffold整合と準備失敗も保持。REASONINGは小さい判断関数のcoding比較。STATEFUL2件はdiscovery、その他fixed_slot。Router設定変更なし、Qwen14は既存experiment binding。

| Task | category | business goal |
|---|---|---|
| ECR228-001 | STRICT_OUTPUT | Render audit execution presence tally as a fixed three-line receipt |
| ECR228-002 | STRICT_OUTPUT | Render sampled disk and service availability as an exact nullable receipt |
| ECR228-003 | COMPILE_SENSITIVE | Borrow present audit events paired with their recorded schema versions |
| ECR228-004 | COMPILE_SENSITIVE | Borrow the first denied policy reason including an empty reason |
| ECR228-005 | SEMANTIC_EDIT | Compute per-observation RSS excess above an inclusive allowance |
| ECR228-006 | SEMANTIC_EDIT | Mark adjacent audit source transitions without trimming |
| ECR228-007 | STATEFUL | Locate the first confirmation policy that also has a recorded proposal |
| ECR228-008 | STATEFUL | Extract evidence row counts from HighLoad events without flattening |
| ECR228-009 | DEBUGGING | Remove audit latency narrowing while keeping inclusive budget equality |
| ECR228-010 | DEBUGGING | Advance a sampled display cursor without usize addition overflow |
| ECR228-011 | REASONING | Choose the least valid available-memory sample while rejecting incomplete validity |
| ECR228-012 | REASONING | Detect nondecreasing recorded risk sequence with ties permitted |
| ECR228-013 | SMALL_REFACTOR | Delegate disk availability caption to the protected optional-count renderer |
| ECR228-014 | SMALL_REFACTOR | Delegate evidence cleanup to the protected trimmed-item selector |

## 4. baseline

品質完成 14/14。Planner → clean Executor → 7 mandatory checks＋scope/hash → independent Reviewer ACCEPT_NO_CHANGE。全baseline freeze前にLocal生成なし。provider STOP `[]`。

## 5. raw Local First PASS

RAW_LOCAL_FIRST_PASS 3件。Local実行14/14、raw自身がapply/format/full validation/scopeを通過したもの。未実行・Host・INFRAは能力FAILへ加算しない。

## 6. LF First PASS

LF追加 6件、full validation PASS 4、canonicalized First PASS 4。既存native2.2.8の+1 byteだけ。raw/normalized byte/hashはaudit body proofs。

## 7. parse failures

CANDIDATE_SYNTAX_FAILURE 0 / compiler corroborated 0。native pinned rustfmt/rustc corroborationをそのまま使用。unknown/fail-closed HOST_FORMAT_ERROR 0（具体的causeはraw formatter record）。Host formatter failure 0、Local cohort STOP `null`。

## 8. semantic failures

Task別Local reason/failure_domainは下表・task-results.json。E0308等はparseへ降格しない。Local syntax/semantic/lint repair0。First FAILはfailed candidate/diff/diagnosticsを見せずclean sourceから独立Codex direct。

| Task | Local status/reason | raw | LF PASS | review | routed quality |
|---|---|---:|---:|---|---:|
| ECR228-001 | ESCALATE/CODE_FAILURE | False | False | None | True |
| ECR228-002 | ESCALATE/CODE_FAILURE | False | False | None | True |
| ECR228-003 | ESCALATE/FORMAT_UNSUPPORTED_NORMALIZATION | False | False | None | True |
| ECR228-004 | ESCALATE/CODE_FAILURE | False | False | None | True |
| ECR228-005 | ESCALATE/LINT_REPAIR_NOT_ELIGIBLE | False | False | None | True |
| ECR228-006 | PASS/TARGETED_CHECKS_PASSED | False | True | ACCEPT_NO_CHANGE | True |
| ECR228-007 | ESCALATE/NO_HANDLE_DISCOVERED | False | False | None | True |
| ECR228-008 | PASS/TARGETED_CHECKS_PASSED | False | True | ACCEPT_NO_CHANGE | True |
| ECR228-009 | PASS/TARGETED_CHECKS_PASSED | True | False | ACCEPT_NO_CHANGE | True |
| ECR228-010 | PASS/TARGETED_CHECKS_PASSED | True | False | REJECT | True |
| ECR228-011 | ESCALATE/CODE_FAILURE | False | False | None | True |
| ECR228-012 | PASS/TARGETED_CHECKS_PASSED | True | False | ACCEPT_NO_CHANGE | True |
| ECR228-013 | PASS/TARGETED_CHECKS_PASSED | False | True | ACCEPT_NO_CHANGE | True |
| ECR228-014 | PASS/TARGETED_CHECKS_PASSED | False | True | ACCEPT_NO_CHANGE | True |

## 9. validation false greens

LOCAL_VALIDATION_FALSE_GREEN 1。独立reviewが採用前に検出した有効contract defectを記録し、そのcandidateは採用せずclean direct。ECR228-010は(1, usize::MAX, 3)でcandidateの加算がoverflowし、exact resultは1。別の算術式replayで64-bit実toolchainのpanicを確認。固定Task/acceptanceは変更せず、証跡 `["ECR228-010.json"]` を追加保存。旧ECC227結果/SAFETY_REGRESSIONは不変。review concern原文はcodex/A-localのRESULTに保持。

## 10. final review quality

Routed最終品質 14/14、Local ACCEPT_NO_CHANGE採用 6。FINAL_PIPELINE_FALSE_GREEN=0（観測範囲、完全正当性の数学的証明ではない）。すべての採用に独立review要求。Local validation false greenと別集計。

## 11. complete accounting

COMPLETE_ECONOMIC_PAIR **11/14 (78.57%)**、目標90%。両経路品質完成＋全発生callのturn.completed実usageのみ。capacity error 3、欠測call `["codex/planner/ECR228-002/plan", "codex/A-clean/ECR228-005/implementation-01", "codex/planner/ECR228-009/plan"]`。元失敗usageをretryで補完しない。

## 12. raw usage

各START.json、events.jsonl、END.jsonにraw turn.completedとinput/cached/uncached/output/totalを保持。Task別phase_usageはPlanner/B/A-review/A-cleanを分離。未実行phaseはcalls0/skipped=true/usage=null。論理的な発生費用0と0 measured tokensを混同しない。coordinator tokensはnull。

## 13. credits

公式Codex pricing（元資料: http[LOCAL_PATH]）を2026-10-05T14:55:34.234841+00:00にraw document/URL/timestamp/SHA256付きfreeze。Standard uncached/cached/output [50.0, 5.0, 250.0] credits/1M。uncached=input−cached。Primaryはcomplete pair限定: **39.06378 → 36.53867**、saved **2.52511** / 6.46%。実invoice/subscription debit確認ではない。

| Task | accounting | B credits | A credits | saved | Codex LOC A/B |
|---|---|---:|---:|---:|---|
| ECR228-001 | COMPLETE_ECONOMIC_PAIR | 5.41207 | 4.38694 | 1.02513 | 20/14 |
| ECR228-002 | INCOMPLETE_ACCOUNTING | null | null | null | 9/11 |
| ECR228-003 | COMPLETE_ECONOMIC_PAIR | 3.22452 | 6.20762 | -2.98310 | 11/9 |
| ECR228-004 | COMPLETE_ECONOMIC_PAIR | 3.46662 | 3.31451 | 0.15211 | 6/8 |
| ECR228-005 | INCOMPLETE_ACCOUNTING | 6.93834 | null | null | 5/5 |
| ECR228-006 | COMPLETE_ECONOMIC_PAIR | 3.90623 | 1.94170 | 1.96453 | 0/9 |
| ECR228-007 | COMPLETE_ECONOMIC_PAIR | 3.75361 | 6.83502 | -3.08141 | 9/9 |
| ECR228-008 | COMPLETE_ECONOMIC_PAIR | 3.18508 | 1.96339 | 1.22169 | 0/7 |
| ECR228-009 | INCOMPLETE_ACCOUNTING | null | null | null | 0/2 |
| ECR228-010 | COMPLETE_ECONOMIC_PAIR | 2.33750 | 2.94814 | -0.61064 | 9/9 |
| ECR228-011 | COMPLETE_ECONOMIC_PAIR | 3.28415 | 3.33320 | -0.04905 | 13/13 |
| ECR228-012 | COMPLETE_ECONOMIC_PAIR | 3.06461 | 1.56096 | 1.50365 | 0/10 |
| ECR228-013 | COMPLETE_ECONOMIC_PAIR | 3.55421 | 1.87519 | 1.67902 | 0/5 |
| ECR228-014 | COMPLETE_ECONOMIC_PAIR | 3.87518 | 2.17200 | 1.70318 | 0/12 |

## 14. LF-specific economics

LF_REVIEW_ACCEPT 4、LF_REVIEW_REJECT 0、LF_CREDITS_SAVED=6.56842。下表はcomplete pairのみ。RAW_PASSの全採用2件のうち009は欠測のため除外。LF採用4件はすべて会計完成。

| group | complete pairs | B credits | A credits | saved | reduction |
|---|---:|---:|---:|---:|---:|
| RAW_PASS | 1 | 3.06461 | 1.56096 | 1.50365 | 49.06% |
| LF_CANONICALIZED_PASS | 4 | 14.52070 | 7.95228 | 6.56842 | 45.23% |
| LOCAL_VALIDATION_FALSE_GREEN | 1 | 2.33750 | 2.94814 | -0.61064 | -26.12% |
| LOCAL_FIRST_FAIL | 5 | 19.14097 | 24.07729 | -4.93632 | -25.79% |

## 15. planner-inclusive economics

共通Planner費用を両経路へ含むPrimaryと、Executor＋Reviewerのみを別表示。後者: 27.54636 → 25.02125、saved 2.52511。Planner absolute costは両側で相殺。Local native promptへPlanner出力を追加しない。

## 16. USD equivalent

公式GPT-6 Sol token pricing（元資料: http[LOCAL_PATH]）の[2.0, 0.2, 10.0] USD/1Mをfreeze。Primary baseline=1.56255、routed=1.46155、saved=0.10100。3種token rateの換算で、API cache-write等を含む実請求額ではない。

## 17. JPY status

user accountのJPY_PER_CREDIT未確認。JPY_PER_CREDIT=null / JPY_SAVED=null。為替や一般購入価格から推定しない。

## 18. Host workload

準備checks 30件 / 159.157秒。Coverage/ReferencePlanはensure_ascii JSON再serialized bytes、reference packetはnative記録のactual packet bytes。合計 `{"Coverage_bytes": 34024, "ReferencePlan_bytes": 11615, "reference_packet_bytes": 17994, "LF_bytes_added": 6, "Host_formatting_LOC": 20, "Local_validation_count": 84, "Local_validation_seconds": 446.266, "Baseline_validation_count": 105, "Baseline_validation_seconds": 744.0450000000274, "Clean_handoff_validation_count": 63, "Clean_handoff_validation_seconds": 456.8440000000119}`。Local tokens `{"ollama_input_tokens": 22232, "ollama_output_tokens": 1241, "ollama_cache_tokens": 6788}`、Worker 696.688秒。Worker wallにはLocal validationを内包し二重加算しない。Task別COMPONENT_WALLは記録済みphase wallの和、実active timeではない。cohort順番待ちやHost手動作業を含む全労働コストはnull。

## 19. GPU/CUDA

INFRA_ERROR 0、CUDA 0。観測値 `{"observations": 663, "gpu_names": ["NVIDIA GeForce RTX 3080"], "driver_versions": ["591.86"], "peak_used_mib": 9904.0, "minimum_free_mib": 148.0, "residency_mismatch_count": 0, "gpu_query_timeout_count": 0}`。VRAM使用量だけからOOMや原因を推定しない。fresh frontend条件はenvironment/quit-confirmedへ保存。Task前/during/後のGPU/API/VRAM/residency/backendPID、保存CIMからfrontend age、Windows events/logsをtask-boundaries.json/gpu-telemetry.csvへ整理。Local STOP後に自動restart/救済なし。

## 20. safety

Host failures 0、scope 0、trace flags `[]`。旧tracked/untracked hash、runtime35 files、digest、budget、実rawLF byte、independent sessions/blindingをaudit。root Worker/Rust regressionはregression/summary。Private copyは完全なOS containmentの主張ではない。Router/Pilot/applicationへのproduction採用なし。

## 21. limitations

14件の小さいpure helper/display/refactorの標本、モデル一般ランキングではない。Hostの仕様/scaffold/acceptance設計・集計・監査のCodex tokens/active timeは未測定null。共通開始preflightのcapacity欠測コストも別保持し、14 pairのPrimaryへ無測定値を混入しない。cache温まり/順番/C:vsD: storage・外部capacityによる選択欠測がある。A-cleanの003/007はformatter unsupportedで2回必要だった一方、各baselineは1回だった。同じ契約の独立Codex実装にもattempt差があり、First FAIL群の費用増をLocal候補閲覧のoverheadへ帰属しない（候補は渡していない）。creditsはprovider raw usageと公式rateの換算であり、全労働/電力/実invoiceのnet削減は主張しない。

## 22. decision

**INCONCLUSIVE**。READY条件成立=False。complete>=90%、最終品質、final false green0、Host/scope/CUDA/INFRA0、独立採用review、新規raw/LF PASS、aggregate正、LF-specific非負を同時要求。未達項目を成功扱いしない。今回Protocol tuning・追加Local retry・model切替・production採用は行わない。
