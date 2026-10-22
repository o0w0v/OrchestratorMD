# Secondary KPIの測定範囲

Local15回はone-shot・repair0、Host PASS 8、独立レビュー後採用 4、clean fallback 11。

歴史的Sol workflowは同じ適格15 TaskでHost PASS 8、採用 6、clean fallback 9。元結果のhashを照合し、再実行・再課金は0。新Astraと旧SolのLocal出力が全件byte一致することや、Reviewer一般能力の順位は主張しない。

採用Local候補は公式採点へ渡した最終候補とのhash一致を確認した。この部分についてのみ、公式FAILならLocal validation false greenと判定できる。Host PASSでもReviewerで不採用となった4候補は、そのLocal候補自体を公式採点していないため未測定。Reviewer REJECTを公式FAILとみなさず、全Host PASSに対する厳密なfalse green件数を0へ補完しない。

Local15件のnative Worker countersはCUDA_ERROR=0、INFRA_ERROR=0、scope_failures=0、Host_failures=2。旧HOST_FORMAT_ERROR2件は原結果のまま保全し、別revisionの構文証拠を付加した。実験全体には別のHost/auth/制御フローSTOPがあり、Localの0を全研究期間の障害0とは表現しない。

この集計から独立に確認できないbackend crash、GPU query timeout、peak/free VRAMの総計はnull。既存raw telemetryは保全するが、欠測から0を推定しない。追加のモデル呼び出し・公式採点は0。
