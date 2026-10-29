# Gemma26の得意分野と補完モデル

Gemma4 26Bへ任せる作業を、実測結果と条件付きで知識として残す。課題を切り分けるクラウドモデルの精度は今回の対象から外す。

- [得意分野のナレッジ](GEMMA26_KNOWLEDGE_JA.md)
- [機械可読のナレッジ8項目](GEMMA26_KNOWLEDGE.json)
- [補完モデルの候補と既存比較](COMPLEMENT_MODEL_CANDIDATES_JA.md)
- [補完性を測る比較計画](COMPARISON_PLAN.md)
- [過去24件の補完性再集計](HISTORICAL_COMPLEMENTARITY.json)
- [診断用30件の候補](DIAGNOSTIC_PANEL_PROPOSAL.json)

追加500件は小課題のスクリーニング、過去24件はbounded 2.2.8の検証・独立レビュー付き採用比較である。分母・profile・環境が異なるため合算しない。実測、過去の別条件の実測、公開資料から選んだ未測定候補を区別する。

今回新たに行ったのは知識化・既存結果の再集計・公式資料調査。新しいモデル生成やdownload、production routing変更は行っていない。公開版には要約と証跡hashを含み、ローカルの全fixtureやraw出力を含む完全再現bundleではない。
