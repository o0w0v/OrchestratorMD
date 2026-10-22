# 公式30課題A/B — 回復run022途中報告

集計: 2026-10-22T04:45:54.505079+00:00

MultiPL-E20課題の両armはHost検証・独立レビューまで終端。SWEを凍結条件のまま継続中で、全60経路の現在の状態は以下。

- Host＋独立Reviewer採用: 44
- workflow失敗終端: 5
- 環境未測定終端: 0
- 未終端: 11

**公式品質は未採点。Host採用を公式resolvedとは扱わない。** 全生成終端・Guest認証削除の後に同じ公式Evaluatorで採点する。

新Astraの既知実支出は 1271.59330 Credits。capacity失敗1 invocationのusage欠測を保持しているため、厳密総額はnull。3 error/failed/incomplete eventを3回の課金にせず、1つの未知残余として保存する。Shared Plannerは実支出で1回、比較workflowでは各armへ全額配賦する。

Localは15回one-shot、repair0、Host PASS8、独立レビュー後採用4、clean fallback11。追加Local生成は0。事前適格15件のAstra比較はA=271.80135、B=280.45510 Creditsで、削減率−3.18%（増加）。公式品質はまだ不明であり、Astra Routerの成功とは判定しない。

SWEのNushellは共有Plannerの未完JSONを保持し、修理・再生成0で両workflowの契約失敗とした。元response・usage・STOPは変更していない。モデル出力契約失敗であり、CUDA/環境エラーやcompilerのcoding failureとは分ける。Rayonも固定4試行の結果を保持し、追加生成しない。Serdeは凍結arm順で継続中。

旧Sol29組はhash照合して再利用し、再実行・再課金0。元30 Task、公式tests/scoring、Router、Production bounded2.2.8は不変。実験用Host分類overlayとcopy/制御フロー修正は別revisionとして開示した。旧STOPや旧Actor Gateは遡って書き換えない。

Tracing-2897の公開base環境問題は独立に未解決で、最終的にも全30分母に残す。全件完了や精度維持、経済的成功をこの途中報告から主張しない。

source commit: `1929a1fed1b15effd649fb719d20880b3e27cd7f`

execution freeze SHA256: `76e6e508a366692082469abfde68faf3eaaebf5e1a17187bd3209efd9ddbe872`
