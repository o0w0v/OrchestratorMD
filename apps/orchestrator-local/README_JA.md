# Orchestrator Local 0.1.0 — Windows向け初期版

ChatGPT/Codexデスクトップから、既存のGemma4 26BへCSV/JSON作業を依頼するローカル版。会話側のモデルが元条件で確認し、そのまま採用または必要箇所だけ差分修正して保存する。小さい仕事は会話側で直接作って保存できる。別のCloud API呼出しは追加しない。

## この版でできること

CSV/JSONの集計・整形・在庫引当などを、いつもの会話からLocalへ依頼し、確認して保存する。使える成果物は原物を採用し、利用に支障がある誤りだけ差分修正する。研究用の実行環境全体を再現するものではない。

Windows、Python 3.11以降、既存Ollamaで`gemma4:26b`を実行できるPCが対象。RTX 3080 10GBを搭載したWindows PCで実機確認したが、別PC・全GPUでの動作を確認したものではない。モデルの重み、Ollama、Pythonは配布に含まない。macOS/Linux、ブラウザだけの利用はこの版の動作確認対象外。

## 導入

リポジトリをcloneまたはZIPで展開し、`apps/orchestrator-local`フォルダをPowerShellで開く。

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.lock
.\.venv\Scripts\python.exe setup_local.py
.\.venv\Scripts\python.exe -X utf8 -B -m unittest discover -s tests -v
.\.venv\Scripts\python.exe setup_local.py --register
.\start-service.ps1
```

既存OllamaがPATHで見つからなければ、最初の`setup_local.py`に`--ollama-exe`で実ファイルを指定する。標準的な配置例は`--ollama-exe "$env:LOCALAPPDATA\Programs\Ollama\ollama.exe"`。モデルを別フォルダに置いている場合だけ`--ollama-models "既存のモデルフォルダ"`も指定する。モデルの自動ダウンロードは行わない。

接続登録後、デスクトップアプリの設定からMCPを再起動し、新しい会話を開く。必要ならアプリを再起動する。接続の仕組みは[公式のデスクトップMCP説明](https://learn.chatgpt.com/docs/extend/mcp)を参照。アカウントやクライアントでLocal MCPが使えることが前提となる。

PowerShellがスクリプト実行を制限する環境では、そのPCの方針に従って実行する。MCP接続登録だけでは独立実行サービスは起動しない。

## 最初の依頼

新しい会話で次を入力する。サンプルはセットアップ時に利用者のinboxへコピーされる。

```text
$orchestrator-local
inboxのinventory-example.jsonを使って、注文ID順に在庫を引き当て、一覧CSVと短い共有文を作ってください。
取消はEXCLUDEDで引当・不足0。対象は引当=min(注文数,残在庫)//lot*lot、不足=注文数-引当とし、引当数だけ在庫を減らします。
数量と件数を区別し、不足がある場合は資料に基づく実際の原因を書いてください。使える成果物はそのまま採用し、必要な箇所だけ直してください。
```

普段の入力は、許可したinboxに置くCSV/JSON/TXT/MD、または会話で読める添付の内容。添付からローカルファイルを自動取得できることは前提にしない。読める内容をinputsへ渡すか、inboxを使う。xlsx/docxのGUI操作、任意コード実行、Web調査はこの実装の対象外。

出力はジョブごとに`artifact.json`、`data.json`、`report.md`、指定したCSV。追加修正は新しいresult版へ保存されるので前のファイルも残る。保存先は`local_status`や完了した保存ツールの結果から分かる。

## 保存先・起動・接続設定

既定の入力フォルダは利用者の`Documents/Codex/OrchestratorLocal/inbox`、結果は同じデータフォルダの`jobs`。厳密な場所はセットアップ結果と`local_status`に表示される。PC固有のパスは`local-settings.json`に作り、GitHubには送らない。

`--register`はこのMCPと同名Skillだけを追加し、既存config.tomlはバックアップする。同名の異なる接続/Skillを上書きしない。`local-settings.json`を変更すると保存先や許可入力フォルダを調整できる。接続設定はstdio、コマンドはこのvenvのPython、引数は`serve.py --config local-settings.json`の絶対パス。登録後はアプリのMCP接続を再起動する。

`start-service.ps1`は独立した実行サービスを非表示で起動する。待機中はモデル生成をしない。MCP接続を閉じてもこのサービスが作業を続ける。手動起動設定ではPC再起動後にこのスクリプトを実行する。停止は`.venv\Scripts\python.exe service_entry.py --stop`。アプリを閉じることと、作業を中止することは別であり、中止したいジョブには`cancel_job`を使う。

ログイン時の自動起動を選ぶ場合は`enable-startup.ps1`、解除は`enable-startup.ps1 -Disable`。自分のユーザーのStartupに専用ショートカットを作る。他の自動起動項目は変更しない。

自動起動は既定では登録しない。登録後はコード・venvのフォルダを移動しないこと。絶対パスが変わる場合は、元の場所で登録解除してから新しい場所で登録する。

`plugin.json`と`mcp.json`は同じ部品の配布用manifest。この初期版のWindowsパッケージはvenvとローカル設定を作成してから使う。ディレクトリへ公開・審査済みのプラグインとは別である。

## 処理と確認

- `start_job`は元依頼・合意条件、inputs/input_paths、任意data_schema/csv_exportsを受け取る。同じrequest_keyと入力を再送しても二重生成しない。別の依頼には別key。
- 生成中は`get_job(wait_seconds=25)`。workerは会話のstdio接続から独立して動作し、ジョブはSQLiteへ保存する。アプリやOSがworkerも終了した場合はINTERRUPTEDとし、自動再生成しない。
- 候補は`CANDIDATE_READY`。会話側が元資料で確認して`finalize_job`へACCEPTまたはPATCHを返すまで成果物として採用しない。
- PATCHはJSON Pointer、厳密なbefore/after、利用への影響を指定。重複・親子の重なり・古いhash・形式違反を拒否し、全差分が有効な時だけ保存する。
- ユーザー指定の追加修正は`amend_result`で対象だけ変更。新しい版を作り、Local生成を増やさない。
- `cancel_job`はそのジョブのHTTP接続を閉じる。他のOllama processは止めない。GPU上の実処理停止時刻はOllama側にも依存する。

保存時のCSVはUTF-8 BOM付き。数式として解釈され得る文字列には先頭アポストロフィを付ける。元の値はJSONに保持する。CSVの数値文字列を入力時に推測変換しない。

## 費用・実験との違い

会話側のモデルはアプリで選択したモデル。プログラムはSol/Luna/Terraを別に呼ばないため、会話側のモデル・effortを固定した実験の再現ではない。会話側の消費Creditsはnull、Local実測tokensと時間だけを記録し、節約額を推測しない。

Gemmaは既存digest・native thinking・ctx65536/output32768・seed/samplingを使用。業務版は既存Ollamaを再利用し、必要な場合だけ所有serverを起動、モデルを5分保持する。100件実験の「毎回fresh load/停止」と条件が異なる。過去の実験成績を業務の品質保証とは扱わない。

既定のdigestは`08ae7ec1744bd7f451c4a530afb39d2673ad9d07a8369b8a33a3613b41212a68`。同じtagでも手元のモデルが別digestなら生成せず停止する。別モデル版を使う場合は利用者が`local-settings.json`を明示変更する必要があり、その構成はこの版の実機確認とは別になる。

入力は許可フォルダ内のファイルに限り、サイズ/形式とLocal入力上限を確認する。候補にshell/tool権限を与えない。形式検証は意味の正しさの証明ではない。会話側による確認が必要。

入力資料と候補は、確認のため会話側にも返る。完全オフラインの構成ではない。設定、入力、SQLite、生成物、ログ、認証情報を公開リポジトリへ追加しない。この公開ソースに利用者のデータや認証情報は含めていない。

## 更新・登録解除

更新前に`service_entry.py --stop`で実行サービスを正常停止し、以下の方法で現在の版の登録を解除する。更新後に依存関係の導入・テスト・登録・起動を行う。自動アップデーターはない。

```powershell
.\.venv\Scripts\python.exe service_entry.py --stop
.\enable-startup.ps1 -Disable
.\.venv\Scripts\python.exe setup_local.py --unregister
```

この導入先と一致するMCPだけを外し、同梱版と一致するSkillをデータフォルダのruntimeへ保全移動する。既存configはバックアップする。別の導入先や利用者が変更したSkillは自動削除せず停止するので、表示内容を確認して手動で整理する。保存済み成果物・inbox・Ollama・モデルは削除しない。解除後はアプリのMCP接続も再起動する。

## 実装と確認

`orchestrator_local/core.py`がジョブ・入力・差分・保存、`service.py`が独立した実行サービス、`worker.py`がOllama生成と中止、`server.py`がMCPの8ツール。Skillは`skills/orchestrator-local/SKILL.md`。

テストは偽Ollamaを用いたstdio MCP→worker→確認・保存、再接続、二重依頼、中止、失敗、パス制限、差分原子性を確認する。実モデルの接続確認は別に小さい1件を使い、実験用100件は再実行しない。

公式仕様：[デスクトップMCP](https://learn.chatgpt.com/docs/extend/mcp)、[SkillとMCP](https://developers.openai.com/plugins/concepts/skills)、[Ollama chat API](https://docs.ollama.com/api/chat)。

公開ソースのライセンスは[MIT](LICENSE)。動作確認の範囲は[VALIDATION.md](VALIDATION.md)、構成図は[DESIGN_JA.md](DESIGN_JA.md)を参照。
