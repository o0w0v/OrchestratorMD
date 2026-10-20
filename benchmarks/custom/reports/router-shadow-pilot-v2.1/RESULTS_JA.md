> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/router-shadow-pilot-v2.1.md). This report alone does not establish a task result.

# Router v2.1 Operational Policy / Shadow Pilot 結果

2026-09-29 JST。新cohort `router-shadow-pilot-v2.1` の **8件を記録完了**。Local 7件、Codex境界確認1件。

**ACCEPT_NO_CHANGEは4/7（57.1%）。Local first/final PASSも4/7。軽微修正2件、REJECT 1件、Codex repair合計6 LOC。INFRA_ERROR・CUDAは0件。**

Gemma12隔離下でPilotを完走できた。一方、7件中3件で自律完了できず、すべてを短い最終レビューだけで済ませる品質には届いていない。**既存の限定Shadow運用は可能だが、広範なPilot拡大・自動採用は見送る**。今回の候補patchはアプリ本体へ適用していない。

機械可読集計（元資料: summary.json） / 8件の履歴（元資料: run-history.json） / 凍結条件（元資料: freeze.json） / 監査結果（元資料: integrity.json） / GPU記録（元資料: gpu-telemetry.csv） / 各requestへの索引（元資料: request-index.json）。

## Router v2.1の変更

実装commit: `87f63f1b600ae6ba19e7c6340204ce6b79536b99`。branch: `feat/router-v2-1-operational-policy`。

既存の能力registry・Protocol Registryをbyte単位で維持し、`config/worker/operational_policy.json` を独立した運用制約として重ねた。モデル能力・リスク判定・protocol選択の再設計はしていない。

| モデル | capability_status | operational_status | 通常dispatch |
| --- | --- | --- | --- |
| gemma4:12b | measured | quarantined | 禁止 |
| gemma4:26b | measured | active | 実測済みcoding/light用途 |
| qwen2.5-Coder:14b | measured | experimental | 通常選択・自動fallbackなし |
| qwen3-coder-next:latest | measured | active | 既存DEBUGGING用途 |

`measured`は能力測定が存在する意味で、全カテゴリの合格を保証しない。Devstral/GPT-OSSも従来どおりexperimental。旧Model Registryの`status`は保存したv2情報であり、live dispatchの可否には新Operational Policyを使う。

Gemma12隔離はrouting時と`/api/chat`送信直前の両方で強制する。古いdecision、未登録alias、experimental候補も送信境界で拒否する。decisionには`preferred_model`、`selected_model`、`override_reason`、能力policyと運用policyのversionを残す。

例: `preferred_model=gemma4:12b → selected_model=gemma4:26b / override_reason=operational_quarantine`。これは**dispatch前の運用制約適用**で、失敗後のcross-model fallbackではない。

## 新routing tableと根拠

| Task | 選択モデル | Protocol |
| --- | --- | --- |
| MECHANICAL_CODE | Gemma26 | 既存の編集位置判定 |
| REPO_EDIT（localized含む） | Gemma26 | 位置既知ならfixed_slot、それ以外agentic |
| AGENTIC_CODING | Gemma26 | 既存の編集位置判定 |
| UNIT_TEST_GENERATION / TEMPLATE_UI | Gemma26 | 既存の編集位置判定 |
| ERROR_ANALYSIS | Gemma26 | 編集なしならreasoning |
| DEBUGGING | CoderNext | 既存の編集位置判定 |
| 複雑・高risk・未分割logic・自由な仕様設計 | Codex | 既存の境界を維持 |

BOUNDED_LOGICの親ID・分割確認、SPECIFICATIONの型付き抽出例外なども維持した。

Phase 1能力表（元資料: ../../docs/MODEL_CAPABILITY_MATRIX.md）とPhase 2実測（元資料: ../model-routing/phase2/resume-001/summaries/RESULTS_PHASE2_JA.md）を再確認した。Gemma26はテスト生成・REPO_EDIT・ERROR_ANALYSISで各final 3/3、first 3/3。UIはfinal 3/3、first 2/3。Qwen14もテスト/UI/原因情報抽出はfirst 3/3だが、REPO_EDITはfinal 1/3。旧fixtureの所要時間中央値でもGemma26が短く、Gemma26への統一は不要なmodel switchingを減らせる。

Phase 3（元資料: ../ollama-cuda-stability-phase3/RESULTS_JA.md）のGemma26/Qwen14各10/10正常応答は**運用安定性の証拠のみ**。coding PASSへ加算していない。Qwen14は2048-token synthetic条件でGemma26より遅かったが、その比率を今回のcoding taskへ直接適用しない。全比較は小標本であり、一般的なモデルランキングではない。

## 固定条件・旧結果保全

旧8仕様（009、002〜008）と選択seedをそのままコピーし、byte一致を検証した。旧001は過去のTASK_DESIGN_FAILUREなので再導入していない。未完了Taskも仕様変更なしで再利用可能だった。

成功済み009も新cohortの独立比較として1回実行した。旧PASSを新分母へ加算したのではない。全Taskのoriginal IDを維持し、cohortと`v2.1-run-001`で旧runと区別した。旧red-test確認・独立Codex baselineは参照情報として保持し、新しい測定値へ混ぜていない。

generation/repair loopは旧コードと一致。temperature=0、seed=20260926、num_ctx=8192、num_predict=2048、元messages/schema、fixed_slot/agentic/reasoning、validation、初回＋same-model repair最大1回を維持した。OUTPUT_LIMIT/CONTEXT_LIMITで上限を上げず、同一タスクを再送しない。cross-model cascadeもない。

196個の実行入力を凍結し、dispatchごとにhash確認。cohort中のRouter/Protocol/Task変更は0。旧実験とapplicationの保護対象4,182ファイルは変更0。旧Pilot、CUDA Phase 1/2/3、CUDA失敗、STOP、raw、token/durationは上書きしていない。

## 8 Taskの結果

全行が新cohortの結果。LOCはCodex修正の追加＋削除行数で、Local patchサイズとは別。

| Task | 単一責務 | モデル / protocol | Local first / final | 最終レビュー | Codex LOC | Worker秒 |
| --- | --- | --- | --- | --- | ---: | ---: |
| 009 | optional CLI件数の表示 | Gemma26 / fixed_slot | PASS / PASS | ACCEPT_NO_CHANGE | 0 | 46.641 |
| 002 | FIFO重複イベントの回帰テスト | Gemma26 / fixed_slot | FAIL / CONTEXT_LIMIT | ACCEPT_WITH_MINOR_FIX | 4 | 63.422 |
| 003 | KiBエラーへのcontext prefix | Gemma26 / fixed_slot | PASS / PASS | ACCEPT_NO_CHANGE | 0 | 23.828 |
| 004 | memory evidenceへ割合を追加 | Gemma26 / agentic | PASS / PASS | ACCEPT_NO_CHANGE | 0 | 31.859 |
| 005 | `inspect --help`の既存help表示 | Gemma26 / agentic | 検証未実行 / TEST_NOT_ALLOWED | ACCEPT_WITH_MINOR_FIX | 2 | 10.594 |
| 006 | `--audit`が次optionをpathに消費する不具合 | CoderNext / agentic | PASS / PASS | ACCEPT_NO_CHANGE | 0 | 106.282 |
| 007 | dedup/cacheの5項目抽出 | Gemma26 / reasoning | FAIL / ATTEMPTS_EXHAUSTED | REJECT | 0 | 30.156 |
| 008 | privileged実行設計の委譲境界 | Codex / none | N/A / CODEX_REQUIRED | CODEX_ONLY | 0 | 0.000 |

002/003/007は旧capability preferenceのGemma12から隔離override。各decision、raw request/response、check結果、diff、短いsummary、reviewは履歴（元資料: run-history.json）から辿れる。

## 失敗とCodex介入

- **002:** LocalはAを再挿入してBをevictした後にBの重複拒否をassertしていた。初回テストは正しく不合格。runnerはrepair準備へ入ったが、元の入力・診断を含むcontextが固定上限を超え、repair generationは0回。Codexは独立reviewコピーで既存のB確認をA再挿入前へ移動した。4 LOC。元validation、3種類のmutation、全workspaceテストがPASS。
- **005:** Workerは`check_ids=["targeted"]`だけを要求した。固定契約は`targeted/format/clippy`全部なので、要求は実行前に拒否された。範囲外変更や新コマンド実行はない。Codexのreviewでは元candidateのformat不合格も確認し、長い長さ/index比較を等価な引数vector比較に置き換えた。2 LOC。全固定validationとworkspaceテストがPASS。
- **007:** 最終回答の`event_key=event_id`は実装の`kind_target`と異なる。同一モデルのrepair後も不合格。回答を書き換えずREJECTとした。infra障害ではない。

002/005のLocal結果はESCALATEのまま。Codex修正後の合格をLocal PASSへ書き換えていない。002修正diff（元資料: reviews/PILOT-002/codex-repair.diff）、005修正diff（元資料: reviews/PILOT-005/codex-repair.diff）と各validationを別保存した。

通常のLocal修正ループにはCodexが入っていない。final reviewは仕様、decision、diff、test結果、短いsummary、必要な型付き回答を使用。全会話は読んでいない。005の停止判定だけは別のprotocol診断として、拒否されたtool名とargumentsを限定確認した。

## 一時STOPと安全な続行

旧controllerと同じ保護動作により005のTEST_NOT_ALLOWEDで一旦STOPした。STOP（元資料: STOP.json）と最初のEND（元資料: END.json）を保持している。

停止後確認（元資料: stop-inspection.json）でcheck選択不足だけと判明し、scope検証・healthが正常だったため、明示的な継続segment（元資料: CONTINUATION_START.json）で未実行006/007/008のみ実行した。005のretryや修正prompt送信はなく、Router・protocol・Taskは凍結どおり。これはINFRA_ERROR後の自動再開ではない。

最終状態はCONTINUATION_END（元資料: CONTINUATION_END.json）で3件完了、追加STOPなし。集計では元STOPの存在とcohort完了を両方保持する。

## KPIとコスト

| 指標 | 値 |
| --- | ---: |
| Local有効Task / dispatch | 7 / 7 |
| Local final PASS / First PASS | 4/7（57.1%） / 4/7（57.1%） |
| **ACCEPT_NO_CHANGE** | **4/7（57.1%）** |
| ACCEPT_WITH_MINOR_FIX | 2/7（28.6%） |
| REJECT | 1/7（14.3%） |
| Codex code intervention | 2/7（28.6%） |
| Codex repair LOC | 6（002: 4、005: 2） |
| Local escalation | 3/7 |
| repair準備へ進んだTask / 実際にrepair生成したTask | 2 / 1 |
| INFRA_ERROR / CUDA / model load error | 0 / 0 / 0 |
| infra正常終了率 | 7/7（100%） |
| infraを含むLocal end-to-end PASS率 | 4/7（57.1%） |
| generation API呼出し | 18（全HTTP 200） |
| Local input / output tokens | 42,944 / 2,260 |
| うちcached input | 23,123（inputへ二重加算しない） |
| Worker wall time合計 | 312.782秒 |
| cohort開始→全Worker終了 | 427.432秒（一時STOPの確認・待機を含む） |
| Codex実token / net savings / active review時間 | null / null / null |

主要率は有効Local 7件を分母とし、Codex境界確認は除外。今回はinfra除外で分母が減っていない。全dispatchを分母にしたACCEPT_NO_CHANGEも4/7。005は初回検証に到達せず、初回成功には数えていない。

minor fixを含む受入れ候補は6/7だが、これは自律成功率ではない。code intervention以外にも停止確認・host validation・レビューが必要だった。0 LOCのREJECTを「Codex作業不要」と解釈しない。各taskのdispatch→review終了wallは履歴に保存し、待機を含むためactive review時間と区別する。

## Infrastructureとmodel switching

開始前Ollama 0.34.4、driver 591.86、RTX 3080 10GB。frontend PID 29992、開始前models=[]、GPU使用量約1.8GB。read-only health checkのみで開始し、generation probeなし。環境・driver/runtime/model filesは変更していない。

Local各Task前後14 snapshotを保存。GPU query timeout 0、API異常0、residency mismatch 0、CUDA/backend障害0。終了後healthも正常。実験時間帯のWindows System/Application警告・エラーqueryはNoMatchingEventsFoundで、該当クラッシュイベントなし。

元のkeep-alive/residency動作を維持し、強制unload・再起動なし。Gemma26→CoderNext→Gemma26の2回の切替で異常は観測しなかった。APIのload duration合計は006で約43.517秒、007で約21.174秒。初回Gemma26は約20.025秒。これは観測値で、純粋なswitching costの統制測定ではない。

GPU telemetryはdispatch境界の軽量観測で、連続samplingや真のpeak値ではない。18 API呼出し・7 Taskの成功から長期無故障率は推定しない。Gemma12へのgenerationは0。過去のGemma12 CUDA failuresは隔離根拠として保持したが、このcohortのcoding失敗やRouter失敗には数えていない。

## 運用判断と次の検証

運用policyは指定どおり維持する。Gemma26 active、CoderNext DEBUGGING、Gemma12 quarantined、Qwen14 experimental。今回Gemma26は実coding 3/6がLocal PASS、CoderNextは1/1。少数かつ種類の異なるTaskなので、順位付け・恒久的な能力優劣は主張しない。

隔離下のInfrastructureは今回のPilotを支えた。ただしACCEPT_NO_CHANGE 57.1%では広範な拡大を支持しない。次は別の変更・別cohortとして以下を検証する。今回のRouterは変更していない。

1. 002: test生成をさらに小さい挙動へ分割し、repair診断を含めてcontext予算内に収まるかを事前確認する。
2. 005: モデルがcheck IDを選び落とさないよう、固定全checkセットの実行契約を別protocol実験で評価する。
3. 007: 実装根拠を正しく抽出できるか、限定referenceと型付き事実確認の追加課題で測る。安易にQwen14へ自動cascadeしない。

受入れ候補6件は全workspace回帰テスト済み。Router変更はPython 77テストとRust fmt/clippy/test/check/buildがPASS。preflightでの一度のWSL sandboxアクセス拒否は別ログに残し、既存toolchainで再検証した。Local Modelのinfra/coding失敗には含めていない。

applicationへの採用、mainへのmerge、push、次cohortの自動実行はしていない。
