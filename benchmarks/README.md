# ベンチマークと実験の案内

実験ごとに課題・モデル・運用・採点条件が異なる。件数や成功率を一つに合算しない。運用ルールそのものは [AGENTS.md](../AGENTS.md)、図を使った説明は [説明資料の目次](../docs/presentations/README.md) を参照。

|調べたいこと|収録先|範囲|
|---|---|---|
|必要箇所だけ直すSol＋Gemmaと通常Solの違い|[2026-11-05 新100件](practical-review-100/2026-11-05/README.md)|合成10業務型、同profileのA/B。相談・確認費を含む。データと文章監査範囲を区別|
|独立Reviewerを足さない通常Solの20件比較|[通常Sol20件](../docs/presentations/2026-10-sol-normal-baseline-20.md)|過去の20件。今回の100件と率をpoolしない|
|Gemma26の型ごとの得意・苦手|[Localモデル知識](local-model-knowledge/2026-10-30/README_JA.md)|2000課題と500件追補。課題集合・モデル比較範囲を個別記載|
|独自に生成した課題・コード・テスト・過去結果|[独自課題](custom/README.md) / [48セットINDEX](custom/INDEX.md)|619エントリ。改訂・再実行・部分集合を含み、独立619能力や全件成功ではない|
|公式データセットの固定部分集合|[公式30課題](official-30/INDEX.md) / [評価手順](official-30/README.md)|MultiPL-E Rust20＋Multi-SWE-bench Rust10。公式全体を代替しない|
|追加課題のカタログと過去の知識|[追加500件](../docs/task-catalog/2026-10-additional-500/README.md)|以前の独自生成課題と条件付き評価|

## 今回の100件のファイル構成

```text
practical-review-100/2026-11-05/
  README.md                    結果の入口
  DETAILED_DESIGN_JA.md         実作業・例外・会計の詳細図
  CASE_INDEX_JA.md              全100件へのリンク
  cases/PR100-001.json ...      元依頼、公開対話、A/B候補、確認、最終成果、期待値
  CASE_RESULTS.csv             全200方式結果
  PATCH_CASES_JA.md             12件の差分と解釈
  analysis-001/                比較・全件採点・role別tokens
  accounting/                  累積/増分usageと監査要約
  source-snapshot/             凍結コードの参照コピー
  replay/ + verify.py          追加推論なしの再確認
  integrity/                   元sealのパス正規化コピー
  SOURCE_PROVENANCE.json       元ファイルhashと加工方法
  PACKAGE_MANIFEST.json        公開ファイルhash
```

過去の資料は元の場所と履歴を維持している。今回追加した案内が古い採点・運用設定を更新したものではない。
