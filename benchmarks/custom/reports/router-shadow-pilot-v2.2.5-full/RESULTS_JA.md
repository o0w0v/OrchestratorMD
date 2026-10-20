> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/router-shadow-pilot-v2.2.5-full.md). This report alone does not establish a task result.

# bounded profile 2.2.5 Full Shadow Pilot Retry

判定: **NEEDS_PROTOCOL_REVISION（STOP分類の限定的なレビューが必要）**。

**Full Pilotは未完了。** 新cohortでP224-001〜003を実行し、P224-003の`EDIT_SCHEMA_ERROR`で固定runtimeがcohort STOPした。Local terminal **3/13（23.08%）**、ACCEPT_NO_CHANGE **1/3（33.33%）**、未実行10件。旧STOPを解除せず、この新cohortのSTOPも保存した。

P224-001のRust構文不良はTask-localに隔離され、repair失敗後も002へ継続できた。今回の停止原因は別の経路で、CoderNextの返却bodyに**末尾改行がない**ため、適用前に拒否されたもの。JSON response schemaはvalid、sourceへのapplyは未実施、最終diffは空、scope/hash検証はPASS。**実際のsource破損ではなく、body契約違反をcohort-wide scope failureへ分類した結果**である。

INFRA_ERROR / CUDA / backend crash / GPU query timeout / FALSE_GREENはいずれも0。単なるmodel coding FAILを理由にRouterやモデル選択の再設計を求める判定ではない。指定したTask-local/cohort-wide境界と固定runtimeの分類に差があり、完走を妨げたことが限定的なprotocol reviewの根拠。途中でpolicyを変更して完走扱いにしていない。

## 1. Fresh process / environment

初回read-only観測時点でOllama frontend / app / llama-serverは既に不在だった。11434は接続拒否、`/api/version`・`/api/ps`も接続拒否、Ollama GPU processなし、nvidia-smi正常を完全終了gate（元資料: infrastructure/quit-001.json）へ保存。今回agentからkillは行わず、既に終了済みだったため新たなユーザーQuit完了発言を記録していない。

同じinstalled binaryを起動し、新frontend **PID43972**、start **2026-10-03 06:31:24.139747 UTC（15:31:24 JST）**、models=[]、backendなし、API正常、両model digest一致、事前inferenceなしを確認した。fresh start（元資料: infrastructure/fresh-start-001.json）。

| 項目 | 固定条件 |
| --- | --- |
| Ollama | 0.35.0、終了前後binary SHA256一致 |
| GPU / driver | RTX 3080 10GB / 591.86 |
| OS boot | 2026-10-01T09:57:54.1526480Z（今回のread-only取得値） |
| profile | bounded_v2_2 2.2.5 |
| Router / operational policy | 既存v2.1不変、Gemma12 quarantined |
| context / output / chars | 8192 / 2048 / 24000 |
| temperature / seed | 0 / 20260926 |
| stream / think | false / false |
| repair | syntax・semantic・lint合計最大1 |
| rustfmt | 1.9.0-stable、既存binary/config/hash固定 |

Gemma26 digest: `08ae7ec1744bd7f451c4a530afb39d2673ad9d07a8369b8a33a3613b41212a68`。
CoderNext digest: `ca06e9e4087c714d44355bf954099187890e63084b4a632b8e9956c4b9492074`。
環境freeze（元資料: environment/freeze.json）とruntime byte snapshot（元資料: runtime-snapshot/index.json）に保存。モデルdownload、settings変更、reboot、driver/runtime変更、generation probeなし。

## 2. Task一覧

新cohort: `router-shadow-pilot-v2.2.5-full`。元P224-001〜014のTask specificationをbyte同一で再利用。325入力ファイル、routing、validation、Coverage、ReferencePlan、Task順序も維持。旧2.2.4 cohortとの変更は保存先/run identityと、既に統合・検証済みのprofile 2.2.5のみ。再利用検証（元資料: reuse-verification.json）。

| Business ID | Task | 集計group | Model | 今回結果 |
| --- | --- | --- | --- | --- |
| P224-001 | CLI telemetryを改行しないescaped一行として表示 | fixed_slot | Gemma26 | ESCALATE / REJECT |
| P224-002 | memory evidenceにused KiBを独立した第2要素として追加 | stateful | Gemma26 | PASS / ACCEPT_NO_CHANGE |
| P224-003 | TCP inventoryが非data行の01を誤countする不具合 | debugging | CoderNext | ESCALATE / REJECT |
| P224-004 | CLIのused memory量を妥当性検査付きで表示 | fixed_slot | Gemma26 | NOT_RUN |
| P224-005 | MockObserverのnested snapshot値をtyped抽出 | reasoning | Gemma26 | NOT_RUN |
| P224-006 | 正常系auditへprocess sampleのcomplete/bounded区別を追加 | stateful | Gemma26 | NOT_RUN |
| P224-007 | VmRSSの値parse失敗へ診断prefixを付与 | fixed_slot | Gemma26 | NOT_RUN |
| P224-008 | HighLoad evidenceへ観測timestampを第2要素で追加 | stateful | Gemma26 | NOT_RUN |
| P224-009 | mock report reasonへ安定したevent kind labelを表示 | fixed_slot | Gemma26 | NOT_RUN |
| P224-010 | skill templateの診断へ現在evidenceのUTF-8 bytes合計を表示 | stateful | Gemma26 | NOT_RUN |
| P224-011 | CLI warning overviewのstable unique preview | fixed_slot | Gemma26 | NOT_RUN |
| P224-012 | meminfo重複診断へMemTotal/MemAvailableの名前を付加 | stateful | Gemma26 | NOT_RUN |
| P224-013 | Telemetry欠測を説明するUIの表示方針を決定 | boundary | Codex | CODEX_ONLY |
| P224-014 | CLI per-CPU loadの欠測/非有限値と小数表示 | fixed_slot | Gemma26 | NOT_RUN |

run identityは`router-shadow-pilot-v2.2.5-full/P224-xxx/run-001`。NOT_RUNは予約IDであり実行済みではない。全14件のroute・結果（元資料: analysis/all-task-outcomes.json）。P224-013はCODEX_ONLYの境界再確認で、アプリ実装の完了とは扱わない。

## 3. Execution order

固定: 001 → 002 → 003 → 004 → 005 → 006 → 007 → 008 → 009 → 010 → 011 → 012 → 014。
実測は001 → 002 → 003。003のSTOPで残り10 Localを未実行として保持した。結果を見たTask除外、並替え、別モデル救済、途中restartはない。run history（元資料: run-history.json）、STOP（元資料: STOP.json）。

## 4. Terminal coverage

Local: **3/13 = 23.08%**。dispatchした3件は全件terminalだが、全planned Localのterminalという主目的は未達。
boundaryを含むterminal: **4/14 = 28.57%**。NOT_RUNをPASS/FAILへ計上しない。

## 5. Cohort completion

**false / STOPあり**。cohort wall **179.187秒**、Worker合計 **154.986秒**。13 Localのうち10件が未測定であり、Full Pilot完走とは報告しない。END（元資料: END.json）。停止理由は固定runtimeが設定したscope-domain STOPで、CUDAやHost formatter failureではない。

## 6. ACCEPT_NO_CHANGE

**1/3 = 33.33%**（実dispatchしたLocalが分母）。002のみ変更なしで採用可能。REJECT 2、minor fix 0、FALSE_GREEN 0。
全planned Localで見ると採用可能を確認できたのは1/13だが、これは測定coverageを含む値でありcoding成功率ではない。未測定Taskについて推定しない。

## 7. First / final PASS

Local final PASSは**1/3**。全dispatchに対して初回PASSを確認した割合も**1/3**。
保存済みruntimeは003の`first_pass=null`（pre-apply rejection）としており、既存evaluable集計ではFirst PASS **1/2 = 50%**。両分母を区別する。003のcoding qualityはvalidation未実施で不明であり、事後にfalseへ書き換えていない。

## 8. Syntax failures / repair

P224-001は初回・repairとも**E0762 / CANDIDATE_SYNTAX_FAILURE**。candidate syntax failureは**2 attempts / 1 Task**、syntax repair invoked **1**、recovered **0**、failed **1**、syntax Task-local reject **1**。
raw候補をHostが書き直したり、Codexがescapeを修正したりしていない。構文不良はTask-localで完結し、002への継続を確認できた。mandatory semantic checksは未到達。

## 9. Semantic repair

invoked **0**、recovery **N/A**。syntax / semantic / lintを別々に1回ずつ許可していない。今回使用した唯一のrepair budgetは001のsyntax repair。

## 10. Lint repair

自然発生`clippy::useless_conversion` **0**、eligible **0**、invoked **0**、recovered **0**、recovery rate **N/A**。Clippyまで到達した002はPASS。
残り10件が未実行のため、今回cohortでlint policyの効果は評価できない。allowlist・eligibility・budget不変。

## 11. Fixed-slot

計画6件中1件（Gemma26、001）を測定。初回とrepairのbounded applyは成功したが、Rust構文不良でREJECT。ACN 0/1。CoderNextのfixed-slotはdebugging群へ分離し二重計上しない。

## 12. Stateful

計画5件中1件（002）を測定。DISCOVERY → issued region handle → EDIT、valid handle apply **1/1**、invalid/stale handle **0**。初回PASS / ACCEPT_NO_CHANGE **1/1**。
元のmemory validity/threshold guardとfirst evidenceを保持し、第2要素`used_kib=N`を追加。typed fieldsを使ったsaturating subtractionは既存のvalid input domainで指定差分と一致する。scopeと全mandatory checks PASS。

## 13. Debugging

計画1件（003 / CoderNext）をdispatch。HTTP200、done=true、done_reason=stop、eval148。JSONは指定slot schemaに適合したが、body末尾が`.count()`で**final newline契約に不適合**だった。
既存経路: `GENERATION_FAILED` → `EDIT_SCHEMA_ERROR` → scope domain → `stop_cohort=true`。
apply前拒否、formatter/mandatory validation未実行、repair未使用、最終diff0 bytes、workspace_verified=true。scope分類件数は1として保存するが、source/handle/hash破損が起きたという意味ではない。別枠分析（元資料: analysis/P224-003-failure.json）。

## 14. Reasoning

計画1件（005）、**NOT_RUN**。typed extractionのlive品質は未測定。fixed/stateful/debuggingの3群をdispatchしたが、reasoningは未到達。全protocolを測定したとは主張しない。

## 15. References

| Task | References | Packet bytes | ReferencePlan bytes |
| --- | ---: | ---: | ---: |
| 001 | 0 | 246 + repair246 | 65 |
| 002 | 2 | 2157 | 887 |
| 003 | 0 | 246 | 65 |

Packetはbinding等を含むサイズ。ReferencePlan bytesはcompact JSON UTF-8の計測値であり、packetや実token数と混同しない。dispatch済み3件のHost-reviewed direct-helper completenessは3/3 PASS。未実行Taskの静的計画はlive効果の測定ではない。references独立input tokensはnull。

## 16. Formatter

| normalization | observed | accepted | rejected | validation reached |
| --- | ---: | ---: | ---: | ---: |
| method-chain例外 | 0 | 0 | 0 | 0 |
| limited std vec comma | 1 | 1 | 0 | 1 |
| closure block | 0 | 0 | 0 | 0 |
| unsupported | 0 | 0 | 0 | 0 |

002のstd vec trailing commaとwhitespace整形を固定guardが受理し、全validationへ到達。Host formatting **21 LOC**。001はnormalization前のsyntax preflightで拒否、003はformatterへ未到達。通常whitespace変更を既存method-chain jointness例外へ勝手に計上しない。

## 17. Task-local unsupported

`FORMAT_UNSUPPORTED_NORMALIZATION` **0**。未対応変換を許容するルール追加なし。今回のSTOPはformatter unsupportedでもHost formatter failureでもなく、body契約違反の分類によるもの。

## 18. Validation

002でacceptance → regression → fmt → clippy → workspace test/check/build → Host scopeを固定順で実行し、**8 check results / 37.749秒**、全PASS。test countはacceptance1、regression1、workspace20でzero-test guardを満たす。
001のsyntax preflight2件はmandatory validation成功数へ含めない。003はNOT_RUN。
開始前の既存Worker **212 tests PASS**、Rust fmt/clippy/test/check/build **全PASS**、fresh gate offline **4/4 PASS**。regression（元資料: regression/summary.json）。その後のproduction変更は0であり、同じsuiteを無意味に再実行しない。

## 19. Context / transport

API chat **5 calls**、すべてHTTP200 / done=true / done_reason=stop。入力 **8592 tokens**、出力 **609 tokens**、Ollama合計 **87.564秒**。raw payload/response、request SHA256、chars/bytes、prompt/cached/eval count/durationはrequest index（元資料: metrics/request-index.json）から辿れる。

001の実repair: **9931 chars / 10219 bytes**、prompt_eval_count **3174**、cached **872**、eval_count **135**、server truncated **0**、**NO_TRUNCATION_EVIDENCE**。budget8192/2048/24000不変。OUTPUT_LIMIT / CONTEXT_LIMIT / repair packet oversized **0**。
全5 callのserver logでも明示的truncation evidenceなし。prompt_eval_countだけで元promptの完全token数を推定していない。repairのtransportは正常だが、生成したコードはsyntax FAILであり成功扱いしない。

## 20. Infrastructure / frontend lifetime

frontend PID43972を維持、ageはcohort開始 **28.099秒** → 終了 **209.023秒**。inference indexは001が1–2、002が3–4、003が5。backend launch **2**（Gemma26 PID3684、CoderNext PID50076）、model switch **1**。Task間restart / forced unload **0**、sleep/resumeなし。

Task境界GPU使用量は**1725〜9890 MiB**。境界samplingのみで真のpeakはnull。Gemma26 `/api/ps` VRAM報告は990348573 bytes、CoderNextは8080358111 bytes。API residencyとnvidia-smi GPU全体使用量は別の診断値として保存し、等しいとは仮定しない。既存mismatch detector0。

CUDA **0** / INFRA_ERROR **0** / backend crash **0** / nvidia-smi timeout **0**。Ollama schedulerがモデル切替時に前モデルをevictした通常ログあり。backend commandはfrontend lifetime（元資料: analysis/frontend-lifetime.json）へ保存。server loading途中のavailabilityログをcrashと誤分類しない。
停止後API正常、backend存在。Windows関連Event Log query取得可能、該当イベント**0**、Display resetなし。post-stop（元資料: infrastructure/post-stop.json）。短い5 callsなので長期安定性を証明しない。

## 21. Codex intervention / LOC

code repair count **0**、repair LOC **0**、コード採用/adoptionなし。001/003は未修正のREJECTであり、修正工数が消滅したことを意味しない。002は変更なし採用可能。
分析・準備・reviewは行っているので「Codex作業ゼロ」とは扱わない。モデル修正ループへのCodex介入なし。

## 22. Host workload

計画Coverage criteria **112**、validation definitions **86**。実mandatory results **8**、37.749秒。Host formatting21 LOC、unsupported0。全TaskのReferencePlan bytes、計画reference、live packetをHost workload（元資料: analysis/host-workload.json）に分離保存。
旧red/static planning証跡は再利用であり今回の再測定ではない。新cohort freeze464ファイル、保護対象の旧tracked15360ファイルをhash検証し不変。runtime/profile/router/application/旧STOPは無変更。final integrity（元資料: analysis/final-integrity.json）。

## 23. Review burden

通常reviewはTask/route/diff/checks/短いsummaryのcompact packetのみ。canonical packet合計**30689 bytes**、中央値10943 bytes。002はそのcompact projectionを表示。これらは保存artifactサイズでありCodex input tokensの実測ではない。
review wall合計約**74.276秒**は経過区間で、待機/他作業を含み得る。planning / normal review / failure analysis / code repair / protocol-infra analysisのexact tokens・active timeは**null**。003のraw responseと分類コードの追加調査は別workload（元資料: analysis/workload-supplement.json）として分離。Local tokensをCodex節約量へ換算しない。

## 24. Failure taxonomy

| 種別 | 実測 | 解釈 |
| --- | --- | --- |
| model Rust syntax | 001、2 attempts | repair後もE0762、Task-local REJECT |
| semantic / lint code failure | 0観測 | 002のみvalidation到達、未実行多数 |
| body-contract / schema classification | 003、1件 | JSON schema validだが末尾改行不備、適用前拒否 |
| formatter unsupported | 0 | 未対応変換による拒否なし |
| task design | 0 | 固定ready gate通過 |
| Host formatter / format integrity | 0 | binary/state/source破損を観測せず |
| runtime scope-domain STOP | 1 | 003をscope分類、実際のsource破損とは区別 |
| infra / CUDA | 0 | HTTP・GPU正常、能力FAILへ混入しない |

003はinvalid bodyの安全な拒否自体には成功した。cohort-wide停止は、すべての`GENERATION_FAILED`を`EDIT_SCHEMA_ERROR`へまとめscopeに置く固定分類による。構文誤りの2.2.5改善は維持されているが、この別経路で全件測定が阻まれた。

## 25. Expansion judgement

**NEEDS_PROTOCOL_REVISION**。理由は001のcoding FAILやACNの低さそのものではなく、**source破損のない適用前body拒否が無関係なTaskまで止める分類経路**。これは今回のTask-local/cohort-wide要件を固定runtimeが満たしていないという構造上の制約で、同じmodelへの再試行を増やす提案ではない。

READY_TO_EXPANDは不可。Local terminal100%、全protocol実測、ACN75%以上をいずれも満たさない。共有データ破損やunsafe acceptanceが実際に起きたと断定する根拠はない。次候補はsaved003を使った**分類の限定レビュー**であり、final newlineの自動追加、schema緩和、model変更、repair追加、現STOP解除は今回実施していない。

## 26. 結論

2.2.5でsyntax failure後の継続を実測でき、stateful1件は初回PASS/ACCEPT_NO_CHANGEとなった。一方、別のbody契約違反がcohort STOPへ分類され、Full Pilotの主目的である全Local terminalと全protocol比較は未達だった。

固定条件を変更せず失敗と未実行を保存した。旧v2.2.4のCUDA/fresh STOP、旧2.2.5 syntax experimentを保全。新しいprotocol改修、再実行、Pilot拡大は開始せず、結果報告で停止する。

集計入口: summary（元資料: metrics/summary.json）、run history（元資料: run-history.json）、全Task結果（元資料: analysis/all-task-outcomes.json）、停止原因（元資料: analysis/P224-003-failure.json）。
