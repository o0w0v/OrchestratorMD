# 公式A/B評価 — 最終結論

集計: 2026-10-22T07:12:25.979297+00:00

**判定: INCONCLUSIVE。現在の完成候補が公式30課題で品質を維持し、費用・Tokensを削減できたと完全確認した状態には達していない。**
測定済み範囲のSol比較には限定的な支持がある。一方、Astra比較では費用・Tokensが増加し、Host validationと公式コンパイル条件の不一致も確認した。

|構成|公式解決 / 測定数|全30に残る未測定|比較Credits|Credits / 解決課題|Final pipeline false green|
|---|---:|---:|---:|---:|---:|
|Sol-only|21/29|1|358.35012|17.06|3|
|Sol＋Gemma|21/29|1|335.19033|15.96|4|
|Astra-only|22/29|1|1124.93880＋欠測分|算出不能|2|
|Astra＋Gemma|22/29|1|1152.74035＋欠測分|算出不能|2|

## 主目的のSol比較

- 同じ29課題で両armとも21件解決。成功・失敗のTask集合も一致した（BOTH21 / NEITHER8 / 未測定1）。
- workflow比較Creditsは358.35012 → 335.19033、観測上6.46%減。Tokensは25,807,856 → 25,652,929、0.60%減。
- 事前Local適格15課題では両arm13/15解決、Credits9.72%減、Tokens12.44%減。
- 全体6.46%をすべてGemma委譲の因果効果とはみなさない。Localを使わないDirect経路にも別実装・cache・実行順による費用差がある。
- 旧Sol結果はhash照合して再利用し、今回のSol再生成・再課金は0。

## 追加のAstra比較

- 両armとも22/29解決。ただし成功Task集合は異なる（BOTH21 / A_ONLY1 / B_ONLY1 / NEITHER6 / 未測定1）。
- Router側は27.80155 Credits、386,915 Tokens増加。共有Planner欠測1 invocationは両armに同額なので差額だけは相殺できるが、厳密な総額・削減率・Credits/解決課題は算出できない。
- 完全計測された事前Local適格15件では両arm14/15解決、Router側Credits3.18%増、Tokens3.67%増。今回のAstra workflowの経済的成功は支持されない。

## 公式採点別

- MultiPL-E: Sol両arm18/20、Astra両arm19/20。
- Multi-SWE-bench: 全4armとも3/9測定、Tracing-2897の1件は環境未測定。元10課題の分母は維持する。

## 新たに確認したHost側の互換性制約

MultiPL-Eの公式Rust compilerは1.75.0、Host公開checkerは1.85.0だった。ただし今回の2件はversion差だけで原因を断定していない。公式ハーネスの固定compile argvは `rustc <source> -o <output>` でedition指定なし、ActorのCargoはedition2021だった。
Astra-onlyのgreatest_common_divisor、Router側のclosest_integerは、公開body内の `try_from` で公式E0599となった。非公開testsを使わず、同じ公式image・同じ公開bodyを比較すると、default compileはE0599、診断用にedition2021を明示したcompileだけが成功した。20件の関数header自体は公式公開promptとexact一致しており、header binding差とは区別した。
**公式Evaluatorへedition2021を追加して直したことにはしない。** 公式flags・tests・scoringは不変で、元のFAIL・成功数・費用は一切書き換えていない。compile-only診断成功は、公式tests PASSやworkflow解決を意味しない。
bytesでは、編集範囲外の未変更benchにstable環境でのE0554が公開baselineから存在した。これをcandidate固有の新しいcoding不具合とは区別する。事前登録したB最終候補1件の別公式採点もFAILであり、「Host問題だけを直せば解決する」とは確認できなかった。

## 安全性・会計の限界

- Final pipeline false greenはSol-only3、Sol＋Gemma4、Astra両arm2。Host＋Reviewer採用を公式正解と同一視せず、false green 0を条件とするproduction成功・自動拡大は主張しない。
- 新Astraは161 CLI invocation、既知実支出換算1,983.67855 Credits＋capacity失敗1 invocationの欠測分。3 error/failed/incomplete eventを3回の費用にしない。
- Shared Plannerは実支出で1回、比較workflowでは両armへ全額。cachedはinputの内数、reasoningはoutputの内数として二重加算しない。
- Creditsはnative usage×開始時の凍結公式Standard単価による換算。請求残高の直接観測ではない。
- Local15回one-shot・repair0。新Astraで採用4/15、旧Solで6/15。LocalのCUDA/INFRA/scope countersは0、旧Host error2件は保全。研究全体のHost STOPを0とは表現しない。
- 公式Evaluator・追加診断scriptのchild AI呼び出しは0。準備・本chatでの結果検討のAI usageは未測定null。プロジェクト全体のnet savingsとJPY換算もnull。
- Guest認証ファイル削除を実測確認した。OpenAIアカウント側のOAuth失効は別の未検証事項。

## 次に必要な修正（今回は未適用）

1. 新しいBenchmark adapter revisionで、公開candidateを公式と同じRust compiler/default edition条件でも検証する。公式Evaluatorの条件は変えず、Hostがsemantic correctionを行わない。
2. SWE公開validationのpristine互換性をTaskごとに再確認し、bytesのbench条件を扱う方針を別freezeにする。未知compiler errorやlintを一括waiveしない。
3. Tracing-2897の公開base環境を解消する。原testsを修理・正常化したり、Taskを差し替えたりしない。
4. 旧結果とSTOPを保持し、条件変更は新cohortとして実施する。今回の凍結評価を後から成功へ変更せず、Production Routerやbounded2.2.8を自動変更しない。

既存の構造に価値がないと一般化する結果でも、公式30課題で完全達成と主張できる結果でもない。得られた支持と、追加検証を要する制約を分けた最終報告である。

## 失敗CLI呼び出しの会計補足

161はTask role registry内のCLI invocation数である。別に、最初のTLS失敗1 invocationも保全しているため、新Astra CLIの合計は162。TLS失敗のraw usageはnullのままで、gatewayにupstream inference未送信の独立証拠があるため、派生推論費だけを構造的0とした。CODEX_FAILED_CALL_USAGE_SUPPLEMENT.csv / FAILED_CALL_ACCOUNTING_SUPPLEMENT.jsonから証拠SHA256を辿れる。capacity失敗は推論側の活動があり同じ0扱いにはせず、欠測1 invocationを保持する。

Shared Planner、retry、失敗を含むrole-registry実支出の既知小計は1,983.67855 Credits。これは準備・本chatでの検討を含む全研究費用の確定総額ではない。
