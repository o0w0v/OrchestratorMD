# 公式A/B評価 — Local生成完了・残経路の回復状況

集計: 2026-10-22T01:48:04.265748+00:00

凍結30課題のAstra拡張評価は継続中です。Solの既存結果は再実行・再課金せず保全しています。新しい公式Astra結果は未採点で、目的達成の結論はまだ出せません。

- Localは15/15件を各1回生成済み、repair 0。Host検証PASSは8/15で、独立レビュー採用率・公式解決率とは区別します。
- 未試行だった6件を実施し、Host PASS 3件、clean Codex実装待ち3件となりました。再生成はありません。
- 旧2件のHOST_FORMAT_ERRORは書き換えず保全。別revisionのpinned native構文診断で不正候補と確認し、clean Codex fallbackへ渡します。候補・失敗diff・診断はExecutorに渡しません。
- Host分類overlayは実験専用です。Production bounded2.2.8、Router、モデル、8192/2048、prompt、公式問題・tests・scoringを変更していません。分類条件の差は比較上の制約として残します。
- 分類負テスト21件、既存Worker275件、回復オーケストレーション40件がPASS。Rust workspace fmt/clippy/test/check/buildもPASSです。
- MultiPL-EのHost側終端はA 20/20、B 12/20。Bの残り8件は独立レビューまたはclean Codex実装です。
- DirectはSWE初回モデル送信前に会計ガードで停止。既知capacity失敗1件の証跡限定継続判定をSWE側にも適用した新runを用意しました。既存STOPは変更しません。
- capacity失敗のraw usageは欠測nullのままです。厳密なAstra総Credits・削減率を捏造しません。数値Creditsは実usage×凍結公式単価による換算で、アカウント請求残高の直接測定ではありません。
- Tracing-2897はpublic pristine trybuildの診断差が未解決で、30課題の分母に残します。公開checkerと公式project imageの実rustcは両方1.85.0で一致しました。原因は未確定です。

新runのGuest認証確認後、残りのCodex経路を処理します。全生成結果をfreezeし、Guest認証の削除を確認してから、同じ公式Evaluatorで採点します。公式評価結果はActorへ戻しません。

新source commit: `33c2e49945ee3084ac5c97e35c1d9d0cb1450ba7`

新execution freeze SHA256: `4a54fc7eaec83c2bb7bc9f9013a76984a42d101b03849063f4ce6ed7b77967a5`

内部46課題の結果と公式30課題の結果は混合しません。A_ONLY/B_ONLY/BOTH/NEITHER、MultiPL-E/SWE別、全課題分母、失敗callを含む会計で品質・Credits/解決課題を判定します。
