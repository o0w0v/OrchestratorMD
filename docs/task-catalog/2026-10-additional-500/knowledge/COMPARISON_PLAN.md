# 補完性を確かめる小規模比較

まず既存出力を使い、Gemmaのモデル誤りと、Host・型参照・採点器の問題を切り離す。その上で、同じclean入力を別モデルへ渡して比較する。クラウドモデルの課題分割精度は評価しない。

## 診断用の30件

既存500件から、Gemmaのコード失敗15件、具体的な意味誤りを確認したOffice5件、成功対照10件を候補にした。ID・元contract/request/result hashは[DIAGNOSTIC_PANEL_PROPOSAL.json](DIAGNOSTIC_PANEL_PROPOSAL.json)に保存。まだ実行freezeではなく、契約と検証の事前レビューが必要である。

選定には過去の成否を使っている。**Gemmaの既知失敗を調べる診断であり、一般的な成功率や将来のrouting精度を測る盲検benchmarkではない。** 得られた使い分けを確かめる際は、別の未使用課題を先にfreezeする。

## 実行前に固定するもの

- 公開入力、Task contract、編集scope、型・参照、合格条件、検証器のhash。
- 各model digest、量子化、context/output/timeout、思考modeとその対応状況。
- 初回1回、semantic repair0。モデルにGemmaの失敗candidate・diff・診断・期待値を見せず、clean初期sourceから実装させる。
- code実行は隔離環境、Officeは同一Host adapter/検証。private期待値をモデル入力へ戻さない。
- Host・契約不備が見つかった課題は能力比較から分離。修正が必要なら元結果は残し、両モデルを同じ新revisionで評価する。片方だけ修正後の条件へ移さない。

最初は現行の8192 context/2048 output予算へ適合できるかを調べる。reasoningを使う場合も最終回答だけでなく思考に使ったtoken・時間を含める。思考設定が異なる比較は、その組合せの評価として記録する。大きい予算でだけ解けた場合は、同予算の優位と主張しない。

## 主要な記録

| 指標 | 意味 |
|---|---|
| Gemmaだけ合格 / 候補だけ合格 / 両方 / 両方不合格 | 同一課題での補完関係 |
| Gemmaの確認済み失敗を救えた件数と分母 | 既知失敗に対する補完率 |
| 成功対照を候補が落とした件数 | 苦手を補うために失う成功 |
| 規則違反・型/構文・意味・Host・infra | 失敗原因を区別 |
| native input/output tokens、duration、output limit | 失敗時も含むLocal費用 |
| モデル切替・load・Host検証・全体wall | 推論速度だけで経済性を判断しない |
| false green、scope、GPU/CUDA | 安全性と運用適合性を分離 |

失敗課題だけに絞った成功率を、全体成功率と呼ばない。両モデルの正解を結果を見て選んだ合計は「事後的な上限」であり、実運用Routerの成績ではない。自動cascadeの導入判断は別変更とする。

今回の段階は知識化と比較計画まで。新しいgeneration・有料Codex比較・モデル追加取得は行っていない。Local tokenからCodex Credits削減を逆算しない。準備作業のCodex実usageは取得できずnullを維持する。
