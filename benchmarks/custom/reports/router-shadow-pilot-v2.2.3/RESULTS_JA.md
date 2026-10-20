> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/router-shadow-pilot-v2.2.3.md). This report alone does not establish a task result.

# bounded profile 2.2.3 Lint-enabled Shadow Pilot 結果

判定: **NEEDS_PROTOCOL_REVISION**。

自然に発生した `clippy::useless_conversion` 1件は、通常Workerのlint repair 1回で回復し、Codex修正なしで受理できた。一方、6番目のLocal Task P223-005で、rustfmtによるクロージャのblock化が固定formatter guardに拒否され、cohortは規定どおり停止した。介入削減の有望な1例は得たが、完走・拡大条件は満たさない。今回protocolを変更せず、未実行Taskを再開していない。

## 1. cohort概要

新cohort `router-shadow-pilot-v2.2.3`。14 Task（Local 13、Codex boundary 1）を準備し、production base `07c4afa`、事前freeze commit `4815e7e` から実行した。実repoのsourceを隔離コピーし、既存interface・testsを保護してbusiness acceptanceを追加した。production applicationへの採用は0。

2026-10-02 00:56:47〜01:04:54 JST（UTCでは10-01 15:56:47〜16:04:54）。本体wall time 486.484秒。通常のLocal repair loopへCodexは参加せず、終了済みTaskをcompact packetでレビューした。

証跡の入口: run-history.json（元資料: run-history.json）、全Task outcome（元資料: metrics/all-task-outcomes.json）、集計（元資料: metrics/summary.json）、Task別metrics（元資料: metrics/task-metrics.json）、依頼全文（元資料: REQUEST_JA.txt）。raw request/response、validation、health、server logsはrun-historyとrequest index（元資料: metrics/request-index.json）から辿れる。

## 2. environment

| 項目 | 開始時の実値・固定条件 |
|---|---|
| GPU | NVIDIA GeForce RTX 3080、10240 MiB、driver 591.86 |
| Ollama | 0.35.0（今回updateしていない） |
| Gemma26 digest | `08ae7ec1744bd7f451c4a530afb39d2673ad9d07a8369b8a33a3613b41212a68` |
| CoderNext digest | `ca06e9e4087c714d44355bf954099187890e63084b4a632b8e9956c4b9492074` |
| profile / guard | bounded_v2_2 2.2.3 / formatter guard 2.2.2 |
| context / output / chars | 8192 / 2048 / 24000 |
| temperature / seed | 0 / 20260926 |
| rustfmt | 1.9.0-stable (48a229ceae 2026-09-01)、既存binary/config hash固定 |
| 起動時residency | models=[]、Local開始前GPU 1922 MiB（準備時snapshot 2041 MiB） |

environment freeze（元資料: environment/freeze.json）にoptions、formatter hash、runtime hashes、CLI出力を保存。Task境界でnvidia-smi、Ollama API/ps、backend PIDをread-only確認。generation probe、強制unload、restart、fallback、downloadは0。Gemma12 quarantine、Qwen14 experimental、CoderNext DEBUGGINGのみのpolicyを維持した。

## 3. Task一覧

ACN=ACCEPT_NO_CHANGE、MINOR=ACCEPT_WITH_MINOR_FIX。未実行のLocal結果はnullでありFAILではない。

| ID | business Task | Protocol / model | Local結果 | Codex review / LOC |
|---|---|---|---|---|
| P223-001 | optional inventoryの不明値と実測ゼロ表示 | fixed / Gemma26 | First PASS | ACN / 0 |
| P223-002 | warningの空要素除外・単複表示 | fixed / Gemma26 | semantic repair PASS | ACN / 0 |
| P223-003 | meminfo重複診断にfield名（旧003 pair） | fixed / Gemma26 | lint repair PASS | ACN / 0 |
| P223-004 | invalid memory range診断へ観測値 | fixed / Gemma26 | semantic repair後lint残存、ESCALATE | MINOR / 3 |
| P223-005 | process ID overflow診断へ対象field | fixed / Gemma26 | repairのHost formatter拒否、STOP | REJECT / 0 |
| P223-006 | report reasonへobserved target追加 | fixed / Gemma26 | NOT_RUN_COHORT_STOP | — |
| P223-007 | memory evidenceへprocess数・truncated追加 | stateful / Gemma26 | NOT_RUN_COHORT_STOP | — |
| P223-008 | template reasonへevidence数（旧008 pair） | stateful / Gemma26 | NOT_RUN_COHORT_STOP | — |
| P223-009 | load evidenceへCPU当たり値追加 | stateful / Gemma26 | NOT_RUN_COHORT_STOP | — |
| P223-010 | invalid process ID診断へfield名 | stateful / Gemma26 | NOT_RUN_COHORT_STOP | — |
| P223-011 | healthy auditへtelemetry warning数追加 | stateful / Gemma26 | NOT_RUN_COHORT_STOP | — |
| P223-012 | diskstats inventoryのmalformed行除外 | fixed / CoderNext、DEBUGGING | First PASS | ACN / 0 |
| P223-013 | application ResourceBudget既定値のtyped抽出 | reasoning / Gemma26 | NOT_RUN_COHORT_STOP | — |
| P223-014 | warning集約の製品仕様境界 | Codex | Local dispatchなし | CODEX_ONLY / 0 |

全Taskの契約、Coverage Matrix、ReferencePlan、validation argvはtasks（元資料: tasks/）とtask-index.json（元資料: task-index.json）に保存。新規business Task中心、historical pairは003/008の2件。小規模repoの診断・表示改善へ偏る選定であり、無作為なproduction workloadではない。

## 4. protocol/model分布

計画: 通常fixed_slot 6、stateful 5、DEBUGGING 1（fixed_slot）、reasoning 1、Codex boundary 1。Gemma26 12、CoderNext 1、Codex 1。

実行: Gemma26 fixed_slot 5、CoderNext DEBUGGING 1。stateful/reasoningは0。実行順はfreeze時点の `012 → 001 → 002 → 003 → 004 → 005 → 006 → 013 → 007 → 008 → 009 → 010 → 011` を維持し、005で停止した。成功率を見て順番を変更していない。

## 5. completion

**cohort未完走**。Local terminal recordは6/13（46.15%）。うちHost STOP前に通常終了したのは5/13（38.46%）。boundaryを含めterminal判定を記録できたのは7/14（50.00%）で、これは全mandatory validation完了率やPASS率ではない。

STOP.json（元資料: STOP.json）とproduction cohort STOPの両方を保持。未実行7件のrecord directoryが存在しないことも監査した。

## 6. ACCEPT_NO_CHANGE

主要指標は **4/6 = 66.67%**。分母はHost失敗も含めた全dispatch Task。ACN 4、MINOR 1、MAJOR 0、REJECT 1。

Host失敗を除いた参考値は4/5=80.00%だが、これを主要指標へ置換しない。計画Local全体に対するACN取得数は4/13=30.77%。未実行を能力FAILとして扱わない。

## 7. First/final PASS

| 指標 | 能力評価可能5件（Host失敗除外） | 全dispatch6件の運用結果 |
|---|---:|---:|
| First PASS | 2/5 = 40.00% | 2/6 = 33.33% |
| Local final PASS | 4/5 = 80.00% | 4/6 = 66.67% |

P223-005のattempt 2はsemantic validation未到達。Host障害をモデル品質の最終FAILへ混ぜない。P223-004のLocal ESCALATEは、後のCodex修正によってPASSへ書き換えていない。

## 8. lint-only eligibility

eligible 1件（P223-003）。その他checksとguardがPASS、Clippy primary lintが既知のString `clippy::useless_conversion`のみ、spanがallowed region内であり、未使用repair budgetがあった。

P223-002はacceptance失敗と`clippy::useless_format`がありlint-only eligibilityなし。既存semantic repair経路による回復であって、lint allowlistの一般化ではない。P223-004は初回compile failure、semantic repair後のuseless_conversionに対して `global code-generation repair budget unavailable`。二重repairを拒否した。

exact lint codes、source span/hash、raw Clippy diagnostic、eligibility reasonsを各result.json（元資料: workspace/records/router-v2.2/P223-003/result.json）とchecks/raw validationに保存した。

## 9. lint repair recovery

invoked 1、recovered 1/1、ACN 1/1。P223-003は `Err(format!("duplicate {}", name).into())` の余分なconversionをGemma26が除去し、Host formatterと**全**mandatory checksを再実行してPASSした。Hostは正解patchを供給していない。

repair output 23 tokens、追加Codex修正0。旧P221R-003のCodex修正2 LOCに対応する **potential historical Codex LOC avoided = 2**。実token/time節約量ではなく、自然発生1例だけの観測である。旧008 pairは未実行で、成功とみなさない。

## 10. semantic repair

invokedは全体3件（002/004/005）。能力評価可能2件のrecoveryは1/2。002は「no warnings」の欠落を修復してPASS。004はOption値をformatしようとするE0277を修復したが、Clippyが残りESCALATE。005はinitialでPPidにもPid診断を返してacceptance FAIL、repair後はHost STOPのためrecovery判定null。

Task共通budgetは全件最大1。semanticとlintを別枠で使ったTaskも、追加retryも0。

## 11. Codex intervention

code repair介入1件（004）。通常Worker repair promptはCodexが作成していない。005にはread-only Host/protocol原因調査を実施し、code repairしなかった。code介入件数にこの調査作業を隠して含めず、別workloadとして記録した。

004の修正はcohort終了後、`scratch/codex-P223-004` の別コピーのみ。全7固定checksとscope/reference/freeze guardsを実行。original Local candidate/result/diffのhash一致を保持した。

## 12. Codex repair LOC

1 file、追加1行・削除2行、**合計3 LOC**。`.into()`除去に伴う閉じ括弧の整理のみ。理由、before/after、diff、全validationはcodex-repairs/P223-004（元資料: codex-repairs/P223-004/）に保存。

別コピーの修正＋validation wall 44.516秒、validation 40.922秒。Codexの正確なactive timeはnull。元applicationへの反映0。

## 13. FALSE_GREEN

**0**。Local PASS 4件をcontract/diff/全validationからreviewし、そのまま受理。Host停止TaskをPASSへ読み替えたり、未検証candidateを成功に数えたりしていない。小標本の観測であり、将来FALSE_GREENが発生しない保証ではない。

## 14. fixed_slot

通常fixed_slotは5件dispatch、ACN 3/5、MINOR 1、Host REJECT 1。known editはHost所有slotを使い、不要なstateful化なし。DEBUGGINGも実protocolはfixed_slotだが、KPIのgroupでは別集計する。

fresh capability、snapshot/hash binding、bounded apply、protected source/tests、format guardは固定runtimeのまま。005のraw model applyは成功し、format出力の採用前に止まった。

## 15. stateful

5件とも未実行。issued handle、DISCOVERY→EDIT、reference受け渡しの新live evidenceは今回得られていない。準備時static checksのPASSをlive品質とみなさない。ここが拡大判断の主要な欠測である。

## 16. debugging

前回Host STOPで未実行だったdiskstatsの同系統Taskを、今回事前に先頭へ固定した。P223-012はCoderNextでFirst PASS / ACN、修正0。

空行、token不足、非ASCII/非数値・u32 overflowのmajor/minorを除外し、device有りの有効行を数える。重複行と後続columnは契約どおり扱う。Worker 105.171秒、input 788 / output 214 tokens、初期model load 41.414秒。

## 17. reasoning

P223-013をfreeze・static preflight済みだがSTOPにより未実行。計画はapplication側ResourceBudget既定値のtyped extractionで、Worker generation budgetとは別物。

P223-014はRouterが `specification_owned_by_codex` と判定し、boundary design note（元資料: boundary/design-note.md）を保存。Local dispatch 0。boundary確認とreasoningの実モデル検証を混同しない。

## 18. references

全13 Local Taskで事前ReferencePlan/direct helper completenessを確認。実行6件は編集本文内の値と標準library呼び出しで閉じ、追加typed symbol reference 0。packet envelopeは各発行246 bytes、初回合計1476 bytes、repairを含む10発行で2460 bytes。

未実行TaskにはEvent、SystemState、Memory、Observer、record helper等を凍結しており、最大packet 2792 bytes、helper signature 1/1の計画も保持。今回の実行結果からnonempty Typed Referencesの有効性を評価することはできない。reference tokensは独立計測なし（null）。

## 19. formatting

採用されたHost formattingは計16 LOC（004の2 attemptで12、012で4）。005の拒否されたformat差分はこれに加算しない。

005のrepair:

```rust
// model candidate
.map_err(|_| if field_name == "PPid" { "PPid overflow" } else { "Pid overflow" })?
// pinned rustfmt output（抜粋）
.map_err(|_| {
    if field_name == "PPid" { "PPid overflow" } else { "Pid overflow" }
})?
```

保存済みbefore/afterのtoken値比較では追加は`{`と`}`各1個で、他のtoken値/順序は同一。read-onlyでfile/region scope PASSを再確認した。これは現行のmethod-chain whitespace／限定std vec comma許可とは別の構文正規化である。

token差分があるとguardは既存vec provenance検査へ進み、同じcrate内の既存`cfg!`がallowlist外として検出された。raw detailは `unknown macro may introduce bindings or interpret tokens`。macro自体が今回変更されたことを意味しない。native TokenTree検証より前に拒否され、attempt 2 semantic validationはNOT_RUN。

read-only分析（元資料: diagnostics/P223-005/post-stop/analysis.json）と保存rustfmt output（元資料: diagnostics/P223-005/post-stop/saved-rustfmt-output.rs）を追加保存。formatter受理範囲の不足／診断の粗さがprotocol検討事項。ただし意味同値性を新たに証明したとは主張せず、candidateのcoding品質も未確定のまま。guardやSTOPを緩めていない。

## 20. validation workload

計画Coverage criteria 112、validation definitions 86（全14 Task、scope guardは別）。実行6件のcriteria 54、外部check実行63回＋host_scope結果9回＝72 results。Worker内validation合計269.278秒。

順序はacceptance→targeted regression→fmt→Clippy→workspace test→check→build→scope。005 attempt 2はformatter段階で止まり、その後のchecksは0。zero-test guardを維持。

停止後の既存repo回帰結果（元資料: regression/summary.json）: **Worker suite 181/181 PASS**、Rust fmt / clippy（all-targets/all-features、warnings deny）/ workspace test / locked check / locked buildすべてPASS。推論なし、依存取得なし。これは旧source/runtimeの回帰確認であり、005 candidateの代替validationではない。

## 21. context/truncation

全10 generation HTTP 200、done=true、done_reason=stop。OUTPUT_LIMIT、schema incomplete、context failure 0。repairは以下の実測値。

| Task / kind | serialized chars | request bytes | prompt_eval_count | cached | eval_count | server truncated |
|---|---:|---:|---:|---:|---:|---:|
| 002 semantic | 15860 | 16148 | 5710 | 777 | 92 | 0 |
| 003 lint | 9029 | 9317 | 2904 | 735 | 23 | 0 |
| 004 semantic | 14772 | 15060 | 4975 | 760 | 41 | 0 |
| 005 semantic | 13719 | 14007 | 4705 | 759 | 53 | 0 |

分類はNO_TRUNCATION_EVIDENCE。log intervalの明示flag 0、警告なし、schema/applyおよび通過したvalidationを合わせて評価した。`prompt_eval_count <= 8192`だけで無欠損を証明していない。original full token countはnull。005のtransport成功とHost formatter失敗は別評価。

repair-context.json（元資料: metrics/repair-context.json）にrequest SHA256、raw transport/diagnostics pathと時間を保存。request interval logsは同時requestの厳密な識別保証ではないという既存注意も保持。

## 22. infrastructure

**INFRA_ERROR 0、CUDA 0、backend crash 0、GPU query timeout 0**（保存したTask境界/終了時healthとserver logsの観測範囲）。Gemma12 inference 0、Qwen fallback 0。今回STOPはGPU障害ではない。

開始は空residency。CoderNext backend PID 14672、Gemma26へ切替後PID 38044が終了時まで観測された。初期Coder load 41.414秒、唯一のmodel switchingでGemma load 22.163秒。その後のGemma loadは各0.002〜0.020秒。全境界でAPI/GPU queryは応答した。

Task snapshotのGPU総使用量は1922〜9776 MiB（sampling peakであり実行中の真のpeakではない）。CoderNext API size_vramは8,080,358,111 bytes。Gemma26ではAPI size_vram 990,348,573 bytesに対してGPU総使用量9639〜9776 MiBが保存されている。GPU全体とmodel metadataは測定対象が異なるため同一視せず、API値から実モデルVRAMを断定しない。既存healthのresidency_mismatchは全てfalseだが、この数値差が無いという意味ではない。原因調査や閾値変更は今回行っていない。

GPU snapshots（元資料: metrics/gpu-snapshots.json）とend health（元資料: environment/end/health/after.json）にraw値を保持。driver/runtime/Ollama設定は変更していない。

## 23. tokens/time

| Task | input tokens | output tokens | Worker秒 | validation秒 |
|---|---:|---:|---:|---:|
| 012 | 788 | 214 | 105.171 | 38.734 |
| 001 | 839 | 42 | 81.547 | 46.405 |
| 002 | 6492 | 180 | 80.453 | 50.578 |
| 003 | 3644 | 48 | 78.969 | 54.297 |
| 004 | 5740 | 76 | 66.672 | 44.201 |
| 005 | 5469 | 87 | 52.375 | 35.063 |
| 合計 | **22972** | **647** | **465.187** | **269.278** |

Ollama reported duration合計115.428秒。wall 486.484秒には境界処理等も含む。token値はOllama報告値でありCodex savingsではない。Codexのみで実装する同時比較baselineは実施していない。

## 24. review burden

通常reviewは6 compact packets、計76,712 bytes、median 13,522.5 bytes。Local会話全文は通常reviewで読んでいない。packetにはcontract/coverage/route/provenance/capability/model diff/format diff/final diff/checks/metricsを含めた。

記録した追加failure分析artifactは12,475 bytes。これはsourceのguard読解や環境確認まで含むCodex総入力量ではない。planning、normal review、failure analysis、code repair、infra/protocol analysisをworkload.json（元資料: reviews/workload.json）で分離。正確なtokens/active secondsはいずれもnull。

review開始〜判定のwall合計435.399秒には並行作業・待機を含むためactive review時間として使わない。Host planning/acceptance/validationと停止原因調査が残り、Local tokensや少数のLOC削減のみで総効率改善を結論しない。

## 25. v2.2.1 comparison

| 指標 | 旧v2.2.1 Shadow Pilot | 今回2.2.3 |
|---|---:|---:|
| dispatched Local | 12 | 6 |
| ACCEPT_NO_CHANGE | 6/12 = 50.00% | 4/6 = 66.67% |
| Codex repair Tasks / LOC | 5 / 12 | 1 / 3 |
| useless_conversion系Codex修正 | 4 / 10 LOC | 1 / 3 LOC（004、budget消費済み） |
| 自然発生lint repair回復 | policy対象外 | 1/1（003） |
| Host formatter STOP | 1 | 1 |

旧cohortのenvironment freezeでもOllama 0.35.0、driverと2 model digestsは同じ。ただしTask集合・実行順・実行数・profile/formatter revisionが異なる。早期STOPによりstateful/reasoningを欠き、4/6や1件3 LOCだけから一般的な改善率は推定できない。

exact business pairで結果が揃ったのは003のみ。旧003はCodex2 LOC、新003はLocal lint repairでACN。potential historical LOC avoided 2。旧008は今回未実行。旧結果を今回分母へ再利用していない。

## 26. expansion judgement

**NEEDS_PROTOCOL_REVISION**。ACNが66.67%でも、Host formatter STOPによりcohort未完走、stateful/reasoning欠測、natural lint recoveryは1件のみ。READY_TO_EXPANDにも、完走を前提とするCONTINUE_LIMITED_SHADOWにも該当しない。

別変更として検討する対象は、クロージャbodyをblockで囲むrustfmt正規化の限定的な意味・scope/token同値性の証明、および拒否理由の具体化。未知macroを一般許可したりformatter出力を全面信頼したりする提案ではない。今回その実装・micro experiment・再Pilotを開始していない。

## 27. conclusion

狭いlint repairは自然な実Task1件でCodexの小修正を肩代わりした。shared repair budgetも動作し、004で2回目のrepairを禁止した。全体運用の阻害要因は、今回もHost formatter受理範囲によるcohort停止だった。

監査: final-audit.json（元資料: metrics/final-audit.json）。既存11,654 files、凍結117 inputs、production runtime/profile/Router/Operational Policy、旧STOP・旧結果・applicationはhash一致。全10 requestのoptions/hash/model、最大1 repair、review binding、Local結果非改変を確認した。

成果物は本独立directoryのみ。source採用、旧STOP解除、cohort再開、protocol修正、次cohort拡大は行わず、本結果を保存して停止する。
