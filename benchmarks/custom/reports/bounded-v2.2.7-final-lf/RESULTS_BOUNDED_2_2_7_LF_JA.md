> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/bounded-v2.2.7-final-lf.md). This report alone does not establish a task result.

# bounded profile 2.2.7 Exact Final-LF Canonicalization Integration

集計: 2026-10-05T06:34:26.624941+00:00
判定: **LF_CANONICALIZATION_PROMISING**

## 1. Design

唯一の実装変更はopt-inされたpre-apply bodyへの最終LF 1 byte追加。`runner.profile_version=2.2.7`が必要。versionなし/2.2.6は従来拒否を維持。default_enabled=false、production Routerへの自動採用はしていない。実行profileと互換経路は別metadataへ保存。

## 2. Eligibility

exact schema、expected slot/issued handle、strict UTF-8、NUL/markerなし、path/region、snapshot/source/hash/freeze、transaction全体のprojected diff budgetを先に確認する。LF不足だけの場合にraw bytes + `0a`。CR-only endingは拒否。trim/indent/CR/escape/brace/literal等の変更なし。

## 3. Provenance

raw HTTP responseは不変。body-canonicalization配下にraw/normalized .binとSHA256、bytes、APPEND_FINAL_LF、HOST_BYTES_ADDEDを分離保存。LF追加時raw契約false・Host適用true。auditでraw responseから抽出したbodyとの同一性とexact +1を検証。

## 4. Saved replay

| Saved Task | 統合replay |
|---|---|
| LSE-008 | semantic FAIL |
| LSE-009 | compile FAIL |
| LSE-010 | PASS |
| LSE-011 | PASS |
| LSE-012 | PASS |

各7固定checksを実行。旧replayの最終sourceとbyte-equivalent、旧resultは不変。モデルAPI/repair 0。新cohort成功率・creditsに混ぜない。

## 5. Negative tests

追加22件: LF有/不足、fixed/stateful、NUL、invalid UTF-8 scalar、non-string/schema、marker、wrong slot、foreign/expired handle、source drift、CR-only、budget超過、複数target不正のatomic拒否、旧version、既存semantic repair最大1回、repair後guard STOP。

## 6. Regression

Worker 255/255 PASS（既存233件不変＋22件）。Rust fmt/clippy/workspace test/check/build全PASS。初回のversion表示assertion失敗はregression-001へ残し、互換経路とprofile表示を分離してregression-002で通過。Generation options、formatter policy、allowlist/global budget、system prompt AST不変。

## 7. New live Tasks

CLI codex-cli 0.160.0, GPT-6 Sol / xhigh / Standard。LocalはQwen14の実験限定binding。Gemma12・他model fallbackなし。10件未使用business Task、6 fixed-slot・4 stateful。共通spec/acceptance/source/rates/runtimeを開始前freeze。baselineを先にblindで完成し、別copyのLocal結果からclean handoffまたは独立review。

| Task | business goal | protocol | Local | review |
|---|---|---|---|---|
| LF227-001 | Project positive sampled root PIDs | fixed_slot | TARGETED_CHECKS_PASSED | ACCEPT_NO_CHANGE |
| LF227-002 | Total sampled RSS without u64 overflow | fixed_slot | TARGETED_CHECKS_PASSED | ACCEPT_NO_CHANGE |
| LF227-003 | Measure each warning UTF-8 payload size | fixed_slot | TARGETED_CHECKS_PASSED | ACCEPT_NO_CHANGE |
| LF227-004 | Compute valid sampled memory availability basis points | fixed_slot | CODE_FAILURE | clean handoff / N/A |
| LF227-005 | Run-length encode adjacent sample warning messages | agentic | CODE_FAILURE | clean handoff / N/A |
| LF227-006 | Display known and unknown TCP sample presence | agentic | CODE_FAILURE | clean handoff / N/A |
| LF227-007 | Choose the latest sampled audit row with last-row tie break | agentic | FORMAT_UNSUPPORTED_NORMALIZATION | clean handoff / N/A |
| LF227-008 | Project sources of explicitly failed audit verification | agentic | TARGETED_CHECKS_PASSED | ACCEPT_NO_CHANGE |
| LF227-009 | Filter sampled proposal risks for report preview | fixed_slot | LINT_REPAIR_NOT_ELIGIBLE | clean handoff / N/A |
| LF227-010 | Fix last matching warning index for duplicate messages | fixed_slot | TARGETED_CHECKS_PASSED | ACCEPT_NO_CHANGE |

## 8. Raw First PASS

RAW_LOCAL_FIRST_PASS: 3/10。Raw contract-followingとHost救済を分ける。

## 9. Canonicalized First PASS

実際にLF追加して初回全checksを通ったCANONICALIZED_LOCAL_FIRST_PASS: 2/10。LF追加対象 3/10。rawと救済は互いに排他的; native Host pipeline First PASS合計 5/10。

## 10. Semantic failures

LF追加はcoding defectの修正ではない。004/005はcompile failure、006はacceptance/Clippy failure。007はunsupported formatter normalizationでsemantic checks NOT_RUN（task-local拒否、Host integrity STOPではない）。009はLF追加後のacceptance/regression/test/check/build/fmtは通過したがclippy::clone_on_copyで拒否された。失敗candidateをCodex directへ渡さず、frozen clean sourceから実装した。Local code repairは経済experiment gateで0、通常Workerの最大1 repairは不変。

## 11. Review quality

Local採用ACCEPT_NO_CHANGE 5/10、clean handoff 5/10、FALSE_GREEN 0。両経路は同じ7 mandatory checks＋scope/hash/freezeと独立reviewを要求。review packetはcontract、diff、checks、必要source/type、短いsummaryとLF provenanceのみ。会話全文や反対経路の実装なし。

## 12. Codex credits

公式Codex pricing（元資料: http[LOCAL_PATH]）を 2026-10-05T05:11:02.563668+00:00 にfreeze。uncached/cached/output 1M token当たり50/5/250 credits。`turn.completed`実usageで計算。欠測はnull、推定なし。creditはrate-card換算値で請求額・subscription debitの確認ではない。

| Task | Codex-only（Planner込み） | Local-routed（Planner込み） | saved | group |
|---|---:|---:|---:|---|
| LF227-001 | 3.83517 | 1.73656 | 2.09861 | LF_RESCUED_ACCEPTED |
| LF227-002 | null | null | 1.75784 | LF_RESCUED_ACCEPTED |
| LF227-003 | 3.51162 | 1.68656 | 1.82506 | RAW_PASS_ACCEPTED |
| LF227-004 | 4.10405 | null | null | CLEAN_HANDOFF |
| LF227-005 | 3.19761 | 3.67565 | -0.47804 | CLEAN_HANDOFF |
| LF227-006 | 4.14356 | null | null | CLEAN_HANDOFF |
| LF227-007 | null | 3.62441 | null | CLEAN_HANDOFF |
| LF227-008 | 2.87585 | null | null | RAW_PASS_ACCEPTED |
| LF227-009 | 3.84881 | 3.95284 | -0.10403 | CLEAN_HANDOFF |
| LF227-010 | null | 1.79196 | null | RAW_PASS_ACCEPTED |

Executor＋Reviewer（10件）: null → null、削減 null credits / null%。
Plannerも全call実測可能なpaired subset（4件）: 14.39321 → 11.05161、削減 3.34160 / 23.22%。
Executor＋Reviewerが全call実測可能なpaired subset（5件）: 11.70172 → 6.60228、削減 5.09944 / 43.58%。欠測Taskを除いた条件付き集計であり全10件の削減率ではない。
capacity interruption（生成前・読み取り後・source書き込み後）7 sessionにusageが無く、該当phaseを含む総額/率はnull。共通Plannerの未知costは両側へ同一に含めるためabsolute savingsでは相殺するが、Executor/Reviewerの未知costは相殺と仮定しない。失敗sessionを0 tokens/creditsと仮定していない。同model/effort/speedのfresh retryは同source/promptで記録。A-clean004のsource書き込み後のCLI失敗では再生成せず、実際のCodex candidateへ全validation＋新独立reviewを実行しPASS。元CLI失敗とusage=nullは保持。

## 13. LF-specific credits saved

LF救済採用group全件の matched direct baseline − 独立Local review: **3.85645 credits**。完全に実測できたLF subset 2件では **3.85645 credits**。raw PASS groupとclean handoff groupはsummary.jsonで分離。共通Plannerは相殺。LFが無ければ旧契約ではrejectされるcandidateについての、この標本内のcounterfactual; 一般的因果・将来の削減率に外挿しない。

## 14. Wall

Local Worker合計 497.797秒（Host validation 314.781秒を内包）。計測phase合算wallはCodex-only 1380.036秒、Local-routed 1467.519秒。共通Planner、coordinator、phase間待機は含まず、benchmark全elapsed/active timeではない。Codex-only validation 521.188秒、clean handoff validation 265.345秒。
Local実usage: input 16419、output 987、reported cache 2983 tokens。Codex source変更量はbaseline 68 LOC、routed 44 LOC、coding-free 5/10。Host LF/formatter/prepはCodex実装LOCへ含めない。
task-results.jsonにWorker全wall、Host validation seconds、CLI implementation/review wall、両経路の計測phase合算を保存。active timeは取得不能。比較copiesはC:（Codex）/D:（Local）でstorage/cache条件差があるためlatencyを厳密な性能差とはしない。別途validation retry/formatter errorはraw記録へ保存。

## 15. Safety

Local INFRA 0, CUDA 0, Host STOP False, FALSE_GREEN 0。Codex service capacity errorは別記録でLocal coding/infra評価に混ぜない。保存済みtracked 37086・preexisting untracked 1253件のhash不変。Router/Operational Policy/model registry/application/旧STOP不変。body proofsとsession trace auditはaudit.json。

## 16. Decision

**LF_CANONICALIZATION_PROMISING**。LF救済2件が全checks＋独立reviewを通り、当該groupでcredits削減を確認した。一方provider欠測で全10件の厳密な総credits/削減率は不明なのでREADYへは進めない。限定されたfinal LF処理の統合・offline regressionと新cohortの安全性/品質/経済性を評価した。production Router defaultやmodel政策は変更せず、追加cohortも自動開始しない。

## 17. Limitations

未使用business Taskでも共通の小さいpure projection interfaceをHostが事前作成した10件の標本であり、既存feature開発全般の代替を主張しない。Hostのcoordinator設計・acceptance/scaffold・integration/debug/audit/集計tokenとcreditsはphase分離不能でnull。したがってwhole-agent net cost savingを確認したとは言わない。標本・単一Qwen14・単一environment・Codex出力のばらつき・cache/storage差・provider欠測がある。private copyとtrace auditはblinding証跡であり完全なOS sandboxとは主張しない。raw/normalized/body/apply/formatter/validation/review/usageは各Task artifact pointerから辿れる。
