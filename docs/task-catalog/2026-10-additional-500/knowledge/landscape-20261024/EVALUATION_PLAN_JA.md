# 「Gemmaが苦手なところを他モデルが補えるか」の確認方法

今回は計画のみ。production Routerや既存の500件採点を変更せず、新しい比較runとして扱う。

## 評価軸を分ける

| 分野 | 公開評価で参考にするもの | 当方の仕事で追加確認するもの |
| --- | --- | --- |
| 小さなコード実装 | [LiveCodeBench](https://livecodebench.github.io/) | 型・field・helperを使った局所修正、scope、compile、意味 |
| repository修正 | [SWE-bench](https://github.com/SWE-bench/SWE-bench) | tool/scaffold込みか、bounded単一責務での成功か |
| 長文資料 | [LongBench](https://github.com/THUDM/LongBench) | 根拠箇所、条件・例外の保持、資料外情報の混入 |
| OCR・表・数式 | [OmniDocBench](https://github.com/opendatalab/OmniDocBench) | 日本語・桁/単位・表の行列対応。英中中心の評価を日本語保証にしない |
| GUI・複数アプリ | [OSWorld](https://github.com/xlang-ai/OSWorld) | 使用tool、アプリ、最終ファイルの正確性を含むシステム全体 |

これらは評価方法を選ぶ資料であり、今回このharnessを実行したという意味ではない。異なるversion・推論budget・agentを使ったscoreを一つの順位表へ足さない。

## 小さな診断から始める

1. 既存[診断panel案](https://github.com/o0w0v/OrchestratorMD/blob/docs/additional-500-task-catalog-20261024/docs/task-catalog/2026-10-additional-500/knowledge/DIAGNOSTIC_PANEL_PROPOSAL.json)の既知失敗20件＋成功control10件を使う。まず分野に合う1〜2モデルに絞る。全26モデル×500件を最初から実行しない。
2. codingとtyped Officeの比較では同じTask、同じHost/acceptance/scopeを固定する。モデルごとに正解例を足したり、失敗後にTaskを簡単にしない。
3. 画像/OCRは別panelを作る。既存text-only失敗例だけで画像入力能力は測れない。GUIやOffice直接編集も別panel。
4. 固定8192/2048で比較する枠と、公開推奨のthinking/contextを使う適性調査枠を分ける。後者で改善しても現行boundedの改善とは呼ばない。
5. 診断で差が見えた分野について、未使用の新Taskで再確認する。既知失敗panelの成績から汎化率を出さない。

## 得意分野として残す単位

「コードが得意」のような大分類だけでなく、条件を一緒に保存する。

- 入力：仕様、参照情報、言語、画像/テキスト、量。
- 出力：変更範囲、schema、成果物形式。
- 難しさ：条件数、必要な型/API、資料間の参照、手順数。
- 検証：意味・形式・ファイル整合性・review。
- コスト：native input/output tokens、wall、RAM/VRAM、infra。
- 結果：Gemmaのみ成功／候補のみ成功／両方成功／両方失敗。

補完率は「Gemmaが不合格だった同じTaskを、候補が同じ基準で合格した割合」。採用条件を満たさない自己申告PASSを数えない。利用できるmodel数が増えただけではRouterの価値は証明されない。

## 判断

- 既存実測のGemma強みは結果として維持する。
- 公開資料から選んだ候補の強みは、当方の業務に対しては未測定。
- 候補がGemma失敗を補完し、成功controlを壊さず、総コストが許容できた時に導入候補とする。
- task分割精度、モデル自動切替、Router更新は今回の比較に含めない。
