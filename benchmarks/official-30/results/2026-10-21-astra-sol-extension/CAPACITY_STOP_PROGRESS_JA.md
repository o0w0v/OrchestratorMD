# 公式30課題 A/B：Provider capacity停止の保全記録

2026-10-21T19:13:10.856901+00:00集計。公式採点前の進捗であり、モデル品質や最終解決率の結果ではない。

完了済み11課題の経路を保持した後、次課題の共有PlannerでAstraが`Selected model is at capacity`を返した。部分的なモデル動作は記録されているが、完成planと`turn.completed` usageはない。モデルを切り替えず停止し、旧STOPを保全した。

重複を除いたこの回復viewのnative invocationは49件、usage実測が揃う呼び出しは48件。失敗した1 invocationにはerror／turn.failed／INCOMPLETE_INVOCATIONの3記録があり、3回の呼び出しとは数えない。これらのtokens／Creditsはnullであり、構造的0ではない。

実usageと凍結単価による既知Credits小計は298.21970。欠測を含む全額、請求アカウントの実引落、厳密な削減率はnull。過去のTLS失敗も別途保持し、欠測を0へ書き換えない。Shared Plannerは実支出では1回、workflow比較では両armへ全額を配賦する。

Localは累計9回を保持し、このdirect区間での追加生成は0。2つのHost formatter停止と未実行6件は保全し、分類条件の選択待ちである。旧Sol29測定は再実行・再課金しない。

Guestのlive認証3ファイルは削除済み。アカウント側の失効確認とは区別する。新runは完成済み出力をhash照合で引き継ぎ、capacityで未完了だったPlannerだけをclean sessionで最大1回試す計画。元の12時間認証期限を延長しない。公式test・Task・Router・bounded 2.2.8・モデル設定は変更しない。
