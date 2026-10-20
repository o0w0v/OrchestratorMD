# 独自生成課題と過去の検証結果

「Create repository AGENTS.md」チャットの実験フォルダーに保存されていた、独自に生成した課題セットをまとめました。公式データセットの30課題とは別の資料です。

**48セット・619課題エントリ**を収録しています。改訂・再実行・部分集合を含みます。目標・インターフェース・受入条件等の完全一致でまとめると403種類ですが、これは意味的に独立した課題数の保証ではありません。全619件が実行済み・成功したという意味でもありません。

| 資料 | 内容 |
| --- | --- |
| [INDEX.md](INDEX.md) | セット別の件数と課題定義へのリンク |
| [synthetic-task-bundle.zip](synthetic-task-bundle.zip) | 全課題文・初期コード・元のテスト・検証結果・取り出しツール |
| [historical-results.csv](historical-results.csv) | 元の記録から抽出した結果表。895行はモデル・工程・証拠ソース別の記録であり895回の独立実験ではありません |
| [result-coverage.json](result-coverage.json) | セット別の結果収録範囲と元レポートの対応 |
| [results-template.csv](results-template.csv) | 別製品で再テストするための空欄CSV |
| [UPLOAD_MANIFEST.json](UPLOAD_MANIFEST.json) | 公開ファイルとZIPのSHA-256 |

## 課題を取り出す

ZIPを展開したフォルダーで実行します。Python 3.11以降の標準ライブラリだけを使い、モデルやテストは自動実行しません。

```sh
python verify_bundle.py
python materialize_task.py --list
python materialize_task.py --set family-gated-local-router-228 --task FGR228-001 --output work/FGR228-001
```

生成した `PROMPT.md` と `task.json` が課題、`workspace/` が元の初期コードと保護されたテストです。`evaluator/evaluation.json` は検証担当用です。Rustの場合、評価対象のCargo workspaceで評価ファイルのCargoコマンドを実行します。元環境固有のWSL・toolchainパス・timeoutラッパーだけを外し、Cargo引数は保持しています。環境に必要な依存取得は別途行ってください。

Python/HTMLの初期モデル比較は、同梱の `evaluators/model_routing.py` が元の決定的validatorです。評価ファイルの `model_routing_task` を検証担当がJSONとして保存し、そのJSONとcandidate workspaceを引数に渡して使用します。構造化回答はcandidate側の `answer.json` を読みます。正解値やmutation用情報を含む評価ファイルは実装担当へ渡さず、テスト生成課題の固定実装と受入条件は元の条件どおり扱ってください。

元のプロトコル固有のHost guard、mutation runner、Router本体を完全に再実装した配布物ではありません。比較条件を決める際は、同梱の受入条件・初期テストと元の検証レポートを確認してください。一部には元のテスト設計不備を調べる対照課題も含まれます。

## 検証結果の読み方

ZIPの `results/<set_id>/` に、過去の構造化結果の抜粋と元の最終検証レポートを収録しました。小さなlive/offline検証や初期runの結果は親実験または後続の総括レポートを参照している場合があり、`source_report` に対応を記録しています。

PASS/FAIL、Local採用、最終品質、未実行、停止、会計欠測を区別し、元の判定値を保持しています。複数モデル・工程・改訂結果を自動で一つの「最新PASS」へまとめていません。構造化結果を取得できなかった課題は `REPORT_ONLY_OR_NOT_IMPORTED` または `NOT_IMPORTED` とし、FAILやNOT_RUNとは推定していません。欠測を0で補完せず、料金・tokensも測定が存在する範囲だけを収録しています。

レポートはローカルファイルパスを `[LOCAL_PATH]` に置換しています。元ファイルのSHA-256と、JSON結果内の位置を記録しています。生の認証情報・全会話・CLI sessionログ・モデル応答全文は含みません。このアップロードでモデル評価を再実行したわけではありません。

ZIPでは共通の初期コードを `objects/` に重複を除いて格納しています。取り出しツールが各課題の元のパスへ復元し、ハッシュを照合します。問題文・受入条件・初期コードの意味は変更せず、配布用の構成と環境依存の実行ラッパーだけを調整しています。課題ファイル名と元のtask_idが異なるケースは両方を表示しています。
