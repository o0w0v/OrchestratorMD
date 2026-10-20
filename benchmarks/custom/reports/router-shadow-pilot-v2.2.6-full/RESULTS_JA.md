> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/router-shadow-pilot-v2.2.6-full.md). This report alone does not establish a task result.

# bounded 2.2.6 Full Shadow Pilot — Terminal Coverage Run

判定: **NOT_READY_INFRASTRUCTURE**。**Local terminal coverage 0/13、未実行13、cohort_completed=false**。
実装やモデル品質の失敗ではない。最初のinferenceより前にOllamaの内蔵updaterが0.35.0→0.35.1を適用し、環境固定条件が成立しなくなったため停止した。生成API呼出し0、Local tokens0。今回の目的である13件の測定は未完了。

## 1. Fresh environment

ユーザーのtray Quit完了後、process/backend不在、11434接続拒否、version/ps API不応答、Ollama GPU process不在と正常GPU queryを保存した。終了gate（元資料: infrastructure/quit-001.json）。
同じinstalled binaryを `ollama app.exe --hide` で起動。2026-10-04 00:04:50 JSTのfresh gateでは0.35.0、新frontend PID47620、models=[]、backend不在、同一model digests、driver591.86がすべてPASSだった。fresh gate（元資料: infrastructure/fresh-start-001.json）。

その後の時系列:

| 時刻 JST | 観測 |
| --- | --- |
| 00:04:43–44 | 同一0.35.0 app起動、frontend PID47620作成 |
| 00:04:47 | 内蔵updaterが0.35.1について `update already downloaded` を記録 |
| 00:04:55 | `starting upgrade`、続いて `Installer started in background, exiting` |
| 00:05:49–50 | app0.35.1起動、新frontend PID50980、0.35.1 listen開始 |
| 00:06頃 | environment候補snapshotは0.35.1を取得 |
| freeze検証 | `AssertionError: ollama_version`。旧0.35.0と不一致、execution freeze作成を拒否 |

こちらがupdate/installコマンドを実行したわけではないが、通常app起動を契機に保留済み更新が適用された。旧ログには前回 `--fast-startup` 時の `deferring pending update for fast startup` も残っている。設定変更、rollback、kill、再restartで隠さない。
app-1.log（元資料: infrastructure/environment-change-logs/app-1.log）、app.log（元資料: infrastructure/environment-change-logs/app.log）、upgrade.log（元資料: infrastructure/environment-change-logs/upgrade.log）、観測snapshot（元資料: infrastructure/environment-change-observed.json）。
両binary SHAも変化。GPUはRTX3080、driver591.86とモデルdigestは不変。OS bootは2026-10-01T09:57:54.1526480Z。
`environment/freeze.json`は検証前候補として保存され、**採用済みfreezeではない**。frontend欄は元fresh gate参照、API版は0.35.1で時点が異なる。失敗判定（元資料: environment/freeze-validation.json）。rootのfreeze.json/START.jsonは作成していない。

## 2. Task一覧

Task JSON14件と325 source filesをbyte-identicalで再利用。reuse verification（元資料: reuse-verification.json）。

| Task | business Task | model | protocol | 今回状態 |
| --- | --- | --- | --- | --- |
| P224-001 | CLI telemetryを改行しないescaped一行として表示 | gemma4:26b | fixed_slot | NOT_RUN |
| P224-002 | memory evidenceにused KiBを独立した第2要素として追加 | gemma4:26b | agentic | NOT_RUN |
| P224-003 | TCP inventoryが非data行の01を誤countする不具合 | qwen3-coder-next:latest | fixed_slot | NOT_RUN |
| P224-004 | CLIのused memory量を妥当性検査付きで表示 | gemma4:26b | fixed_slot | NOT_RUN |
| P224-005 | MockObserverのnested snapshot値をtyped抽出 | gemma4:26b | reasoning | NOT_RUN |
| P224-006 | 正常系auditへprocess sampleのcomplete/bounded区別を追加 | gemma4:26b | agentic | NOT_RUN |
| P224-007 | VmRSSの値parse失敗へ診断prefixを付与 | gemma4:26b | fixed_slot | NOT_RUN |
| P224-008 | HighLoad evidenceへ観測timestampを第2要素で追加 | gemma4:26b | agentic | NOT_RUN |
| P224-009 | mock report reasonへ安定したevent kind labelを表示 | gemma4:26b | fixed_slot | NOT_RUN |
| P224-010 | skill templateの診断へ現在evidenceのUTF-8 bytes合計を表示 | gemma4:26b | agentic | NOT_RUN |
| P224-011 | CLI warning overviewのstable unique preview | gemma4:26b | fixed_slot | NOT_RUN |
| P224-012 | meminfo重複診断へMemTotal/MemAvailableの名前を付加 | gemma4:26b | agentic | NOT_RUN |
| P224-013 | Telemetry欠測を説明するUIの表示方針を決定 | Codex | boundary | CODEX_ONLY |
| P224-014 | CLI per-CPU loadの欠測/非有限値と小数表示 | gemma4:26b | fixed_slot | NOT_RUN |

## 3. Execution order

001→002→003→004→005→006→007→008→009→010→011→012→014を準備。並べ替え・001/003除外・成功しやすいTaskへの置換なし。013は既存CODEX_ONLY境界を再照合、Local分母に含めない。

## 4. Terminal coverage

**0/13（0%）**。全Local TaskはNOT_RUN。preflight STOPをTask terminalとして水増しせず、全13件に同じINFRA_ERRORを付けることもしない。Task metrics（元資料: metrics/task-metrics.json）。

## 5. Cohort completion

**false**。cohort起動前のSTOP1件。STOP.json（元資料: STOP.json）、run-history（元資料: run-history.json）。旧cohortのSTOP/結果は変更しない。

## 6. ACCEPT_NO_CHANGE

ACCEPT_NO_CHANGE0 / dispatched0、率は**null（N/A）**。0%品質と解釈しない。レビュー可能なLocal候補なし。

## 7. First / final PASS

観測0件、率N/A。Local final result自体が未作成で、モデルFAIL0と安定性を主張することもできない。

## 8. Syntax failure

今回live未測定。既存2.2.6のsyntax repair合計1/Task-local挙動を維持。元001は再利用し除外していない。

## 9. Generation contract failure

今回live未測定。LF自動追加・追加repairなし。CoderNext003の未適用body失敗は既存classificationのまま測定予定だった。

## 10. Semantic repair

live実行0。既存eligibilityとglobal budget1を変更していない。

## 11. Lint repair

live実行0。clippy::useless_conversion限定、他checks PASS、残budgetありの条件を維持。

## 12. Formatter unsupported

live未測定。method-chain/std vec/closureの既存許容とTask-local unsupported分類を維持。formatter binary SHAは固定値と一致した。

## 13. Fixed-slot

planned7（うちDEBUGGING1）、terminal0、First/final PASS0、repair0、review REJECT0、率N/A。DEBUGGING除外の通常fixedは6。

## 14. Stateful

planned5、terminal0、DISCOVERY/valid handle apply/reference packet送信は未測定。既存issued authority/hash binding不変。

## 15. Debugging

CoderNext003は必須対象として維持。未dispatch、body rejection後の継続は今回確認不能。

## 16. Reasoning

005のtyped reasoningは未到達。未実行をPASS/FAILへ変えない。

## 17. References

全Taskのfinite ReferencePlan/direct-helper completenessを保持。planning/staticの値は過去の準備証跡の再利用で、新しいlive測定ではない。reference input tokens/bytesの実送信は0。

## 18. Context

8192 / 2048 / 24000、temperature0、seed20260926不変。generation/repair request0件のためprompt_eval/cached/eval/done_reason/truncatedはN/A。推定値からcontext安全を主張しない。

## 19. Validation

開始前に**Worker233 tests PASS**、Rust fmt/clippy/test/check/buildすべてPASS。fresh continuity negative4 testsもPASS。regression summary（元資料: regression/summary.json）。モデル生成を伴うmandatory validation0件。

## 20. Infrastructure

**環境変更incident1、Local Task INFRA_ERROR0、CUDA0（inferenceなし）**。CUDA障害の再発ではない。frontend age/連続inference/backend launch/model switchingのlive比較はN/A。
GPU/API/binary/process、既存server/app/upgrade log、関連Windows Event Logをread-only保存。events（元資料: infrastructure/environment-change-events.json）。Ollama版とfrontendの変更がfreezeを阻害した直接証拠であり、driver故障やGPU不足とは判定しない。

## 21. Codex intervention / LOC

candidate code repair0、changed files[]、added/deleted LOC0。今回の未解決工数を削減成功へ換算しない。planning/normal review/failure analysis/code repair/protocol-infra analysisのexact tokens/active timeはnull。通常Local reviewは未実施。

## 22. Host workload

準備:14 Task／325 source files再照合、全16995既存tracked filesのhash保全、runtime snapshots、fresh gates、必須regression、環境変化の証跡保存。Host formatting LOC0、live validation count0、Task-local unsupported観測0。planning criteria/reference設計は再利用。
artifact snapshot helperのpath取り扱いで一度失敗し修正。absolute keyを元pathへ同一bytesで書き戻したが、全旧ファイルbyte一致を確認。最終snapshotを別directoryへ保存した。preflight failures（元資料: preflight-failures.json）。Worker/runtimeコードの変更はない。

## 23. Failure taxonomy

MODEL_SYNTAX / GENERATION_CONTRACT / MODEL_SEMANTIC / LINT / FORMAT_UNSUPPORTED / TASK_DESIGN / CAPABILITY-SCOPE / HOST_INTEGRITYはすべて**未測定**。今回確認されたのはcohort準備中のInfrastructure environment drift1件のみ。summary（元資料: metrics/summary.json）。モデル能力PASS率の分母へ混入しない。

## 24. Expansion judgement

**NOT_READY_INFRASTRUCTURE**。原因はfresh start後のOllama version/frontend変更であり、2.2.6 protocolやモデル能力の評価ではない。READY_TO_EXPANDやCONTINUE_LIMITED_SHADOWの品質判定に必要な13件の結果はない。

## 25. 結論と再実行条件

13件の準備とoffline検証は完了したが、Local inference前に環境freezeが不成立となった。このSTOPを保持し、自動再開しない。
再実行案は、現在installedの**0.35.1を別環境条件として明示承認**し、別cohort/runでfresh確認後、同じ13 Taskと2.2.6 runtimeを測定すること。旧0.35.0との結果比較は環境差を明示する。ダウングレードや更新設定変更を無断実行しない。
