> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/router-shadow-pilot-v2.2.1.md). This report alone does not establish a task result.

# Router / Worker v2.2.1 Shadow Pilot Retry — 結果

**最終判定: NEEDS_PROTOCOL_REVISION**

14 Taskを固定して開始し、Local 12件をdispatch。P221R-011でHost formatterが停止し、CoderNextのP221R-012は未実行。
主指標 **ACCEPT_NO_CHANGE = 6/12 (50.0%)**。Codexの小修正は5件・12 LOC、FALSE_GREEN / INFRA_ERROR / CUDAは各0。
旧Pilotと今回のSTOPを保持し、追加dispatch・Protocol修正・自動再開は行っていない。

## 1. Cohort概要

独立cohort `router-shadow-pilot-v2.2.1`。固定条件で実repoの単一責務を委譲し、通常実装・repair・小修正をどこまでWorker/Hostへ移せるか測定した。
新規business Task 12、過去business比較2（007/008）。過去のPASSを分母へ流用せず、dispatch分はすべて新規実行。
CLI・診断・audit・inventory中心の小さいRust repoであり、複雑な一般開発を代表するsampleではない。
Task選定・seed・acceptance・有限参照・runtime hashはinference前のcommit `c4ad0fa` で固定。開始前のPython Worker検証は153/153 PASS。
applicationへの自動採用は0。実行・Codex修正とも実repoから作成した独立コピーに限定した。

## 2. Environment

- Ollama **0.35.0**、GPU **NVIDIA GeForce RTX 3080 / 10240 MiB**、driver **591.86**。
- Gemma26 digest: `08ae7ec1744bd7f451c4a530afb39d2673ad9d07a8369b8a33a3613b41212a68`。
- CoderNext digest（固定済み、今回未dispatch）: `ca06e9e4087c714d44355bf954099187890e63084b4a632b8e9956c4b9492074`。
- Profile `bounded_v2_2 / 2.2.1`、temperature=0、seed=20260926、num_ctx=8192、num_predict=2048、stream=false、think=false。
- Formatter `rustfmt 1.9.0-stable (48a229ceae 2026-09-01)`。実行binary/config hash、runtime hashesは environment/freeze.json（元資料: environment/freeze.json） と freeze.json（元資料: freeze.json） に保存。
- Gemma12 quarantined、Gemma26 active、Qwen14 experimental、CoderNext DEBUGGINGを維持。fallback、generation health probe、forced unload、restart、更新は0。

## 3. Task一覧

| Task | 責務 | 群 | Local | Codex review | Codex LOC |
| --- | --- | --- | --- | --- | --- |
| P221R-001 | CLI process inventoryの下限表示 | fixed_slot | PASS | ACCEPT_NO_CHANGE | 0 |
| P221R-002 | CLI available memory割合の整数表示 | fixed_slot | PASS | ACCEPT_NO_CHANGE | 0 |
| P221R-003 | meminfo重複診断にfield名を含める | fixed_slot | ESCALATE | ACCEPT_WITH_MINOR_FIX | 2 |
| P221R-004 | process statusのmissing field表記を一致 | fixed_slot | ESCALATE | ACCEPT_WITH_MINOR_FIX | 2 |
| P221R-005 | CLI evidenceの空要素省略表示 | fixed_slot | PASS | ACCEPT_NO_CHANGE | 0 |
| P221R-006 | mock report reasonへevent kindを追加 | fixed_slot | ESCALATE | ACCEPT_WITH_MINOR_FIX | 3 |
| P221R-007 | anomaly-free auditへprocess数を追加 | stateful | PASS | ACCEPT_NO_CHANGE | 0 |
| P221R-008 | skill template reasonへ現在のevidence件数 | stateful | ESCALATE | ACCEPT_WITH_MINOR_FIX | 3 |
| P221R-009 | HighLoad evidenceへthreshold超過量を表示 | stateful | PASS | ACCEPT_NO_CHANGE | 0 |
| P221R-010 | process重複ID診断でPidとPPidを区別 | stateful | ESCALATE | ACCEPT_WITH_MINOR_FIX | 2 |
| P221R-011 | memory evidenceへ観測RSSのsaturating合計 | stateful | ESCALATE | REJECT | 0 |
| P221R-012 | diskstats inventoryで空行とmalformed rowを除外 | debugging | NOT_RUN | N/A | 0 |
| P221R-013 | Observerのbounded inventory limitsをsourceから抽出 | reasoning | PASS | ACCEPT_NO_CHANGE | 0 |
| P221R-014 | Partial process inventoryのユーザー向け表示要件を決定 | boundary | N/A | CODEX_ONLY | 0 |

全Task low/normal risk、dependency/schema/authority変更なし。既知位置はfixed、未知候補位置は有限Stateful discovery。
code Taskは事前にcompile成功かつ期待するacceptanceのredを確認した。故意のcompile障害をseedに入れていない。
Task 014は曖昧な仕様決定をCodex所有と判定し、design-note（元資料: boundary/design-note.md） を保存。Local呼出し0。

## 4. Model / protocol distribution

| 群 | 予定 / dispatch | ACCEPT_NO_CHANGE | First PASS¹ | final PASS¹ | Worker repair | Codex LOC |
| --- | --- | --- | --- | --- | --- | --- |
| fixed_slot | 6 / 6 | 3/6 (50.0%) | 2/6 (33.33%) | 3/6 (50.0%) | 2 | 7 |
| stateful | 5 / 5 | 2/5 (40.0%) | 2/4 (50.0%) | 2/4 (50.0%) | 0 | 5 |
| debugging | 1 / 0 | N/A | N/A | N/A | 0 | 0 |
| reasoning | 1 / 1 | 1/1 (100.0%) | 1/1 (100.0%) | 1/1 (100.0%) | 0 | 0 |

全実dispatchはGemma26。CoderNextはHost停止により未観測。モデル切替の安定性も今回未評価。
¹能力分母はHost/design/infraを除外。ACCEPT_NO_CHANGEの運用分母にはdispatchされたHost失敗も含め、未実行とCodex boundaryを除く。

## 5. Completion

**完走していない。** terminal recordはLocal 12/13、Codex boundaryを含む結果記録到達は13/14 (92.86%)。
この到達率はPASS率ではなく、Host停止Taskも記録に数える。Host停止なしで通常Worker経路を終了したLocalは11/13 (84.62%)。
停止時刻は2026-10-01 11:34:02 UTC / 20:34:02 JST。P221R-012は`NOT_RUN_COHORT_STOP`であり能力FAILではない。
STOP.json（元資料: STOP.json） と cohort.json.STOP.json（元資料: cohort.json.STOP.json） を保持。

## 6. ACCEPT_NO_CHANGE

**6/12 (50.0%)**。未実行を含む全計画Localでの到達は6/13 (46.15%)。
Host失敗を除いた評価可能Localでは6/11 (54.55%)。codingのみでは5/11 dispatch (45.45%)、reasoningは1/1。
「Codexがコードを書かずに済んだ」という主指標は、Local repair後でもCodex無修正なら含めるため005も対象。
boundaryを成功扱いして分母・分子を増やしていない。

## 7. First / final PASS

Host失敗除外・reasoning込み: First PASS **5/11 (45.45%)**、Local final PASS **6/11 (54.55%)**。
codingのみ: First 4/10、final 5/10。運用上の全dispatchに対するLocal final PASSは6/12。
Codex修正後に通った5件をLocal PASSへ書き換えていない。全結果は all-task-outcomes（元資料: metrics/all-task-outcomes.json） を参照。

## 8. Repair / context

same-model repairは2件、回復1件 (50%)。CodexはWorker内のdiagnostic解析・retry prompt作成に参加していない。

| Task | message chars | request bytes | prompt_eval | cached | eval | done_reason | truncation分類 | Local final |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P221R-004 | 18289 | 18577 | 6621 | 1092 | 117 | stop | NO_TRUNCATION_EVIDENCE | ESCALATE |
| P221R-005 | 12838 | 13126 | 4584 | 732 | 107 | stop | NO_TRUNCATION_EVIDENCE | PASS |

両方HTTP 200、done=true。server logに各callの`truncated = 0`があり、明示的truncationは観測しなかった。
004はschema/bounded apply後にE0283が残り、コード修復失敗として記録。005は空入力の`(none)`欠落を修復し全検証PASS。
004のprompt_eval=6621に最大output予算2048を足すと8192を超えるが、実outputは117で終了している。
この実成功transportを最大長outputまでの一般的なcontext保証と解釈しない。char gateは24000のまま、token heuristicは現行どおり非強制。
今回のplain-text検証出力はcanonical compiler unit数0、lossless residual textとしてpacking。diagnostic policyの変更なし。
raw stdout/stderr、wire request bytes/SHA256、response、context判定、既存server logを保存した。OUTPUT_LIMIT / REPAIR_PACKET_TOO_LARGEは0。

## 9. Codex intervention

通常の最終コード修正は **5件**（003/004/006/008/010）。4件がClippy-only、1件がWorker repair後のE0283。
停止後の集計・レビュー段階で、既に終了済みのWorker candidateを別コピーへ複製し修正した。
元Local result、diff、candidate、凍結Taskは保持。停止Task 011の修正・検証や未実行012のdispatchはしていない。
これと別にHost停止原因のread-only分析1件。Protocol/infra構成変更は0。

## 10. Codex repair LOC

| Task | file（独立コピー内） | added | deleted | 合計 |
| --- | --- | --- | --- | --- |
| P221R-003 | units/P221R-003/crates/ncos-observer-linux/src/lib.rs | 1 | 1 | 2 |
| P221R-004 | units/P221R-004/crates/ncos-observer-linux/src/lib.rs | 1 | 1 | 2 |
| P221R-006 | units/P221R-006/crates/ncos-agent/src/lib.rs | 1 | 2 | 3 |
| P221R-008 | units/P221R-008/crates/ncos-skills/src/lib.rs | 1 | 2 | 3 |
| P221R-010 | units/P221R-010/crates/ncos-observer-linux/src/lib.rs | 1 | 1 | 2 |

合計added 5 / deleted 7 = **12 LOC**。すべて不要な`.into()`を取り除く最小修正。
003/010は`format!`が既にString、006/008は同じ問題にrustfmtの改行が加わったもの。004は`ok_or`の型推論を曖昧にする変換。
5件すべて固定acceptance / regression / fmt / clippy -D warnings / workspace check / buildとscope/reference guardがPASS。
codex-repairs（元資料: codex-repairs/） にbefore/after、Codex diff、各checkとLOCを保存。productionへの採用なし。

## 11. FALSE_GREEN

**0**。Local PASSの6件をcompact packetでレビューし、受入契約違反を認めなかった。
Host停止011はvalidation未実行でPASSではなく、false greenにも能力FAILにも数えない。
この小さいsampleと有限acceptanceでの観測であり、未知ケースの不存在証明ではない。

## 12. fixed_slot

6件、ACCEPT_NO_CHANGE 3/6、first 2/6、final 3/6。
005はWorker自身のrepairで回復。003/006のClippy-onlyと004の修復後compile失敗がCodexへ残った。
known editをStatefulへ昇格せず、Host所有slot/source snapshot contractを維持した。

## 13. Stateful

5件dispatch、issued handleの選択・exact apply **5/5有効**。invalid/stale/fuzzy applyは0。
reference completenessは5/5 PASS。ACCEPT_NO_CHANGE 2/5、Host停止を除くfirst/finalは2/4。
007のdirect `self.record` signatureを含む参照は充足し初回PASS。008/010はClippy-only、011はformatter段階で停止。
Stateful repairは今回発生せず、前回のrepair fit成功を今回の全経路保証に転用していない。

## 14. Debugging

CoderNext/P221R-012は **N/A: 未実行**。実repoのdisk inventory行カウントbugを選定・preflightしたが、先行TaskのHost STOPが優先された。
PASS率・速度・model switchingについて結論を出さない。完走のための順序変更や停止解除をしていない。

## 15. Reasoning

013は1/1初回PASS、ACCEPT_NO_CHANGE。read take=65537とaccepted text=65536を区別し、directory=8192、processes=256を正しく抽出。
typed answerのみで編集権限なし。Task014の自由仕様決定との境界も維持。

## 16. References

| Task末尾 | refs | packet bytes（issueごと） | symbols |
| --- | --- | --- | --- |
| 001 | 0 | 246 | — |
| 002 | 0 | 246 | — |
| 003 | 0 | 246 | — |
| 004 | 1 | 856,856 | Process |
| 005 | 0 | 246,246 | — |
| 006 | 2 | 1522 | Event, EventKind |
| 007 | 3 | 2763 | Observer, SystemState, record |
| 008 | 1 | 1154 | Event |
| 009 | 2 | 2079 | SystemState, Memory |
| 010 | 0 | 509 | — |
| 011 | 3 | 2684 | SystemState, Memory, Process |
| 013 | 0 | — | — |

実dispatchで宣言参照計12件。packet初回合計12551 bytes、再issue込み13653 bytes、最大2763 bytes。
bytesはbinding/envelopeを含み、refs=0でも小さいpacketがある。reference専用input tokensは分離計測不能のためnull。
Host-reviewed finite dependenciesのみ。モデルの自由なread/search、helper実装全文、golden patchの追加なし。
reference planning failure 0。UNKNOWN_FIELD / UNKNOWN_SYMBOL / WRONG_SIGNATURE / WRONG_TYPE_ASSUMPTIONは現行分類で0。
004のE0283は実在するが、この4分類には含まれないため「型問題0」とは要約しない。

## 17. Host formatting

採用されたHost formattingは **34 LOC**。format-only model repairは0。
011ではモデルのbounded apply後、rustfmtが標準`vec!`の最後の要素にカンマを1個追加した。kind/value/order差分はその挿入だけ。
変更範囲guardはPASSしたが、lexical token identity guardが`FORMAT_SCOPE_VIOLATION: token kind/value/order changed`を返した。
これは有効な末尾カンマを許容できないHost formattingの制約で、v2.2.1のmethod-chain whitespace例外とは別のケース。
不採用formatter出力はstagingにとどまり、semantic validationはNOT_RUN。モデルコードの合否は確定していない。
host-failure-analysis（元資料: diagnostics/P221R-011/host-failure-analysis.json） と拒否したdiff（元資料: workspace/records/router-v2.2/P221R-011/format-1/host_format_diff.diff） を保存。
formatter binary/config/guardは変更せず、conservativeな停止挙動をそのまま評価した。recordのHost LOC=0は拒否された変更が採用されなかったため。

## 18. Host validation workload

計画全14件のCoverage criteria **100**、固定validation定義 **74**（Host scopeは別）。preflight design failure 0。
実Worker validation結果は86件（repair反復とHost scope含む）、コマンドelapsed合計 **383.046秒**。
さらにCodex修正の別コピー検証 **187.686秒**。モデルAPI時間だけでは委譲総コストを表せない。
実dispatchしたcode Task用のHost seed差分はadded355/deleted4 LOC。acceptance・markers・scaffold・formattingを含み、Codex repair LOCとは別。
Host/test設計は今回も必要であり、Local実装が短くても準備・検証負担が消えるわけではない。

## 19. Infrastructure

**INFRA_ERROR=0、CUDA=0、観測したGPU query timeout=0、backend crash=0**。開始/終了と各Task前後でread-only snapshot。
Gemma12 inference=0、他モデルfallback=0。Ollama/GPU/driver/digest/optionsはfreezeと一致。
24 Task境界snapshotの総GPU使用量は972〜9862 MiB。高使用量のみからOOMを推論していない。
既存healthのresidency_mismatch flagは0。ただしAPIの`size_vram=990348573` bytesと、総GPU使用量約9.6 GiBには差がある。
総GPU使用量はモデル単体とは限らず、この差の原因は今回切り分けていない。flag=0をAPI residency精度の証明としない。
既存health ruleを変更せずraw値を保持した。障害停止原因はCUDAではなくHost formatter。
旧tracked artifact/source **9025 files**のSHA256と新cohort freeze/runtimeを終了後照合し、不変を確認。

## 20. Tokens / time

| Task末尾 | input tokens | output tokens | Worker秒 | Host validation秒 |
| --- | --- | --- | --- | --- |
| 001 | 696 | 39 | 65.531 | 39.565 |
| 002 | 749 | 93 | 43.234 | 33.203 |
| 003 | 722 | 25 | 44.328 | 36.171 |
| 004 | 7717 | 238 | 68.422 | 43.453 |
| 005 | 5321 | 166 | 75.64 | 51.765 |
| 006 | 1302 | 38 | 46.75 | 37.609 |
| 007 | 3615 | 164 | 51.531 | 37.765 |
| 008 | 2925 | 129 | 46.25 | 34.484 |
| 009 | 3459 | 174 | 46.109 | 32.452 |
| 010 | 2599 | 122 | 47.953 | 36.579 |
| 011 | 3821 | 210 | 10.281 | 0 |
| 013 | 2569 | 56 | 7.484 | 0 |

Local input **35,495** / output **1,454 tokens**、generation API **19 calls**。
Ollama報告duration合計 **73.627秒**、Worker経過合計 **553.513秒**、cohort実行wall **560.828秒**。
inputはAPI報告値を合算しcached tokenを二重加算していない。順序・model load・WSLビルドcacheの影響を含むためモデル速度比較には使わない。
Codex最小修正と再検証のwall計 **206.281秒**は別計測。
Codex exact tokens / active time / net_codex_tokens_savedはすべてnull。比較可能なCodex-only baselineは実施していない。

## 21. Review burden

| Task末尾 | packet bytes | files | 最終diff LOC | validation結果数 | 追加分析bytes² | review wall秒 |
| --- | --- | --- | --- | --- | --- | --- |
| 001 | 8019 | 1 | 7 | 7 | 0 | 14.139 |
| 002 | 8415 | 1 | 8 | 7 | 0 | 41.667 |
| 003 | 8062 | 1 | 2 | 7 | 3021 | 394.131 |
| 004 | 13093 | 1 | 12 | 14 | 7960 | 352.458 |
| 005 | 12290 | 1 | 12 | 14 | 0 | 17.342 |
| 006 | 11264 | 1 | 6 | 7 | 3496 | 116.212 |
| 007 | 13934 | 1 | 5 | 7 | 0 | 21.979 |
| 008 | 10471 | 1 | 6 | 7 | 3326 | 71.990 |
| 009 | 12069 | 1 | 6 | 7 | 0 | 30.287 |
| 010 | 8340 | 1 | 2 | 7 | 3071 | 45.852 |
| 011 | 11196 | 1 | 3 | 0 | 35615 | 204.072 |
| 013 | 3672 | 1 | 0 | 2 | 0 | 14.719 |

通常レビューpacket合計 **120,825 bytes**、中央値 **10833.5 bytes**。各Taskは構成済みpacket 1ファイル。
元artifact数・hashも保存している。Local全会話を通常レビューへ展開していない。
²追加分析bytesは保存した診断・Host解析の計測値（同じ内容の再読やすべてのtool出力を含む正確なCodex入力token計測ではない）。
review wall interval合計 **1324.849秒**は待機・他Taskとの重なりを含み、active timeでも純レビュー作業時間でもない。
planning / normal final review / failure analysis / code repair / infra-protocol analysisをworkload.json（元資料: reviews/workload.json）で分離した。
通常レビューが短い例は得られたが、Host停止分析を含めた全体の省力化やtoken削減を断定できない。

## 22. Failures

- 003/006/008/010: 不要なString→String `.into()`。semantic/acceptanceはPASS、Clippy-onlyでESCALATE。現行lint-only eligibility維持。
- 004: 初回acceptanceのerror文字列未変更、repair後にE0283。same-model repairは1回で終了。
- 011: Host formatterによる末尾カンマ挿入とlexical guardの不一致。cohort STOP、能力評価から除外。
- 012: 停止により未実行。失敗扱い・代替モデル実行なし。

REJECTは1件（Host停止）、重大Codex修正0、task design failure0、scope/hash違反0。今後のlint-only policy検討は別変更として扱う。

## 23. Expansion judgement

**NEEDS_PROTOCOL_REVISION**。
ACCEPT_NO_CHANGE 50%と小さいCodex修正量だけならlimited shadowの材料になるが、cohortを止めるHost制約が再現した。
完走率100%とDEBUGGING観測を満たせず、20〜30 Taskへの拡大を推奨する段階ではない。
次の独立変更では、rustfmtによる標準構文の末尾カンマ正規化を安全に扱う境界を検討する。
macro一般へ無条件にtoken変更を許す案は避け、対応範囲とscope・literal・comment・macro保護の回帰を別レビューする。
lint-only repair eligibilityは別論点。今回の結果を受けて両者を同時に無断変更していない。
再試行は承認された改修・検証後の新cohortとし、今回/旧STOPを解除して継続しない。

## 24. 結論

固定v2.2.1で、dispatchしたLocal Taskの半数（6/12）はCodexがコードを書かずに受け入れられた。
一方5件に合計12 LOCのCodex修正が残り、Host formatting制約1件でcohort完走に届かなかった。
小さい修正量だけをもって運用成功とはせず、model capability、Host制約、Codex負担、infrastructureを分離して保存した。

入口: run-history（元資料: run-history.json）、summary（元資料: metrics/summary.json）、Task CSV（元資料: metrics/task-metrics.csv）、
requests（元資料: metrics/request-index.json）、repair context（元資料: metrics/repair-context.json）、integrity（元資料: metrics/integrity.json）。
新しいmicro experiment、routing変更、budget増加、追加model inferenceは行っていない。
