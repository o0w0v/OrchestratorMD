# 公式A/B評価 — MultiPL-E生成終端・SWE継続

集計: 2026-10-22T03:18:33.640866+00:00

MultiPL-E20課題はAstra-only / Astra＋Gemmaの両経路でHost検証・独立レビューまで終端しました。公式採点は全生成freezeとGuest認証削除後に実施します。Host採用を公式resolvedと同一視しません。Solの既存29組は再実行・再課金0で保全しています。

Localは15/15 one-shot、repair0。Host PASS8件、独立AstraレビューでLocal候補を採用4件、clean Codex fallback11件です。失敗candidate/diff/diagnosticsはclean Executorへ渡しません。

|事前固定のLocal適格15課題|Codex-only|Gemma Router|Credits削減率|
|---|---:|---:|---:|
|新Astra workflow（公式品質未採点）|271.80135|280.45510|−3.18%（増加）|
|旧Sol workflow（immutable reference）|75.49859|68.16259|9.72%減|

旧Solのこの15件の公式resolvedは両arm13/15。新Astraの公式品質はまだ未測定です。Creditsは実native usage×凍結公式Standard単価の換算で、請求残高の直接観測ではありません。Shared Plannerは比較各armへ全額配賦し、実支出では1回です。失敗費用も含めています。

**この時点でAstra Routerの経済的成功とは判定しません。** 結果を見て途中でprompt・routing・model・validationを最適化せず、SWEも同条件で継続します。Direct課題の費用差までGemmaの因果効果とはみなしません。

旧Host STOPは変更しません。新revisionでは、copy先rootの束縛漏れ、凍結arm enumの対応漏れを修正し、保存済みCodex実装とSWE Plannerを再利用しました。修正を理由とする完了済みAIの再生成は0です。30課題・60経路の実control flowをsyntheticで巡回し、完了40経路の再実行0、保存Planner再実行0、未知enum拒否を確認しました。AI呼出し0です。公開pristine SWEの固定6検証・289テストも隔離network=noneでPASSしました。

SWEの実処理ではripgrep BがHost＋独立レビューを通過し、A側を処理中です。公式テスト/gold/cacheをActorへ戻す経路はありません。

capacity失敗1 invocationのusage欠測はnullのままです。全体の厳密なAstra Credits・削減率を捏造しません。Tracing-2897のpublic pristine診断差も未解決で、全30件の分母に保持します。

実験用Host分類overlay、パス束縛・制御フロー修正を新revisionとして開示し、Production Router、bounded2.2.8原本、公式問題・tests・scoringは変更していません。旧Sandbox GateもPASSへ昇格しません。

source commit: `7501b3dc9d03a7a8db3371ad59be63a357278faa`

execution freeze SHA256: `161e499d62f42600740e6d7b97745791325727455a55bddf798206651d1d77bf`

最終品質・経済比較は公式結果とusage coverageを揃えて判定します。準備の未測定Codex usage、JPY、project全体net savingsはnullです。
