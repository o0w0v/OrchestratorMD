# 追加500件 実行結果の公開範囲

全500件へGemma4 26Bを1回ずつ実行した。コード85/100、Office248/400が狭い固定チェックを通過。OfficeはHost補助と採点/変換不備を含み、業務全体成功率ではない。

- [結果報告](RESULTS_JA.md)
- [50分類](FAMILY_RESULTS.md)
- [分割テンプレート](DECOMPOSITION_TEMPLATES.md)
- [集計JSON](SUMMARY.json)
- Task別CSV: [コード](COD_RESULTS.csv) / [PowerPoint](PPT_RESULTS.csv) / [Excel](XLS_RESULTS.csv) / [Word](DOC_RESULTS.csv) / [複数アプリ](WRK_RESULTS.csv)
- [QA所見](QA_REVIEW.json) / [会計](TOKEN_ACCOUNTING.json) / [原証跡の照合](INTEGRITY.json)

この公開フォルダーは要約と500件の結果・証跡hashを含む。raw request/response、具体fixture、生成ファイル、コンテナ、GPU全ログはローカルで保全し、ここには全量を含めない。公開ファイルだけで実行を完全再現できるbundleとは主張しない。

元カタログは作成時の状態として保全した。カタログ内のNOT_RUNは最新実行状態ではなく、この結果フォルダーが実行後の記録である。
