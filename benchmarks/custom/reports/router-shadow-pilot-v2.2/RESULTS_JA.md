> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/router-shadow-pilot-v2.2.md). This report alone does not establish a task result.

# Router / Worker v2.2 Shadow Pilot 結果

判定: **NEEDS_PROTOCOL_REVISION**。

12 Taskを事前freezeし、Local対象11件のうち8件を実行した。
**6件が初回PASS・ACCEPT_NO_CHANGE**。通常のCodex実装・retry prompt・修正は0、Codex repair LOCも0だった。
一方、1件はcompile failure後のrepair context超過、1件はHost formatter guardで停止した。
後者でcohort STOPとなり、3件は未実行。途中で条件変更・再実行・別モデルfallbackは行っていない。

**INFRA_ERROR=0、CUDA=0、FALSE_GREEN=0**。今回の停止はCUDAではなくHostのformatting境界による。
Hostを含む運用全体の完走性が不足しているため、75%という実行済みACCEPT_NO_CHANGE率だけで拡大を判断しない。

## 1. Cohort概要

- Cohort: `router-shadow-pilot-v2.2`
- 実装基点: `d06483c`（実装本体 `1e3362d`）
- 実行前freeze commit: `08e1eaf`
- Profile: `bounded_v2_2` / `2.2.0`
- 実行日時: 2026-09-29 22:36:06〜22:42:26 JST
- 実行順: P22-001〜009 → 011 → 010。Gemma26をまとめてから既存DEBUGGING roleのCoderNextへ進む計画
- 実際はP22-008で停止。P22-012のCodex boundaryは事前に判定済み

freeze.json（元資料: freeze.json）は12 Task、planning、harness、runtime hashを保持する。
cohort.json（元資料: cohort.json）はLocal対象11 Taskのsource/tests、Coverage Matrix、ReferencePlan、
model digest/options、validation argv/順序、routing decisionを凍結する。

実repo sourceの私有コピーに、Hostがregion、固定interface/scaffold、acceptanceを用意した。
対象は現在のdry-runアプリケーションの診断・表示・局所処理。新規business Task 10件、既存business比較2件。
10件のコードTaskは全件、dispatch前に意図したacceptance失敗を確認した。
選定理由・除外理由はplanning/selection.json（元資料: planning/selection.json）、事前検証はplanning/checks/（元資料: planning/checks/）に保存した。
結果を見たTask差し替えや、成功Taskだけへの絞り込みは行っていない。
小規模repoのため診断/表示Taskに偏っており、広範な開発仕事への代表性は限定される。

## 2. Task一覧

| ID | Task | Protocol / model | Local final | Codex review |
|---|---|---|---|---|
| P22-001 | MemoryPressure evidenceへused_kib | fixed / Gemma26 | PASS・初回 | ACCEPT_NO_CHANGE |
| P22-002 | CLI optional inventoryをdecimal/unavailable表示 | fixed / Gemma26 | PASS・初回 | ACCEPT_NO_CHANGE |
| P22-003 | meminfo欠落fieldの診断 | fixed / Gemma26 | PASS・初回 | ACCEPT_NO_CHANGE |
| P22-004 | VmRSS parse errorへfield context | fixed / Gemma26 | PASS・初回 | ACCEPT_NO_CHANGE |
| P22-005 | CLI警告の順序を保った重複除去 | fixed / Gemma26 | PASS・初回 | ACCEPT_NO_CHANGE |
| P22-006 | HighLoad evidenceへCPUあたりload | stateful / Gemma26 | PASS・初回 | ACCEPT_NO_CHANGE |
| P22-007 | no-anomaly auditへprocess数 | stateful / Gemma26 | ESCALATE / CONTEXT_LIMIT | REJECT |
| P22-008 | skill reasonへevidence件数 | stateful / Gemma26 | ESCALATE / FORMAT_SCOPE_VIOLATION | REJECT（Host失敗） |
| P22-009 | memory evidenceへ最大RSS process | stateful / Gemma26 | NOT_RUN | N/A |
| P22-010 | CPU labelの過剰count修正 | fixed / CoderNext | NOT_RUN | N/A |
| P22-011 | ResourceBudget defaultのtyped抽出 | reasoning / Gemma26 | NOT_RUN | N/A |
| P22-012 | 高リスクの実行権限再設計という境界 | Codex boundary | Local dispatch 0 | CODEX_ONLY |

P22-006/007はB5-003/004と同じbusiness目的だが、新しいTask/acceptanceから実際に再生成した。
旧PASSを分母へ再利用していない。Task 009/010/011をFAILやREJECTとして数えない。
P22-012は安全なrouting判定の確認だけで、実行権限を変更する実装はしていない。

## 3. Protocol / model分布

計画はGemma26 fixed 5、stateful 4、reasoning 1、CoderNext DEBUGGING fixed 1、Codex boundary 1。
実行できたのはGemma26 fixed 5、stateful 3。実generationは合計11 call（fixed 5、statefulのread+editが6）。

Gemma12 quarantine、Gemma26 active、Qwen14 experimental、CoderNextのDEBUGGING roleを維持した。
Gemma12/Qwen14へのdispatchは0。CoderNextは未実行なので、今回の成功率・速度・品質評価はN/A。
Gemma26から別モデルへの切替は実際には発生していない。

## 4. ACCEPT_NO_CHANGE

| 分母 | 結果 | 解釈 |
|---|---|---|
| 実行・レビュー済みLocal 8件 | **6/8 = 75.0%** | Host失敗も含む主要運用KPI |
| Host失敗1件を除く能力/protocol評価対象 | 6/7 = 85.7% | capability補助指標。Host失敗をモデル能力FAILへ混ぜない |
| 当初計画Local 11件 | 6/11 = 54.5% | cohort全体で得られた無修正成果の割合。未実行を能力FAILとはしない |

ACCEPT_NO_CHANGEは、モデル生成とHost formattingの後にCodex修正が不要だったという意味。
raw model candidateが常にformat済みだったという意味ではない。
ACCEPT_WITH_MINOR_FIX / ACCEPT_WITH_MAJOR_FIXはともに0。REJECTは2件。

## 5. First / final PASS

初回PASSは6件、Local final PASSも6件。
実行済み全体では6/8（75.0%）。Host失敗を除く分母では6/7（85.7%）。
P22-008はsemantic validation未実施のためfirst_pass=null。coding FAILへ変換していない。
Local FAIL後にCodexが直してPASSへ書き換えたTaskはない。

## 6. Repair

repair generationのdispatchは0。repair recoveryは分母0なのでN/A。
P22-007ではrepair用fresh capability/referenceをHostが準備したが、入力上限によりAPI前で停止した。
`attempts=2` / `edit_generations=2`はこの予約段階も含む既存runtime counterであり、
2回の実コード生成を意味しない。実際はread 1 + 初回edit 1、repair generation 0だった。

repair入力は **27,230 serialized message chars > 24,000**。
上限引上げ、diagnosticの書換え、Codex retry prompt、format-only LLM repairは行っていない。
証跡: P22-007-repair-budget.json（元資料: diagnostics/P22-007-repair-budget.json）。

## 7. Codex intervention / workload

- 通常実装・repairへの介入: **0/8**
- Codexが書いたretry prompt: **0**
- 終了結果に対するHost/protocol failure分析: **2/8 = 25.0%**（007/008）
- planning、最終review、failure分析の正確なCodex tokens / active time: **null**

したがって「介入0」を全作業について主張しない。
Task分割、scaffold、acceptance、ReferencePlanはCodex/Hostが先に作成している。
変更前acceptanceの確認や、各Taskの全workspace検証にも作業・実行コストがある。
reviews/workload.json（元資料: reviews/workload.json）にphaseを分けて保存した。
code採否のreview annotationは元のまま保持し、その後のfailure分析を別記録として追加している。

## 8. Codex repair LOC

全実行Taskでchanged files=[]、added/deleted LOC=0、Codex repair LOC=0。
007/008の小修正をCodexが代行していない。アプリケーションへの採用もしていない。
Host formatterによる14 LOCはCodex repair LOCへ混ぜない。

## 9. FALSE_GREEN

**0件**。Local PASS 6件すべてで、configured validation PASSと最終diffの契約整合を確認した。
007/008はLocal PASSではないためFALSE_GREENではない。
Coverage mappingが完全であることと、全入力についてのsemantic coverageが完全であることは区別する。

## 10. Stateful apply / protocol別

| Protocol | 実行 | First/final PASS（Host含む） | ACCEPT_NO_CHANGE | repair dispatch |
|---|---:|---:|---:|---:|
| fixed_slot | 5 | 5/5 | 5/5 | 0 |
| stateful | 3 | 1/3 | 1/3 | 0 |
| reasoning | 0 | N/A | N/A | 0 |

statefulのcapability評価: **3 selected / 3 valid apply = 100%**。
unknown/stale/foreign handle、unsafe fuzzy apply、モデルによるscope逸脱は0。
DISCOVERYではread-only、EDITではissued-ID enumを使用した。
007/008もbody適用そのものは成功しており、valid applyと最終PASSを同一視しない。

## 11. Typed References

| Task | 宣言数 | symbols | Host packet bytes |
|---|---:|---|---:|
| 001 | 2 | SystemState, Memory | 1,828 |
| 003 | 1 | Memory | 855 |
| 006 | 3 | SystemState, Event, EventKind | 2,840 |
| 007 | 2 | Observer, SystemState | 2,103 × 2 issue |
| 008 | 1 | Event | 1,173 |

宣言付きReferencePlanは計画6 Task/13宣言、実行5 Task/9宣言。
007の2回目packetは準備のみで送信されていない。
型参照不要の002/004/005は宣言0。既存profileが発行する空referencesとslot bindingのenvelopeは各246 bytesで、
追加の型contextとして扱わない。参照単体の厳密input tokensはnull。

UNKNOWN_FIELD=0、UNKNOWN_SYMBOL=0、WRONG_SIGNATURE=0、**WRONG_TYPE_ASSUMPTION=1（007のE0308）**。
007は正しい`state.processes.len()`を使ったが、`self.record`の引数に必要なborrowを満たさなかった。
Host planにはObserver/SystemStateがあり、record helper signatureは含まれていなかった。
型参照あり/なしTaskの単純ランキングや、今回から参照の因果効果を推定することはしない。

## 12. Host formatting / validation workload

採用済みHost formatting LOCは **14**（001:5、006:4、007:5）。
008にはformatter diffが存在するがguardで拒否され、候補へ採用されていないため採用LOCは0。
raw model diff、Host format diff、最終候補diffを別保存している。

事前freezeしたCoverage criteriaは85、validation定義は62（boundaryの決定的検査を含む）。
コードTaskはacceptance → regression → format → clippy → workspace check → build、その後scope guard。
001〜006は各7結果すべてPASS。007はcompile errorを複数の固定checkが報告。008はmandatory validation前に停止。
Host validation実行時間は合計 **266.447秒**。単純なLocal生成の短さだけで総効率を評価しない。

## 13. Task design failure

runtimeが返したTASK_DESIGN_FAILUREは0。全12 TaskのCoverage mappingはdispatch前に検査した。
ただし007は直接helperの型契約がcontextに不足しており、Host planning品質に改善余地がある。
これは観測済みLocal結果を後からTASK_DESIGN_FAILUREへ変更する意味ではない。
未実行3件についてはpreflightだけで実装品質を評価しない。

## 14. Infrastructure

Ollama 0.34.4、RTX 3080 10GB、driver 591.86。
Gemma26 digest: `08ae7ec1744bd7f451c4a530afb39d2673ad9d07a8369b8a33a3613b41212a68`。
temperature=0、seed=20260926、num_ctx=8192、num_predict=2048、stream=false、think=falseを維持した。

- generation 11 callはHTTP 200。Gemma12 dispatchは0
- INFRA_ERROR / CUDA / GPU query timeout / residency mismatch: すべて0
- Task前後のsnapshotは16件。GPU使用量は1,025〜9,743 MiB（sampling中の真のpeakではない）
- 開始前・停止後のread-only health checkもPASS
- generation probe、強制unload、restart、driver/runtime/model変更は0

今回Gemma26だけが実際に動いたため、model switchingやCoderNextの安定性は未測定。
VRAM使用量の高さからOOM等を推定しない。証跡はenvironment/（元資料: environment/）とGPU snapshots（元資料: metrics/gpu-snapshots.json）。

## 15. Tokens / time

| Task | input | output | Worker秒 | validation秒 |
|---|---:|---:|---:|---:|
| 001 | 1,434 | 92 | 73.406 | 39.983 |
| 002 | 687 | 42 | 41.906 | 32.780 |
| 003 | 1,143 | 148 | 49.719 | 38.889 |
| 004 | 695 | 42 | 49.359 | 40.358 |
| 005 | 688 | 86 | 51.328 | 41.579 |
| 006 | 3,931 | 223 | 55.125 | 40.125 |
| 007 | 3,386 | 160 | 45.922 | 32.733 |
| 008 | 2,905 | 129 | 8.407 | 0 |
| **合計** | **14,869** | **922** | **375.172** | **266.447** |

cohort実行wall timeは379.797秒。Ollama報告total_durationの合計は53.331秒。
Worker秒にはprivate copy、format、checks、health等も含む。planning/review時間は含めない。
cache tokensは別のraw usageとして保存しており、inputから恣意的に減算しない。

## 16. Review burden

通常review入力はTask Spec、review.json、model diff、Host diff、最終diffの5 files。
Local会話全文は読んでいない。失敗2件のみ、その後に実validation/formatter/context診断を追加確認した。

| Task | 通常入力bytes | diff LOC | validation結果数 | review wall秒 | 追加分析bytes |
|---|---:|---:|---:|---:|---:|
| 001 | 23,310 | 9 | 7 | 12.64 | 0 |
| 002 | 20,035 | 5 | 7 | 23.86 | 0 |
| 003 | 22,389 | 12 | 7 | 8.41 | 0 |
| 004 | 20,475 | 2 | 7 | 10.50 | 0 |
| 005 | 20,618 | 8 | 7 | 19.78 | 0 |
| 006 | 25,063 | 6 | 7 | 19.86 | 0 |
| 007 | 22,870 | 5 | 7 | 104.47 | 15,871 |
| 008 | 20,284 | 2 | 0 | 68.57 | 8,563 |

review.json単体は中央値7,683 bytes。Task/diffsを含む通常入力は中央値21,503.5 bytes、計175,044 bytes。
失敗分析は各2 filesを追加。上表のwall intervalにはtool待ち・分析が入り、batch reviewでは区間が重複する。
合計268.080秒をactive review timeや正味Codex労働時間と解釈しない。active timeはnull。
start/end、各fileのbytes/SHA、分類はreviews/（元資料: reviews/）に保存した。

## 17. Optional baseline / Codex節約

Codex-only baselineは未実施。追加の独立実装コストと、厳密token/active-time計測手段がないことを理由に見送った。
**net Codex tokens saved = null**。Local tokensを節約量へ換算しない。
確認できたのは、6件で事前planning後の実装・通常repair・小修正をCodexが行わずに済んだことまで。

## 18. Failure analysis

### P22-007: compile failure → repair context超過

初回候補は`format!`の`String`を`&str`引数へ渡し、E0308で失敗した。
field hallucinationは回避できたが、直接helperのsignature理解が不足していた。
acceptance/regression/clippy/check/buildの実stderrはそれぞれコンパイル進捗等も含み、
losslessなrepair入力が27,230文字になった。完全に同一でないdiagnosticsは既存方式では共有化されない。
上限guardは正しく機能し、repair APIを送っていない。
残る課題は、Task planningでのhelper契約充足と、固定予算内でのdiagnostic運用である。

### P22-008: Host lexical guardによる停止

rustfmtは`format!(...).into()`を複数行へ整形した。
scope内の変更であり、比較した全tokenの種類・値は同一だった。
差は、閉じ括弧と`.`の隣接状態を記録するfingerprint flag **true→falseの1箇所だけ**。
通常のmethod-chain改行を保守的guardが拒否したという根拠が得られた。
これはモデルのcoding能力失敗やCUDAではなく、Hostのformatting適用可能性の問題である。

証跡: lexical comparison（元資料: diagnostics/P22-008-lexical-comparison.json）、
拒否されたnormalized source（元資料: diagnostics/P22-008-rejected-normalized.rs）、
formatter record（元資料: workspace/records/router-v2.2/P22-008/format-1/record.json）。
候補のsemantic/clippy validationは実行されていないので、「guardさえなければPASS」とは評価しない。
補助観測として固定stable rustfmtは`skip_children=true`がnightly専用である旨のwarningも返したが、
今回の直接停止理由はlexical identity判定であり、このwarningと混同しない。

STOPはSTOP.json（元資料: STOP.json）とcohort STOP（元資料: cohort.json.STOP.json）に保存した。
profile/formatter/Task/checksを変更して回避することはせず、残り009/011/010を停止した。

## 19. Expansion judgement

**NEEDS_PROTOCOL_REVISION**。

fixed_slot 5/5無修正成功は有望だが、statefulの2失敗、Hostによるcohort停止、
DEBUGGING/reasoning未実施が残る。20〜30 Taskへの拡大を現時点では推奨しない。

次の別変更で検討する事項:

1. method-chain改行と意味に関係するpunctuation jointnessを区別できるHost guardの検証。guardを単に無効化しない。
2. helper引数・戻り値の契約がHost planで不足するTaskをdispatch前に識別する。reference/edit source重複制約は維持して設計する。
3. lossless diagnosticsと固定context予算の両立を、今回の保存済み失敗を用いて検討する。今回の上限を後から引き上げない。

この作業では上記修正、追加micro experiment、停止cohortの再開を実施していない。

## 20. 結論 / 証跡保全

6件ではCodexの仕事を事前planningと短いfinal reviewへ限定できた。
一方、2件でHost/contract運用の分析が必要になり、全cohortを完走できなかった。
無修正成功件数と同時に、Host設定・validation負担・停止による未実行を含めて評価する必要がある。

旧tracked 7,595 files、実装/profile/registry、freezeしたTask/source/tests/referencesのhashは不変。
旧Pilot、CUDA Phase 1/2/3、B2〜B5、applicationへの変更は0。Local結果の再ラベル・上書きは0。

主要成果物:

- run history（元資料: run-history.json）: result / review / raw / healthへ追跡
- 集計（元資料: metrics/summary.json）、Task別JSON（元資料: metrics/task-metrics.json）、Task別CSV（元資料: metrics/task-metrics.csv）
- Request監査（元資料: metrics/request-index.json）、整合性監査（元資料: metrics/integrity.json）
- Task index（元資料: task-index.json）、Task specs（元資料: tasks/）、Coverage/Reference/runtime freeze（元資料: cohort.json）
- Workload記録（元資料: reviews/workload.json）、failure診断（元資料: diagnostics/）
