# bytesの公開validation制約と別診断

元の公開baselineにも、未変更の `benches/bytes_mut.rs` にE0554（stable release channelで `#![feature]` を使えない）が存在した。該当benchはActorの許可編集範囲外であり、固定Host validatorはnon-Clippy compiler errorをwaiveしない。

これはcandidate固有の新しい機能不具合とは分ける必要がある。公開tests/check/buildがPASSでも、Clippy構成上のこのエラーによりworkflowは候補を採用できなかった。評価中にコマンド・waiver・scope・原テスト・公式scoringを変更していない。元のworkflow失敗、空patchの公式結果、全試行の実usage/費用はそのまま保持した。

## 公式結果を見る前に固定した別診断

- 選択: bytes B側の第4候補。Clippy以外は全PASS、残る非waive診断1件がbaseline E0554にexact一致、該当ファイルは不変かつ編集範囲外。
- 追加model生成・Codex Reviewer・fallback・Credits: 0。保存候補だけを、全Actor終了・Guest認証削除・本採点完了後に同じ公式Evaluatorへ渡した。
- 診断結果: SELECTED_REJECTED_CANDIDATE_ALSO_OFFICIAL_FAIL。
- 事前固定したB最終候補は公式テストでも未解決だった。Hostのbaseline不整合は実在するが、この候補で公式品質を回復できたとは言えない。

別診断の成功をprimary workflowの成功へ足さない。Reviewerはこのcontrolに対して実行しておらず、修正後の採用率・Credits削減率・再開後のworkflow品質を推定しない。これは1候補の切り分けであり、Host false-negative率一般の推定ではない。

上記0は診断実行scriptの新規CLI/Local呼び出しの構造的0である。準備・調査に使った本chatのAI usageは未測定nullであり、準備費用を0と主張しない。

会計のphase範囲はACCOUNTING_PHASE_SCOPE.jsonに分離した。公式Evaluator実行scriptのchild AI callは構造的0だが、本chatでの準備・結果検討のAI消費は未測定null。旧TOKEN_ACCOUNTING.jsonのvalidation 0はpure-script child callの範囲であり、全研究・全検証費用が0という意味ではない。

この制約とTracing-2897の未測定、capacity usage欠測を含め、現状から「公式30課題で開発目的を完全達成」とは判定しない。測定済みworkflowの公式結果と費用比較は、元のRESULTS_JA.md / FOUR_ARM_RESULTS.jsonに保全した。Protocol/model/Router改善を結果に合わせて適用した研究ではない。
