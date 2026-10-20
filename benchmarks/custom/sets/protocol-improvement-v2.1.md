# 実装・検証手順の比較 / protocol-improvement-v2.1

セットID: `protocol-improvement-v2.1`

課題数: 9。個別記録あり: 9、個別記録未確認: 0。

[全セット一覧](../INDEX.md) / [課題定義JSON](protocol-improvement-v2.1.json) / [結果と根拠のJSON](../results/protocol-improvement-v2.1.json) / [判定の読み方](../README.md#判定の読み方)

各結果はこのセットの保存記録に対応します。収録外の別runの結果を新たに代入していません。SHA-256が記録されている結果は課題定義と照合し、それ以外は実行キー・ディレクトリ・同一セット内の一意のIDによる対応として表示しています。元の記録が過去の工程を再利用している場合、独立した再実行の結果とは扱わないでください。

参考の実験レポート: [RESULTS_JA.md](../reports/protocol-improvement-v2.1/RESULTS_JA.md)

**実験で固定した設定**（実際の結果・モデル情報は各記録を参照）

```json
[
  {
    "model": "gemma4:26b"
  }
]
```

| 課題ID | 内容 | 個別記録 |
| --- | --- | --- |
| [A-001](#a-001) | Add regression coverage that duplicate events do not refresh the FIFO deduplication window. | 記録あり |
| [A-002](#a-002) | Add cache regression coverage that duplicate remember calls do not refresh FIFO order. | 記録あり |
| [A-003](#a-003) | Add regression coverage for the KiB parser lexical and u64 boundaries. | 記録あり |
| [B-001](#b-001) | Support the conventional ncos inspect --help spelling with exactly the existing global help output, without observation. | 記録あり |
| [B-002](#b-002) | Find where memory-pressure evidence is built and append a two-decimal available_percent for CLI/audit readability. | 記録あり |
| [B-003](#b-003) | Append load_per_cpu with two decimals to high-load evidence for CLI/audit readability. | 記録あり |
| [C-001](#c-001) | Extract the existing event deduplication and skill cache behavior into a typed maintenance summary. | 記録あり |
| [C-002](#c-002) | Extract five lexical and numeric facts about the existing KiB value parser. | 記録あり |
| [C-003](#c-003) | Extract five facts about HighLoad event generation and its ordering relative to memory events. | 記録あり |

<a id="a-001"></a>
## A-001

Add regression coverage that duplicate events do not refresh the FIFO deduplication window.

元のtask_id: `PILOT-002`。初期ファイル数: 29。

**課題・インターフェース**

Implement only pilot_dedup_duplicate_does_not_refresh() test body. Event has id, kind, target, evidence; Deduplicator::new and EventFilter::accept are existing APIs.

取り出し方:

```sh
python materialize_task.py --set protocol-improvement-v2.1 --task A-001 --output work/A-001
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | model=gemma4:26b | ESCALATE | ESCALATE | — | false | — | — | [R-14364d6af88884](#r-14364d6af88884) |
| ローカル実装 | model=gemma4:26b | ESCALATE | ESCALATE | — | false | — | — | [R-971f553c36ddb4](#r-971f553c36ddb4) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-14364d6af88884"></a>
### 根拠 R-14364d6af88884

- 対応方法: 同一セット内で一意のtask_idによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/1`
- 出典ファイルのSHA-256: `15ed69c09d40536288d746dbb645bc5ffe04482be6ccba86f827cef54cef9b04`
- [抽出した測定値・他の工程の記録](../results/protocol-improvement-v2.1.json)

<a id="r-971f553c36ddb4"></a>
### 根拠 R-971f553c36ddb4

- 対応方法: 同一セット内で一意のtask_idによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/0`
- 出典ファイルのSHA-256: `15ed69c09d40536288d746dbb645bc5ffe04482be6ccba86f827cef54cef9b04`
- [抽出した測定値・他の工程の記録](../results/protocol-improvement-v2.1.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "capacity 2: accept A and B, reject duplicate A, insert C, B still rejected and A accepted after eviction",
    "same kind but different target is a distinct key",
    "capacity zero accepts the same event repeatedly"
  ],
  "acceptance_criteria": null,
  "checks": [
    {
      "id": "targeted",
      "kind": "test",
      "parser": "rust",
      "cwd": ".",
      "timeout_seconds": 210,
      "required_test_ids": [
        "pilot_dedup_duplicate_does_not_refresh"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "180",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--test",
        "pilot",
        "--",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": ".",
      "timeout_seconds": 210,
      "argv": [
        "cargo",
        "timeout",
        "180",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "fmt",
        "--check"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "clippy",
      "kind": "lint",
      "cwd": ".",
      "timeout_seconds": 210,
      "argv": [
        "cargo",
        "timeout",
        "180",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "clippy",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--all-targets",
        "--",
        "-D",
        "warnings"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "mutation-contract",
      "kind": "lint",
      "cwd": ".",
      "timeout_seconds": 600,
      "argv": null,
      "portability_note": "Original adapter-specific check; use the declared acceptance contract and fixture tests."
    }
  ]
}
```

</details>

<a id="a-002"></a>
## A-002

Add cache regression coverage that duplicate remember calls do not refresh FIFO order.

元のtask_id: `PEX-A02`。初期ファイル数: 30。

**課題・インターフェース**

Implement only protocol_cache_fifo test body using MemorySkills::new, SkillStore::remember/lookup and SkillKey { goal, kind }.

取り出し方:

```sh
python materialize_task.py --set protocol-improvement-v2.1 --task A-002 --output work/A-002
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | model=gemma4:26b | ESCALATE | ESCALATE | — | false | — | — | [R-bd272a8a9726cd](#r-bd272a8a9726cd) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-bd272a8a9726cd"></a>
### 根拠 R-bd272a8a9726cd

- 対応方法: 同一セット内で一意のtask_idによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/2`
- 出典ファイルのSHA-256: `15ed69c09d40536288d746dbb645bc5ffe04482be6ccba86f827cef54cef9b04`
- [抽出した測定値・他の工程の記録](../results/protocol-improvement-v2.1.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Capacity 2: remember A, B, duplicate A, then C; A is evicted while B and C remain.",
    "Keys with equal goal but different EventKind remain distinct.",
    "Capacity zero retains no key."
  ],
  "acceptance_criteria": null,
  "checks": [
    {
      "id": "targeted",
      "kind": "test",
      "parser": "rust",
      "cwd": ".",
      "timeout_seconds": 210,
      "required_test_ids": [
        "protocol_cache_fifo"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "180",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-skills",
        "--test",
        "protocol",
        "--",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": ".",
      "timeout_seconds": 210,
      "argv": [
        "cargo",
        "timeout",
        "180",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "fmt",
        "--check"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "clippy",
      "kind": "lint",
      "cwd": ".",
      "timeout_seconds": 210,
      "argv": [
        "cargo",
        "timeout",
        "180",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "clippy",
        "--offline",
        "--locked",
        "-p",
        "ncos-skills",
        "--all-targets",
        "--",
        "-D",
        "warnings"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "mutation-contract",
      "kind": "lint",
      "cwd": ".",
      "timeout_seconds": 540,
      "argv": null,
      "portability_note": "Original adapter-specific check; use the declared acceptance contract and fixture tests."
    }
  ]
}
```

</details>

<a id="a-003"></a>
## A-003

Add regression coverage for the KiB parser lexical and u64 boundaries.

元のtask_id: `PEX-A03`。初期ファイル数: 30。

**課題・インターフェース**

Implement only protocol_kib_boundaries test body; parse_kib_value(&str) -> Result<u64, String> is unchanged.

取り出し方:

```sh
python materialize_task.py --set protocol-improvement-v2.1 --task A-003 --output work/A-003
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | model=gemma4:26b | ESCALATE | ESCALATE | — | false | — | — | [R-956aafda6bf5f9](#r-956aafda6bf5f9) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-956aafda6bf5f9"></a>
### 根拠 R-956aafda6bf5f9

- 対応方法: 同一セット内で一意のtask_idによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/3`
- 出典ファイルのSHA-256: `15ed69c09d40536288d746dbb645bc5ffe04482be6ccba86f827cef54cef9b04`
- [抽出した測定値・他の工程の記録](../results/protocol-improvement-v2.1.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Whitespace and leading zeros are accepted: \"  0007 kB\\t\" -> 7.",
    "18446744073709551615 kB is accepted; 18446744073709551616 kB returns overflow.",
    "+1 kB returns invalid number; 1 KB returns invalid unit.",
    "1 MB extra returns extra tokens before unit validation."
  ],
  "acceptance_criteria": null,
  "checks": [
    {
      "id": "targeted",
      "kind": "test",
      "parser": "rust",
      "cwd": ".",
      "timeout_seconds": 210,
      "required_test_ids": [
        "protocol_kib_boundaries"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "180",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-observer-linux",
        "--test",
        "protocol",
        "--",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": ".",
      "timeout_seconds": 210,
      "argv": [
        "cargo",
        "timeout",
        "180",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "fmt",
        "--check"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "clippy",
      "kind": "lint",
      "cwd": ".",
      "timeout_seconds": 210,
      "argv": [
        "cargo",
        "timeout",
        "180",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "clippy",
        "--offline",
        "--locked",
        "-p",
        "ncos-observer-linux",
        "--all-targets",
        "--",
        "-D",
        "warnings"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "mutation-contract",
      "kind": "lint",
      "cwd": ".",
      "timeout_seconds": 540,
      "argv": null,
      "portability_note": "Original adapter-specific check; use the declared acceptance contract and fixture tests."
    }
  ]
}
```

</details>

<a id="b-001"></a>
## B-001

Support the conventional ncos inspect --help spelling with exactly the existing global help output, without observation.

元のtask_id: `PILOT-005`。初期ファイル数: 28。

**課題・インターフェース**

CLI arguments: [] and [--help] continue working. [inspect,--help] succeeds identically. Unknown command or extra options remain errors. Locate the appropriate argument handling.

取り出し方:

```sh
python materialize_task.py --set protocol-improvement-v2.1 --task B-001 --output work/B-001
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | model=gemma4:26b | PASS | PASS | — | true | — | — | [R-1fa3a286bc22e7](#r-1fa3a286bc22e7) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-1fa3a286bc22e7"></a>
### 根拠 R-1fa3a286bc22e7

- 対応方法: 同一セット内で一意のtask_idによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/4`
- 出典ファイルのSHA-256: `15ed69c09d40536288d746dbb645bc5ffe04482be6ccba86f827cef54cef9b04`
- [抽出した測定値・他の工程の記録](../results/protocol-improvement-v2.1.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "inspect --help equals --help and succeeds",
    "other --help fails",
    "inspect --help --execute fails"
  ],
  "acceptance_criteria": null,
  "checks": [
    {
      "id": "targeted",
      "kind": "test",
      "parser": "rust",
      "cwd": ".",
      "timeout_seconds": 210,
      "required_test_ids": [
        "pilot_inspect_help"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "180",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-cli",
        "--test",
        "pilot",
        "--",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": ".",
      "timeout_seconds": 210,
      "argv": [
        "cargo",
        "timeout",
        "180",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "fmt",
        "--check"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "clippy",
      "kind": "lint",
      "cwd": ".",
      "timeout_seconds": 210,
      "argv": [
        "cargo",
        "timeout",
        "180",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "clippy",
        "--offline",
        "--locked",
        "-p",
        "ncos-cli",
        "--all-targets",
        "--",
        "-D",
        "warnings"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    }
  ]
}
```

</details>

<a id="b-002"></a>
## B-002

Find where memory-pressure evidence is built and append a two-decimal available_percent for CLI/audit readability.

元のtask_id: `PILOT-004`。初期ファイル数: 28。

**課題・インターフェース**

Preserve Event id/kind/target, existing threshold behavior and raw KiB evidence. Required single evidence string: available_kib=N; total_kib=T; available_percent=P.PP. Percentage is 100 * available / total.

取り出し方:

```sh
python materialize_task.py --set protocol-improvement-v2.1 --task B-002 --output work/B-002
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | model=gemma4:26b | PASS | PASS | — | true | — | — | [R-4c9d1dbcc926d2](#r-4c9d1dbcc926d2) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-4c9d1dbcc926d2"></a>
### 根拠 R-4c9d1dbcc926d2

- 対応方法: 同一セット内で一意のtask_idによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/5`
- 出典ファイルのSHA-256: `15ed69c09d40536288d746dbb645bc5ffe04482be6ccba86f827cef54cef9b04`
- [抽出した測定値・他の工程の記録](../results/protocol-improvement-v2.1.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    {
      "total": 100,
      "available": 9,
      "expected_suffix": "available_percent=9.00"
    },
    {
      "total": 100,
      "available": 0,
      "expected_suffix": "available_percent=0.00"
    },
    {
      "total": 100,
      "available": 10,
      "expected": "no event"
    },
    {
      "total": 0,
      "available": 0,
      "expected": "no event"
    }
  ],
  "acceptance_criteria": null,
  "checks": [
    {
      "id": "targeted",
      "kind": "test",
      "parser": "rust",
      "cwd": ".",
      "timeout_seconds": 210,
      "required_test_ids": [
        "pilot_memory_evidence_percentage"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "180",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--test",
        "pilot",
        "--",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": ".",
      "timeout_seconds": 210,
      "argv": [
        "cargo",
        "timeout",
        "180",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "fmt",
        "--check"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "clippy",
      "kind": "lint",
      "cwd": ".",
      "timeout_seconds": 210,
      "argv": [
        "cargo",
        "timeout",
        "180",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "clippy",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--all-targets",
        "--",
        "-D",
        "warnings"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    }
  ]
}
```

</details>

<a id="b-003"></a>
## B-003

Append load_per_cpu with two decimals to high-load evidence for CLI/audit readability.

元のtask_id: `PEX-B03`。初期ファイル数: 28。

**課題・インターフェース**

Find the high-load event builder. Preserve its existing trigger, IDs, kind, target, evidence prefix and event ordering; append "; load_per_cpu=<ratio>".

取り出し方:

```sh
python materialize_task.py --set protocol-improvement-v2.1 --task B-003 --output work/B-003
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | model=gemma4:26b | ESCALATE | ESCALATE | — | false | — | — | [R-4351b583499e26](#r-4351b583499e26) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-4351b583499e26"></a>
### 根拠 R-4351b583499e26

- 対応方法: 同一セット内で一意のtask_idによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/6`
- 出典ファイルのSHA-256: `15ed69c09d40536288d746dbb645bc5ffe04482be6ccba86f827cef54cef9b04`
- [抽出した測定値・他の工程の記録](../results/protocol-improvement-v2.1.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "load=9, CPUs=4 -> suffix load_per_cpu=2.25; load=3, CPUs=1 -> 3.00.",
    "Threshold equality, zero CPU count and non-finite load still produce no HighLoad event."
  ],
  "acceptance_criteria": null,
  "checks": [
    {
      "id": "targeted",
      "kind": "test",
      "parser": "rust",
      "cwd": ".",
      "timeout_seconds": 210,
      "required_test_ids": [
        "protocol_load_ratio"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "180",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--test",
        "protocol",
        "--",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": ".",
      "timeout_seconds": 210,
      "argv": [
        "cargo",
        "timeout",
        "180",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "fmt",
        "--check"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "clippy",
      "kind": "lint",
      "cwd": ".",
      "timeout_seconds": 210,
      "argv": [
        "cargo",
        "timeout",
        "180",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "clippy",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--all-targets",
        "--",
        "-D",
        "warnings"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    }
  ]
}
```

</details>

<a id="c-001"></a>
## C-001

Extract the existing event deduplication and skill cache behavior into a typed maintenance summary.

元のtask_id: `PILOT-007`。初期ファイル数: 2。

**課題・インターフェース**

Return exact typed keys: event_key, skill_key, duplicate_refreshes_fifo, zero_capacity_accepts_event, skills_rebind_evidence. Read the existing implementations; no edits.

取り出し方:

```sh
python materialize_task.py --set protocol-improvement-v2.1 --task C-001 --output work/C-001
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | model=gemma4:26b | ESCALATE | ESCALATE | — | false | — | — | [R-7481d65da8b8e2](#r-7481d65da8b8e2) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-7481d65da8b8e2"></a>
### 根拠 R-7481d65da8b8e2

- 対応方法: 同一セット内で一意のtask_idによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/7`
- 出典ファイルのSHA-256: `15ed69c09d40536288d746dbb645bc5ffe04482be6ccba86f827cef54cef9b04`
- [抽出した測定値・他の工程の記録](../results/protocol-improvement-v2.1.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Describe the actual keys, duplicate ordering, capacity-zero behavior and current evidence rebinding."
  ],
  "acceptance_criteria": null,
  "checks": [
    {
      "id": "implementation-facts",
      "kind": "structured",
      "argv": null,
      "portability_note": "Original adapter-specific check; use the declared acceptance contract and fixture tests."
    }
  ]
}
```

</details>

<a id="c-002"></a>
## C-002

Extract five lexical and numeric facts about the existing KiB value parser.

元のtask_id: `PEX-C02`。初期ファイル数: 27。

**課題・インターフェース**

Return the exact five typed fields declared in answer_fields; describe existing code only.

取り出し方:

```sh
python materialize_task.py --set protocol-improvement-v2.1 --task C-002 --output work/C-002
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | model=gemma4:26b | ESCALATE | ESCALATE | — | false | — | — | [R-cec1140c515f68](#r-cec1140c515f68) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-cec1140c515f68"></a>
### 根拠 R-cec1140c515f68

- 対応方法: 同一セット内で一意のtask_idによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/8`
- 出典ファイルのSHA-256: `15ed69c09d40536288d746dbb645bc5ffe04482be6ccba86f827cef54cef9b04`
- [抽出した測定値・他の工程の記録](../results/protocol-improvement-v2.1.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "All five facts reflect the cited implementation."
  ],
  "acceptance_criteria": null,
  "checks": [
    {
      "id": "implementation-facts",
      "kind": "structured",
      "argv": null,
      "portability_note": "Original adapter-specific check; use the declared acceptance contract and fixture tests."
    }
  ]
}
```

</details>

<a id="c-003"></a>
## C-003

Extract five facts about HighLoad event generation and its ordering relative to memory events.

元のtask_id: `PEX-C03`。初期ファイル数: 27。

**課題・インターフェース**

Return the exact five typed fields declared in answer_fields; describe existing code only.

取り出し方:

```sh
python materialize_task.py --set protocol-improvement-v2.1 --task C-003 --output work/C-003
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | model=gemma4:26b | ESCALATE | ESCALATE | — | false | — | — | [R-b1d5569d4a783f](#r-b1d5569d4a783f) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-b1d5569d4a783f"></a>
### 根拠 R-b1d5569d4a783f

- 対応方法: 同一セット内で一意のtask_idによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/9`
- 出典ファイルのSHA-256: `15ed69c09d40536288d746dbb645bc5ffe04482be6ccba86f827cef54cef9b04`
- [抽出した測定値・他の工程の記録](../results/protocol-improvement-v2.1.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "All five facts reflect the cited implementation."
  ],
  "acceptance_criteria": null,
  "checks": [
    {
      "id": "implementation-facts",
      "kind": "structured",
      "argv": null,
      "portability_note": "Original adapter-specific check; use the declared acceptance contract and fixture tests."
    }
  ]
}
```

</details>
