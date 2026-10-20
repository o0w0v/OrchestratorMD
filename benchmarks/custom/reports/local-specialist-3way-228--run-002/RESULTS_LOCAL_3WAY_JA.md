> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/local-specialist-3way-228--run-002.md). This report alone does not establish a task result.

# Local Specialist 3-Way Challenger Benchmark

集計: 2026-10-06T12:04:14.105797+00:00

判定: **INCONCLUSIVE**。Productionへの反映なし。

## 1. Model identities

| Arm | Model | Digest | Quantization | Size bytes |
| --- | --- | --- | --- | --- |
| qwen14 | qwen2.5-Coder:14b | 9ec8897f747e246e970bc5cfdda85d22f1123dc2e3d34978a010a75968716849 | Q4_K_M | 8988124298 |
| qwen35 | qwen3.5:9b | 56671c2ab9385f9cfcb404638e32cd62d88e3501d44822208363c010179a3c90 | Q4_K_M | 6550825550 |
| gemma26 | gemma4:26b | 08ae7ec1744bd7f451c4a530afb39d2673ad9d07a8369b8a33a3613b41212a68 | Q4_K_M | 18604148513 |

Qwen3.5 licenseはinstalled manifestのlicense layerにあるApache 2.0。全identityはmodel-identities.jsonと各cohort installed-shows.jsonから追跡可能。Gemma12/CoderNext使用なし。

## 2. Environment

RTX 3080 10GB。各model cohortにuser tray Quit→process/API/port/residency終了確認→installed Ollama fresh start→models=[]を要求。実version、frontend PID/creation、driver/GPU/VRAMとbinary SHAはlocal/<model>/environment.json。OS/driver/runtime/settings変更、download、generation health probeなし。

## 3. Task / family

| Task | Family | Business goal |
| --- | --- | --- |
| LS3W228-001 | COLLECTION | Collect direct child process IDs for one selected parent |
| LS3W228-002 | COLLECTION | Collect sources of explicitly changed executions |
| LS3W228-003 | COLLECTION | Collect intent IDs for explicitly denied policies |
| LS3W228-004 | COLLECTION | Project warning UTF-8 byte lengths without filtering |
| LS3W228-005 | COLLECTION | Collect targets of high-risk action proposals |
| LS3W228-006 | COLLECTION | Locate executed audit rows with no verification object |
| LS3W228-007 | NUMERIC | Compute observed process RSS spread in KiB |
| LS3W228-008 | NUMERIC | Compute remaining inference-call allowance with saturation |
| LS3W228-009 | NUMERIC | Accumulate audit inference elapsed milliseconds saturating at u128 |
| LS3W228-010 | NUMERIC | Compute available-memory integer percentage safely |
| LS3W228-011 | NUMERIC | Accumulate byte size of intent constraint strings |
| LS3W228-012 | NUMERIC | Find minimum age among observed event rows |
| LS3W228-013 | ADAPTER | Forward optional verification to protected status formatter |
| LS3W228-014 | ADAPTER | Forward wide elapsed milliseconds to protected seconds conversion |
| LS3W228-015 | ADAPTER | Delegate proposal reversibility label to protected boolean helper |
| LS3W228-016 | ADAPTER | Delegate reserved-token presence to protected predicate |
| LS3W228-017 | ADAPTER | Delegate observation epoch bucket to two-argument protected helper |
| LS3W228-018 | ADAPTER | Delegate proposal evidence bytes to protected slice helper |
| LS3W228-019 | RECEIPT | Render inference calls and reserved tokens in one exact receipt |
| LS3W228-020 | RECEIPT | Render empty versus nonempty warning inventory receipt |
| LS3W228-021 | RECEIPT | Render three-state event evidence presence receipt |
| LS3W228-022 | RECEIPT | Render verification scope byte length without exposing text |
| LS3W228-023 | RECEIPT | Render intent identity and requester byte sizes in exact receipt |
| LS3W228-024 | RECEIPT | Render process observation completeness flag receipt |

各family 6件。歴史source-plansのtitle/functionとの衝突を確認し、新規fixtureを作成。Task/source/acceptance/regression/ReferencePlan/Coverage/risksと全3 armをFREEZE.jsonで固定。実顧客ticketではなく、既存business型上のheld-out単一挙動fixture。全初期stubはcompile成功・acceptance RED。

## 4. Shared Codex baseline

各Task一度だけgpt-6-sol/xhigh/Standardの独立Planner→clean Executor→full mandatory validation→independent Reviewer。ACCEPT_NO_CHANGEを完成条件とし、BASELINE_FROZEN.jsonを全Local前に保存。baseline solutionはLocal/clean handoffへ露出しない。

| Task | Quality | Credits | Wall seconds |
| --- | --- | --- | --- |
| LS3W228-001 | ACCEPT_NO_CHANGE | 4.554170 | 138.313000 |
| LS3W228-002 | ACCEPT_NO_CHANGE | 4.691830 | 202.734000 |
| LS3W228-003 | ACCEPT_NO_CHANGE | 5.741910 | 192.234000 |
| LS3W228-004 | ACCEPT_NO_CHANGE | 3.741420 | 135.219000 |
| LS3W228-005 | ACCEPT_NO_CHANGE | 3.706690 | 160.781000 |
| LS3W228-006 | ACCEPT_NO_CHANGE | 4.031450 | 158.469000 |
| LS3W228-007 | ACCEPT_NO_CHANGE | 4.472350 | 166.235000 |
| LS3W228-008 | ACCEPT_NO_CHANGE | 3.731450 | 151.937000 |
| LS3W228-009 | ACCEPT_NO_CHANGE | 2.312450 | 143.906000 |
| LS3W228-010 | ACCEPT_NO_CHANGE | 2.643590 | 171.532000 |
| LS3W228-011 | ACCEPT_NO_CHANGE | 3.748170 | 206.437000 |
| LS3W228-012 | ACCEPT_NO_CHANGE | 3.948260 | 142.406000 |
| LS3W228-013 | ACCEPT_NO_CHANGE | 2.224010 | 140.797000 |
| LS3W228-014 | ACCEPT_NO_CHANGE | 3.520740 | 147.031000 |
| LS3W228-015 | ACCEPT_NO_CHANGE | 2.865280 | 142.734000 |
| LS3W228-016 | ACCEPT_NO_CHANGE | 2.523620 | 147.266000 |
| LS3W228-017 | ACCEPT_NO_CHANGE | 3.618870 | 164.125000 |
| LS3W228-018 | ACCEPT_NO_CHANGE | 3.173220 | 152.922000 |
| LS3W228-019 | ACCEPT_NO_CHANGE | 3.112030 | 158.656000 |
| LS3W228-020 | ACCEPT_NO_CHANGE | 3.070520 | 163.360000 |
| LS3W228-021 | ACCEPT_NO_CHANGE | 4.021480 | 177.750000 |
| LS3W228-022 | ACCEPT_NO_CHANGE | 2.792440 | 169.875000 |
| LS3W228-023 | ACCEPT_NO_CHANGE | 2.457580 | 153.328000 |
| LS3W228-024 | ACCEPT_NO_CHANGE | 2.580820 | 140.843000 |

## 5. qwen14 results

```json
{
  "model": "qwen2.5-Coder:14b",
  "planned": 24,
  "ATTEMPTS": 0,
  "RAW_PASS": 0,
  "LF_RESCUE": 0,
  "ADOPTED": 0,
  "FIRST_FAIL": 0,
  "VALIDATION_FALSE_GREEN": 0,
  "FINAL_PIPELINE_FALSE_GREEN": 0,
  "BASELINE_CREDITS": 83.28435,
  "ROUTED_CREDITS": null,
  "CREDITS_SAVED": null,
  "REDUCTION_RATE": null,
  "AVERAGE_CREDITS_SAVED_PER_TASK": null,
  "AVERAGE_CREDITS_SAVED_PER_ADOPTED_TASK": null,
  "total_saved_per_adoption": null,
  "RAW_ADOPTED": 0,
  "LF_RESCUED_ADOPTED": 0,
  "LF_DEPENDENCY_RATE": null,
  "CUDA": 0,
  "INFRA_ERROR": 0,
  "backend_crash": 0,
  "GPU_query_timeout": 0,
  "accounting_complete_tasks": 0,
  "Local_gate_wall": {
    "n": 0,
    "mean": null,
    "median": null,
    "minimum": null,
    "maximum": null
  },
  "Ollama_API_wall": {
    "n": 0,
    "mean": null,
    "median": null,
    "minimum": null,
    "maximum": null
  },
  "total_routed_wall": {
    "n": 0,
    "mean": null,
    "median": null,
    "minimum": null,
    "maximum": null
  },
  "Host_validation_seconds": 0,
  "USD_EQUIVALENT_SAVED": null,
  "JPY_SAVED": null
}
```

過去coding/Host STOP結果は今回分母に混入しない。

## 6. gemma26 results

```json
{
  "model": "gemma4:26b",
  "planned": 24,
  "ATTEMPTS": 0,
  "RAW_PASS": 0,
  "LF_RESCUE": 0,
  "ADOPTED": 0,
  "FIRST_FAIL": 0,
  "VALIDATION_FALSE_GREEN": 0,
  "FINAL_PIPELINE_FALSE_GREEN": 0,
  "BASELINE_CREDITS": 83.28435,
  "ROUTED_CREDITS": null,
  "CREDITS_SAVED": null,
  "REDUCTION_RATE": null,
  "AVERAGE_CREDITS_SAVED_PER_TASK": null,
  "AVERAGE_CREDITS_SAVED_PER_ADOPTED_TASK": null,
  "total_saved_per_adoption": null,
  "RAW_ADOPTED": 0,
  "LF_RESCUED_ADOPTED": 0,
  "LF_DEPENDENCY_RATE": null,
  "CUDA": 0,
  "INFRA_ERROR": 0,
  "backend_crash": 0,
  "GPU_query_timeout": 0,
  "accounting_complete_tasks": 0,
  "Local_gate_wall": {
    "n": 0,
    "mean": null,
    "median": null,
    "minimum": null,
    "maximum": null
  },
  "Ollama_API_wall": {
    "n": 0,
    "mean": null,
    "median": null,
    "minimum": null,
    "maximum": null
  },
  "total_routed_wall": {
    "n": 0,
    "mean": null,
    "median": null,
    "minimum": null,
    "maximum": null
  },
  "Host_validation_seconds": 0,
  "USD_EQUIVALENT_SAVED": null,
  "JPY_SAVED": null
}
```

過去coding/Host STOP結果は今回分母に混入しない。

## 7. qwen35 results

```json
{
  "model": "qwen3.5:9b",
  "planned": 24,
  "ATTEMPTS": 0,
  "RAW_PASS": 0,
  "LF_RESCUE": 0,
  "ADOPTED": 0,
  "FIRST_FAIL": 0,
  "VALIDATION_FALSE_GREEN": 0,
  "FINAL_PIPELINE_FALSE_GREEN": 0,
  "BASELINE_CREDITS": 83.28435,
  "ROUTED_CREDITS": null,
  "CREDITS_SAVED": null,
  "REDUCTION_RATE": null,
  "AVERAGE_CREDITS_SAVED_PER_TASK": null,
  "AVERAGE_CREDITS_SAVED_PER_ADOPTED_TASK": null,
  "total_saved_per_adoption": null,
  "RAW_ADOPTED": 0,
  "LF_RESCUED_ADOPTED": 0,
  "LF_DEPENDENCY_RATE": null,
  "CUDA": 0,
  "INFRA_ERROR": 0,
  "backend_crash": 0,
  "GPU_query_timeout": 0,
  "accounting_complete_tasks": 0,
  "Local_gate_wall": {
    "n": 0,
    "mean": null,
    "median": null,
    "minimum": null,
    "maximum": null
  },
  "Ollama_API_wall": {
    "n": 0,
    "mean": null,
    "median": null,
    "minimum": null,
    "maximum": null
  },
  "total_routed_wall": {
    "n": 0,
    "mean": null,
    "median": null,
    "minimum": null,
    "maximum": null
  },
  "Host_validation_seconds": 0,
  "USD_EQUIVALENT_SAVED": null,
  "JPY_SAVED": null
}
```

過去coding/Host STOP結果は今回分母に混入しない。

## 8. Raw First PASS

| Model | Attempts | RAW_PASS | RAW_ADOPTED |
| --- | --- | --- | --- |
| qwen14 | 0 | 0 | 0 |
| qwen35 | 0 | 0 | 0 |
| gemma26 | 0 | 0 | 0 |

## 9. Final-LF rescue

| Model | LF_RESCUE | LF_RESCUED_ADOPTED |
| --- | --- | --- |
| qwen14 | 0 | 0 |
| qwen35 | 0 | 0 |
| gemma26 | 0 | 0 |

唯一のmissing-final-LFのみraw+exactly one 0x0A。監査はraw/normalized byte一致を確認。他format/semantic修正で救済していない。

## 10. Independent review quality

Local Host PASSは独立compact reviewへ送り、ACCEPT_NO_CHANGEのみ採用。FAIL/REJECTは別のclean initial source/contract/shared planへhandoff。Local candidate/diff/diagnostics、baseline implementationはExecutorに含めない。全conversationをreviewに渡していない。session/prompt/input SHAとblindingはpre-send/、blinding/、codex/に保存。

## 11. False greens

| Model | Local validation false green | Final pipeline false green |
| --- | --- | --- |
| qwen14 | 0 | 0 |
| qwen35 | 0 | 0 |
| gemma26 | 0 | 0 |

Local検証PASS後のreview REJECTは採用前defectとして分離。最終qualityは同じmandatory checksと独立review。テストだけで完全正しさを証明したとはしない。

## 12. Task-by-Task 3-way

| Task | Qwen14 adopted | Qwen3.5 adopted | Gemma26 adopted | Outcome | Cheapest final-quality workflow |
| --- | --- | --- | --- | --- | --- |
| LS3W228-001 | null | null | null | NOT_COMPLETE | null |
| LS3W228-002 | null | null | null | NOT_COMPLETE | null |
| LS3W228-003 | null | null | null | NOT_COMPLETE | null |
| LS3W228-004 | null | null | null | NOT_COMPLETE | null |
| LS3W228-005 | null | null | null | NOT_COMPLETE | null |
| LS3W228-006 | null | null | null | NOT_COMPLETE | null |
| LS3W228-007 | null | null | null | NOT_COMPLETE | null |
| LS3W228-008 | null | null | null | NOT_COMPLETE | null |
| LS3W228-009 | null | null | null | NOT_COMPLETE | null |
| LS3W228-010 | null | null | null | NOT_COMPLETE | null |
| LS3W228-011 | null | null | null | NOT_COMPLETE | null |
| LS3W228-012 | null | null | null | NOT_COMPLETE | null |
| LS3W228-013 | null | null | null | NOT_COMPLETE | null |
| LS3W228-014 | null | null | null | NOT_COMPLETE | null |
| LS3W228-015 | null | null | null | NOT_COMPLETE | null |
| LS3W228-016 | null | null | null | NOT_COMPLETE | null |
| LS3W228-017 | null | null | null | NOT_COMPLETE | null |
| LS3W228-018 | null | null | null | NOT_COMPLETE | null |
| LS3W228-019 | null | null | null | NOT_COMPLETE | null |
| LS3W228-020 | null | null | null | NOT_COMPLETE | null |
| LS3W228-021 | null | null | null | NOT_COMPLETE | null |
| LS3W228-022 | null | null | null | NOT_COMPLETE | null |
| LS3W228-023 | null | null | null | NOT_COMPLETE | null |
| LS3W228-024 | null | null | null | NOT_COMPLETE | null |

cheapestはreview/clean directまで含む最終品質PASS workflowの後知恵oracle。production Routerへ直接使わない。

## 13. Family adoption

| Family | Model | Attempts | Raw | LF | Adopted | First FAIL | Validation FG |
| --- | --- | --- | --- | --- | --- | --- | --- |
| COLLECTION | qwen14 | 0 | 0 | 0 | 0 | 0 | 0 |
| COLLECTION | qwen35 | 0 | 0 | 0 | 0 | 0 | 0 |
| COLLECTION | gemma26 | 0 | 0 | 0 | 0 | 0 | 0 |
| NUMERIC | qwen14 | 0 | 0 | 0 | 0 | 0 | 0 |
| NUMERIC | qwen35 | 0 | 0 | 0 | 0 | 0 | 0 |
| NUMERIC | gemma26 | 0 | 0 | 0 | 0 | 0 | 0 |
| ADAPTER | qwen14 | 0 | 0 | 0 | 0 | 0 | 0 |
| ADAPTER | qwen35 | 0 | 0 | 0 | 0 | 0 | 0 |
| ADAPTER | gemma26 | 0 | 0 | 0 | 0 | 0 | 0 |
| RECEIPT | qwen14 | 0 | 0 | 0 | 0 | 0 | 0 |
| RECEIPT | qwen35 | 0 | 0 | 0 | 0 | 0 | 0 |
| RECEIPT | gemma26 | 0 | 0 | 0 | 0 | 0 | 0 |

## 14. Family paired economics

| Family | Model | Baseline credits | Routed credits | Saved | Reduction rate |
| --- | --- | --- | --- | --- | --- |
| COLLECTION | qwen14 | 26.467470 | null | null | null |
| COLLECTION | qwen35 | 26.467470 | null | null | null |
| COLLECTION | gemma26 | 26.467470 | null | null | null |
| NUMERIC | qwen14 | 20.856270 | null | null | null |
| NUMERIC | qwen35 | 20.856270 | null | null | null |
| NUMERIC | gemma26 | 20.856270 | null | null | null |
| ADAPTER | qwen14 | 17.925740 | null | null | null |
| ADAPTER | qwen35 | 17.925740 | null | null | null |
| ADAPTER | gemma26 | 17.925740 | null | null | null |
| RECEIPT | qwen14 | 18.034870 | null | null | null |
| RECEIPT | qwen35 | 18.034870 | null | null | null |
| RECEIPT | gemma26 | 18.034870 | null | null | null |

## 15. Total credits

| Model | Same-task baseline | Local routed | Actual own arm cost excluding shared plan |
| --- | --- | --- | --- |
| qwen14 | 83.284350 | null | null |
| qwen35 | 83.284350 | null | null |
| gemma26 | 83.284350 | null | null |

全実session ledger: 83.284350 credits / 72 calls。Plannerは実支払いで一度だけ数える。paired各workflowには同じ実Planner feeを対称配賦しているため、arm totalsの単純和は実請求ledgerと異なる。公式Standard rates uncached/cached/output: [50.0, 5.0, 250.0] /1M。raw URL/time/SHAはrates/rate-card.json。

## 16. Credits saved

| Model | Saved | Reduction | Mean saved/task | Mean saved/adopted task |
| --- | --- | --- | --- | --- |
| qwen14 | null | null | null | null |
| qwen35 | null | null | null | null |
| gemma26 | null | null | null | null |

FULL_4_WAY_ECONOMIC_TASK=0/24、coverage=0.00%。欠測usageはnull、推定なし。Actual CLI turn.completed/raw_usageを保存。

## 17. USD equivalent / JPY

| Model | USD equivalent saved | JPY saved |
| --- | --- | --- |
| qwen14 | null | null |
| qwen35 | null | null |
| gemma26 | null | null |

公式token USD rates [2.0, 0.2, 10.0] /1Mに基づく等価値で、subscription実請求額ではない。API cache-write課金はCLI raw usageから測れず含めない。JPY_PER_CREDIT未取得。

## 18. GPU / VRAM / CUDA

| Model | Peak used MiB | Minimum free MiB | Mean loaded used MiB | CUDA | Crash | Timeout | Mismatch | Invalid samples |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| qwen14 | null | null | null | 0 | 0 | 0 | 0 | 0 |
| qwen35 | null | null | null | 0 | 0 | 0 | 0 | 0 |
| gemma26 | null | null | null | 0 | 0 | 0 | 0 | 0 |

GPU/ollama-residency.csvは別々の観測。physically invalid rawは保持しderived=null。backend PID lifecycle/frontend ageはGPU_SUMMARY.json、raw process command/Ollama log/Event Logはlocal/<model>/infrastructure/。VRAM高使用だけでOOMとは断定しない。

## 19. Latency

| Family | Model | Mean Local gate sec | Mean Ollama API sec | Mean routed wall sec |
| --- | --- | --- | --- | --- |
| COLLECTION | qwen14 | null | null | null |
| COLLECTION | qwen35 | null | null | null |
| COLLECTION | gemma26 | null | null | null |
| NUMERIC | qwen14 | null | null | null |
| NUMERIC | qwen35 | null | null | null |
| NUMERIC | gemma26 | null | null | null |
| ADAPTER | qwen14 | null | null | null |
| ADAPTER | qwen35 | null | null | null |
| ADAPTER | gemma26 | null | null | null |
| RECEIPT | qwen14 | null | null | null |
| RECEIPT | qwen35 | null | null | null |
| RECEIPT | gemma26 | null | null | null |

共通Planner wallはrouted wallから除外し、baseline wallには初回Plannerが含まれる。phase別raw wallで補正可能。速度は副指標、異なるモデル間でTask中switchなし。Host validation secondsもSUMMARY.jsonに分離。

## 20. Infrastructure status

| Model | Status |
| --- | --- |
| qwen14 | INCONCLUSIVE |
| qwen35 | INCONCLUSIVE |
| gemma26 | INCONCLUSIVE |

CUDA/backend crashはそのmodel cohortを停止し、他model coding failureへ波及させない。自動restart/retryなし。安定は観測した当PC/有限24 call条件に限定。

## 21. LF dependency

| Model | Raw adopted | LF adopted | LF dependency |
| --- | --- | --- | --- |
| qwen14 | 0 | 0 | null |
| qwen35 | 0 | 0 | null |
| gemma26 | 0 | 0 | null |

## 22. Family winners

| Family | Highest adoption | Highest credit saving | Stable models |
| --- | --- | --- | --- |
| COLLECTION |  |  |  |
| NUMERIC |  |  |  |
| ADAPTER |  |  |  |
| RECEIPT |  |  |  |

Infra 0件同士は同率であり、大きなVRAM余裕だけでGPU stability winnerと断定しない。

## 23. Proposed mixed Router

| Family | Candidate |
| --- | --- |
| COLLECTION | null |
| NUMERIC | null |
| ADAPTER | null |
| RECEIPT | null |

Quality/finalFG→stable infrastructure→adoption→credits→latency→headroomの優先順。candidateは有限sampleの提案のみ。production設定は未変更。

## 24. Limitations

各family6件、固定model順で時間/provider cacheの交絡あり。Taskは既存型上の小fixtureで一般能力ランキングではない。CodeX usageはCLI sessionのみ実測、coordinatorのTask/Host設計・artifact作成usageとactive timeはnullでnet savingsへ推定加算しない。共有planningの配賦と実ledgerを分離。private copiesは絶対OS sandboxではない。過去preflight STOPと旧結果は保持。全production/runtime/旧tracked/untracked source evidenceのhash保全とrequired regressionsはaudit.json/regression/を参照。

## 25. Decision

**INCONCLUSIVE**。3-way workflow costを比較した実験結果であり、自動採用・Router変更は行わない。新旧cohortは独立保持。
