> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/bounded-v2.2.5-syntax-preflight--offline.md). This report alone does not establish a task result.

# bounded 2.2.5 Candidate Syntax / Formatter Preflight Classification

判定: **READY_FOR_FULL_SHADOW_PILOT_RETRY**。保存済みP224-001をcandidate構文失敗へ正しく分類し、実モデルでもsame-model repair 1回とTask-local終了を確認した。独立3 Taskはcohort STOPなしで完了した。

ただし**実モデルのsyntax repairは0/1成功**。P224-001相当ではrepair後もE0762が残り、REJECTを保持した。今回のREADYは分類・安全なrepair制御の検証結果であり、モデル修復品質の改善やFull Pilotの合格を意味しない。Full Pilotは自動開始していない。

## 変更内容と維持条件

profileを2.2.4から2.2.5へ更新した。`bounded_syntax.py`でpinned rustfmtの限定rendererを認識し、exit codeに加えて診断code/message、正確なstaging path、行/列、候補と一致する表示ソース、変更されたallowed bodyへのprimary span bindingを要求する。candidate/source/staging/freeze/Git metadataとformatter pin/versionを再確認した場合だけ`CANDIDATE_SYNTAX_FAILURE`へ分類する。

未知renderer、混在エラー、panic、曖昧なspan、I/O/config/executable異常は安全側のHost STOP。既存identity違反の`FORMAT_INTEGRITY_FAILURE`は維持し、candidateへ降格しない。未知診断は既存`HOST_FORMAT_ERROR`へまとめるため、独立した`UNKNOWN_FORMATTER_FAILURE`件数は0。

Router、Operational Policy、Gemma12 quarantine、model routing、fixed-slot/stateful authority、Typed References、Coverage Gate、lint allowlist、formatter binary/version/config/構造正規化ルールは変更していない。profile JSONはversionのみ変更。既存構造正規化関数のソース一致と全regressionを確認した。

syntax / semantic / lintを合わせてTask全体最大1 repair。raw診断は既存lossless packingで返し、span/hash・candidate diff・fresh capability・Typed Referencesを供給する。Hostが正解literalやpatchをモデルへ教えることはない。成功したrepairはpreflight → formatter → structural guard → 全mandatory validationへ戻る。

設計: DESIGN.md（元資料: DESIGN.md）、実装文書（元資料: ../../docs/V2_2_5_SYNTAX_CLASSIFICATION_JA.md）。

実行時のruntime/configはbyte snapshot索引（元資料: runtime-source/index.json）へ保存し、Gitのtext改行正規化とは独立してfreeze hashを再検証できるようにした。

## 保存済みP224-001 replay

旧`router-shadow-pilot-v2.2.4-fresh-001`のcandidate、exit 101、raw E0762、formatter recordをread-onlyで使用した。旧result / STOPは不変。

1. 保存raw診断を保存staging path・candidate行118/列13へbindingし、CANDIDATE_SYNTAX_FAILUREと判定。
2. 新しい隔離copyで同じ候補をpinned rustfmtへ渡し、実runtimeのsource/staging/freeze/pin guardを経て同分類を確認。
3. 実runtimeが構築する次のrepair requestをAPI直前で捕捉。offline inferenceは0。

offline requestは**9,999 chars / 10,287 bytes**。num_ctx=8192、num_predict=2048、temperature=0、seed=20260926、max_context_chars=24000を維持し、既存char gate内。token推定はheuristicであり、実測や無損失の証明として使用しない。

保存診断分類（元資料: offline/saved-classification.json）、offline summary（元資料: offline/summary.json）、repair request（元資料: offline/repair-request.json）。offline responseのtoken値は旧run由来であり、今回のlive集計から除外した。

## 独立live cohort

Ollama 0.35.0 / RTX 3080 / driver 591.86 / Gemma26の既存digestを使用。read-only GPU/API/residency確認を各Task前後に実行した。generation probe、restart、forced unload、Gemma12、Qwen/CoderNext fallbackはない。

Task/coverage IDと隔離先だけを変更し、business仕様、保護acceptance、reference計画、generation optionsを再利用。固定順で3件を実行し、意図的なsyntax errorはpromptへ加えていない。

| Task | 元Task / protocol | First PASS | repair | Local final | Codex review |
| --- | --- | --- | --- | --- | --- |
| S225-001 | P224-001 / fixed_slot | FAIL | syntax ×1、未回復 | ESCALATE: CANDIDATE_SYNTAX_FAILURE | REJECT |
| S225-002 | P224-004 / fixed_slot | PASS | なし | PASS | ACCEPT_NO_CHANGE |
| S225-003 | P224-002 / stateful | PASS | なし | PASS | ACCEPT_NO_CHANGE |

S225-001は初回とrepair後の両方でE0762。残りbudgetがないため追加generationを行わずTask-local終了し、次Taskへ進んだ。構文が直っていないのでmandatory acceptance等は未実行であり、実行済み/PASSとは記録しない。

S225-002/003はacceptance、regression、fmt、clippy、workspace test/check/build、scope guardを全てPASS。S225-003はstatefulのissued handle適用と既存formatter正規化も通過した。Codexはdiffとcontractを確認し、used-memoryの境界条件、元evidence保持、valid snapshot上の減算同値性を確認した。

run history（元資料: live/run-history.json）、Task別指標（元資料: metrics/task-metrics.json）、compact review（元資料: reviews/summary.json）。applicationへの自動採用はない。

## Repair transport

実syntax repair requestは**9,951 chars / 10,239 bytes**。HTTP 200、prompt_eval_count **3178**、eval_count **135**、done_reason=`stop`、server truncated flag **0**。既存budgetのまま処理された。truncation evidenceなしと修復品質は分離し、E0762残存をコード失敗として保持した。

初回+repairのAPIは2 callで打ち切り。実モデルの修復成功率は0/1であり、必ず修復できるpolicyとは評価しない。全request/response索引（元資料: metrics/request-index.json）。

## 修復成功時の全validation経路

liveでsyntax repair成功が得られなかったため、別の**offline injected-response fixture**でも確認した。実pinned rustfmtで不正候補を拒否し、次のfixture応答で構文を修復した後、acceptance・regression・fmt・clippy・workspace check/build/test・scope guardを実Rust toolchainで全て再実行しPASSした。

これは実モデルによる回復ではなく、成功時のruntime経路を確認するソフトウェアtest。追加Ollama inferenceは0、実Taskへ正解patchを渡していない。native-repair summary（元資料: native-repair/summary.json）。

## Regression / 安全性

Worker suite **212/212 PASS**（新規syntax関連11 testsを含む）。Rust fmt / clippy / test / check / buildもPASS。

検証した境界は、正確なdiag binding、未知renderer/mixed Host error/panic拒否、stage/source変更、formatter未配置/launch異常、修復前後のfresh capability、stateful repair、semantic→syntax、syntax→semantic/lint、syntax再失敗時の追加generation禁止、最終guardでのsource drift STOP。既存method-chain、vec trailing comma、closure normalization、unsupported task-local、lint repair、reference/scope/freeze suiteを維持した。

実cohortのHost failure / scope failure / FALSE_GREEN / INFRA_ERROR / CUDA / cohort STOPはいずれも0。既存保護ファイル14,819件不変（明示した既存7ファイルの改修のみ除外）。過去experiment artifactは全て保全。regression（元資料: regression/worker-summary.json）、Rust checks（元資料: regression/rust-summary.json）、integrity（元資料: metrics/summary.json）。

## Metrics

| 指標 | 結果 |
| --- | --- |
| 完走 | 3/3 terminal、STOP 0 |
| formatter preflight attempts | 4 |
| CANDIDATE_SYNTAX_FAILURE | 2 attempts / 1 Task |
| HOST_FORMAT_ERROR / UNKNOWN_FORMATTER_FAILURE | 0 / 0 |
| syntax repair invoked / recovered | 1 / 0 |
| global repair budget使用 | 合計1、各Task上限1 |
| First PASS / Local final PASS | 2/3 / 2/3 |
| ACCEPT_NO_CHANGE | 2/3 = 66.7% |
| Codex candidate repair LOC | 0 |
| FALSE_GREEN / Host・scope failure | 0 / 0 |
| INFRA / CUDA | 0 / 0 |
| live generation calls | 5（stateful DISCOVERYを含む） |
| live input / output tokens | 8549 / 514 |
| Worker合計 / cohort wall time | 128.280秒 / 131.766秒 |

normal review packetは6,268 / 6,779 / 7,289 bytes。通常reviewで全Local会話は読んでいない。Host分類実装・test作成と、候補のCodex修正LOCを分離した。Codex tokens/active time、net savingsは取得できないためnull。workload（元資料: metrics/codex-workload.json）。

## 限界と次の判断

限定renderer以外、primary spanが変更region外、複数pathが曖昧なsyntax errorはHost側へ倒す。一般Rust parserとして全エラーを分類する実装ではない。構造正規化の許可範囲は広げていない。

分類変更によって、今回のE0762はcohort全体を止めず、モデルへの1回repairとTask-local REJECTへ到達した。Full Shadow Pilot再試行の安全上の条件は満たしたが、P224-001のcoding失敗は残る。成功率改善・長期GPU安定・モデル能力向上は主張しない。次のFull Pilotは新cohortとして別途実施し、今回は開始しない。
