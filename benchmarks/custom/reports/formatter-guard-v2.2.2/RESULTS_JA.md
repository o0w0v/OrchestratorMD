> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/formatter-guard-v2.2.2.md). This report alone does not establish a task result.

# Router / Worker v2.2.2 Formatter Guard Revision

**判定: READY_FOR_LINT_POLICY_REVIEW**

**FORMATTER_REVISION_PROMISING: true**

## 1. 目的と変更範囲

P221R-011型のrustfmt末尾カンマ正規化だけを安全に受理できるか検証した。
既存productionファイルの変更はHost formatterのlexical guardのみ。新しいguard helper・native tokenizer helper・testsを追加。
bounded profileは**2.2.1のまま**、formatter guard revisionを**2.2.2**として明示し、Router/Operational Policy/ReferencePlan/Coverage/repair eligibility/回数/context/model selection/formatter設定を変更していない。
旧STOPは保持。新しい独立ディレクトリでsaved replayと4 Taskのlive cohortを実行した。

## 2. 限定したnormalization

標準 `vec![a, b]` expression listのoptional trailing comma追加/削除だけを許可。
完全なdefault crate rootとCargo manifestから、macro定義・macro import/alias/glob・module・extern crate・custom attributes・未知macro expansionがない限定環境を確認する。
未知macroやvec以外のmacro内部、repeat/空vec、function arguments、format! arguments、struct/tuple/arrayのcomma変更は今回fail closed。
特に `(x)`→`(x,)` を同一扱いしない。構文ごとの検討表はdesign.md（元資料: design.md）。一般Rust resolver/parserを実装したとは主張しない。

## 3. Token / scope safety

元scannerでliteral・identifier・operator・comment・順序とpunctuation jointnessを保持し、許可したvec groupの末尾comma以外は同一を要求する。
file set、region外bytes、source/reference/hash guardはそのまま。既存delimiter→dot whitespace例外も維持。
commaを含む受理では `token_identity=false`、`normalized_token_identity=true` と記録し、完全に同じtoken列だったことにはしない。
formatterの出力だから許すのではなく、範囲・macro provenance・scanner・native比較・mandatory validationの全条件が必要。

## 4. Native Rust evidence

installed pinned rustcを使用し、stdのみのproc-macro helperをcompile。`proc_macro::TokenStream::from_str`と再帰TokenTreeをbefore/afterで保存した。
native側でも独立したgroup/list判定とPunct spacingを比較する。通常commentはTokenTreeから消えるため、従来scannerとのAND条件。
これはtokenizer evidenceであり完全なsemantic parserではない。tokenizerはcandidateを実行しない。
別の3 fixtureだけはcompile・実行し、副作用の評価順/回数、nested削除、単一要素の標準qualified vecで観測同値を確認した。
native helper source、rustc SHA/version、argv、stdout/stderr、JSON TokenTreeは一覧（元資料: native-token-evidence.json）から追跡できる。install/downloadなし。

## 5. Saved P221R-011 replay

旧raw candidate、旧formatter record、旧拒否出力をread-onlyで参照。
新しいコピーで同じpinned rustfmtを実行し、出力が旧保存出力とbyte一致することを確認した。
**formatter accepted / scope PASS / lexical safety PASS / mandatory validation到達**。
ここで初めて実行した元の固定acceptance、regression、fmt、clippy、workspace check/buildとHost scopeは**全PASS**。
旧P221R-011のFORMAT_SCOPE_VIOLATION、NOT_RUN、STOPをPASSへ書き換えていない。
saved replay結果（元資料: saved-replay/P221R-011/result.json）

## 6. Saved P22-008 method-chain control

既存method-chain normalizationを受理し、native evidenceも保存。acceptance/regression/fmt/check/build/scopeはPASS。
元からの不要な `.into()` による**Clippy-only failureは残る**。このため全mandatory PASSではないがformatter regressionではない。
修正・retry eligibility変更をせず、formatter受理とcoding品質を分離した。
saved control結果（元資料: saved-replay/P22-008/result.json）

## 7. Positive / negative regression

- Worker suite: **159/159 PASS**（既存153を維持、新規6 test methodsに多数の境界subcases）。
- literal/identifier/operator/comment変更、non-trailing comma、token順序、region外、readonly file、新規file、未知macro/alias/shadowingは拒否。
- native不在・拒否・spacing差、tuple単一要素、repeat/empty vec、unsupported構文も拒否。
- 既存method-chain・compound punctuation・scope testsは変更なしでPASS。
- native compile/観測同値fixture: **3/3 PASS**。
- application: fmt、Clippy -D warnings、workspace test/check/buildをinstalled WSL toolchainでoffline実行し全PASS。

negative case sourceと対応結果（元資料: negative-cases/index.json）、regression（元資料: regression/）、positive cases（元資料: positive-cases/）。

## 8. Small live cohort

Offline成功後、4件をfreezeして実行。Gemma26のみ。1件目はP221R-011同business、2件目method-chain control、3件目format変更なしcontrol、4件目は新規HighLoad evidence要素追加。

| Task | 用途 | Local | 理由 | 初回 | repair | Codex review | comma例外 | chain例外 | Host LOC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F222-001 | saved_business | PASS | TARGETED_CHECKS_PASSED | True | False | ACCEPT_NO_CHANGE | 1 | 2 | 21 |
| F222-002 | method_chain_control | PASS | TARGETED_CHECKS_PASSED | False | True | ACCEPT_NO_CHANGE | 0 | 4 | 10 |
| F222-003 | no_format_control | PASS | TARGETED_CHECKS_PASSED | True | False | ACCEPT_NO_CHANGE | 0 | 0 | 0 |
| F222-004 | new_vec_list_business | ESCALATE | OUTPUT_LIMIT | False | True | REJECT | 0 | 0 | 4 |

Local PASS 3/4、First PASS 2/4、ACCEPT_NO_CHANGE 3/4。
F222-001は初回から正しい候補を生成し、実際にvec末尾comma例外を通過して全mandatory checksにPASSした。
F222-002は全要素が空白のときの `(none)` が初回欠落し、Worker自身の1回repairでPASS。F222-003はformat変更なしで初回PASS。
**F222-004は未完了・REJECTのまま**。要件の「2番目のevidence要素を追加」に対し、初回候補は既存の1番目の文字列へ連結したためacceptance/regressionが正しく失敗した。
通常repairはHTTP 200だが `done_reason=length`、`prompt_eval_count=8136`、`eval_count=54`。server logは `n_ctx_slot=8192`、終了時 `n_tokens=8191, truncated=1` を記録した。
これは**context境界でrepairが完了しなかった証拠**であり、2048 output tokensを生成したことにはしない。`truncated=1`だけから元の入力が欠落したとも断定しない。
完全なrepair候補は適用せず、既存policyどおりOUTPUT_LIMIT後の追加retry・budget引上げ・その場での再分割実行を行わなかった。
このTaskでは期待した新規comma例外は発生しておらず、追加positive evidenceには数えない。失敗分析とraw証跡（元資料: live-results/F222-004/failure-analysis.json）。
Codex repair LOC **0**。model promptのformat改善やCodexによるWorker内retry prompt作成なし。
liveのnativeで検証したcomma normalizationは **1件**、method-chain spacing例外は **6箇所**。
Host formattingは **35 LOC**。formatter受理をLocal PASSと同一視せず、全checksとcompact final reviewを確認した。
run history（元資料: run-history.json）、Task metrics（元資料: live-task-metrics.json）、raw requests（元資料: request-index.json）。

## 9. Environment / infrastructure

Ollama **0.35.0**、GPU **NVIDIA GeForce RTX 3080**、driver **591.86**。
Gemma26 digest `08ae7ec1744bd7f451c4a530afb39d2673ad9d07a8369b8a33a3613b41212a68`。
temperature=0、seed=20260926、num_ctx=8192、num_predict=2048、stream=false、think=falseを維持。
Gemma12 inference=0、cross-model fallback=0、generation probe=0、unload/restart/update=0。
**Host failure 0 / scope failure 0 / INFRA_ERROR 0 / CUDA 0 / FALSE_GREEN 0**。
Task前後・開始終了のGPU/API/residency/CLI psとserver logを保存。旧artifact・変更禁止ファイル **10368件**のSHA不変を確認した。
STOP policyは弱めず、今回も既存のHost/scope/infra停止条件を使用。

## 10. Costと限界

Local input/output: **21438 / 693 tokens**、generation 8 calls、Worker wall合計 **247.157秒**。
live native検査の外部command時間合計 **2.219秒**。comma例外時のみhelperをcompile/tokenizeする追加Host負担がある。
この4件はspeed benchmarkやmodel能力ランキングではない。Codex exact tokens/active time/net savingsはnull。
compact final reviewとは別に、F222-004のresponse metadata/server logの失敗分析を実施した。追加分析の正確なtokens/active secondsもnullとし、ゼロコストとは扱わない。
許容構文とmacro binding環境は意図的に狭い。他の正当なrustfmt変更もfail closedし得る。未知macro/全tuple/struct/関数引数へ安全性を外挿しない。
Windows/WSLと固定rustcに依存し、不一致・利用不能時には受理を降格せずHost errorで停止する。

## 11. lint-only policy

003/006/008/010型のClippy-only `.into()` は別の次期policy review候補。今回のP22-008保存ケースでも残存を確認した。
same-model semantic repair最大1回、lint-only eligibilityは変更していない。今回の判定はreviewへ進む根拠であり、自動policy改修の承認ではない。

## 12. 判定

**READY_FOR_LINT_POLICY_REVIEW**。対象を限定したformatter revisionについて **FORMATTER_REVISION_PROMISING=true**。
P221R-011の停止原因を除去し、保存候補の実coding品質を全mandatory checksで確認できた。
既存method-chain case、negative guardsを維持し、小規模liveでもscope/Host/infra/false greenの回帰を観測しなかった。
これは**限定したformatter改善の判定**。Local品質は3/4 PASSであり、Worker全体や大規模PilotのREADY判定ではない。
lint-only policyのreviewに加え、F222-004で見つかったrepair context余裕の不足は別の残課題。今回の固定条件のまま全Taskのrepair安全性を保証したとは主張しない。
広い構文への自動拡張、lint policy変更、旧Pilot STOP解除、次cohortの自動開始は行っていない。
