> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/bounded-2.2.6-codex-value.md). This report alone does not establish a task result.

# Codex Value Benchmark — Local-first vs Codex-only

**判定: INCONCLUSIVE / STOPPED_INFRA_ERROR。A/B比較は未完了。**

fresh Ollama起動後、CVB-004のEDIT生成中にGemma26がCUDA illegal memory accessで停止した。成功済み3件と失敗証跡を保持し、CVB-005・自動retry・再起動は実施していない。これはLocalモデル能力のFAILではない。

## 1. Benchmark目的
通常bounded 2.2.6のLocal-firstが直接Codex implementationよりCodex作業を減らすか、共通準備とLocal専用準備を分離して比較する。Protocol/model/router改善ではない。

## 2. Task一覧
| ID | 未使用business責務 | Frozen Local route |
|---|---|---|
| CVB-001 | 観測process sampleのPID最小・最大表示 | Gemma26 / fixed_slot |
| CVB-002 | AuditRecordのpolicy disposition件数集計 | Gemma26 / fixed_slot |
| CVB-003 | sample内に存在しないnonzero parentの件数evidence | Gemma26 / stateful |
| CVB-004 | provider-rejected auditの保持済みreservation表示 | Gemma26 / stateful |
| CVB-005 | bounded readがUTF-8境界でsize超過を誤分類する不具合 | CoderNext / fixed_slot |

同じrepoの過去104 goalを照合し、既存Taskの別定数・再実行にしないよう選定。全て単一責務、low/normal risk。CVB-005は元実装のread_to_string→サイズ検査順による既存不具合をbaselineとした。

## 3. Freeze
freeze.json（元資料: freeze.json）に259ファイルを固定。base commitは431256c。goal/interface/allowed regions/acceptance/checks/risk/source hashesを両経路前に固定した。共通Rust workspaceと5つの独立Codexコピーの初期source hashは一致する。実行後もfreeze・runtime・20,671件の既存tracked fileのSHAは不変。

Codex-onlyへWorker固有handle/ReferencePlanは強制せず、同じscope境界とacceptanceをplain contractで渡す設計。A/Bで相手の実装を供給しない。

## 4. Local-first結果
| Task | Local terminal | First PASS | repair | Worker秒 | Host validation秒 |
|---|---|---:|---|---:|---:|
| CVB-001 | PASS | true | なし | 84.250 | 44.422 |
| CVB-002 | PASS | false | semantic 1回、回復 | 82.656 | 54.485 |
| CVB-003 | PASS | true | なし | 58.547 | 39.798 |
| CVB-004 | INFRA_ERROR / CUDA_ERROR | null | なし | 23.984 | 0 |
| CVB-005 | NOT_RUN | null | 未実行 | null | null |

Local terminal 4/5、有効なcoding結果3件、Local PASS 3/3（INFRA除外）、First PASS 2/3。これはCodex reviewによるACCEPT_NO_CHANGEではない。INFRAを含む実行済み4 Taskの正常PASS返却は3/4=75%。未実行をモデルFAILに数えない。

run-history.json（元資料: run-history.json）、Local compact summary（元資料: local-summary/summary.json）、STOP.json（元資料: STOP.json）にraw request/response/check/diffへのpathを保存した。

## 5. Codex-only結果
0/5、未実行。独立Codex CLI sessionの使用確認が未回答だったため開始していない。5つのblind baselineは全て不変。独立final review/fallbackも未実行。未実行を0 token/0 LOCで完了した実装とは扱わない。

## 6. Codex token取得可否
Installed CLI 0.158.0-alpha.2.1の`--json`と、公式仕様の`turn.completed.usage`（input/cached-input/output）を調査済み。ただしbenchmark CLI sessionは0 callなので、実usageの取得動作は未検証。Codex model/effortは現在の設定と同じgpt-6-astra / xhighで固定した。

root会話の保存usageから今回のplanning/implementation/review/fallbackを正確に分離できず、全てnull。文字数、Local tokens、アカウント残量から逆算しない。

公式 non-interactive mode（元資料: http[LOCAL_PATH]）

## 7. Codex LOC比較
全TaskのLOCAL_FIRST_CODEX_LOC / CODEX_ONLY_LOCは未確定のnull。現時点のCodexによるbusiness code編集は0だが、review前のためCODEX_CODING_AVOIDEDやcoding-free率は未確定。Local生成diffのLOCをCodex削減LOCへ読み替えない。

## 8. Intervention比較
Codex implementation/review/fallback呼出は観測上0。完成workflowの介入量はnull。coding episodeとreviewを別記録する設計を維持した。

開始時に私のHost orchestrationが環境freeze完了前にrunnerを起動したため、FileNotFoundErrorでpreflight ABORTが1件あった。この時点でgeneration 0。旧ABORT.json（元資料: ABORT.json）と最初のhealth snapshotを保持し、環境freeze完了後に別launch記録START.json（元資料: START.json）で同一Task・Workerを開始した。これはWorkerのcoding failureではないが、benchmark運営上のHost負担として残す。

## 9. Candidate reuse
Codex fallback未実行なのでreuse lines% / fallback class / fallback LOCはnull。CVB-004はDISCOVERY完了後、EDIT responseを返す前の障害であり、repair可能なcoding failureと決めつけない。

## 10. Host prep workload
preparation-workload.json（元資料: planning/preparation-workload.json）を参照。

- SHARED_PREP: scaffold/wiring/acceptance差分206 LOC（追加+削除、5ファイル）。acceptance本文187行を含む。
- LOCAL_ONLY_PREP: 追加marker14行、生成済みCoverage/runner metadata 25,860 bytes、型Reference packetを別記録。
- CODEX_ONLY_PREP: plain contract projectionと独立sessionコピー。business解答コードは0行。
- BENCHMARK_ONLY: blinding、usage取得器、比較・計測器、環境診断、preflight開始順序修正。毎Task固有の実装コストとは分離。

artifact LOC/bytesは思考量ではない。著作したtask generator LOCと再利用したharness量も保存。各bucketのactive timeとCodex tokensは測定できずnull。準備開始/終了のtimestampはあるが、計測基盤作業やユーザー待機が混ざる区間を純粋な準備時間としない。今回のHost専用準備が過大でないとは判定できない。

## 11. Validation workload
両経路に同じacceptance/regression/fmt/clippy/workspace test/check/build/scopeを定義。5件とも事前にred acceptanceを確認し、scaffold ClippyはPASS。準備用check subprocess合計107.064秒。

元repoのWorker 233 tests、Rust fmt/clippy/test/check/buildは全PASS。以降runtime/sourceはSHAで不変。Codex隔離copyの配線確認では未実装CVB-001のacceptance/workspace-testのみ期待どおりFAIL、残りPASS（benchmark本体へ加算しない）。

実Local Host checksは計138.705秒。CVB-002の初回失敗とrepair後の全checksを両方保存。整形の実行記録も別に保持。

## 12. Wall time
Local Workerの4 terminal run合計249.437秒。cohort実行区間は289.438秒（前後health等を含む）。正常3 TaskだけのWorker合計225.453秒。ユーザーQuit待機や過去の実験時間は含めない。

レビュー/fallback未実行なのでLOCAL_FIRST_TOTAL_WALLはnull。CODEX_ONLY_TOTAL_WALLもnull。active reasoning timeは不明。Codex用Cドライブ・Local用Dドライブのコピーとcold build差は、今後paired計測する場合の制約。

## 13. Quality / Infrastructure
正常3件は同じmandatory checksとscope/hash guardをPASS。Codex contract review前なのでFALSE_GREEN=0やACCEPT_NO_CHANGEを主張しない。Worker Host/scope failureは0、別枠のpreflight Host abortは1。

環境: RTX 3080 10GB / NVIDIA 591.86 / Ollama 0.35.1。tray Quit後にprocess不在、11434拒否、API応答なし、GPU上のOllama process不在を確認。新frontend PID 15004、2026-10-04 03:29:39 JST起動、models=[]、同一binary/digestsを確認した。

CVB-004のDISCOVERY responseは正常。その次のEDIT generation（cohort通算7番目のchat、先行成功6回）が約18.52秒でHTTP 500。

```
CUDA error: an illegal memory access was encountered
in function ggml_backend_cuda_synchronize
cudaStreamSynchronize(cuda_ctx->stream())
```

2026-10-04 03:37:00 JSTにbackend PID 61328がexit 0xc0000409。モデル切替なし。温度・seed・8192 context・2048 output budgetは固定のまま。

Windows記録: 03:36:46〜03:36:59 JSTのnvlddmkm Event 153が7件、03:36:58 JSTのApplication Error 1000（llama-server.exe / ucrtbase.dll / c0000409）が1件。Event 153だけではdriver resetとは断定しない。

GPU使用量: Task前9882 MiB → 直後1214 MiB → post-fault1175 MiB。nvidia-smi query timeoutは観測0。Ollama frontend/APIは生存したがbackendは消失し、/api/psには990,348,573 bytesのVRAM residencyが残った。既存residency_mismatch閾値はfalseだったが、post-healthはRESIDENT_WITHOUT_BACKENDを検出。APIとGPUの値を同一値として扱わない。

CUDA/INFRA incident 1（派生health異常を別のcoding失敗として重複計上しない）。OOM、driver bug、Ollama bug、model固有bugとは断定しない。failure layerはOllama/CUDA backend周辺まで。

障害概要（元資料: infrastructure/fault-summary.json）、post-fault snapshot（元資料: infrastructure/post-fault-cvb004/snapshot.json）、Windows Event Log（元資料: infrastructure/post-fault-cvb004/windows-events.json）、Ollama raw log（元資料: diagnostics/CVB-004/server.log）。

## 14. Task別A/B
全5 Taskとも比較分類INCONCLUSIVE。Aの正常3件に対するBがなく、同一品質基準を両経路で完了したpairは0。CUDA Taskを簡単なTaskへ差し替えていない。

## 15. Aggregate
benchmark-summary.json（元資料: benchmark-summary.json）に要求されたTask別metricsとmissing理由を保存。

- 有効Local coding結果3、Local PASS3、First PASS2、semantic repair回復1。
- coding-free率、fallback率/LOC、Codex-only LOC、candidate reuse、ACCEPT_NO_CHANGE、FALSE_GREEN: null。
- 完全に計測された正常3 TaskのLocal input14,790 / output725 tokens。
- 障害Taskの成功DISCOVERYも含む部分計測値: input15,473 / output763。失敗generation1 callは未計測のため、cohort全体の正確なtoken総量はnull。
- Codex tokens / 完成A/B wall: null。Local validation138.705秒。
- INFRA/CUDA1、backend crash1、Worker Host/scope failure0、preflight Host abort1、cohort STOP1。

## 16. Net savings
NET_CODEX_TOKENS_SAVED=null。Codexの比較実測がなく、準備分もphase分離できないため計算しない。Local input/outputの多さはCodex削減量ではない。

## 17. Limitations
小標本、目的抽出、観測・表示中心、Host-provided scaffold/tests。さらにCUDAによる打ち切りとCodex経路未実行があるため、Local-firstのworkflow価値の比較は成立していない。過去cohortの60% coding-free結果を今回のB値として代用しない。

## 18. Decision / 次の条件
**INCONCLUSIVE**。Local-firstがCodex-onlyより有利とも不利とも結論できない。

CUDA後に追加inference/別モデルへの差替え/自動restart/OS・driver・runtime変更は実施しなかった。旧STOPや旧結果を解除・上書きしていない。独立Codex sessionの使用確認は未回答のままである。

fresh frontendだけでは今回のGemma26連続実行の安全性を保証できなかった。比較再開にはインフラ復帰条件を先に決める必要がある。このcohortの失敗をPASSへ書き換えず、再実行するなら旧runとの対応を保持した別runとして扱う。Protocol/model routingを変更して結果を改善することは今回の範囲外。
