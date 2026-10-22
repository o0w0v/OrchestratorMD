# 発表用要点 — Codex＋Gemma26の公式workflow評価

**結論: 限定的な支持はあるが、公式30課題での完全達成は未確認（INCONCLUSIVE）。**

|測定済み29課題|Codex-only|Gemma Router|
|---|---:|---:|
|GPT-6 Sol 公式解決|21/29|21/29|
|Sol 比較Credits|358.35012|335.19033|
|Sol Credits/解決課題|17.06|15.96|
|GPT-6 Astra 公式解決|22/29|22/29|

- Solの観測上の削減: Credits **6.46%**、Tokens **0.60%**。事前Local適格15件だけなら、同じ13/15解決でCredits9.72%・Tokens12.44%減。
- Astraは同じ解決数でも成功Taskが1件ずつ異なり、Router側が27.80155 Credits・386,915 Tokens増。適格15件ではCredits3.18%増。総額の欠測があり、全体の削減率は算出不能。
- 全体の費用差をすべてGemma委譲の因果効果とはみなさない。Localを使わないDirect経路の変動を分けた。

重要な未解決事項:

1. Tracing-2897の1 Taskは環境未測定。30分母から除外せず、全30の厳密な解決率は未確定。
2. HostのCargo edition2021と公式のedition指定なしcompileに互換性差があり、保存済み2 bodyのE0599を公開情報だけの比較で再現した。公式flags・tests・元FAILは変更していない。
3. bytesの公開baselineには編集範囲外benchのE0554があった。保存候補の別公式診断もFAILで、Host問題の解消だけで正解になるとは確認できなかった。
4. Final pipeline false greenはSol-only3 / Sol＋Gemma4 / Astra各2。production成功や自動拡大を支持しない。
5. capacity失敗1 invocationのusage欠測と、準備・結果検討の本chatの未測定usageを保持。project全体のnet savingsは不明。

旧Solはhash照合して再利用し、今回の再生成・再課金0。新Astraはrole registry161＋推論送信前TLS失敗1の計162 CLI invocation。既知推論費換算1,983.67855 Credits＋capacity欠測分。Shared Plannerは実支出1回、比較では各armへ全額。Local one-shot15回・repair0。

次に必要なのは、公式条件を変えることではなく、公開Host validationを公式コンパイル条件へ揃える別adapter revisionと、SWE/Tracing環境の整合性確認。Production Router・bounded2.2.8は未変更。

詳細と全Task結果は[RESULTS_JA.md](RESULTS_JA.md)、機械可読の主結果は[FOUR_ARM_RESULTS.json](FOUR_ARM_RESULTS.json)を参照。
