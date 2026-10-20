> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/router-shadow-pilot.md). This report alone does not establish a task result.

# Router v2 + Shadow Mode 実repository Pilot 部分結果

実施日: 2026-09-27 JST。対象: `New-Concept-OS`、base commit `c549c17454baf8a2590290016e86cadc270a25b1`、専用branch `experiment/router-shadow-pilot`。

**暫定推奨は C: Local Worker運用を見直す。まずOllama/CUDAの安定性と計測を整える。** 8件を凍結したが、Local推論のCUDA障害が2件で発生したため4件は未実行。20〜30件への拡大や、Routerのモデル選択ルール変更を支持する証拠は足りない。モデル全体の能力不足、GPUメモリ不足、driver不具合等の根本原因を断定した結論ではない。

確認できた成果は、**Gemma26 + FIXED_SLOTの1件が初回PASS・Codex修正0行**、**高リスク境界がCODEX_REQUIRED**、**検証結果が同じモデルのrepairへ直接戻ること**。一方、準備・障害対応まで含めたCodex総作業量の削減は未証明である。

## 1. Pilot概要と停止経緯

モデルランキング用のfixtureではなく、既存Rust workspaceのCLI、observer、events、skillsを対象とした。8 crates、dry-runのみという既存の権限境界を維持し、依存追加も行っていない。開始時に既存69 Python testsとRust fmt/clippy/test/check/buildはすべて成功。実装6件は新しい要件のred testを先に確認した。

すべて `protocol_hint: auto`、Host管理のscope/check argv、最大初回+repair 1回。Router実装、registries、repair/failure/scope/Shadow方針は凍結した。ModelやProtocolの期待値は選定理由に残しただけで、実行時に強制していない。

| 時刻 JST | 実測事象・対応 |
| --- | --- |
| 00:20:42 | Local実行開始。3件の独立Codex baselineは完了済み |
| 00:25:31 | PILOT-002がHTTP 500で終了し、コホートを停止 |
| 00:30:56 | 保存済みエラーと管理APIを確認後、**未実行IDだけ**を続行。失敗IDは再送せず、設定変更・プロセス再起動なし |
| 00:31:49 | PILOT-003の自律repairもHTTP 500。以降のLocal推論を停止。推論不要のPILOT-008のみ確認 |

2件のHTTP応答はいずれも `CUDA error: an illegal memory access was encountered`。最初は初回生成、次はrepair生成で発生した。続行開始時に `/api/ps` は空のモデル一覧で応答していたが、管理APIの成功は推論の安定性を保証しなかった。runnerが失敗記録を保存したので、応答・diff・checksを失っていない。

元の STOP.json（元資料: STOP.json） と STOP-continuation.json（元資料: STOP-continuation.json） を保持し、失敗IDのreset/retry、別モデルへのfallback、GPU設定変更は行っていない。継続用controllerはPilot harnessだけに追加し、凍結済みcontrollerやRouterは編集していない。

## 2. 8 Task一覧と選定理由

| ID | 実repositoryでの単一挙動 | 選定理由 | Local実行結果 | 最終review |
| --- | --- | --- | --- | --- |
| PILOT-009 | CLI inventoryのSome/Noneを数値/unavailableへ表示 | private formatterの小実装。Hostがinterface・呼出し・境界値テストを準備 | 初回PASS | ACCEPT_NO_CHANGE |
| PILOT-002 | event重複時にFIFO順を更新しない回帰テスト | 既存基本テストの不足を補う。3種のmutation check付き | 初回CUDA障害、生成なし | REJECT（候補なし） |
| PILOT-003 | KiB parserのエラーにcontext prefixを追加 | 既存文法・優先順位を維持する局所診断改善 | 初回コンパイル失敗→repair CUDA障害 | REJECT |
| PILOT-004 | memory event evidenceへavailable_percent追加 | observer/events間で生成位置を探す小変更 | NOT_RUN_INFRA_STOP | 未評価 |
| PILOT-005 | `inspect --help`をglobal helpと同じ挙動にする | CLI/intentの限定探索。未知引数は引き続き拒否 | NOT_RUN_INFRA_STOP | 未評価 |
| PILOT-006 | `--audit`が次のoptionをpathとして消費する実bug | demoで `--repeat` というファイルが作られることを事前再現 | NOT_RUN_INFRA_STOP | 未評価 |
| PILOT-007 | dedup/cacheの実装上の5事実をtyped抽出 | コード編集不要の保守分析 | NOT_RUN_INFRA_STOP | 未評価 |
| PILOT-008 | live privileged DeletePath設計のrouting境界 | architecture/securityをLocalに渡さない確認だけ | CODEX_REQUIRED、API呼出し0 | CODEX_ONLY |

PILOT-006は架空bugではない。preflight/cli-reproduction（元資料: preflight/cli-reproduction） に再現証跡を保存した。本番コードは未修正。PILOT-008では危険な実装・操作をしていない。

**Task設計失敗も保存:** 元のPILOT-001のテストがinventory以外のEvent表示にある `Some(...)` まで禁止していた。独立baselineがこの誤りをLocal推論前に検出した。元spec・失敗baseline・freezeをそのまま残し、誤ったassertionだけを直したPILOT-009を新IDとして再凍結。モデル失敗後の易化ではない。このCodex準備ミスをLocalの失敗に計上せず、準備コストからも隠していない。

## 3. 実Router判断

| ID | task_type / complexity / risk | Model | Protocol | router_reason |
| --- | --- | --- | --- | --- |
| 009 | MECHANICAL_CODE / small / low | gemma4:26b | fixed_slot | edit_location_known; risk:low; measured_candidate:normal_code |
| 002 | UNIT_TEST_GENERATION / small / low | gemma4:12b | fixed_slot | edit_location_known; risk:low; measured_candidate:light |
| 003 | REPO_EDIT / small / low | gemma4:12b | fixed_slot | edit_location_known; risk:low; measured_candidate:light |
| 004 | AGENTIC_CODING / small / low | gemma4:26b | agentic | location_search_required; risk:low; measured_candidate:normal_code |
| 005 | REPO_EDIT / small / low | gemma4:26b | agentic | location_search_required; risk:low; measured_candidate:normal_code |
| 006 | DEBUGGING / small / normal | qwen3-coder-next:latest | agentic | location_search_required; risk:normal; measured_candidate:debugging |
| 007 | ERROR_ANALYSIS / small / low | gemma4:12b | reasoning | no_code_edit; risk:low; measured_candidate:light |
| 008 | AGENTIC_CODING / complex / high | Codex | なし | codex_design_or_risk_boundary |

正規のdecisionは metrics/selection-outcomes.json（元資料: metrics/selection-outcomes.json）。未実行4件も凍結した実Routerによるread-only decisionを保存したが、推論成功を意味しない。

## 4. Task Type × Model × Protocol結果

| task_type | Model + Protocol | dispatch/選定 | PASS / 初回PASS / 無修正採用 | repair開始 | Worker秒 | input / output tokens |
| --- | --- | --- | --- | --- | --- | --- |
| MECHANICAL_CODE | Gemma26 + fixed_slot | 1/1 | 1 / 1 / 1 | 0 | 219.093 | 386 / 42 |
| UNIT_TEST_GENERATION | Gemma12 + fixed_slot | 1/1 | 0 / 未観測 / 0 | 0 | 69.531 | null / null |
| REPO_EDIT | Gemma12 + fixed_slot | 1/1 | 0 / 0 / 0 | 1（中断） | 53.141 | null / null |
| AGENTIC_CODING | Gemma26 + agentic | 0/1 | 未実行 | 未実行 | null | null |
| REPO_EDIT | Gemma26 + agentic | 0/1 | 未実行 | 未実行 | null | null |
| DEBUGGING | CoderNext + agentic | 0/1 | 未実行 | 未実行 | null | null |
| ERROR_ANALYSIS | Gemma12 + reasoning | 0/1 | 未実行 | 未実行 | null | null |

Gemma12 + fixed_slot合計はdispatch 2件、PASS 0、最終INFRA_ERROR 2、Worker 122.672秒。これはモデル能力の失敗率100%を示さない。003の初回実装失敗は観測済みだが、002の実装と003のrepair完了は観測できていない。

## 5. Local PASS率とKPI

分母を明記し、未実行4件は成功にも失敗にも入れない。

| KPI | 実測 | 解釈 |
| --- | --- | --- |
| Local dispatch count | 3 | 境界1件を除く。選定Localは7件 |
| Local final PASS率（運用） | 1/3 = 33.3% | INFRA_ERRORも成果未到達に含む |
| Local final PASS率（infra除外） | 1/1 = 100% | 観測が残った1件のみ。一般化不可 |
| 初回PASS率（初回検証観測済み） | 1/2 = 50.0% | 003の初回FAILを除外しない。002は未観測 |
| escalation率（Local） | 2/3 = 66.7% | 2件とも最終INFRA_ERROR |
| ACCEPT_NO_CHANGE率 | 1/3 = 33.3% | ACCEPT_WITH_MINOR_FIXとの合計も33.3% |
| ACCEPT_WITH_MINOR_FIX率 | 0/3 = 0% | Codexによる救済をしていない |
| ACCEPT_WITH_MAJOR_FIX率 | 0/3 = 0% | 同上 |
| REJECT率 | 2/3 = 66.7% | 002は候補なし、003は未検証patch |
| Codexコード修正介入率 | 0/3 = 0% | 障害対応を含む総介入率ではない |
| Codexインフラ対応介入率 | 2/3 = 66.7% | 停止・診断・再開可否の判断が必要だった |
| Codex repair LOC | 0 | 準備コード・baseline・計測harnessは別 |
| 無修正採用候補数 | 1 | 009のみ。本体への採用は0件 |
| median end-to-end | 431.842秒 | Local dispatchからreview判定まで。待ち時間込み |
| Local tokens per accepted task | null | 2 API callsの使用量が未取得 |
| Codex tokens per completed task | null | 正確なphase別値が取得不能 |

全KPI: metrics/summary.json（元資料: metrics/summary.json）、タスク別: metrics/tasks.csv（元資料: metrics/tasks.csv）。最終statusでinfraを除外しても、初回品質の観測まで消してはいけないため、初回指標は独立した分母で計算した。

## 6. 初回PASSと7. repair結果

009は4行のmatch式を1 slotへ返し、初回のtargeted tests、fmt、clippyに合格した。

003の初回patchはparser処理を重複させ、`?` を落としたResult値を文字列として扱い、コンパイルエラー9件を発生させた。テストは実行以前に失敗し、fmt/clippyも失敗。最小の意味変更という目的を満たしていない。

runnerは実stderrをGemma12へ返して1回のrepairを開始した。Codexは途中で解析・prompt作成・コード修正をしていない。metrics/repair-feedback.json（元資料: metrics/repair-feedback.json） は全3 checkの非空stderrが同じモデルのrepair requestへ完全一致で含まれることを、会話を表示せず機械確認した記録。

repairはCUDA障害で生成未完了。開始済みrepairの観測回復は0/1だが、**能力としてのrepair recovery rateは0/0 = null**。2回正常生成して失敗した事例ではない。OUTPUT_LIMITは発生せず、その再分割動作は今回未評価。

## 8. Codex reviewと9. repair LOC

009はtask/decision、6 LOC（4 added + 2 removed）のdiff、4 targeted tests、lint結果、21 testsのworkspace integration結果を確認し、ACCEPT_NO_CHANGEとした。Optionの全ケースとusize上限を満たし、権限・依存・public interface変更はない。

003は停止後にcompact packetとdiff、check stderrを確認してREJECT。002は生成なしのためREJECT。008は境界確認としてCODEX_ONLY。長いWorker会話は通読せず、通常repairにも介入していない。

レビュー対象compact packetは4件計16,980 bytes。003では追加check artifact 11,739 bytesと短いHTTPエラーも参照した。この値はartifactのサイズであり、**実際のCodex入力token数や読解時間ではない**。active review秒は信頼できる開始計測がないためnull。機械的なtrace集計で会話をsupervisor contextへ戻していない。

全Local patchへのCodex repairは0行・0ファイル。ただし、Hostが作ったscaffold、呼出し配線、acceptance tests、task設計、baseline、停止診断、実験harness作成の作業量は0ではない。今回の「修正0行」を「総作業量削減」と言い換えない。

## 10. Model choice評価

| ID | 評価 | 観測に基づく理由 |
| --- | --- | --- |
| 009 | GOOD | 初回に正しい最小実装。遅延は別途評価する |
| 002 | ACCEPTABLE（適合性のみ） | 小さいtest bodyという入力は登録用途に合う。実装能力は生成前のCUDA障害で未評価 |
| 003 | POOR（初回品質） | 単純なprefix変更に対し重複ロジックと構文・型エラー。repair能力はinfraで未評価 |
| 008 | GOOD | 危険な設計をCodexに保持 |
| 004〜007 | 未評価 | 実行されていないため推測で評価しない |

LocalのGOODは1/3、GOODまたはACCEPTABLEは2/3。これはretrospectiveな適合性評価であり、別モデルでのcounterfactual比較によるaccuracyではない。002を能力成功に数えず、003の1例だけでGemma12全般や別モデルへの変更効果を断定しない。

## 11. Protocol choice・Fixed Slot・Agentic評価

実行記録のある4件はすべてGOOD（Localだけなら3/3）。既知の局所bodyにfixed_slotを使い、高リスク案件をLocalから除外した。AgenticやReasoningの実走がないため、全Protocolの精度100%を主張する結果ではない。

| ID | slot数 | 許可/変更ファイル数 | replacement body LOC | 最終diff added+removed | scope violation / marker issue / apply failure |
| --- | --- | --- | --- | --- | --- |
| 009 | 1 | 1 / 1 | 4 | 6 | 0 / 0 / 0 |
| 002 | 1 | 1 / 0 | 未生成 | 0 | 0 / 0 / 0（apply未到達） |
| 003 | 1 | 1 / 1 | 32 | 25 | 0 / 0 / 0 |

003の構文エラーはscope違反やpatch適用失敗ではない。ファイル/marker境界は維持された。

Agenticのread/search/edit/test/tool rejection/scope violation/unnecessary accessは**未実行につき評価不能**。実行数0を探索効率の良さと解釈しない。Reasoningにはspec上edit権限がなく、Routerの選択もreasoningだが、回答品質・実行中の権限境界は未検証。

また、`edit_location_known` や限定scopeを作るのはCodexである。Routerが自力でrepositoryを理解して編集位置を発見した実験ではない。004〜006の候補scope選定負担もCodex側に残る。

## 12. Safety

実行済み記録ではscope違反、marker破損、tool拒否、予期しない書き込みの検知は0。Localがcommit/push/mergeした記録はなく、原本アプリへの反映も0。利用endpointは既存runnerのloopback Ollamaのみ。自由shell・network・package install・secret access toolは付与していない。

ただし隔離GitコピーはOS sandboxではなく、生成コードの実行は開発者権限である。packet-level network監視やOS全体のsecret access監査はしていない。したがって、observed violations = 0と、OS上の絶対的安全保証は区別する。

重大なRouter security bugは今回確認されていない。推論インフラ障害が再発し実験を継続できる安定性がなかったため、残りのLocal dispatchを止めた。

## 13. wall time

| 区間 | 実測秒 |
| --- | --- |
| 共有準備開始→最初のLocal dispatch（baseline・設計失敗対応込み） | 915.556 |
| 最初のdispatch→最後のrunner返却（停止/続行判断込み） | 667.006 |
| 最初のdispatch→最後のreview判定 | 731.041 |
| Local Worker実行秒の合計 | 341.765 |
| Local Worker秒の中央値 | 69.531 |
| Local dispatch→reviewの中央値 | 431.842 |

task別のdispatch→reviewは009: 651.082秒、002: 431.842秒、003: 117.397秒。待ち時間・batch処理・障害診断を含み、純粋な推論時間とは異なる。共通準備時間を恣意的に各taskへ分配していない。報告書作成・最終artifact検証・commitはこのreview終了までの区間に含まれない。

## 14. Local tokens

| ID | input | cached input | output | Ollama秒 | attempts |
| --- | --- | --- | --- | --- | --- |
| 009 | 386 | 0 | 42 | 193.4784593 | 1 |
| 002 | null | null | null | null | 1 |
| 003（task合計） | null | null | null | null | 2 |
| 003（観測できた初回のみ） | 635 | 0 | 479 | 14.3035562 | 初回のみ |
| 008 | 0 | 0 | 0 | 0 | 0 |

完了応答から取得できた下限はinput 1,021、output 521。未計測chat callsが2件あるため全体合計とLocal tokens per accepted taskはnullを維持。009単独のinput+outputは428だが、失敗コスト込みのcohort指標に代用しない。cacheをinputへ二重加算していない。

## 15. Codex tokensと17. net_codex_tokens_saved

planning/review/repair別の正確なCodex input/outputが取得できないため、すべてnull。`net_codex_tokens_saved = null`、`codex_tokens_per_completed_task = null`。文字数、LOC、Local tokensや処理時間からtokenを推定していない。

## 16. Codex-only baseline

| ID | 独立baseline | 同一仕様での検証 | 観測完了秒 | Local側 |
| --- | --- | --- | --- | --- |
| 009 | private formatterを直接実装 | PASS | 36.417 | 219.093秒でWorker PASS、その後integration/review |
| 005 | CLI help条件を直接実装 | PASS | 35.483 | 未実行 |
| 006 | audit path消費条件を直接修正 | PASS | 61.524 | 未実行 |

同じbase commitから別のclean Git worktreeを作り、同じfrozen specとseedを配置。3件ともLocal推論開始前に完了し、patchは相互流用していない。worktree・spec SHA・開始時hashは metrics/baselines.json（元資料: metrics/baselines.json） に保存。

009ではLocalのWorker完了自体が直接baselineより長かった。ただし両方とも実行各1回、compile/cache/queueは統制しておらず、baselineには計測区間中の他作業も入る。006には設計失敗の確認作業が重なっている。速度比から一般的な優劣や費用削減率は計算しない。対応比較が完成したのは009の1組だけ。

PILOT-001の失敗baseline（51.813秒）は別途残し、代表3件の成功結果へ混ぜていない。共有準備にもLocal固有の設計負担があるため、単純な秒数差はnet savingsではない。

## 18. 実運用へ進むべきか

**現段階では進めない。推奨Cは推論インフラと運用計測の見直しを先行する、という限定的な結論。**

- Aを支持できない: 運用PASSと無修正採用はともに33.3%、infra対応2件、Agentic/Reasoning/debuggingのLocal実走なし。観測済みscope違反0だけでは拡大根拠が弱い。
- Bを直ちに選ぶ根拠も弱い: Protocolの選択誤りを確認しておらず、CUDA障害はrouting ruleを変えれば直ると示せていない。
- Cで先に確認したいこと: 同PC・同model digest・同optionsで初回生成、モデル切替、repairの複数呼出しが安定して完走するかを独立したインフラ検証として扱う。CUDAの根本原因はその検証で切り分ける。

インフラ安定性を確認した後に、未実行004〜007を凍結仕様のまま実施する。失敗002/003を追加測定する場合は新ID・parent ID・新しい実行記録を用い、今回の失敗を消さない。20〜30件への拡大は、8件の完走とrepair/Agentic/Reasoningの証拠が揃ってから判断する。

## 19. Router v2で変更したい点（提案のみ）

現状のモデル優先順位やprotocol選択規則を変更する提案は保留する。再Pilot前の小改善候補は次の計測・運用部分。

1. 生成エラーの構造化結果へHTTP code、短いCUDA原因、infrastructure stageを含める。今回のcompact summaryは `HTTP error: 500` までで、分類にはraw errorの確認が必要だった。
2. aggregate最終INFRA_ERRORとは独立して、初回validation outcomeとrepair中断を標準metricsに残す。今回003の初回品質を消さず集計するためにPilot分析側で補った。
3. 明示的なcohort停止・未実行だけの続行記録を運用上整える。自動infra retryや同IDの上書きを追加する提案ではない。
4. Host準備、active review、infra対応を別intervalで計測する。修正LOC 0だけを目的達成とみなさない。

これらの有効性自体は本Pilotで比較検証していない。GPU/driver/Ollama更新やmodel optionの変更も、このPilot中には行っていない。

## 20. 凍結・原本保全・成果物

metrics/integrity.json（元資料: metrics/integrity.json） で、元のtracked 2,820ファイル、凍結input 215件、Router関連12ファイルのSHA-256が一致。Workerが保存したevidenceのコピーもbyte単位で一致し、3 baselineのspec/seed一致を再確認した。過去のPhase 1/2やRouter実装、AGENTS、registry、本体アプリは変更していない。

専用branchでcommitするのは `experiments/router-shadow-pilot/` 配下のartifactだけ。patchは隔離scratch・baseline worktreeと証跡diffに残り、本体採用・mainへのmerge・pushはしない。

| 参照先 | 内容 |
| --- | --- |
| README.md（元資料: README.md） | 再現方法・仕様と制約 |
| tasks（元資料: tasks） / seeds（元資料: seeds） / freeze-v2.json（元資料: freeze-v2.json） | 事前凍結した仕様・実ソース・hash |
| results（元資料: results） / diffs（元資料: diffs） | 生の結果、checks、失敗、最小diff |
| reviews（元資料: reviews） | 採否とretrospective理由。元runner resultは上書きしない |
| metrics（元資料: metrics） | KPI、全8件の状態、baselines、repair feedback、完全性 |
| baseline（元資料: baseline） / preflight（元資料: preflight） | 独立baseline、事前検証、実bug再現 |

**この報告は停止したPilotの部分結果。Local Workerが自力実装しCodexが短いreviewだけで済む運用を、現状の環境全体で達成したとはまだ言えない。**


---

# Shadow Pilot 再開結果（resume-001）

2026-09-27 13:10 JST、**PILOT-003 / run-002のCUDA再発により、指定された上限に従ってPilotを再停止した。8件完走には至っていない。** 正常応答する単発health probeだけでは連続実行の安定性を確認できなかった。

今回、Router・Task・model/protocol registry・sampling/context/output・validation・repair policyは変更していない。前回成功した009と境界確認008を再利用し、CUDA障害だった002/003だけをrun-002として実行した。旧結果をPASSで置き換えていない。以下は前回の部分報告を補足する結果であり、原報告と旧runは保持している。

## 前回停止原因とhealth check

前回のPILOT-002 / run-001、PILOT-003 / run-001はともにOllama HTTP 500とCUDA illegal memory access。両方を `final_status = INFRA_ERROR` として履歴に残し、coding PASS率の分母から除外した。003の旧runには初回コンパイル失敗も記録されているが、最終INFRA_ERRORを正常完了の能力評価として流用していない。

再開前に `nvidia-smi`、`ollama list`、`ollama ps` がすべてexit 0。RTX 3080、10,240 MiB、driver 591.86。Ollama 0.34.4、model digestは既存登録値と一致。最初のモデル一覧は空で、異常residencyとして解放すべきモデルはなかった。

Gemma12への小さい単発generationもPASS。`{"status":"OK"}` を返し、input 20 / cached input 0 / output 6 tokens、Ollama total 9.254秒（load 8.980秒）だった。このprobeはPilot外のhealth checkとして全要求・応答を保存し、能力・Pilot tokensの集計には混ぜていない。

health check前のGPU使用量は1,656 MiB、成功後は9,871 MiB。probe後のGemma12が常駐した状態からPilotを開始した。これは今回必須の事前確認によるwarm stateであり、前回とcold-start latencyが同一という主張はしない。モデル条件・生成optionsは据え置きである。

## 再開方法と保持

| Task | 旧run | 今回の扱い |
| --- | --- | --- |
| PILOT-009 | run-001 / PASS | 再利用。再推論なし |
| PILOT-002 | run-001 / INFRA_ERROR | 新規run-002。元Task ID・specを維持 |
| PILOT-003 | run-001 / INFRA_ERROR | 新規run-002。元Task ID・specを維持 |
| PILOT-004〜007 | 未実行 | 003再発のため今回も未実行 |
| PILOT-008 | run-001 / CODEX_REQUIRED | 再利用。再実行なし |

旧runは従来の `results/<Task ID>/` にそのまま保存。新runは `resume-001/runs/<Task ID>/run-002/` に置き、`outcome.json` に `original_task_id` / `run_id` / `prior_run_id` / `final_status` / 実際の `failure_reason` を記録した。元runnerの `records/result.json` やraw応答は改変せず、そのままコピーしている。

Task仕様を新IDへ書き換える方法は使っていない。出力先の隔離rootだけを分け、同じspecを凍結済みrunnerへ渡した。002/003とも、**初回chat payload全体（messages・JSON schema・options含む）が旧runと完全一致**したことを機械検証済み。temperature 0、seed 20260926、num_ctx 8192、num_predict 2048、最大2 code attemptsを維持している。

GPU・Ollama情報を各Task前後、および実行中おおむね10秒ごとに取得した。この観測のoverheadはあるが、unload・モデル置換・prompt追加・コード生成への介入は行っていない。Ollama/server/OSの再起動、driver/runtimeの変更、恒久設定変更もしていない。

## rerun結果と8 Taskの現在状態

| Task / 採用run | Router model / protocol | 初回 / repair | Local最終状態 | Codex review | repair LOC | input / cached / output | Worker秒 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 009 / run-001（再利用） | Gemma26 / fixed_slot | PASS / なし | PASS | ACCEPT_NO_CHANGE | 0 | 386 / 0 / 42 | 219.093 |
| 002 / run-002 | Gemma12 / fixed_slot | OUTPUT_LIMIT / なし | ESCALATE | REJECT | 0 | 2,580 / 0 / 2,048 | 39.516 |
| 003 / run-002 | Gemma12 / fixed_slot | CUDA障害 / なし | INFRA_ERROR | REJECT（生成候補なし） | 0 | null / null / null | 13.031 |
| 004 / 未実行 | Gemma26 / agentic | 未実行 | NOT_RUN_INFRA_STOP | null | null | null | null |
| 005 / 未実行 | Gemma26 / agentic | 未実行 | NOT_RUN_INFRA_STOP | null | null | null | null |
| 006 / 未実行 | CoderNext / agentic | 未実行 | NOT_RUN_INFRA_STOP | null | null | null | null |
| 007 / 未実行 | Gemma12 / reasoning | 未実行 | NOT_RUN_INFRA_STOP | null | null | null | null |
| 008 / run-001（再利用） | Codex / Localなし | API呼出し0 | CODEX_REQUIRED | CODEX_ONLY | 0 | 0 / 0 / 0 | 0 |

未実行4件のRouter decisionは旧凍結条件の選択を保存しているが、推論・reviewの値は捏造せずnull。全Taskについてdecision・status・run履歴・tokens・duration・infra件数を metrics/tasks.json（元資料: resume-001/metrics/tasks.json） と metrics/tasks.csv（元資料: resume-001/metrics/tasks.csv） に揃えた。

002は `done_reason=length`、`eval_count=2048`。上限到達した出力は適用されず、diffは空、validation実行0。従来のOUTPUT_LIMIT規則どおりRESPLITへ返った。今回の条件変更禁止に従い、上限引上げ・続きを生成・再分割Taskの実行はしていない。このrunはCUDAによる能力評価不能ではなく、**固定予算内でのTask完了失敗**として有効な評価に含める。生成testの正しさは検証前なので評価できない。

003のrun-002は最初のchat requestでHTTP 500。code適用・targeted test・repairには到達しなかった。元の実エラーは次のとおり保存した。

```text
an error was encountered while running the model: CUDA error: an illegal memory access was encountered
CUDA error
```

003には旧CUDA runに対する1回のinfrastructure retryを使用済み。再発後にrun-003を作らず、004以降もdispatchしていない。停止記録は STOP.json（元資料: resume-001/STOP.json）。

## CUDA再発時の診断

| 項目 | 観測 |
| --- | --- |
| 発生Task / run | PILOT-003 / run-002 |
| モデル | gemma4:12b、digest 4eb23ef187e2… |
| Protocol | fixed_slot |
| 時刻 | 2026-09-27 13:10:03 JSTに停止記録を保存 |
| タイミング | 初回attemptの `/api/chat`、開始から約13.031秒 |
| loadかgenerationか | API内部の正確なphaseはnull。既に同モデルが常駐し、直前に生成応答あり。ただしbackend内部の再loadを断定的に除外できない |
| 直前Task | PILOT-002 / run-002、同じGemma12、OUTPUT_LIMITで完了応答 |
| GPU使用量 | 開始前9,684 MiB → 実行中sample 9,376 MiB → 終了後1,413 MiB（全GPU使用量、瞬間peakではない） |
| GPU query | 前・中・後ともnvidia-smiはexit 0 |
| Ollama API residency | 前後ともGemma12をsize_vram=8,067,240,426 bytesとして返した |
| Ollamaプロセス | 観測上server PID 11140、app PID 28132が前後で継続。再起動なし |
| modelごとの正確な実VRAM | null。WDDMで上記全GPU値から厳密な内訳は出せない |

障害後は**全GPU使用量が約1.4 GiBなのにAPIが約8.1 GBのモデル常駐を報告**していた。API residencyと実GPU使用量の不一致は確認できたが、具体的なdriver不具合、OOM、allocation failure、model weightの問題のどれかは断定できない。`illegal memory access` を単純に「VRAM不足」と言い換えていない。

今回のTask列はGemma12→Gemma12で、モデル切替は一度もない。したがって「複数モデル切替だけが原因」という仮説では今回を説明できない。Gemma26/CoderNextへの切替安定性は未実験である。小さいhealth probeの成功や `/api/ps` の応答を、連続inferenceの健全性保証に使えないことが分かった。

## 能力評価とInfrastructure reliabilityの分離

| KPI | 実測・分母 |
| --- | --- |
| 有効Local Task数 | 2件（009 run-001、002 run-002） |
| INFRA_ERROR除外のLocal PASS率 | 1/2 = **50.0%** |
| 有効Taskの初回完了率 | 1/2 = 50.0%。002はvalidationに達しないため初回test判定そのものはnull |
| repair回復率 | null（有効runではrepair開始0件） |
| 旧+新のLocal実行run数 | 5件（旧3 + 新2） |
| infra_error_count | **3**（旧2 + 新1） |
| cuda_error_count | **3**（旧2 + 新1） |
| model_load_error_count | **null**。load障害確定0件、内部phase不明3件。0件と断定しない |
| CUDA/infra障害率 | 3/5 = 60.0%（健康確認probeを除くTask run） |
| infraなしでrunnerが返った率 | 2/5 = 40.0%（PASSとOUTPUT_LIMIT） |
| INFRA_ERROR込みのend-to-end PASS reliability | 1/5 = **20.0%**（全Local runを保持した分母） |
| Taskごとに最新有効結果を選んだ運用PASS | 1/3 = 33.3%（dispatchした3 Task。未実行4件・Codex境界を除く） |
| Codex repair LOC | 0。今回の新runは双方diff空 |

「有効な能力評価」には、正常なAPI応答で規定上限に達した002を含める。一方、CUDAで応答が失われた003は含めない。run-001のCUDAをrun-002の結果で消さず、reliabilityでは両方を数える。未実行4件をFAILにする集計も行わない。

正規の集計: metrics/summary.json（元資料: resume-001/metrics/summary.json）、全run履歴: metrics/run-history.json（元資料: resume-001/metrics/run-history.json）。

## Model qualityとOperational suitability

| 対象 | Model quality / 完了品質 | RTX 3080上の実行安定性 | Protocol |
| --- | --- | --- | --- |
| 009 Gemma26 | GOOD（旧runの正しい実装を再利用） | 旧1 runは障害なし。強い一般化は不可 | GOOD |
| 002 Gemma12 | POOR（固定output budget内で完了せず。test自体の正しさは未評価） | 同モデルのTask run全4件でCUDA 3件のためPOOR。ただし002の今回runはCUDAなし | GOOD |
| 003 Gemma12 | **null / NOT_EVALUABLE_INFRA_ERROR** | 同一Taskで再発のためPOOR | GOOD |
| 004〜007 | 未実行につきnull | null | 実走未評価 |
| 008 | 高リスクをCodexへ保持 | Local実行なし | GOOD |

CUDA再発を理由にRouter/model choiceの能力評価を下げていない。旧003 reviewは歴史的な初回生成への評価として保存し、新しい有効結果表ではINFRA_ERRORによる能力評価不能を明示した。Gemma12に障害が集中していることはこのPCでのoperational suitabilityの証拠だが、他モデルとの同条件比較を完了していないため、モデル固有の欠陥やrouting変更の優越性は示していない。

## tokens・duration・Codex負担

新002はinput 2,580、cached 0、output 2,048、Ollama 38.952秒、Worker 39.516秒。新003はAPI response countersを取得できず各token値はnull、Worker 13.031秒。新run合計52.547秒、旧+新Local Worker合計394.312秒。診断・review・report作業はこのWorker秒とは別。

全Local Task runで取得できた下限はinput 3,601、output 2,569。未計測callsが3件あるため全体token合計・失敗費用込みのtokens per accepted taskはnull。health probeのinput 20/output 6は別記録に保存した。

Codex planning/review/repair tokensと `net_codex_tokens_saved` は引き続きnull。002/003のreviewはcompact packet、空diff、call counters、短い実エラー、GPU診断を中心に行い、生成途中の会話全文は読んでいない。Codexは通常repairに入っていないが、障害診断の作業が必要だったため、総作業量削減を主張しない。

## 今後の安定化と変更の有無

**今後のCUDA/Ollama安定化が必要。今回の再開は「単なる再実行で安定した」とは言えない。** 指定された再発時停止条件を優先し、恒久設定変更・Ollama/OS再起動・追加health generation・別モデルへの差替え・run-003は行っていない。再起動が必須かどうかも、現在の証拠だけでは断定しない。

次のInfrastructure調査では、この常駐モデルへの連続呼出しとbackend residency不一致を対象とし、CUDA/driver/Ollamaログからphaseを特定する必要がある。必要な一時的residency解放や再起動の効果は、Pilotと区別して記録する。driver/runtimeや恒久設定の変更には別途判断が必要。8件の続行を、試行上限を無視して進めることはしない。

今回はInfrastructure fix自体を実装していないため、fix commitは存在しない。追加したものは診断・新run保存・別分母集計・検証のPilot harnessとartifactのみ。将来loaderやresidency制御を修正する場合は、指示どおりInfrastructure fixを独立commitにし、その後のPilot結果も別commitにする。

無変更の確認結果は metrics/integrity.json（元資料: resume-001/metrics/integrity.json）。旧artifact 413件を確認し、元RESULTS_JA.mdには追記だけを行う。原報告全文のbyte一致コピーも保存。旧STOP・logs・token/duration・partial diff・旧reviewを含め、その他の旧artifactに変更はない。凍結input 215件、Router関連12件、元repository 2,820件のhash一致を確認した。

applicationへの採用、merge、pushは行っていない。成功009を再生成せず、追加で消費したLocal推論はhealth probe 1回とTask run 2件だけである。
