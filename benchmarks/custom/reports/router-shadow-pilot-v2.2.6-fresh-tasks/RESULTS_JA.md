> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/router-shadow-pilot-v2.2.6-fresh-tasks.md). This report alone does not establish a task result.

# bounded 2.2.6 Fresh-Task Limited Shadow Evaluation — RESULTS_JA

判定: **CONTINUE_LIMITED_SHADOW**。Local terminal coverage **10/10（100%）**、ACCEPT_NO_CHANGE / CODEX_CODE_FREE_RATE **6/10（60%）**。失敗4件は別コピーでCodexが完成させた。Codex自身の変更は**10 LOC（+5/−5）**、Host formattingを含む保守的な最終候補差分は**24 LOC**。FALSE_GREEN / shared Host STOP / scope failure / INFRA / CUDAはすべて0。

## 1. cohort概要

独立cohort `router-shadow-pilot-v2.2.6-fresh-tasks`。base commit `80c1f40`、branch `experiment/bounded-2.2.6-fresh-tasks`。2026-10-04 JSTに実行。Local 10 Task＋Codex boundary 1 Task。旧Task IDの再利用・旧STOPの解除・production/applicationへのadoptは行っていない。

bounded profile 2.2.6、Router v2.1、Operational Policy、prompts、ReferencePlan規則、formatter、coverage、repair eligibility、failure分類、scope/STOP policyを固定。temp=0、seed=20260926、num_ctx=8192、num_predict=2048、max_context_chars=24000、stream=false、think=false。途中調整なし。証跡: freeze（元資料: freeze.json）、cohort（元資料: cohort.json）、Task specs（元資料: tasks/）、環境freeze（元資料: environment/freeze.json）。

## 2. fresh Task selection

過去の95種のgoalを照合し、P224-001〜014とB2〜B5等のbusiness Taskを除外した。選定理由（元資料: planning/selection.json）と照合一覧（元資料: planning/historical-business-screen.json）をgeneration前にfreeze。各Taskの理由・除外範囲・risk・責務・files・acceptance・checks・ReferencePlan・routingは`planning/PFT-*.json`、`tasks/`、task-index（元資料: task-index.json）にある。

小規模repoを観測表示・診断の新しい挙動に限定し、近似Taskで件数を増やさず11件とした。全code Taskはeditable file 1件、private helper/scaffoldまたは既存式の狭いregion。dependency/schema/authority/API/architecture変更なし。9 code Taskすべてで、構文エラーではない赤acceptanceとHost scaffoldのClippy PASSを事前確認した。ランダムsampleではなく、Hostがinterface/testsを準備したobservability中心の小Taskである。

## 3. protocol/model distribution

固定slot 4、stateful 4、DEBUGGING/fixed_slot 1、typed reasoning 1、Codex boundary 1。Gemma26 9 Task、CoderNext 1 Task。Gemma12 0、Qwen14 0、cross-model fallback 0。statefulは限定された候補regionからissued handleを選ぶ。自由なrepo探索権限は追加していない。

| Task | 新規business Task | 経路 | First | Local final / review | fallback |
|---|---|---|---|---|---|
| PFT-001 | CLIの累積inference時間を整数演算で秒表示 | fixed_slot | FAIL | PASS / ACCEPT_NO_CHANGE | 0 LOC 不要 |
| PFT-002 | 重複抑制auditが現在event IDを示す | stateful | FAIL | ESCALATE / REJECT | 2 LOC TRIVIAL_FIX |
| PFT-003 | CLIに実行結果DryRun/Blockedの固定labelを表示 | fixed_slot | PASS | PASS / ACCEPT_NO_CHANGE | 0 LOC 不要 |
| PFT-004 | MockProviderの不足token数を診断する | stateful | FAIL | PASS / ACCEPT_NO_CHANGE | 0 LOC 不要 |
| PFT-005 | telemetry readのUTF-8エラーをI/O欠測と区別 | fixed_slot | PASS | PASS / ACCEPT_NO_CHANGE | 0 LOC 不要 |
| PFT-006 | TCP欠測warningが失敗したIP familyを列挙 | stateful | PASS | PASS / ACCEPT_NO_CHANGE | 0 LOC 不要 |
| PFT-007 | CLI引数エラーへinspect基準のindexを追加 | fixed_slot | NOT_RUN（適用前拒否） | ESCALATE / REJECT | 2 LOC TRIVIAL_FIX |
| PFT-008 | policy評価済みauditがproposal由来を説明 | stateful | FAIL | ESCALATE / REJECT | 2 LOC TRIVIAL_FIX |
| PFT-009 | proc directory識別が符号付き/zero名を受理する不具合 | debugging | NOT_RUN（適用前拒否） | ESCALATE / REJECT | 4 LOC SMALL_FIX |
| PFT-010 | Runtime constructorの固定容量と初期化契約をtyped抽出 | reasoning | PASS | PASS / ACCEPT_NO_CHANGE | 0 LOC 不要 |
| PFT-011 | audit viewerのrecord grouping方針 | Codex boundary | N/A | CODEX_ONLY・Local dispatch 0 | 実装なし |

## 4. terminal coverage

Local **10/10**、boundary込み **11/11**。未実行0、cohort_completed=true、STOP/ABORTなし。run-history（元資料: run-history.json）、END（元資料: END.json）。通常failureを残したまま次のTaskへ進んだ。末尾LF不足の2件はapply=0・source mutation=0の証拠付きでTask-local拒否された。

## 5. ACCEPT_NO_CHANGE / CODEX_CODE_FREE_RATE

どちらも**6/10 = 60%**。Worker自身のrepairで完了したPFT-001/004もCodexコード変更なしの完了に含む。reasoning 1件を含むLocal全体が主分母。codeだけでは5/9 = 55.56%。boundaryとCodex fallback後の完了をLocal PASSへ加算していない。

## 6. Local First / final PASS

全Local分母のFirst PASSは**4/10 = 40%**、final PASSは**6/10 = 60%**。適用前拒否2件を除いた初回validation到達例では4/8だが、主KPIに置き換えない。pre-apply拒否の`first_pass=null`は保存したまま。

## 7. Local failure taxonomy

最終failure: MODEL_SEMANTIC 2（PFT-002 E0308、PFT-008 E0433）、GENERATION_CONTRACT 2（PFT-007/009、final LF不足）。MODEL_SYNTAX / 最終LINT / FORMAT_UNSUPPORTED / TASK_DESIGN / HOST / INFRAは0。

PFT-009の未適用raw bodyには、`name.len() > 10`で長いゼロ埋め有効PIDを拒否する追加のsemantic defectがあった。これはCodex fallback reviewで発見した補足であり、元Local分類を後から変更していない。

## 8. repairs

共有1回budgetを使用したTaskは4件。semantic repairは3件中1件回復（001回復、002/008不回復）。allowlisted lint repairは1/1回復（004の`clippy::useless_conversion`）。syntax repair 0、追加retry 0。PFT-004の初回failureはClippy-onlyで、compile failureとは区別する。LF不足をWorkerへ再投入していない。各repairのcontext/transportとraw diagnosticsは`workspace/records/router-v2.2/PFT-*/`に保存。

## 9. fixed / stateful / debugging / reasoning

fixed 3/4 ACN、stateful 2/4 ACN、debugging 0/1 ACN、reasoning 1/1 ACN。debuggingは適用前に拒否され、Localではcode checksに到達していない。statefulのissued handle applyは7/7、invalid/stale handle 0。モデル間の能力ランキングや因果結論は出さない。

## 10. Codex fallback Task一覧

Local集計・review完了後、Local証跡864ファイルのSHA256（元資料: fallback/local-artifacts-sha256.json）を保存してから独立copyを作成。fallback開始（元資料: fallback/START.json）はLocal END（元資料: END.json）より後。通常入力はTask/acceptance/final diff/checks/summaryで、Local会話全文は渡していない。LF拒否2件だけは追加で最終raw response bodyと固定slot bindingを確認した。

| Task | 変更内容 | Codex追加/削除 | Codex LOC / class | Host fmt LOC | 最終候補差分 LOC | 候補由来 |
|---|---|---|---|---|---|---|
| PFT-002 | `format!`を借用して`&str`引数へ渡す | +1/−1 | 2 / TRIVIAL_FIX | 0 | 2 | applied_local_candidate |
| PFT-007 | 最終LFだけ補完 | +1/−1 | 2 / TRIVIAL_FIX | 5 | 5 | unapplied_raw_body |
| PFT-008 | 未知enumを既存string `"skill"`へ置換 | +1/−1 | 2 / TRIVIAL_FIX | 0 | 2 | applied_local_candidate |
| PFT-009 | 最終LF＋誤った文字数制限の除去 | +2/−2 | 4 / SMALL_FIX | 11 | 15 | unapplied_raw_body |


4件とも元と同じmandatory acceptance/regression/fmt/clippy/workspace test/check/buildとscope/hash/freeze guardsを再実行しPASS。完成sourceと差分は各`fallback/PFT-*/completed-files/`、`validation-summary.json`、`codex-body-edit.diff`に保存。Local resultは4件ともESCALATE/REJECTのまま、fallback後の別reviewは4件ともACCEPT_WITH_MINOR_FIX。

## 11. Codex fallback LOC

Codexの手作業差分は**追加5＋削除5＝10 LOC**。LF-only修正は事前ルールどおり1追加＋1削除で2 LOC。raw未適用bodyも安全にbindingを確認して再利用できる場合はそのbodyを比較基準とし、元Localへの適用成功とは扱わない。sourceへの実適用LOCはTask別metrics（元資料: summaries/task-outcomes.json）の`source_application_counts`に別保存。

Host formatterによる追加作業は**16 LOC**。Local最終bodyからformat後完成bodyまでの保守的差分は**24 LOC**。差分区間が重なるため10＋16を最終差分とみなさない。Hostの整形をCodexの手書きLOCに混ぜない一方、最終差分を小さく見せないため両方を報告する。

## 12. Local candidate reuse

fallback候補再利用 **4/4**。適用済みfile由来2件、pre-apply拒否raw body由来2件。Codex編集後・deterministic formatting前の非空実装行の残存率は002=75%、007=100%、008=80%、009=91.67%。newlineだけの違いは行の内容の再利用判定を下げず、LOCには計上する。

LOCAL_USEFULNESS: Local完成6、Local＋trivial Codex fix3、Local＋small Codex fix1。全Local 10件でLocal成果物を使って完成したが、うち4件にはCodex実装介入が必要だった。100%自動完了を意味しない。

## 13. trivial / small / substantial / from-scratch

事前thresholdは1〜3 LOCをTRIVIAL、4〜12 LOCかつ50%以上再利用をSMALL、それ以外をSUBSTANTIAL、ほぼ再利用不能をFROM_SCRATCH。Codex自身の編集ではTRIVIAL 3、SMALL 1、SUBSTANTIAL 0、FROM_SCRATCH 0、TASK_SPEC_PROBLEM 0。

保守的なformat後差分にも同じLOC thresholdを当てた分類を別保存した。002/008はTRIVIAL、007はSMALL（5 LOC）、009はSUBSTANTIAL相当（15 LOC）。009の実際のCodex編集は4 LOCで、残りの増加はHostの行折り返しを含む。分類の差を隠さず、手書き負担と最終diffの大きさを分離する。

## 14. FALSE_GREEN

Local PASSに対するFALSE_GREENは**0/6**。fallback完成4件も全checkと最終コードreviewを通過。PFT-009では凍結済みtest例が長いゼロ埋めを含んでいなかったため、別のread-only source由来review probeを追加。元bodyはFAIL（exit101）、修正版はPASS（exit0）。追加review証跡（元資料: fallback/PFT-009/additional-contract-review.json）。元Task/acceptanceは一切変更せず、追加確認は既存の「leading zeros許可」という契約に基づく。test greenだけで契約充足を断定しない。

## 15. Host workload

Coverage criteria **85**、validation定義65。新規scaffold＋testsの差分は**+280/−12 LOC**、そのうちacceptance本体 **207 LOC / 6,215 bytes**。各TaskへのTyped Reference declaration数は最大1、発行packet総量 **6,946 bytes**（再repair時の再発行とcapability metadataを含み、refs=0でもpacketは存在）。サイズ証跡（元資料: planning/scaffold-workload.json）、Reference詳細（元資料: metrics/task-metrics.json）。

Local Host formatting **18 LOC**、validation結果90件・**325.533秒**（scope行を含む件数）。fallback validation結果32件・**152.925秒**、Host formatting16 LOC。compact review packetは合計108,283 bytes。Taskコピーにはbuild用のworkspaceが存在するが、モデルへrepo全文を送っていない。これはHost準備・検証・artifact harnessにも相応の作業がかかる評価であり、修正10 LOCだけで全体コストを評価できない。

## 16. infrastructure

ユーザーtray Quit後、frontend/backend不在、11434拒否、API拒否、GPU residency残留なしを観測。その後同じinstalled `ollama app.exe --hide --fast-startup`を非表示起動。恒久設定を変えず、既存app flagでpending updaterを起動時に延期した。fresh PID **51764**、Ollama **0.35.1**、driver **591.86**、RTX 3080 10GB、開始時`models=[]`。

Gemma26 digest `08ae7ec1744bd7f451c4a530afb39d2673ad9d07a8369b8a33a3613b41212a68`、CoderNext digest `ca06e9e4087c714d44355bf954099187890e63084b4a632b8e9956c4b9492074`。cohort中frontend/boot/version/GPU/driver/digests/runtimeを確認し、restart・generation probe・強制unloadなし。Gemma26→CoderNext→Gemma26のswitchを含めINFRA/CUDA 0。全10 TaskでNO_TRUNCATION_EVIDENCE。これは一般的な無故障保証ではない。health（元資料: metrics/gpu-health.json）、transport（元資料: metrics/request-index.json）、truncation（元資料: metrics/truncation.json）。

## 17. tokens / time

Local chat **18 call**、input **42,586**、output **1,353 tokens**。Worker累積 **910.829秒**、cohort wall **969.766秒**。validationやモデルload/switchも含む観測で、speed benchmarkではない。

Codex planning/review/fallback codingの正確なtokens・active secondsはすべて**null**。review/fallbackの記録時刻間wallは別保存し、active推論時間と混同しない。Local tokenからCodex savingsを推測しない。直接Codex実装との純コスト差は未測定。

## 18. P224 cohortとの比較

前回P224はACN 8/13=61.54%、今回は6/10=60%（記述上−1.54ポイント）。いずれもterminal100%、shared安全性/infra事故0。Task構成・件数が違うため、統計的な改善/悪化・モデル能力変化を断定しない。今回初めて、Local失敗をCodexが完成させる実編集と再利用率を別phaseで測定した。

## 19. optional Codex-only baseline

追加コスト抑制のためskip。したがって「Codex-onlyより総作業量が少ない」「tokensを何%削減した」という結論は出さない。

## 20. expansion judgement

**CONTINUE_LIMITED_SHADOW**。terminal100%、ACN60%、failure4件は小さいCodex編集で完成、FALSE_GREEN/Host/infra0。限定運用の補助としては価値を観測したが、ACNは20〜30 Task拡大の参考帯70〜75%へ達していない。Host contract/test準備のコストとstatefulの型/symbol不足にも注意が必要。

今回はProtocol改善へ戻らず、既存freezeを維持した。次cohort・micro experiment・routing改善・production採用は自動開始しない。

## 21. conclusion

新しいTaskでも6/10はCodexコード変更なしで完了。残り4件には合計10 LOCのCodex編集が必要で、全件でLocal候補を再利用できた。ただしformat後の候補差分は24 LOC、Host scaffold/tests差分292 LOC、full validationも必要だった。短い最終reviewだけで完了する範囲と、手修正・追加意味確認が残る範囲を区別できた。

既存19,136 tracked files、旧Pilot/STOP/CUDA証跡、Router/Worker/applicationを保全。既存Worker suite **233 tests PASS**、Rust fmt/clippy/test/check/build PASS。全Local/fallback artifactは独立directoryに保存し、原本へのadopt/merge/pushなし。集計JSON（元資料: summaries/summary.json）、全Task outcome（元資料: summaries/task-outcomes.json）、回帰結果（元資料: regression/summary.json）、fallback完了（元資料: fallback/END.json）。
