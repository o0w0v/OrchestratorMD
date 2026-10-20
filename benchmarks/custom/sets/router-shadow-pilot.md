# 実装委譲の検証 / 手順

セットID: `router-shadow-pilot`

課題数: 9。個別記録あり: 9、個別記録未確認: 0。

[全セット一覧](../INDEX.md) / [課題定義JSON](router-shadow-pilot.json) / [結果と根拠のJSON](../results/router-shadow-pilot.json) / [判定の読み方](../README.md#判定の読み方)

各結果はこのセットの保存記録に対応します。収録外の別runの結果を新たに代入していません。SHA-256が記録されている結果は課題定義と照合し、それ以外は実行キー・ディレクトリ・同一セット内の一意のIDによる対応として表示しています。元の記録が過去の工程を再利用している場合、独立した再実行の結果とは扱わないでください。

参考の実験レポート: [RESULTS_JA.md](../reports/router-shadow-pilot/RESULTS_JA.md)

| 課題ID | 内容 | 個別記録 |
| --- | --- | --- |
| [PILOT-001](#pilot-001) | Format optional CLI inventory counts for users instead of Rust Debug wrappers. | 記録あり |
| [PILOT-002](#pilot-002) | Add regression coverage that duplicate events do not refresh the FIFO deduplication window. | 記録あり |
| [PILOT-003](#pilot-003) | Add a stable KiB value context prefix to parser errors propagated by Linux observation. | 記録あり |
| [PILOT-004](#pilot-004) | Find where memory-pressure evidence is built and append a two-decimal available_percent for CLI/audit readability. | 記録あり |
| [PILOT-005](#pilot-005) | Support the conventional ncos inspect --help spelling with exactly the existing global help output, without observation. | 記録あり |
| [PILOT-006](#pilot-006) | Fix the reproduced CLI bug where the token after --audit can be another option and gets created as an audit file. | 記録あり |
| [PILOT-007](#pilot-007) | Extract the existing event deduplication and skill cache behavior into a typed maintenance summary. | 記録あり |
| [PILOT-008](#pilot-008) | Design a live privileged DeletePath execution backend beyond the current dry-run boundary. | 記録あり |
| [PILOT-009](#pilot-009) | Format optional CLI inventory counts for users instead of Rust Debug wrappers. | 記録あり |

<a id="pilot-001"></a>
## PILOT-001

Format optional CLI inventory counts for users instead of Rust Debug wrappers.

元のtask_id: `PILOT-001`。初期ファイル数: 28。

**課題・インターフェース**

Private fn inventory_count(value: Option<usize>) -> String. Some(n) returns decimal n; None returns "unavailable". No public API change.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot --task PILOT-001 --output work/PILOT-001
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| コードの検証 | results_condition=PILOT-001-task-design-failure.json | TASK_DESIGN_FAILURE | — | — | — | — | — | [R-e212daf735dd16](#r-e212daf735dd16) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-e212daf735dd16"></a>
### 根拠 R-e212daf735dd16

- 対応方法: 同一セット・課題IDによる対応
- 出典: `results/PILOT-001-task-design-failure.json` / 位置: `/`
- 出典ファイルのSHA-256: `071cc591f5f115348eca83954cfa46c3c191c3a208643489129a04c3be10bf15`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot.json)

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

<a id="pilot-002"></a>
## PILOT-002

Add regression coverage that duplicate events do not refresh the FIFO deduplication window.

元のtask_id: `PILOT-002`。初期ファイル数: 29。

**課題・インターフェース**

Implement only pilot_dedup_duplicate_does_not_refresh() test body. Event has id, kind, target, evidence; Deduplicator::new and EventFilter::accept are existing APIs.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot --task PILOT-002 --output work/PILOT-002
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | model=gemma4:12b | INFRA_ERROR | INFRA_ERROR | — | — | REJECT | — | [R-6e5808e2b7e939](#r-6e5808e2b7e939) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-6e5808e2b7e939"></a>
### 根拠 R-6e5808e2b7e939

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/tasks.json` / 位置: `/1`
- 出典ファイルのSHA-256: `f528c6de197bb6e66cba30825627f1a116bf45e50c965cbc822ad0e7a57874cd`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot.json)

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
python materialize_task.py --set router-shadow-pilot --task PILOT-003 --output work/PILOT-003
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | model=gemma4:12b | INFRA_ERROR | INFRA_ERROR | — | — | REJECT | — | [R-f637ac07090d6a](#r-f637ac07090d6a) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-f637ac07090d6a"></a>
### 根拠 R-f637ac07090d6a

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/tasks.json` / 位置: `/2`
- 出典ファイルのSHA-256: `f528c6de197bb6e66cba30825627f1a116bf45e50c965cbc822ad0e7a57874cd`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot.json)

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
python materialize_task.py --set router-shadow-pilot --task PILOT-004 --output work/PILOT-004
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実行状態・対照条件 | source=report_table | NOT_RUN_INFRA_STOP | — | — | — | — | — | [R-2f77ce900ae511](#r-2f77ce900ae511) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-2f77ce900ae511"></a>
### 根拠 R-2f77ce900ae511

- 対応方法: 同一セット・課題IDによる対応
- 出典: `RESULTS_JA.md` / 位置: `markdown-line:33`
- 出典ファイルのSHA-256: `228d4ba1fe5002ee88fa5436030475f780c40c94524c5a8498e86c0c550bf9d9`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot.json)

出典の表の該当行:

```text
| PILOT-004 | memory event evidenceへavailable_percent追加 | observer/events間で生成位置を探す小変更 | NOT_RUN_INFRA_STOP | 未評価 |
```

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
python materialize_task.py --set router-shadow-pilot --task PILOT-005 --output work/PILOT-005
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実行状態・対照条件 | source=report_table | NOT_RUN_INFRA_STOP | — | — | — | — | — | [R-f17d81b9e86c52](#r-f17d81b9e86c52) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-f17d81b9e86c52"></a>
### 根拠 R-f17d81b9e86c52

- 対応方法: 同一セット・課題IDによる対応
- 出典: `RESULTS_JA.md` / 位置: `markdown-line:34`
- 出典ファイルのSHA-256: `228d4ba1fe5002ee88fa5436030475f780c40c94524c5a8498e86c0c550bf9d9`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot.json)

出典の表の該当行:

```text
| PILOT-005 | `inspect --help`をglobal helpと同じ挙動にする | CLI/intentの限定探索。未知引数は引き続き拒否 | NOT_RUN_INFRA_STOP | 未評価 |
```

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
python materialize_task.py --set router-shadow-pilot --task PILOT-006 --output work/PILOT-006
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実行状態・対照条件 | source=report_table | NOT_RUN_INFRA_STOP | — | — | — | — | — | [R-2f7dcbce37ec7c](#r-2f7dcbce37ec7c) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-2f7dcbce37ec7c"></a>
### 根拠 R-2f7dcbce37ec7c

- 対応方法: 同一セット・課題IDによる対応
- 出典: `RESULTS_JA.md` / 位置: `markdown-line:35`
- 出典ファイルのSHA-256: `228d4ba1fe5002ee88fa5436030475f780c40c94524c5a8498e86c0c550bf9d9`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot.json)

出典の表の該当行:

```text
| PILOT-006 | `--audit`が次のoptionをpathとして消費する実bug | demoで `--repeat` というファイルが作られることを事前再現 | NOT_RUN_INFRA_STOP | 未評価 |
```

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
python materialize_task.py --set router-shadow-pilot --task PILOT-007 --output work/PILOT-007
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実行状態・対照条件 | source=report_table | NOT_RUN_INFRA_STOP | — | — | — | — | — | [R-d04b94a5aac061](#r-d04b94a5aac061) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-d04b94a5aac061"></a>
### 根拠 R-d04b94a5aac061

- 対応方法: 同一セット・課題IDによる対応
- 出典: `RESULTS_JA.md` / 位置: `markdown-line:36`
- 出典ファイルのSHA-256: `228d4ba1fe5002ee88fa5436030475f780c40c94524c5a8498e86c0c550bf9d9`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot.json)

出典の表の該当行:

```text
| PILOT-007 | dedup/cacheの実装上の5事実をtyped抽出 | コード編集不要の保守分析 | NOT_RUN_INFRA_STOP | 未評価 |
```

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
python materialize_task.py --set router-shadow-pilot --task PILOT-008 --output work/PILOT-008
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | ESCALATE | ESCALATE | — | — | CODEX_ONLY | — | [R-0ace041151d85e](#r-0ace041151d85e) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-0ace041151d85e"></a>
### 根拠 R-0ace041151d85e

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/tasks.json` / 位置: `/3`
- 出典ファイルのSHA-256: `f528c6de197bb6e66cba30825627f1a116bf45e50c965cbc822ad0e7a57874cd`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot.json)

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
python materialize_task.py --set router-shadow-pilot --task PILOT-009 --output work/PILOT-009
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | model=gemma4:26b | PASS | PASS | — | — | ACCEPT_NO_CHANGE | — | [R-d5e006c02e42ff](#r-d5e006c02e42ff) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-d5e006c02e42ff"></a>
### 根拠 R-d5e006c02e42ff

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/tasks.json` / 位置: `/0`
- 出典ファイルのSHA-256: `f528c6de197bb6e66cba30825627f1a116bf45e50c965cbc822ad0e7a57874cd`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot.json)

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
