# 差分修正12件の読み方

Sol確認86回の出力内で12件のPATCHが返った。これを適用した後に追加の生成や独立再確認は行っていない。10件は指定データの不一致を訂正し、2件は文章だけの変更。全12件が同じ重大度の失敗だったとは扱わない。

|課題（全原文・初期候補・確認・最終候補）|型|JSON変更数|対象|補足|
|---|---|---:|---|---|
| [PR100-011](cases/PR100-011.json) | dependency_schedule | 5 | データ訂正あり |  |
| [PR100-019](cases/PR100-019.json) | allocation | 1 | 文章のみ |  |
| [PR100-020](cases/PR100-020.json) | document_edits | 2 | データ訂正あり |  |
| [PR100-021](cases/PR100-021.json) | allocation | 7 | データ訂正あり |  |
| [PR100-024](cases/PR100-024.json) | allocation | 3 | データ訂正あり |  |
| [PR100-038](cases/PR100-038.json) | dependency_schedule | 1 | 文章のみ | 任意補足寄りの境界例。元の結論は正しく、必須修正と断定しない。 |
| [PR100-040](cases/PR100-040.json) | service_queue | 13 | データ訂正あり |  |
| [PR100-042](cases/PR100-042.json) | allocation | 3 | データ訂正あり |  |
| [PR100-051](cases/PR100-051.json) | dependency_schedule | 9 | データ訂正あり |  |
| [PR100-060](cases/PR100-060.json) | allocation | 3 | データ訂正あり |  |
| [PR100-067](cases/PR100-067.json) | allocation | 12 | データ訂正あり |  |
| [PR100-094](cases/PR100-094.json) | allocation | 6 | データ訂正あり |  |

数量と件数の混同・不足原因の訂正（019）は利用上の意味がある。一方038は、正しい予定の説明に期限ちょうどの注意を追記した境界例。対象外の状態ラベルだけを直す例と、予定の優先順から後続明細を再計算する011・051は修正規模が異なる。

詳しい利用への影響は [完了時の原文レビュー](COMPLETION_REVIEW_JA.md) を参照。凍結済みの採否や集計は書き換えていない。
