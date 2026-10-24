# Native sampling revision002

元の`PLAN_JA.md`とrun-001は保全する。run-001は温度0のGemma26で2応答が6144 tokensに達し、最終contentは空だった。思考内の反復を観測したが、それだけで温度・量子化・backend等の根本原因を断定しない。

2件のAPI完了後、追加API未送信の境界で所有controller/serverを停止。旧freezeは修正せず、残りはNOT_RUN。run-001をresumeしない。

ユーザーが求めるのはTask委譲に使えるLocalモデルの運用知識なので、run-002はメーカー推奨のsamplingとnative thinkingを使用する。全Task、messages、schema、scope、validatorsを維持し、102件を実行前にfreezeした。

|モデル|thinking|sampling|
|---|---|---|
|Gemma26|true|temperature=1、top_p=.95、top_k=64|
|Qwen3.5 9B / COD|true|temperature=.6、top_p=.95、top_k=20、min_p=0、presence_penalty=0、repeat_penalty=1|
|Qwen3.5 9B / Office|true|temperature=1、top_p=.95、top_k=20、min_p=0、presence_penalty=1.5、repeat_penalty=1|
|gpt-oss 20B|medium本体、low/high代表6件|temperature=1（installed Ollama modelのdefault）|

共通はnum_ctx=8192、num_predict=6144、seed=20260926、FA1/KVf16。予算は思考と最終回答の合計。生産Workerを変更するものではない。低い予算の運用で適さないことと、モデル自体がその課題を解けないことを分離する。

推奨値の確認元：

- [Google Gemma 4 model card](https://ai.google.dev/gemma/docs/core/model_card_4)
- [Qwen公式Qwen3.5-9B model card](https://huggingface.co/Qwen/Qwen3.5-9B)
- [Ollama thinking API](https://docs.ollama.com/capabilities/thinking)

Qwen公式の推奨出力長は今回の6144より大きい。このPCでの限定予算内の適性を測る試験であり、モデルの最大能力を測ったとは扱わない。

思考レベルとquality/time/resourceの関係は、profile別・Task別に記録する。主評価は厳密なbody/slot契約を維持。全関数出力をそのままcompileして意味テストを通るかの補助診断は、別スコアとしてのみ扱う。
