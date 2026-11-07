# 公開物と再現できる範囲

この公開版は完了済み100件の検証資料。モデルを再呼出しせずに、全成果物のデータ採点・差分適用・会計増分・ファイルhashを再確認できる。現在のモデルを同じ条件で再実行する機能や同じ回答の再生成保証は含まない。

## オフライン確認

Python 3標準ライブラリだけで、このディレクトリで実行する。

```sh
python verify.py
```

100件200成果物を保存された期待値と再比較し、reference.pyでも元添付から期待値を再計算。12件のPATCHを初期候補へ再適用し、最終成果物と照合する。386件の増分ledgerをsession順に照合し、各sessionの増分合計＝最後の累積、role別集計とCredits既知小計を確認する。文章の新しい採点・推論・通信はしない。

## 含むもの

100件の公開5発言対話、元添付と指定schema、初期/最終成果物、可視のSol確認応答、12PATCH、全件採点、role別tokens、386件usage metadata、集計・資源・時間、事前計画と設定、実行コードの履歴snapshot、元証跡hashと公開版hash。

正解データは研究中はprivateに保ち、全採否seal後だけHost採点に使った。公開版では各case内のexpected_data_after_routing_sealedとして配布する。採否や成果物を正解で修正し直したことはない。

## 公開用の加工

原本は不変。公開版はallowlistで抽出し、端末の絶対パスをsource-file:/host-file:識別子に置換、JSONを整形した。非公開思考本文、CLIセッション全文、認証設定、実行バイナリ、モデル重み、個人端末の全ファイル一覧は含めない。公開対話や成果物の業務内容は変更していない。PACKAGE_MANIFEST.jsonが公開版hash、SOURCE_PROVENANCE.jsonが元ファイルhashと加工方法。元freezeのhashは公開版byte列のhashとは区別する。

integrity/は絶対パスを置換した元sealの参照コピー。sealが参照する非公開raw全体を公開した証明ではない。元Host監査14304チェックの成功は記録するが、この配布物だけで元raw全体を再監査できるとは言わない。SESSION_COUNTER_EVIDENCEはusage metadataだけで思考本文は含まない。

## 実行コード

source-snapshot/*.py.txtは凍結時コードの参照用。runtimeは端末固有のverified capture、CLI、Ollama helperと保全履歴に依存するため、この配布だけで起動できない。scenario.pyには旧試験由来の未使用関数が残る。今回の実行経路はrunner.pyとpolicy.pyのSOL_CONTINUE/PRACTICALだけで、Luna/Terra処理を測った試験ではない。

replay/のpolicy/protocol/reference/task_factoryだけを検証に使用する。source-snapshotのlaunch/runnerを起動する必要はない。別PCでの新規実行を整備済みと呼ばない。

## 会計

CLIのusageは会話session累積。INCREMENTAL_USAGEは前counterとの差分。cacheはInput、reasoningはOutputの内数。研究採点AI0回、Bの最終Sol確認費は運用費へ含む。不明消費2件、準備chat・手修正実時間・電力はnull。study unique小計は219.55402 Credits、方式別比較和303.74824との差は共有相談71.34362＋共有small12.85060。実請求の全額計測ではない。

事前COST_AND_SCOPEのpublish_GitHub=falseは実験中の凍結条件を保存したもの。完了後の今回のユーザー依頼で、この別の公開版を作成した。凍結条件の書き換えは行っていない。今回の公開に伴う新規モデル呼出しは0。
