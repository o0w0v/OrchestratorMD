# レビュー判断と追加レビューの比較

セットID: `adaptive-reviewer-escalation`

課題数: 8。個別記録あり: 8、個別記録未確認: 0。

[全セット一覧](../INDEX.md) / [課題定義JSON](adaptive-reviewer-escalation.json) / [結果と根拠のJSON](../results/adaptive-reviewer-escalation.json) / [判定の読み方](../README.md#判定の読み方)

各結果はこのセットの保存記録に対応します。収録外の別runの結果を新たに代入していません。SHA-256が記録されている結果は課題定義と照合し、それ以外は実行キー・ディレクトリ・同一セット内の一意のIDによる対応として表示しています。元の記録が過去の工程を再利用している場合、独立した再実行の結果とは扱わないでください。

参考の実験レポート: [RESULTS_JA.md](../reports/adaptive-reviewer-escalation/RESULTS_JA.md)

**実験で固定した設定**（実際の結果・モデル情報は各記録を参照）

```json
[
  {
    "effort": "xhigh",
    "speed": "Standard"
  }
]
```

| 課題ID | 内容 | 個別記録 |
| --- | --- | --- |
| [ARE-001](#are-001) | Memory occupancy gauge in basis points | 記録あり |
| [ARE-002](#are-002) | Consecutive audit source run compression | 記録あり |
| [ARE-003](#are-003) | Observed direct-child RSS totals | 記録あり |
| [ARE-004](#are-004) | Occurrence-aware shared evidence | 記録あり |
| [ARE-005](#are-005) | Nearest-rank recorded latency percentile | 記録あり |
| [ARE-006](#are-006) | Stable event grouping with merged exact evidence | 記録あり |
| [ARE-007](#are-007) | Latest intent verification projection | 記録あり |
| [ARE-008](#are-008) | Observation freshness with explicit future clock state | 記録あり |

<a id="are-001"></a>
## ARE-001

Memory occupancy gauge in basis points

元のtask_id: `ARE-001`。初期ファイル数: 30。

**課題・インターフェース**

Implement memory_basis_points(&Memory) -> Option<u16>. Return None if total is zero or available > total. Otherwise round used/total * 10000 to nearest integer, exact halves upward, without overflow for every u64 input. Range 0..=10000. This is a display gauge, not an event threshold or policy decision.

取り出し方:

```sh
python materialize_task.py --set adaptive-reviewer-escalation --task ARE-001 --output work/ARE-001
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| レビュー判断 | review_arm=always61 | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-5ea2f441bc22e2](#r-5ea2f441bc22e2) |
| レビュー判断 | review_arm=primary | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-1d79642bea170d](#r-1d79642bea170d) |
| コードの検証 | 記録に条件の明記なし | — | — | — | true | — | — | [R-26a822ebf458c7](#r-26a822ebf458c7) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-5ea2f441bc22e2"></a>
### 根拠 R-5ea2f441bc22e2

- 対応方法: 同一セット・課題IDによる対応
- 出典: `summaries/cases.json` / 位置: `/0/arms/always61`
- 出典ファイルのSHA-256: `58efbbedcd597b93316b683e5c36fb0b3b4beed7f986328daf62cff296aa8e23`
- [抽出した測定値・他の工程の記録](../results/adaptive-reviewer-escalation.json)

<a id="r-1d79642bea170d"></a>
### 根拠 R-1d79642bea170d

- 対応方法: 同一セット・課題IDによる対応
- 出典: `summaries/cases.json` / 位置: `/0/arms/primary`
- 出典ファイルのSHA-256: `58efbbedcd597b93316b683e5c36fb0b3b4beed7f986328daf62cff296aa8e23`
- [抽出した測定値・他の工程の記録](../results/adaptive-reviewer-escalation.json)

<a id="r-26a822ebf458c7"></a>
### 根拠 R-26a822ebf458c7

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `runs/ARE-001/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `b9163365d60d6d891feae1d69f386aa068e56122908845005cef4e5605b902cb`
- [抽出した測定値・他の工程の記録](../results/adaptive-reviewer-escalation.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": null,
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="are-002"></a>
## ARE-002

Consecutive audit source run compression

元のtask_id: `ARE-002`。初期ファイル数: 30。

**課題・インターフェース**

Implement source_runs(records) returning consecutive equal-source runs as (source, start_index, end_exclusive). Preserve chronological input order, include empty source strings, compare case-sensitively. Nonadjacent equal sources remain separate. Empty input -> empty result. No sorting or deduplication across runs.

取り出し方:

```sh
python materialize_task.py --set adaptive-reviewer-escalation --task ARE-002 --output work/ARE-002
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| レビュー判断 | review_arm=always61 | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-e2ee0f1c8e8a6e](#r-e2ee0f1c8e8a6e) |
| レビュー判断 | review_arm=primary | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-95a36107197f2e](#r-95a36107197f2e) |
| コードの検証 | 記録に条件の明記なし | — | — | — | true | — | — | [R-880fd7a71db92e](#r-880fd7a71db92e) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-e2ee0f1c8e8a6e"></a>
### 根拠 R-e2ee0f1c8e8a6e

- 対応方法: 同一セット・課題IDによる対応
- 出典: `summaries/cases.json` / 位置: `/1/arms/always61`
- 出典ファイルのSHA-256: `58efbbedcd597b93316b683e5c36fb0b3b4beed7f986328daf62cff296aa8e23`
- [抽出した測定値・他の工程の記録](../results/adaptive-reviewer-escalation.json)

<a id="r-95a36107197f2e"></a>
### 根拠 R-95a36107197f2e

- 対応方法: 同一セット・課題IDによる対応
- 出典: `summaries/cases.json` / 位置: `/1/arms/primary`
- 出典ファイルのSHA-256: `58efbbedcd597b93316b683e5c36fb0b3b4beed7f986328daf62cff296aa8e23`
- [抽出した測定値・他の工程の記録](../results/adaptive-reviewer-escalation.json)

<a id="r-880fd7a71db92e"></a>
### 根拠 R-880fd7a71db92e

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `runs/ARE-002/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `5bccb3b8025a3a1cea8eaab5d764c5bc38bd72569ec5d241f64d978e3d611d17`
- [抽出した測定値・他の工程の記録](../results/adaptive-reviewer-escalation.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": null,
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="are-003"></a>
## ARE-003

Observed direct-child RSS totals

元のtask_id: `ARE-003`。初期ファイル数: 30。

**課題・インターフェース**

Implement child_rss_by_parent(rows) as ascending parent PID -> sum of RSS in supplied child rows. Exclude self-parent rows and parent_pid=0. Count duplicate rows separately because this is a row aggregate, not PID identity resolution. Saturate u64 additions. Include a parent with zero total if a matching zero-RSS row exists. Do not infer missing processes, traverse ancestors or mutate input.

取り出し方:

```sh
python materialize_task.py --set adaptive-reviewer-escalation --task ARE-003 --output work/ARE-003
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| レビュー判断 | review_arm=always61 | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-66ec43808b47bd](#r-66ec43808b47bd) |
| レビュー判断 | review_arm=primary | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-1bbd263a590a46](#r-1bbd263a590a46) |
| コードの検証 | 記録に条件の明記なし | — | — | — | true | — | — | [R-ae91a68c814802](#r-ae91a68c814802) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-66ec43808b47bd"></a>
### 根拠 R-66ec43808b47bd

- 対応方法: 同一セット・課題IDによる対応
- 出典: `summaries/cases.json` / 位置: `/2/arms/always61`
- 出典ファイルのSHA-256: `58efbbedcd597b93316b683e5c36fb0b3b4beed7f986328daf62cff296aa8e23`
- [抽出した測定値・他の工程の記録](../results/adaptive-reviewer-escalation.json)

<a id="r-1bbd263a590a46"></a>
### 根拠 R-1bbd263a590a46

- 対応方法: 同一セット・課題IDによる対応
- 出典: `summaries/cases.json` / 位置: `/2/arms/primary`
- 出典ファイルのSHA-256: `58efbbedcd597b93316b683e5c36fb0b3b4beed7f986328daf62cff296aa8e23`
- [抽出した測定値・他の工程の記録](../results/adaptive-reviewer-escalation.json)

<a id="r-ae91a68c814802"></a>
### 根拠 R-ae91a68c814802

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `runs/ARE-003/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `2e495292adaa400c662cbc3dfb0f67255bdb00a845b718e29578f3d6fd41373e`
- [抽出した測定値・他の工程の記録](../results/adaptive-reviewer-escalation.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": null,
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="are-004"></a>
## ARE-004

Occurrence-aware shared evidence

元のtask_id: `ARE-004`。初期ファイル数: 30。

**課題・インターフェース**

Implement shared_evidence(left, right). Return the multiset intersection of exact UTF-8 strings, in left occurrence order. A right occurrence can be consumed at most once. No trim, case folding, sorting, or input modification. Empty string is a normal value. Output each value min(left_count,right_count) times.

取り出し方:

```sh
python materialize_task.py --set adaptive-reviewer-escalation --task ARE-004 --output work/ARE-004
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| レビュー判断 | review_arm=always61 | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-0d3e4954bdd039](#r-0d3e4954bdd039) |
| レビュー判断 | review_arm=primary | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-ca547d218acdea](#r-ca547d218acdea) |
| コードの検証 | 記録に条件の明記なし | — | — | — | true | — | — | [R-701ae3cadc96c7](#r-701ae3cadc96c7) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-0d3e4954bdd039"></a>
### 根拠 R-0d3e4954bdd039

- 対応方法: 同一セット・課題IDによる対応
- 出典: `summaries/cases.json` / 位置: `/3/arms/always61`
- 出典ファイルのSHA-256: `58efbbedcd597b93316b683e5c36fb0b3b4beed7f986328daf62cff296aa8e23`
- [抽出した測定値・他の工程の記録](../results/adaptive-reviewer-escalation.json)

<a id="r-ca547d218acdea"></a>
### 根拠 R-ca547d218acdea

- 対応方法: 同一セット・課題IDによる対応
- 出典: `summaries/cases.json` / 位置: `/3/arms/primary`
- 出典ファイルのSHA-256: `58efbbedcd597b93316b683e5c36fb0b3b4beed7f986328daf62cff296aa8e23`
- [抽出した測定値・他の工程の記録](../results/adaptive-reviewer-escalation.json)

<a id="r-701ae3cadc96c7"></a>
### 根拠 R-701ae3cadc96c7

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `runs/ARE-004/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `d39abe9a052426df5bf9d5a68cbd574e8abdb70d2874ee89f399e811671c96ac`
- [抽出した測定値・他の工程の記録](../results/adaptive-reviewer-escalation.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": null,
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="are-005"></a>
## ARE-005

Nearest-rank recorded latency percentile

元のtask_id: `ARE-005`。初期ファイル数: 30。

**課題・インターフェース**

Implement latency_percentile(samples, percentile). Empty input or percentile outside 1..=100 -> None. Otherwise sort a private copy of u128 latency samples and return nearest-rank: 1-based ceil(percentile * N / 100). Retain duplicate samples; do not interpolate, narrow u128, or change original input. No overflow in rank calculation.

取り出し方:

```sh
python materialize_task.py --set adaptive-reviewer-escalation --task ARE-005 --output work/ARE-005
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| レビュー判断 | review_arm=always61 | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-c53e4f5f25561c](#r-c53e4f5f25561c) |
| レビュー判断 | review_arm=primary | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-47fea7446c8dac](#r-47fea7446c8dac) |
| コードの検証 | 記録に条件の明記なし | — | — | — | true | — | — | [R-db650a879ebacf](#r-db650a879ebacf) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-c53e4f5f25561c"></a>
### 根拠 R-c53e4f5f25561c

- 対応方法: 同一セット・課題IDによる対応
- 出典: `summaries/cases.json` / 位置: `/4/arms/always61`
- 出典ファイルのSHA-256: `58efbbedcd597b93316b683e5c36fb0b3b4beed7f986328daf62cff296aa8e23`
- [抽出した測定値・他の工程の記録](../results/adaptive-reviewer-escalation.json)

<a id="r-47fea7446c8dac"></a>
### 根拠 R-47fea7446c8dac

- 対応方法: 同一セット・課題IDによる対応
- 出典: `summaries/cases.json` / 位置: `/4/arms/primary`
- 出典ファイルのSHA-256: `58efbbedcd597b93316b683e5c36fb0b3b4beed7f986328daf62cff296aa8e23`
- [抽出した測定値・他の工程の記録](../results/adaptive-reviewer-escalation.json)

<a id="r-db650a879ebacf"></a>
### 根拠 R-db650a879ebacf

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `runs/ARE-005/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `3151dbc23b4fd6848e50cb215388998a177be1b3179faf9300e70c01924f937e`
- [抽出した測定値・他の工程の記録](../results/adaptive-reviewer-escalation.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": null,
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="are-006"></a>
## ARE-006

Stable event grouping with merged exact evidence

元のtask_id: `ARE-006`。初期ファイル数: 30。

**課題・インターフェース**

Implement merge_events(events) for a display-only projection. Group by (id, kind, target) exact equality, not by id alone. Groups appear at first occurrence position. For each group, retain unique exact evidence strings in first-seen order across all matching events, including removing duplicates within its first row. Preserve first row id/kind/target. Empty input empty. No policy changes or mutation of input.

取り出し方:

```sh
python materialize_task.py --set adaptive-reviewer-escalation --task ARE-006 --output work/ARE-006
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| レビュー判断 | review_arm=always61 | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-0944bb0a7fab3b](#r-0944bb0a7fab3b) |
| レビュー判断 | review_arm=primary | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-91b5e9f0cdfb68](#r-91b5e9f0cdfb68) |
| コードの検証 | 記録に条件の明記なし | — | — | — | true | — | — | [R-dc27fb701f86ea](#r-dc27fb701f86ea) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-0944bb0a7fab3b"></a>
### 根拠 R-0944bb0a7fab3b

- 対応方法: 同一セット・課題IDによる対応
- 出典: `summaries/cases.json` / 位置: `/5/arms/always61`
- 出典ファイルのSHA-256: `58efbbedcd597b93316b683e5c36fb0b3b4beed7f986328daf62cff296aa8e23`
- [抽出した測定値・他の工程の記録](../results/adaptive-reviewer-escalation.json)

<a id="r-91b5e9f0cdfb68"></a>
### 根拠 R-91b5e9f0cdfb68

- 対応方法: 同一セット・課題IDによる対応
- 出典: `summaries/cases.json` / 位置: `/5/arms/primary`
- 出典ファイルのSHA-256: `58efbbedcd597b93316b683e5c36fb0b3b4beed7f986328daf62cff296aa8e23`
- [抽出した測定値・他の工程の記録](../results/adaptive-reviewer-escalation.json)

<a id="r-dc27fb701f86ea"></a>
### 根拠 R-dc27fb701f86ea

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `runs/ARE-006/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `ce30beb0a64632a41c51b629e320c1a061af99d0a274d9f230353580a0f336d6`
- [抽出した測定値・他の工程の記録](../results/adaptive-reviewer-escalation.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": null,
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="are-007"></a>
## ARE-007

Latest intent verification projection

元のtask_id: `ARE-007`。初期ファイル数: 30。

**課題・インターフェース**

Implement latest_verification(records, intent_id) -> Option<bool>. Match exact intent.id. Select the row with greatest observed_unix_ms, breaking equal timestamps toward the last input row. Then project selected row.verification.passed; if the selected row has no verification return None, even when older rows were verified. No match -> None. Input need not be sorted. This is display data, not authorization.

取り出し方:

```sh
python materialize_task.py --set adaptive-reviewer-escalation --task ARE-007 --output work/ARE-007
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| レビュー判断 | review_arm=always61 | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-21c3575b53c098](#r-21c3575b53c098) |
| レビュー判断 | review_arm=primary | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-03e17400c4379b](#r-03e17400c4379b) |
| コードの検証 | 記録に条件の明記なし | — | — | — | true | — | — | [R-5a9dc89d5480fc](#r-5a9dc89d5480fc) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-21c3575b53c098"></a>
### 根拠 R-21c3575b53c098

- 対応方法: 同一セット・課題IDによる対応
- 出典: `summaries/cases.json` / 位置: `/6/arms/always61`
- 出典ファイルのSHA-256: `58efbbedcd597b93316b683e5c36fb0b3b4beed7f986328daf62cff296aa8e23`
- [抽出した測定値・他の工程の記録](../results/adaptive-reviewer-escalation.json)

<a id="r-03e17400c4379b"></a>
### 根拠 R-03e17400c4379b

- 対応方法: 同一セット・課題IDによる対応
- 出典: `summaries/cases.json` / 位置: `/6/arms/primary`
- 出典ファイルのSHA-256: `58efbbedcd597b93316b683e5c36fb0b3b4beed7f986328daf62cff296aa8e23`
- [抽出した測定値・他の工程の記録](../results/adaptive-reviewer-escalation.json)

<a id="r-5a9dc89d5480fc"></a>
### 根拠 R-5a9dc89d5480fc

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `runs/ARE-007/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `aa0ae41970f43d1efee89f82ea7716c8e762b53959e258b4f82d9d81630a472e`
- [抽出した測定値・他の工程の記録](../results/adaptive-reviewer-escalation.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": null,
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="are-008"></a>
## ARE-008

Observation freshness with explicit future clock state

元のtask_id: `ARE-008`。初期ファイル数: 30。

**課題・インターフェース**

Implement freshness(observed_ms, now_ms, ttl_ms) returning Future for observed > now; otherwise Fresh if age <= ttl_ms inclusive, else Stale. ttl_ms is u64 but timestamps u128; never narrow age. ttl zero means only identical timestamps are Fresh. No wall clock reads and no expiry policy changes.

取り出し方:

```sh
python materialize_task.py --set adaptive-reviewer-escalation --task ARE-008 --output work/ARE-008
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| レビュー判断 | review_arm=always61 | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-615dcc1b94b6a5](#r-615dcc1b94b6a5) |
| レビュー判断 | review_arm=primary | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-84ac5a6b5735d7](#r-84ac5a6b5735d7) |
| コードの検証 | 記録に条件の明記なし | — | — | — | true | — | — | [R-908af1b5f9393e](#r-908af1b5f9393e) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-615dcc1b94b6a5"></a>
### 根拠 R-615dcc1b94b6a5

- 対応方法: 同一セット・課題IDによる対応
- 出典: `summaries/cases.json` / 位置: `/7/arms/always61`
- 出典ファイルのSHA-256: `58efbbedcd597b93316b683e5c36fb0b3b4beed7f986328daf62cff296aa8e23`
- [抽出した測定値・他の工程の記録](../results/adaptive-reviewer-escalation.json)

<a id="r-84ac5a6b5735d7"></a>
### 根拠 R-84ac5a6b5735d7

- 対応方法: 同一セット・課題IDによる対応
- 出典: `summaries/cases.json` / 位置: `/7/arms/primary`
- 出典ファイルのSHA-256: `58efbbedcd597b93316b683e5c36fb0b3b4beed7f986328daf62cff296aa8e23`
- [抽出した測定値・他の工程の記録](../results/adaptive-reviewer-escalation.json)

<a id="r-908af1b5f9393e"></a>
### 根拠 R-908af1b5f9393e

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `runs/ARE-008/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `8e85c40229368a35df87b1583818062b252ccbbf9e60666b942341d8ca69053c`
- [抽出した測定値・他の工程の記録](../results/adaptive-reviewer-escalation.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": null,
  "acceptance_criteria": null,
  "checks": []
}
```

</details>
