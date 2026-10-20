> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/formatter-structural-v2.2.4.md). This report alone does not establish a task result.

# Router / Worker bounded 2.2.4 — Formatter Structural Normalization / Stop Classification

判定: **READY_FOR_SHADOW_PILOT_RETRY**。

P223-005型のclosure body block化を、pinned rustfmt・限定構文検査・native TokenTree比較の組合せで受理し、元のmandatory validationへ到達できた。証明できない変換は未採用のままTask-localに隔離でき、真のintegrity異常をcohort STOPにする検査も維持した。独立live cohortは4/4件を測定し、Local PASS / ACCEPT_NO_CHANGEは2/4件。これはformatter・停止分類の再検証完了であり、コード品質が全件合格したという判定ではない。

実行日: 2026-10-02 JST。live開始/終了: 02:01:52–02:05:43 JST（artifactの時刻はUTC）。実装・offline証跡・事前freezeのcommitは `fbeeb66`、branchは `fix/bounded-formatter-v2.2.4`。live結果と本報告は後続の独立commitに保存する。旧cohortのSTOP解除、旧Pilotの続行、拡大Pilotの開始は行っていない。

## 変更内容と固定条件

Host formatterの検証と停止分類、対応するmetrics/tests/docsを変更し、bounded profileを2.2.4へ更新した。Router v2.1、Operational Policy、Gemma12 quarantine、モデル選択、Coverage Gate、ReferencePlan、fixed/stateful capability、mandatory validation、`clippy::useless_conversion`限定eligibility、共有repair上限1回は変更していない。profileの差分はversionとformatter契約の説明だけ。

実行条件はGemma26、temperature=0、seed=20260926、num_ctx=8192、num_predict=2048、max_context_chars=24000、stream=false、think=false。formatter binary/hash/version/configを固定し、live途中のrule・prompt・Task・runtime変更は0。モデル切替、fallback、generation health probe、環境更新は行っていない。

設計は design.md（元資料: design.md）、事前条件は environment/freeze.json（元資料: environment/freeze.json）、runtime/Task/helperのfreezeは live-freeze.json（元資料: live-freeze.json） に保存した。

## Closure構造変換の検証

基本比較はtoken kind/value/order、comment、jointnessの同一性。差分がある場合、balanced delimiter ancestryと最小token windowから、closureの**全body expression**を囲む新しいBrace groupだけを識別する。単にbrace数が2増えた場合を許可するruleではない。

受理条件は、単純parameter binding/typeと既存moveが不変、bodyが対応済みの単一式、追加statement/semicolon/control transferなし、closure外token不変、file集合・allowed region・protected source不変。native Rust TokenTreeでも、新しいclosure-tail Brace groupを取り除いた内容、既存group、punctuation spacingが一致することを必須とした。

有限文法は値/path、call、field、index、単項/二項式、tail式だけを持つif/elseなどに限定する。async、明示return annotation、turbofishを含むgeneric method call、statementを含むbody、nested/mixed構造変換などは未対応として拒否する。Rustの完全な構文/意味解析とは主張しない。

Macro判定は変更された構文とそのenclosing syntaxを見る。closureと無関係な既存`cfg!`を、変更されたmacroとは扱わない。未知macroのinput内、macro定義内、影響を証明できないattribute配下はfail closed。std vec commaは従来の保守的binding/provenance検査を維持し、vecのbindingに影響する宣言は引き続き関係するものとして扱う。任意macroへのtoken追加は許可していない。

## 停止分類

| 分類 | 必要証跡と処置 |
|---|---|
| FORMAT_UNSUPPORTED_NORMALIZATION | staging内の変換だけが未証明。candidate未変更、source/reference/Git/cohort freeze、scope/file集合、staging identity、formatter hash/version/configを再検証。staging outputを採用せず、Task ESCALATE。format-only repairは行わず、cohortは継続可能。 |
| FORMAT_INTEGRITY_FAILURE | region/file/source/protected bytes、candidate/staging identity、formatter pin/config、Host状態の不一致はcohort STOP。soft rejection後の最終guardで検出したdriftもfatalへ昇格。 |
| その他既存fatal | validation infrastructure corruptionやformatter実行不能などのHost/infra failureも従来どおりSTOP。soft分類へ置換しない。 |

「未対応」は変換が意味的に安全という認定ではない。安全に**拒否して隔離できた**ことを示す。raw model candidateはprivate copyに証跡として残るが、未検証・不採用であり、applicationには反映しない。

## Saved replay

旧artifactをread-onlyで読み、新しいコピーで実際のpinned rustfmtと元の固定checksを実行した。旧result/STOPは変更していない。

| Saved case | Formatter / scope | Mandatory validationで得た結果 |
|---|---|---|
| P223-005 attempt 2 | closure block化を受理。native unwrap 1 group、scope PASS。旧saved rustfmt出力とbyte一致。 | 全checksに到達。**E0425: `field_name`未定義でcoding FAIL**。従来のformatter STOPの先にあった問題が可視化された。 |
| P22-008 | method-chain whitespaceを従来どおり受理。scope PASS。 | 既存Clippy failureを保持。他checks PASS。 |
| P221R-011 | 限定std vec trailing commaを従来どおり受理。native/scope PASS。 | 元のmandatory checksすべてPASS。 |

saved-replay-summary.json（元資料: saved-replay-summary.json） の `passed=true` はformatter proofとmandatory validation到達を示し、3候補すべてのcoding PASSを意味しない。各caseの `saved-replay/<ID>/` にbefore/after、native token、diff、formatter record、元のcheck結果を保存した。Codexによるcandidate修正や追加inferenceは0。

## Native evidenceとoffline regression

Installed rustc 1.98.1の `proc_macro::TokenStream::from_str / TokenTree` を使用。token取得時にmodel candidateは実行しない。別の小さい実行可能fixtureでbeforeとactual rustfmt afterをcompile/runし、以下3件が一致した。

| Fixture | 観測 |
|---|---|
| side-effect-order-and-count | 副作用回数/順序 `[10, 20]` が一致。 |
| move-fn-once-and-drop-order | move/FnOnceとdrop順序 `[2, 1]` が一致。 |
| borrow-and-return-value-long | borrow元が使用可能で、戻り値 `first-owned-reference:second-owned-reference` が一致。 |

短いborrow fixtureではrustfmtがblock化しなかったため、NO_STRUCTURAL_NORMALIZATION_OBSERVEDとして保存し、上記3件に数えない。有限fixtureは一般的なsemantic equivalence proofではない。native-fixtures-summary.json（元資料: native-fixtures-summary.json） と各 `native-fixtures/` が証跡。

既存181件を保持し、追加20件を含む**Worker tests 201/201 PASS**。semicolon、statement、return、parameter/move、literal/identifier/operator/comment、closure外token、partial expression、macro input、native groupingの変更を拒否する検査を追加した。unsupportedの未採用・repairなし・次Task継続、およびscope/file/source/candidate/pin/version/final guard driftのSTOPを検証。既存formatter、lint、reference、handle、scope、shared repair budget検査もPASS。

Rust fmt、Clippy（all-targets/all-features、warnings拒否）、workspace test、locked check、locked buildはすべてPASS。regression/summary.json（元資料: regression/summary.json）。Worker unit test内の模擬CUDA出力はlive infra障害には数えていない。

## 独立live cohort

全TaskでGemma26を使用し、元のbusiness仕様・固定acceptanceを引き継いだ。レビューはTask/decision、diff、checks、短いWorker summaryのpacketを読み、全会話は読んでいない。

| Task | 対象 | 初回 | Repair | 最終Local / Codex review |
|---|---|---|---|---|
| F224-001 | P223-005相当、Pid/PPid overflow診断 | closure block化を受理→E0425 `field_name`未定義 | 同モデルsemantic repair 1回。そのbodyのgeneric method構文はformatter有限文法外 | FORMAT_UNSUPPORTED_NORMALIZATION / REJECT。Task-local隔離、cohort継続。 |
| F224-002 | method-chain、空白だけのevidenceを省略 | empty/all-blank時に空文字を返しacceptance FAIL | 1回で`(none)`へ修正。全checks PASS | PASS / ACCEPT_NO_CHANGE |
| F224-003 | P221R-011相当、RSS saturating合計の第2 evidence追加 | 第1文字列を変更してしまいacceptance FAIL。formatterは成功 | canonical repair packetが24,540 charsで24,000 gate超過。API送信せずrepair 0回 | REPAIR_PACKET_TOO_LARGE / REJECT |
| F224-004 | format変更なし、process count下限の`+`表示 | 全checks PASS、Host format diffなし | 不要 | PASS / ACCEPT_NO_CHANGE |

F224-001の初回normalizationは実モデル出力でも受理され、元の課題である「validationへ進めない」を解消した。repair出力の `field.is::<Option<u32>>() && field.is_some()` は対応文法外だった。attempt 2のsemantic validationはNOT_RUNであり、新しいcompile診断を得たとは主張しない。stagingだけの変換であることを再検証し、未採用のまま拒否した。

F224-001の終了はUTC 17:02:53.876002、次Task開始は17:02:53.882152。この拒否後も残り3件の測定が完了した。詳細は formatter-analysis.json（元資料: diagnostics/F224-001/formatter-analysis.json）。このHost recordの限定追加調査は通常final reviewとは別に保存した。

method-chain例外はF224-002/003で観測された。F224-003ではvec trailing commaが自然発生しなかったため、liveでcomma変換の追加成功例を得たとはしない。comma回帰の根拠はsaved P221R-011とoffline guard testsである。結果を誘導するprompt変更や追加runはしていない。

## Metrics

| 指標 | 実測 |
|---|---:|
| 完了測定 / planned | 4 / 4（100%） |
| First PASS | 1 / 4（25%） |
| Local final PASS | 2 / 4（50%） |
| ACCEPT_NO_CHANGE | 2 / 4（50%） |
| Semantic repair API実行 | 2 Task、各1回 |
| Lint repair API実行 | 0 |
| Codex candidate repair LOC | 0 |
| Closure normalization observed / accepted（live） | 2 / 1 |
| FORMAT_UNSUPPORTED_NORMALIZATION | 1 |
| FORMAT_INTEGRITY_FAILURE / Host / scope failure | 0 / 0 / 0 |
| FALSE_GREEN / cohort STOP | 0 / 0 |
| INFRA_ERROR / CUDA | 0 / 0 |
| Ollama chat calls（discoveryを含む） | 7 |
| Model input / output tokens | 15,270 / 595 |
| Worker合計 / cohort wall | 228.157 s / 230.969 s |
| Host validation合計（Worker時間に内包） | 151.189 s |
| 4 final review packet合計 | 51,390 bytes |

PASS/ACCEPT_NO_CHANGEの分母は全dispatch 4件。terminal formatter rejectionやbudget rejectionをcoding能力FAIL率へ混ぜたmodelランキングは作らない。ただしF224-001/003の初回coding failure自体はchecksに残し、隠していない。Codex実token・正確なactive review/設計/調査時間は未取得なのでnull。repair LOC 0は候補を修正せず2件REJECTにした結果であり、採用件数や節約量の水増しに使わない。

送信されたrepairのcharsは13,931 / 13,277、request bytesは14,219 / 13,565、prompt_eval_countは4,595 / 4,668。いずれもHTTP 200、done_reason=stop、server truncated flag=0で明示的なtruncation証拠なし。F224-003はAPI未送信なのでprompt_eval_count=null。num_ctx/num_predict/context gateやrepair上限は一切引き上げていない。

task-metrics.json（元資料: metrics/task-metrics.json）、summary.json（元資料: metrics/summary.json）、request-index.json（元資料: metrics/request-index.json）、format-windows.json（元資料: metrics/format-windows.json） にtask別数値、raw request/responseへのpath、SHA256、changed token windowとmacro relevanceを記録した。各 `workspace/records/router-v2.2/<ID>/` にformat/native/check/diff/transportの証跡がある。

## Infrastructureと保全

実開始時点はOllama **0.35.0**、RTX 3080 10GB、driver **591.86**。過去Phaseの0.34.4とは区別し、今回versionを変更していない。Gemma26 digestは `08ae7ec1744bd7f451c4a530afb39d2673ad9d07a8369b8a33a3613b41212a68`。pinned rustfmtは1.9.0-stable、binary hash/config hashともfreeze一致。

cohort境界と各Task前後のread-only health snapshot 10件でnvidia-smi/APIが応答し、residency mismatchなし。開始GPU使用量1,298 MiB、終了9,774 MiB。before/after測定であり連続samplingやGPU peak測定ではない。高いVRAM使用量だけでOOMとは評価しない。health-summary.json（元資料: metrics/health-summary.json） と `environment/`、Task別 `health/`、Ollama log intervalを保存した。

旧artifact/application/Router/policy等の**12,733 filesのSHA256不変**を確認。例外として許可した `bounded_review.py` の変更はunsupported domainの別集計のみで、旧結果を編集していない。旧STOPすべて保持。live中のruntime/input/helper freeze不変、request options/hash、review evidence binding、shared repair budget、PASS候補の全固定checksを再照合した。audit.json（元資料: metrics/audit.json）。

## 判定と残る限界

要求されたformatter/停止分類の成功条件を満たすため、**READY_FOR_SHADOW_PILOT_RETRY**と判定する。P223-005のsaved/live初回でnormalization受理→validation到達を確認し、既存method-chain/vec/negative guardの回帰0、safe-local拒否後のcohort継続を実測、true integrity failureのSTOPをoffline検証した。FALSE_GREEN/INFRA/CUDAは0。

ただしモデルの未定義symbol、仕様違反、repair packet上限は残った。今回これらを修正するReferencePlan/prompt/context/policyの変更はしていない。未対応構文を広げるなら別の証拠とレビューが必要で、unknown macro、turbofish、async/明示return型などを自動で許可しない。

次の評価は新cohortで実施する候補とし、旧STOPを解除せず、今回はここで停止する。狙いはformatterの保守的拒否を安全に局所化し、残りTaskの測定を継続できるようにすることであり、2/4の実装品質を本番採用可能と一般化することではない。
