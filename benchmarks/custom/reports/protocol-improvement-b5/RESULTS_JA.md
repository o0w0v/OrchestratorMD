> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/protocol-improvement-b5.md). This report alone does not establish a task result.

# B5 — Host-provided Typed Read-only References 実験結果

判定: **PROMISING_FOR_V2_2**。

3 Taskすべて初回PASS、最終PASS、ACCEPT_NO_CHANGE。B4-004の`UNKNOWN_FIELD`を初回で回避し、
repairは1→0、FALSE_GREEN / Codex repair LOC / INFRA_ERRORは0だった。
追加micro experimentは一旦終了し、Router / Worker v2.2統合案（元資料: V2_2_INTEGRATION_PROPOSAL_JA.md）を作成した。
production統合、B6、Pilot再開は行っていない。

実行: 2026-09-29 18:55:30–18:57:57 JST。条件freeze: commit `4c66c5e`。
branch: `experiment/protocol-improvement-b5`。元B4結果commit: `3666e15`。

## 1. 目的

EDIT開始時にHostが小さいtyped read-only referenceを供給し、型・field・signature不足による
初回compile/semantic failureが減るか確認する。モデルの自由な探索権限は増やさない。

主変数は参照packetのみ。B4と同じ3 business Task、acceptance、seed source、checks、Gemma26、
generation optionsを使用した。参照に正解コードやgolden patchは含めていない。

## 2. B4の残課題

B4-004の最初の候補は`state.process_count`を使用し、rustc E0609でcompile失敗。
same-model repairで`state.processes.len()`へ直り、Host formatting後にPASSした。
この初回失敗はformatの問題ではない。B4-003/005は初回PASSだった。

旧結果はread-only比較。B4の失敗・repair・tokens・diffは書き換えていない。
比較元: B4結果（元資料: ../protocol-improvement-b4/RESULTS_JA.md）。

## 3. Reference Packet設計

EDIT feedbackの`typed_read_only_references`に次を追加した。

- `read_only=true`
- 現在発行済みの`region_id`、source hash、content hash
- `kind / symbol / file / range / source_hash / excerpt_hash / excerpt / extraction_rule / inclusion_reason`

body自体は既存discovery feedbackにあるため重複させない。
型sourceはprotected inputで、edit handleを発行しない。
1 Taskにつき初回EDITで1 packet。repair時もfresh handleに対応するpacketを渡す実装だが、
今回liveではrepairなし。repairの参照再発行はofflineで検証した。

上限4 references、packet 4096 UTF-8 bytes、単一宣言1600 bytes。
サイズ超過やprovenance不一致はHost errorで停止し、truncateや追加探索はしない。

## 4. Extraction rule

Hostが事前固定した有限のdependency edgeから宣言を抽出する。

| Task | 抽出規則 | symbols |
|---|---|---|
| B5-003 | function parameter / return element / direct enum | SystemState, Event, EventKind |
| B5-004 | parameter trait signature / direct helper return | Observer, SystemState |
| B5-005 | function parameters / return element | Intent, Event, ActionProposal |

抽出元は各seedの`crates/ncos-core/src/lib.rs`。
実装はflat struct fields、unit enum、bodyなしtrait signatureだけを受け付ける。
未対応構文や曖昧なsymbolは拒否し、無制限に依存型へ辿らない。
型の候補選定はHostがレビューした静的tableであり、一般的なRust型推論を実装したわけではない。

file全体SHA256、抜粋SHA256、行/byte範囲、ruleとinclusion reasonを
references/（元資料: references/）に保存しfreezeした。runtimeがbaselineから再抽出して完全照合し、
EDIT直前にもdiskとメモリ上のprotected sourceを検証した。

## 5. Task一覧

| B5 | 対応B4 | 責務 | 役割 |
|---|---|---|---|
| B5-003 | B4-003 | HighLoad evidenceへload/CPU比を追加 | 成功control |
| B5-004 | B4-004 | anomaly-free auditへsnapshot process数を追加 | 主paired Task |
| B5-005 | B4-005 | skill report reasonへevent targetを追加 | 成功control |

追加Taskは0。今回の主変数を3つの既存Taskで比較することを優先した。
Task JSONとcoverageの差はcohort Task IDのみ。source、validationは同一。
readable filesやmodel tool schemaを拡張していない。

## 6. Referenceサイズ

| Task | count | symbols | excerpt bytes | packet bytes | packet tokens推定 |
|---|---:|---|---:|---:|---:|
| B5-003 | 3 | SystemState / Event / EventKind | 681 | 2,285 | 572 |
| B5-004 | 2 | Observer / SystemState | 507 | 1,710 | 428 |
| B5-005 | 3 | Intent / Event / ActionProposal | 500 | 2,117 | 530 |

packetはmetadata・provenance・handle binding込み。合計6,112 bytes、平均2,037.3 bytes。
宣言本文合計は1,688 bytesであり、metadataにもコストがある。

**参照単体の厳密input tokensはnull**。Ollama APIはwhole requestのtoken数を返し、
区間単位のtoken数は返さない。上表は`ceil(serialized UTF-8 bytes / 4)`の推定。
tokenizer実測として扱わず、追加probeやpackage installもしていない。
実際のEDIT全入力の増加は第12節で別に示す。この例では単純bytes推定は増分より小さい。

## 7. Initial compile / semantic結果

| Task | initial compile | initial semantic | raw候補format | Host後format |
|---|---|---|---|---|
| B5-003 | PASS | PASS | FAIL | PASS |
| B5-004 | PASS | PASS | FAIL | PASS |
| B5-005 | PASS | PASS | FAIL | PASS |

compile/semanticはB4同様、Host正規化後の最初の固定validationで判断する。
raw候補に対するsemantic testは実施していないため、その段階はNOT_RUN。
formatter前後のRust lexical identityを全3候補で確認し、Hostによる意味変更はない。

B4-004の初回はcompile FAIL / semantic NOT_RUN_COMPILE_FAILED。
B5-004ではraw候補の時点で`state.processes.len()`を使っており、formatterがfieldを修正したのではない。

## 8. First PASS

**B4 2/3（66.7%）→ B5 3/3（100%）**。

B5-004に`REFERENCE_ASSISTED_FIRST_PASS=true`を記録した。
B4の初回compile失敗に対し、B5は同じbusiness Task・acceptanceで初回合格したという対比較を表す。
一般的な因果、未知Taskへの成功率、すべての型hallucination防止へは外挿しない。

controlsは両方とも初回PASSを維持。3件の最終diffは、対応するB4最終diffとbyte一致した。

## 9. Repairとformatting

semantic / compile / acceptance failureだけsame-model repair最大1回というB4 policyを維持。
今回repairは**0回**。B4の1回から削減した。repair recovery rateは分母0なのでN/A。
Codexが通常retry promptを書いた回数は0。

Host formatterは全3候補で動作し、formatを回復した。
Host変更LOCは4 / 5 / 5、合計14。B4の合計19との差5 LOCは、B4-004初回失敗候補にも
formatを行っていたことによる。format-only LLM repairは0。

model-generated diff、Host format diff、final normalized diffは別保存。
scope外format変更、token変更、formatter errorは0。

## 10. ACCEPT_NO_CHANGE

**3/3（100%）**。最終diff、Task/coverage、selected handle、実check結果、短いsummaryを確認した。
Local全会話はreview入力にしていない。raw JSONは機械監査でschema・hash・費用を照合した。

- B5-003: threshold、zero CPU/non-finite guard、event identity、memory-first orderingを維持し、比率表記だけ追加。
- B5-004: no-anomaly reasonだけ変更。返却snapshot、record、provider/token、anomaly/invalid-intent経路は不変。
- B5-005: reasonにevent targetを追加。実action targetはsystemのままで、権限・risk・evidence・unsupported rejectionを維持。

ACCEPT_NO_CHANGEは**model + Host formatter候補にCodex修正が不要**という意味。
raw modelだけでformatも完成していたとは扱わない。Codex repair LOC=0、FALSE_GREEN=0、REJECT=0。
application sourceへの採用は行っていない。

## 11. 型hallucination

| 分類（初回Task件数） | B4 | B5 |
|---|---:|---:|
| UNKNOWN_FIELD | 1 | 0 |
| UNKNOWN_SYMBOL | 0 | 0 |
| WRONG_SIGNATURE | 0 | 0 |
| WRONG_TYPE_ASSUMPTION | 0 | 0 |

error codeと診断から分類。B4-004の同じE0609が複数checkに出てもTask件数としては1。
対象code mappingはREADMEおよびmetrics scriptに保存した。
UNKNOWN_SYMBOL/signature/type assumptionについて失敗→改善のlive例は今回なく、改善効果は未検証。

## 12. Token costと時間

| Task | input B4→B5 | output B4→B5 | Worker秒 B4→B5 | 初回EDIT input増分 |
|---|---:|---:|---:|---:|
| 003 | 1,826→2,880 | 274→274 | 55.453→66.188 | +1,054 |
| 004 | 7,949→2,570 | 430→230 | 55.843→41.453 | +785 |
| 005 | 1,686→2,694 | 181→182 | 35.703→36.828 | +1,008 |
| 合計 | **11,461→8,144** | **885→686** | **146.999→144.469** | **+2,847** |

初回EDITの実入力増分は平均949 tokens/Task。既に成功していたcontrolsには純粋な追加費用がある。
この3件では、初回EDITに計2,847 input tokens追加し、B4-004のrepair 1回を省けた。
B4の当該repair入力6,164 tokensがなくなったため、cohort全体は3,317 input tokens減少した。
つまり「毎回約1,000 tokensを追加して今回1 repairを減らした」という規模のtradeoffであり、
常に得になるとは言えない。型参照不要Taskへ無条件に大きいpacketを配る根拠にはしない。

上の初回EDIT差はAPI報告whole-inputのpaired差であり、参照区間の厳密token数ではない。
Task IDとopaque handle namespaceを正規化すると、初回requestは参照packet以外すべて一致した。
raw request bytes、hash、packet bytes、累積転送bytesと推定値はrequest indexから監査可能。

generation callsは7→6、wall timeは150.069→147.601秒。
少数・別時点の実行であり、load/cache・validation時間にも変動がある。速度改善とは断定しない。
Codex planning/review tokens・作業時間は未計測のためnull。local tokensをCodex節約量へ換算しない。

## 13. Security / scope

Coverage Gate、stateful DISCOVERY→EDIT、issued-ID enum、snapshot/hash binding、formatter、mandatory checksを維持。
reference sourceに任意read/search/path/edit権限を追加せず、EDITに公開するのはreplace_regionだけ。
3 issued / 3 selected / 3 valid apply、valid-region-apply Task率3/3。
invalid/stale ID、unsafe fuzzy apply、scope違反、TEST_NOT_ALLOWEDは0。

オフライン境界検証は42/42 PASS（reference10 + formatter11 + stateful11 + B2 regression10）。
参照改変・source drift・oversize・未知宣言・stale capability・format-only repair禁止等を検証した。
既存Python検証77 PASS、必須cargo fmt/clippy/test/check/build PASS。
最終3 candidateのfull workspace regressionも全PASSで、実行前後source hash不変。

private Git copyはOS sandboxではないという既存制限は残る。任意の悪意あるコードに対するOS隔離を主張しない。

## 14. Infrastructure

- Model: `gemma4:26b`
- Digest: `08ae7ec1744bd7f451c4a530afb39d2673ad9d07a8369b8a33a3613b41212a68`
- Ollama: 0.34.4、GPU: RTX 3080 10GB、driver: 591.86
- Options: temperature=0、seed=20260926、num_ctx=8192、num_predict=2048、stream=false、think=false
- generation response 6件すべてHTTP 200 / done=true / done_reason=stop
- INFRA_ERROR=0、CUDA=0、backend crash=0、GPU query timeout=0、OUTPUT_LIMIT=0
- baseline/finalとTask前後のhealth snapshot 8件、問題検出0
- snapshot GPU used: 1,046–9,629 MiB（連続samplingのpeak値ではない）

generation probe、強制unload、restart、model switching、Gemma12、Qwen/CoderNext fallbackは実行していない。
Router/Operational Policy/driver/runtime/model filesは不変。infra stabilityをcoding scoreへ加算していない。

## 15. B4 paired comparison

| 指標 | B4 | B5 |
|---|---:|---:|
| Task | 3 | 3 |
| First PASS | 2/3 | 3/3 |
| Final PASS | 3/3 | 3/3 |
| ACCEPT_NO_CHANGE | 3/3 | 3/3 |
| repair | 1 | 0 |
| UNKNOWN_FIELD / UNKNOWN_SYMBOL | 1 / 0 | 0 / 0 |
| FALSE_GREEN | 0 | 0 |
| Codex repair LOC | 0 | 0 |
| input tokens | 11,461 | 8,144 |
| output tokens | 885 | 686 |
| Worker秒 | 146.999 | 144.469 |
| valid region apply | 3/3 | 3/3 |
| INFRA_ERROR / CUDA | 0 / 0 | 0 / 0 |

Task/check/sourceは同一。モデル/option、coverage、phase tool schema、formatting engineは不変。
Task ID・opaque handle namespaceの差を除き、packetを外した初回EDIT requestがB4と一致することを
paired request監査（元資料: metrics/paired-request-equivalence.json）で確認した。
最終diffも全3件がB4最終diffとbyte一致。採点条件の緩和はない。

## 16. v2.2採用可否

**PROMISING_FOR_V2_2**。
主対象の初回型誤認回避、controlsの初回成功維持、小さいpacket、scope/security維持、
FALSE_GREEN=0、valid apply維持という事前の条件を満たした。

ただし対象は静的Host tableを作成したRustの3 Task、Gemma26のagentic経路のみ。
型抽出の汎用性・fixed_slotへのlive効果・他model・大型repo・長期運用は未検証。
常時参照によるinput増加とHost plan作成工数も採用時に評価する必要がある。

## 17. 統合へ進むか

追加micro experimentは一旦終了する。B6は自動開始しない。
v2.2統合案（元資料: V2_2_INTEGRATION_PROPOSAL_JA.md）に次を整理した。

Coverage Gate、known edit→fixed_slot、unknown edit→Stateful Discovery、issued-ID enum、
Typed Read-only References、bounded edit、snapshot binding、Host formatting、mandatory validation、
semantic repair×1、compact Codex review。

統合は新profileとして設計し、v2.1と旧artifactの互換性を維持する案。
実装と統合Pilotは別作業とし、今回productionやRouter設定は変更していない。

## 18. 結論と成果物

このpaired試験では、Hostが`Observer`/`SystemState`をread-onlyで供給することにより、
B4で発生したfield誤認がB5では初回候補に現れなかった。
Local修復を1回省き、controlsの成功と既存の適用・検証境界を維持できた。
1回の対比較として有望と判断し、ここでmicro experimentを止める。

主要成果物:

- run history（元資料: run-history.json）: raw request/response、diff、validation、packet、reviewへのpath
- paired comparison（元資料: metrics/paired-comparison.json）: Task別metricsとB4/B5集計
- reference metrics（元資料: metrics/reference-task-metrics.json）、reference request index（元資料: metrics/reference-request-index.json）
- formatting監査（元資料: metrics/format-task-metrics.json）、採用判定（元資料: metrics/adoption.json）
- health summary（元資料: metrics/health-summary.json）、整合性監査（元資料: metrics/final-audit.json）
- freeze（元資料: freeze.json）、旧証跡保護hash（元資料: protected-sha256.json）、統合案（元資料: V2_2_INTEGRATION_PROPOSAL_JA.md）

B5固定127 files・旧tracked 6,699 filesはhash不変。旧実験、Router、applicationの変更は0。
commitはB5専用artifactのみ。pushやapplicationへの自動反映は行っていない。
