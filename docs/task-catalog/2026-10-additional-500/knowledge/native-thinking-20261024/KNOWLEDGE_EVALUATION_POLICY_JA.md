# Local LLMの委譲先を選ぶための評価方針

目的は「総合で一番のモデル」を選ぶことではなく、「このTaskなら、どのモデル・設定へ渡すとよいか」を知識として保存すること。

## 思考機能を使う

- 対応する全候補でnative thinkingを有効にする。effortを選べる場合は、対応enumを実環境で確認して使う。
- 速度を揃えるために全モデルへthink=falseを強制しない。
- メーカー推奨samplingと、このPCで扱える思考・最終回答の予算を実行前に固定する。設定差を明示し、条件が完全に同一とは呼ばない。
- 過去の思考なし結果も保存し、どの設定で得た結果かを区別する。
- 設定を変えて再試験する場合は別profile/runとし、前の失敗を成功へ上書きしない。

## 1件のナレッジに残すもの

|項目|例|
|---|---|
|Taskの条件|重なった区間を統合して空白を求める。半開区間、空区間、範囲外の予約を扱う|
|変更範囲と入力|関数本体のみ。interfaceと公開referenceをHostが固定|
|モデルと設定|digest、量子化、runtime、thinking/effort、sampling、context/output budget|
|完了の種類|契約PASS、形式違反、compile失敗、意味テスト失敗、出力上限、infra|
|時間と消費|初回load、API wall、native eval duration、Host検証時間、native tokens|
|資源|GPU全体使用量と背景使用量、空きVRAM、Host RAM、Ollama/backend memory、offload|
|根拠|Taskとrequestのhash、raw response、検証結果への参照|
|適用範囲|今回の具体例で確認済み。未測定の同類Taskは別に検証する|

## 成功と未完了を分ける

最終contentを同じ固定検証へ渡す。思考textの存在自体は失敗ではない。

OUTPUT_LIMITは「この予算で最終回答を完了できなかった」結果。意味テストFAILと混ぜず、モデルがその問題を解く能力を持たないとは断定しない。関数全体を返してしまった場合も、body契約の不適合と実装内容の正誤を別に記録する。補助診断で意味テストが通っても、元の厳密な契約PASSへ昇格しない。

CUDA・API・backend・Host検証器の障害は、モデルの実装品質と分離する。回復時は障害証拠と別attemptを保存する。

## 割り振りの判断

同じTaskで合格した候補の品質・時間・資源を比較する。複数モデルの合格例を事後に足して、実装済みRouterの成績とは呼ばない。新しいrouting ruleやモデル追加は、この知識を踏まえた別変更にする。

思考tokensを含むOllama native usageを記録する。Local tokensをCodex tokens savedへ換算しない。Codex作業削減を主張するには、別のworkflow比較と実usageが必要。

Officeは今回、発行済みtyped slotへの回答とHostのファイル生成・native renderを評価する。自由なOffice GUI操作や業務全体の完成品質とは区別する。

モデルの機能を使う方針は、任意shell・自由なHost読取・無制限の実行権限を与えることではない。生成コードの隔離、固定検証、旧証拠の保全を維持する。
