# 別PCでCodex＋Gemmaを動かせるか — 配布状況の確認

**現時点では、このリポジトリをcloneするだけでは実行できません。運用ルール・課題・結果の公開と、実行ソフトウェアの配布は別です。**

確認対象はOrchestratorMDのmain commit `2f59d8bf6949cd60bb353acb4b2c3bcd0b58bb15`です。目的は研究環境やbenchmarkの完全再現ではなく、利用者のPCでCodex＋Gemmaによる開発workflowを開始できるかの確認です。

## 公開されているもの

- AGENTS.mdによる役割分担、単一責務への分割、最終レビュー、計測に関する方針。
- 独自課題の公開fixture、公式課題の公開入力、結果・usageの安全な集計。
- 実測したworkflowの条件と制約を記載したreport。

## 実行に必要だが配布されていないもの

|必要な配布物|必要になる理由|
|---|---|
|Workerの実装一式（run_workerと参照module）|Ollama呼出し、構造化出力、bounded apply、結果保存を実行するため|
|Router・profile・model/protocol設定|どのTaskをLocalへ送るかと、現在のone-shot/repair0条件を機械的に適用するため|
|Coverage・typed references・handle・scope/hash・formatter guard|AGENTSの文章だけでなくHostが編集権限と検証を強制するため|
|Host所有check runnerと固定check定義|対象repoのacceptance/regression/fmt/clippy/test/check/build等を再現可能に実行するため|
|Planner／Executor／独立Reviewerのprompt・schema・起動adapter|stock Codex CLIとLocalの役割分担・clean fallbackを実装するため|
|依存関係とOS別の導入・起動・診断手順|PC固有の絶対pathやWSL前提をそのまま他PCへ流用しないため|
|小さいno-model／mock検証と起動smoke|インストール後に境界・接続・結果保存が動くことを確認するため|
|対象repositoryへのTask作成例|研究用New-Concept-OS固有の型・check・regionを、利用者のrepo向けに準備するため|

元の開発環境にある実装と、公開GitHubの配布範囲は一致していません。custom ZIPにも元のHost/Router実行系全体は含まれていません。

## 任意のPCに対する意味

同じGPU・driver・環境hashを要求する必要はありません。一方で、対応OS、Codex CLIとOllamaの動作、モデルの実行資源、Rust等の対象言語toolchain、隔離/validation手段は導入要件として定義する必要があります。全PC・全OSで動くと検証済みではありません。利用者の認証情報は各PCで設定し、公開packageへ含めません。

今後の配布packageでは、既存実装を実行に必要な依存と一緒に切り出し、PC固有pathを設定化し、最小の起動例を一つの手順で通す必要があります。その際もHost guardを省略した簡易版を、検証済みbounded workflowと同等とは扱いません。

## 今回実施した範囲

公開repositoryのファイルと元環境の配布範囲を照合しました。この更新は配布状況の文書化だけで、新しいWorkerの実装やインストール、認証、provider/Local生成を実行したものではありません。

旧の結果・Task・STOP・Production Routerは変更していません。公式解決率やCredits削減の結論も変えていません。研究用の追加入力ZIPと環境fingerprintの公開は、この確認の目的とは別なので実施しません。

**判定: PORTABLE_RUNTIME_PACKAGE_INCOMPLETE**

