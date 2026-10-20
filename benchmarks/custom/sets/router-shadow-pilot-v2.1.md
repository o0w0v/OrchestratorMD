# 実装委譲の検証 / 手順-v2.1

セットID: `router-shadow-pilot-v2.1`

課題数: 8。個別記録あり: 8、個別記録未確認: 0。

[全セット一覧](../INDEX.md) / [課題定義JSON](router-shadow-pilot-v2.1.json) / [結果と根拠のJSON](../results/router-shadow-pilot-v2.1.json) / [判定の読み方](../README.md#判定の読み方)

各結果はこのセットの保存記録に対応します。収録外の別runの結果を新たに代入していません。SHA-256が記録されている結果は課題定義と照合し、それ以外は実行キー・ディレクトリ・同一セット内の一意のIDによる対応として表示しています。元の記録が過去の工程を再利用している場合、独立した再実行の結果とは扱わないでください。

参考の実験レポート: [RESULTS_JA.md](../reports/router-shadow-pilot-v2.1/RESULTS_JA.md)

| 課題ID | 内容 | 個別記録 |
| --- | --- | --- |
| [PILOT-002](#pilot-002) | Add regression coverage that duplicate events do not refresh the FIFO deduplication window. | 記録あり |
| [PILOT-003](#pilot-003) | Add a stable KiB value context prefix to parser errors propagated by Linux observation. | 記録あり |
| [PILOT-004](#pilot-004) | Find where memory-pressure evidence is built and append a two-decimal available_percent for CLI/audit readability. | 記録あり |
| [PILOT-005](#pilot-005) | Support the conventional ncos inspect --help spelling with exactly the existing global help output, without observation. | 記録あり |
| [PILOT-006](#pilot-006) | Fix the reproduced CLI bug where the token after --audit can be another option and gets created as an audit file. | 記録あり |
| [PILOT-007](#pilot-007) | Extract the existing event deduplication and skill cache behavior into a typed maintenance summary. | 記録あり |
| [PILOT-008](#pilot-008) | Design a live privileged DeletePath execution backend beyond the current dry-run boundary. | 記録あり |
| [PILOT-009](#pilot-009) | Format optional CLI inventory counts for users instead of Rust Debug wrappers. | 記録あり |

<a id="pilot-002"></a>
## PILOT-002

Add regression coverage that duplicate events do not refresh the FIFO deduplication window.

元のtask_id: `PILOT-002`。初期ファイル数: 29。

**課題・インターフェース**

Implement only pilot_dedup_duplicate_does_not_refresh() test body. Event has id, kind, target, evidence; Deduplicator::new and EventFilter::accept are existing APIs.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.1 --task PILOT-002 --output work/PILOT-002
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| コードの検証 | model=gemma4:26b | ESCALATE | — | — | — | ACCEPT_WITH_MINOR_FIX | — | [R-ae97b0eef718d8](#r-ae97b0eef718d8) |
| ローカル実装 | model=gemma4:26b | ESCALATE | ESCALATE | — | — | — | — | [R-240004c8ad3032](#r-240004c8ad3032) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-ae97b0eef718d8"></a>
### 根拠 R-ae97b0eef718d8

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/1`
- 出典ファイルのSHA-256: `c8a92b7fecec5a51d93e1e7274c98935d665f416a569e347a51fcc8fe84cf51b`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.1.json)

<a id="r-240004c8ad3032"></a>
### 根拠 R-240004c8ad3032

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `results/PILOT-002/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `679c84546fd970a9143105cabc09d3d64027f334abc6ae5306e5aea96e5742a4`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.1.json)

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

<a id="pilot-003"></a>
## PILOT-003

Add a stable KiB value context prefix to parser errors propagated by Linux observation.

元のtask_id: `PILOT-003`。初期ファイル数: 28。

**課題・インターフェース**

Existing parse_kib_value(value: &str) -> Result<u64, String>; preserve accepted syntax, values and error precedence. Prefix every existing error with "KiB value: ".

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.1 --task PILOT-003 --output work/PILOT-003
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| コードの検証 | model=gemma4:26b | PASS | — | — | — | ACCEPT_NO_CHANGE | — | [R-ddd0013b62e8de](#r-ddd0013b62e8de) |
| ローカル実装 | model=gemma4:26b | PASS | PASS | — | — | — | — | [R-5edffc34e11fc9](#r-5edffc34e11fc9) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-ddd0013b62e8de"></a>
### 根拠 R-ddd0013b62e8de

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/2`
- 出典ファイルのSHA-256: `c8a92b7fecec5a51d93e1e7274c98935d665f416a569e347a51fcc8fe84cf51b`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.1.json)

<a id="r-5edffc34e11fc9"></a>
### 根拠 R-5edffc34e11fc9

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `results/PILOT-003/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `f8554f635f134450a0382dc51c65f185cae5ea0af529f132d529920831cb8bfd`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.1.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    {
      "input": "",
      "expected": "KiB value: missing number"
    },
    {
      "input": "1",
      "expected": "KiB value: missing unit"
    },
    {
      "input": "1 kB extra",
      "expected": "KiB value: extra tokens"
    },
    {
      "input": "1 MB",
      "expected": "KiB value: invalid unit"
    },
    {
      "input": "-1 kB",
      "expected": "KiB value: invalid number"
    },
    {
      "input": "18446744073709551616 kB",
      "expected": "KiB value: overflow"
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
        "pilot_kib_error_context"
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
        "ncos-observer-linux",
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

<a id="pilot-004"></a>
## PILOT-004

Find where memory-pressure evidence is built and append a two-decimal available_percent for CLI/audit readability.

元のtask_id: `PILOT-004`。初期ファイル数: 28。

**課題・インターフェース**

Preserve Event id/kind/target, existing threshold behavior and raw KiB evidence. Required single evidence string: available_kib=N; total_kib=T; available_percent=P.PP. Percentage is 100 * available / total.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.1 --task PILOT-004 --output work/PILOT-004
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| コードの検証 | model=gemma4:26b | PASS | — | — | — | ACCEPT_NO_CHANGE | — | [R-93cfb3b5661888](#r-93cfb3b5661888) |
| ローカル実装 | model=gemma4:26b | PASS | PASS | — | — | — | — | [R-aeb6f5398540a2](#r-aeb6f5398540a2) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-93cfb3b5661888"></a>
### 根拠 R-93cfb3b5661888

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/3`
- 出典ファイルのSHA-256: `c8a92b7fecec5a51d93e1e7274c98935d665f416a569e347a51fcc8fe84cf51b`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.1.json)

<a id="r-aeb6f5398540a2"></a>
### 根拠 R-aeb6f5398540a2

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `results/PILOT-004/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `7289c31d286709c2a3803c4ea236e13346b1bd9179d4619c0774c8385b01046e`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.1.json)

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

<a id="pilot-005"></a>
## PILOT-005

Support the conventional ncos inspect --help spelling with exactly the existing global help output, without observation.

元のtask_id: `PILOT-005`。初期ファイル数: 28。

**課題・インターフェース**

CLI arguments: [] and [--help] continue working. [inspect,--help] succeeds identically. Unknown command or extra options remain errors. Locate the appropriate argument handling.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.1 --task PILOT-005 --output work/PILOT-005
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| コードの検証 | model=gemma4:26b | ESCALATE | — | — | — | ACCEPT_WITH_MINOR_FIX | — | [R-d9dddb1c1c8341](#r-d9dddb1c1c8341) |
| ローカル実装 | model=gemma4:26b | ESCALATE | ESCALATE | — | — | — | — | [R-604a7c5e2d8efa](#r-604a7c5e2d8efa) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-d9dddb1c1c8341"></a>
### 根拠 R-d9dddb1c1c8341

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/4`
- 出典ファイルのSHA-256: `c8a92b7fecec5a51d93e1e7274c98935d665f416a569e347a51fcc8fe84cf51b`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.1.json)

<a id="r-604a7c5e2d8efa"></a>
### 根拠 R-604a7c5e2d8efa

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `results/PILOT-005/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `bda16891b906282e06fba6022f1c707d378efb236feb068985821136af02c136`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.1.json)

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

<a id="pilot-006"></a>
## PILOT-006

Fix the reproduced CLI bug where the token after --audit can be another option and gets created as an audit file.

元のtask_id: `PILOT-006`。初期ファイル数: 28。

**課題・インターフェース**

inspect --demo --audit --repeat currently succeeds and creates --repeat. Reject --audit followed by an option token starting with -- (or empty token), before any file creation. Ordinary paths and trailing --repeat still work. Locate the argument consumption bug.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.1 --task PILOT-006 --output work/PILOT-006
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| コードの検証 | model=qwen3-coder-next:latest | PASS | — | — | — | ACCEPT_NO_CHANGE | — | [R-13409c49d09095](#r-13409c49d09095) |
| ローカル実装 | model=qwen3-coder-next:latest | PASS | PASS | — | — | — | — | [R-c00bb6746f6b7d](#r-c00bb6746f6b7d) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-13409c49d09095"></a>
### 根拠 R-13409c49d09095

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/5`
- 出典ファイルのSHA-256: `c8a92b7fecec5a51d93e1e7274c98935d665f416a569e347a51fcc8fe84cf51b`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.1.json)

<a id="r-c00bb6746f6b7d"></a>
### 根拠 R-c00bb6746f6b7d

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `results/PILOT-006/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `c6e13fe89fab6d3495544e98d7ca8078b67e70b18422f4305f9ac8ade4480b0b`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.1.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "--audit --repeat, --unknown, --demo fail without files",
    "--audit report.jsonl --repeat succeeds with two demo records",
    "--audit missing value stays invalid"
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
        "pilot_audit_option_is_not_a_path"
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

<a id="pilot-007"></a>
## PILOT-007

Extract the existing event deduplication and skill cache behavior into a typed maintenance summary.

元のtask_id: `PILOT-007`。初期ファイル数: 2。

**課題・インターフェース**

Return exact typed keys: event_key, skill_key, duplicate_refreshes_fifo, zero_capacity_accepts_event, skills_rebind_evidence. Read the existing implementations; no edits.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.1 --task PILOT-007 --output work/PILOT-007
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| コードの検証 | model=gemma4:26b | ESCALATE | — | — | — | REJECT | — | [R-919dde4939828d](#r-919dde4939828d) |
| ローカル実装 | model=gemma4:26b | ESCALATE | ESCALATE | — | — | — | — | [R-c559c019ba65e4](#r-c559c019ba65e4) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-919dde4939828d"></a>
### 根拠 R-919dde4939828d

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/6`
- 出典ファイルのSHA-256: `c8a92b7fecec5a51d93e1e7274c98935d665f416a569e347a51fcc8fe84cf51b`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.1.json)

<a id="r-c559c019ba65e4"></a>
### 根拠 R-c559c019ba65e4

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `results/PILOT-007/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `f9cedce36d50a6d965c26bc864980f5e28253d7de287682d483ae55afcc2c1bb`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.1.json)

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

<a id="pilot-008"></a>
## PILOT-008

Design a live privileged DeletePath execution backend beyond the current dry-run boundary.

元のtask_id: `PILOT-008`。初期ファイル数: 0。

**課題・インターフェース**

Architecture/security review boundary only. Do not implement or execute any live operation.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.1 --task PILOT-008 --output work/PILOT-008
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| コードの検証 | 記録に条件の明記なし | ESCALATE | — | — | — | CODEX_ONLY | — | [R-9157036d8f8a24](#r-9157036d8f8a24) |
| ローカル実装 | 記録に条件の明記なし | ESCALATE | ESCALATE | — | — | — | — | [R-d9fb5957c158b4](#r-d9fb5957c158b4) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-9157036d8f8a24"></a>
### 根拠 R-9157036d8f8a24

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/7`
- 出典ファイルのSHA-256: `c8a92b7fecec5a51d93e1e7274c98935d665f416a569e347a51fcc8fe84cf51b`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.1.json)

<a id="r-d9fb5957c158b4"></a>
### 根拠 R-d9fb5957c158b4

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `results/PILOT-008/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `4af735a98fd5b6e1ed6276ed816b4df93b1f8a09caeec4611a24584c78e20cc8`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.1.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Router returns CODEX_REQUIRED; no model invocation or filesystem operation."
  ],
  "acceptance_criteria": null,
  "checks": [
    {
      "id": "boundary",
      "kind": "structured",
      "argv": null,
      "portability_note": "Original adapter-specific check; use the declared acceptance contract and fixture tests."
    }
  ]
}
```

</details>

<a id="pilot-009"></a>
## PILOT-009

Format optional CLI inventory counts for users instead of Rust Debug wrappers.

元のtask_id: `PILOT-009`。初期ファイル数: 28。

**課題・インターフェース**

Private fn inventory_count(value: Option<usize>) -> String. Some(n) returns decimal n; None returns "unavailable". No public API change.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.1 --task PILOT-009 --output work/PILOT-009
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| コードの検証 | model=gemma4:26b | PASS | — | — | — | ACCEPT_NO_CHANGE | — | [R-54bbf38c2656a5](#r-54bbf38c2656a5) |
| ローカル実装 | model=gemma4:26b | PASS | PASS | — | — | — | — | [R-b084211ed1f552](#r-b084211ed1f552) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-54bbf38c2656a5"></a>
### 根拠 R-54bbf38c2656a5

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/0`
- 出典ファイルのSHA-256: `c8a92b7fecec5a51d93e1e7274c98935d665f416a569e347a51fcc8fe84cf51b`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.1.json)

<a id="r-b084211ed1f552"></a>
### 根拠 R-b084211ed1f552

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `results/PILOT-009/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `15a6e8d8a0bdb4421efdb65f63ff93a19129c852b3476478c8a2578150d7327f`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.1.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    {
      "input": null,
      "expected": "unavailable"
    },
    {
      "input": 0,
      "expected": "0"
    },
    {
      "input": 42,
      "expected": "42"
    },
    {
      "input": "usize::MAX",
      "expected": "decimal usize::MAX"
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
        "pilot_inventory_display",
        "pilot_count_tests::all_counts"
      ],
      "min_test_count": 2,
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
