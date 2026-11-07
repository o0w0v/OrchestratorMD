# Orchestrator Local

> いつものAIへの頼み方はそのまま。作業の一部をPC内のAIに分担させ、クラウドAIの消費を抑えることを目指します。

**今までと同じように依頼して、必要な品質の結果を受け取り、そのためのコストを下げること**が狙いです。相談・設計と最終確認をふだんの会話で行い、実作業の一部を手元のAIに任せます。

このリポジトリ（OrchestratorMD）のメインコンテンツは、[Orchestrator Local](apps/orchestrator-local)です。現在は、CSV/JSONの整理・集計や、一覧と短い共有文を作成するWindows向け初期版を公開しています。

**[導入・使い方](apps/orchestrator-local/README_JA.md)** · [ソースコード](apps/orchestrator-local) · [内部の構成図](apps/orchestrator-local/DESIGN_JA.md) · [English](apps/orchestrator-local/README.md)

## 使い始める

Python 3.11以降と、OllamaでGemma4 26Bを実行できるWindows PCが必要です。モデル本体は同梱していません。

1. このリポジトリを[ZIPでダウンロード](https://github.com/o0w0v/OrchestratorMD/archive/refs/heads/main.zip)するか、cloneします。
2. `apps/orchestrator-local`を開き、[導入手順](apps/orchestrator-local/README_JA.md#導入)に沿って接続と実行サービスを設定します。
3. デスクトップアプリのMCP接続を再起動し、[最初の依頼例](apps/orchestrator-local/examples/first-request.md)で使い始めます。

一度の導入後は、いつもの会話から作業を依頼します。必要な条件を相談し、作成した結果を確認してCSV・JSON・共有文として受け取れます。ログイン時の自動起動や、後からの登録解除にも対応しています。

## コストについて分かったこと

設計の参考にした100件比較では、初期相談・設計からSolの最終確認・部分修正までを含めて、次の結果になりました。

|項目|通常Sol|新方式（Sol確認・部分修正込み）|
|---|---:|---:|
|既知Credits小計|181.64328|122.10496|
|採用データ正解|100/100件|100/100件|
|平均active時間（相談込み）|63.10秒|247.32秒|

**既知小計は59.53832 Credits、約32.78％減りました。** その一方で、処理時間は増えました。小さい14件は両方式で直接Solの実行を共有し、新方式では残る86件をGemmaに任せています。

これは合成業務データ100件の実測です。共通工程の未計測消費があるため総支出と厳密な削減率は未確定で、全件文章の独立した同等性評価も実施していません。公開アプリの会話側Creditsはまだ計測しておらず、実験結果と各利用場面の効果は分けて扱います。[比較の条件・全記録](benchmarks/practical-review-100/2026-11-05/COMPLETION_REVIEW_JA.md)を参照してください。

## 内部の仕組み

会話側のAIが相談・設計と最終確認を担当し、Gemmaが実作業の一部を担当します。小さい仕事は会話側で直接処理することもできます。使える成果物はそのまま採用し、必要な箇所だけ直して保存します。別のCloud Reviewerは追加しません。

受け渡し・確認・部分修正・保存は、この使い方を支える裏側の仕組みです。実行中の状態や成果物を残し、会話の接続を開き直しても確認できるようにしています。

- [構成図と処理の流れ](apps/orchestrator-local/DESIGN_JA.md)
- [処理・確認・保存の詳しい説明](apps/orchestrator-local/README_JA.md#処理と確認)
- [実装と動作確認の範囲](apps/orchestrator-local/VALIDATION.md)
- [MCP・Skill・テストを含む実装一式](apps/orchestrator-local)

この初期版の実機確認は一台のWindows PCで行っています。入力と候補は確認のため会話側にも渡るので、完全オフラインの構成ではありません。

## 開発の背景・実験資料

Orchestrator Localの説明をトップに置き、従来の開発ルールや研究資料の案内は[開発ルール・資料の背景ページ](DEVELOPMENT_RULES_OVERVIEW_JA.md)へまとめました。

- [100件比較の説明資料](docs/presentations/2026-11-practical-review-100.md)
- [100件の課題・結果・詳細設計・再検証](benchmarks/practical-review-100/2026-11-05/README.md)
- [実験・課題の一覧](benchmarks/README.md)
- [過去の説明資料・図](docs/presentations/README.md)
- [従来の開発用ルール](AGENTS.md) / [従来の開発用実行系の配布状況](PORTABLE_EXECUTION_READINESS_JA.md)

従来のRust開発用Host/Routerや研究環境全体は、このCSV/JSONアプリとは別です。過去の課題・結果・実行記録は保持しています。

## ライセンス

公開ソースは[MIT License](LICENSE)。公開ファイルのSHA-256は[PACKAGE_MANIFEST.json](PACKAGE_MANIFEST.json)に記録しています。第三者の公式課題の出典・ライセンスは[こちら](benchmarks/official-30/THIRD_PARTY_NOTICES.md)を参照してください。
