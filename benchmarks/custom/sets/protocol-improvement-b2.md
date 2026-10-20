# 実装・検証手順の比較 / protocol-improvement-b2

セットID: `protocol-improvement-b2`

課題数: 5。個別記録あり: 5、個別記録未確認: 0。

[全セット一覧](../INDEX.md) / [課題定義JSON](protocol-improvement-b2.json) / [結果と根拠のJSON](../results/protocol-improvement-b2.json) / [判定の読み方](../README.md#判定の読み方)

各結果はこのセットの保存記録に対応します。収録外の別runの結果を新たに代入していません。SHA-256が記録されている結果は課題定義と照合し、それ以外は実行キー・ディレクトリ・同一セット内の一意のIDによる対応として表示しています。元の記録が過去の工程を再利用している場合、独立した再実行の結果とは扱わないでください。

参考の実験レポート: [RESULTS_JA.md](../reports/protocol-improvement-b2/RESULTS_JA.md)

| 課題ID | 内容 | 個別記録 |
| --- | --- | --- |
| [B2-001](#b2-001) | Support the conventional ncos inspect --help spelling with exactly the existing global help output, without observation. | 記録あり |
| [B2-002](#b2-002) | Find where memory-pressure evidence is built and append a two-decimal available_percent for CLI/audit readability. | 記録あり |
| [B2-003](#b2-003) | Append load_per_cpu with two decimals to high-load evidence for CLI/audit readability. | 記録あり |
| [B2-004](#b2-004) | Include snapshot process count in the audit summary for an anomaly-free inspection. | 記録あり |
| [B2-005](#b2-005) | Include the current event target in the reusable skill proposal reason for audit readability. | 記録あり |

<a id="b2-001"></a>
## B2-001

Support the conventional ncos inspect --help spelling with exactly the existing global help output, without observation.

元のtask_id: `B2-001`。初期ファイル数: 29。

**課題・インターフェース**

CLI arguments: [] and [--help] continue working. [inspect,--help] succeeds identically. Unknown command or extra options remain errors. Locate the appropriate argument handling.

取り出し方:

```sh
python materialize_task.py --set protocol-improvement-b2 --task B2-001 --output work/B2-001
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | PASS | PASS | — | true | ACCEPT_NO_CHANGE | — | [R-ef22f618b2202a](#r-ef22f618b2202a) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-ef22f618b2202a"></a>
### 根拠 R-ef22f618b2202a

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/0`
- 出典ファイルのSHA-256: `a07b2ba6ebb99a7d9f6ea39d3f90ce0410f920a8f31b7d42da6e88388fb6216e`
- [抽出した測定値・他の工程の記録](../results/protocol-improvement-b2.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "No arguments retain the exact existing successful help output.",
    "--help retains exact successful output without observation.",
    "inspect --help returns the same exact help without observation.",
    "Unknown command, extra help flags and duplicate flags remain errors.",
    "Existing inspect --demo --repeat remains dry-run and produces both passes.",
    "Existing targeted regression tests remain passing.",
    "Workspace rustfmt remains clean.",
    "Impacted crate clippy with warnings denied remains clean.",
    "Only the declared body changes; public signatures, all other source, tests, dependencies and Git identity remain fixed."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "AC-1",
      "criterion_text": "No arguments retain the exact existing successful help output.",
      "category": "functional"
    },
    {
      "criterion_id": "AC-2",
      "criterion_text": "--help retains exact successful output without observation.",
      "category": "functional"
    },
    {
      "criterion_id": "AC-3",
      "criterion_text": "inspect --help returns the same exact help without observation.",
      "category": "functional"
    },
    {
      "criterion_id": "AC-4",
      "criterion_text": "Unknown command, extra help flags and duplicate flags remain errors.",
      "category": "functional"
    },
    {
      "criterion_id": "AC-5",
      "criterion_text": "Existing inspect --demo --repeat remains dry-run and produces both passes.",
      "category": "functional"
    },
    {
      "criterion_id": "AC-REGRESSION",
      "criterion_text": "Existing targeted regression tests remain passing.",
      "category": "functional"
    },
    {
      "criterion_id": "AC-FORMAT",
      "criterion_text": "Workspace rustfmt remains clean.",
      "category": "quality"
    },
    {
      "criterion_id": "AC-LINT",
      "criterion_text": "Impacted crate clippy with warnings denied remains clean.",
      "category": "quality"
    },
    {
      "criterion_id": "AC-SCOPE",
      "criterion_text": "Only the declared body changes; public signatures, all other source, tests, dependencies and Git identity remain fixed.",
      "category": "structural"
    }
  ],
  "checks": [
    {
      "id": "acceptance-no_args",
      "kind": "test",
      "parser": "rust",
      "cwd": ".",
      "timeout_seconds": 210,
      "required_test_ids": [
        "ac_cli_no_args"
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
        "b2",
        "ac_cli_no_args",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "acceptance-help",
      "kind": "test",
      "parser": "rust",
      "cwd": ".",
      "timeout_seconds": 210,
      "required_test_ids": [
        "ac_cli_help"
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
        "b2",
        "ac_cli_help",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "acceptance-new_help",
      "kind": "test",
      "parser": "rust",
      "cwd": ".",
      "timeout_seconds": 210,
      "required_test_ids": [
        "ac_cli_new_help"
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
        "b2",
        "ac_cli_new_help",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "acceptance-invalid",
      "kind": "test",
      "parser": "rust",
      "cwd": ".",
      "timeout_seconds": 210,
      "required_test_ids": [
        "ac_cli_invalid"
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
        "b2",
        "ac_cli_invalid",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "acceptance-demo",
      "kind": "test",
      "parser": "rust",
      "cwd": ".",
      "timeout_seconds": 210,
      "required_test_ids": [
        "ac_cli_existing_demo"
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
        "b2",
        "ac_cli_existing_demo",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "targeted-regression",
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
        "--all-features",
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

<a id="b2-002"></a>
## B2-002

Find where memory-pressure evidence is built and append a two-decimal available_percent for CLI/audit readability.

元のtask_id: `B2-002`。初期ファイル数: 29。

**課題・インターフェース**

Preserve Event id/kind/target, existing threshold behavior and raw KiB evidence. Required single evidence string: available_kib=N; total_kib=T; available_percent=P.PP. Percentage is 100 * available / total.

取り出し方:

```sh
python materialize_task.py --set protocol-improvement-b2 --task B2-002 --output work/B2-002
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | PASS | PASS | — | true | ACCEPT_NO_CHANGE | — | [R-64ee904ee87c8e](#r-64ee904ee87c8e) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-64ee904ee87c8e"></a>
### 根拠 R-64ee904ee87c8e

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/1`
- 出典ファイルのSHA-256: `a07b2ba6ebb99a7d9f6ea39d3f90ce0410f920a8f31b7d42da6e88388fb6216e`
- [抽出した測定値・他の工程の記録](../results/protocol-improvement-b2.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Append available_percent=100*available/total with two decimals, retaining raw KiB prefix and one evidence string.",
    "Retain Event id/kind/target.",
    "Retain strict memory threshold, zero-total and large-u64 behavior.",
    "Existing HighLoad detection/evidence remains unchanged.",
    "Existing targeted regression tests remain passing.",
    "Workspace rustfmt remains clean.",
    "Impacted crate clippy with warnings denied remains clean.",
    "Only the declared body changes; public signatures, all other source, tests, dependencies and Git identity remain fixed."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "AC-1",
      "criterion_text": "Append available_percent=100*available/total with two decimals, retaining raw KiB prefix and one evidence string.",
      "category": "functional"
    },
    {
      "criterion_id": "AC-2",
      "criterion_text": "Retain Event id/kind/target.",
      "category": "functional"
    },
    {
      "criterion_id": "AC-3",
      "criterion_text": "Retain strict memory threshold, zero-total and large-u64 behavior.",
      "category": "functional"
    },
    {
      "criterion_id": "AC-4",
      "criterion_text": "Existing HighLoad detection/evidence remains unchanged.",
      "category": "functional"
    },
    {
      "criterion_id": "AC-REGRESSION",
      "criterion_text": "Existing targeted regression tests remain passing.",
      "category": "functional"
    },
    {
      "criterion_id": "AC-FORMAT",
      "criterion_text": "Workspace rustfmt remains clean.",
      "category": "quality"
    },
    {
      "criterion_id": "AC-LINT",
      "criterion_text": "Impacted crate clippy with warnings denied remains clean.",
      "category": "quality"
    },
    {
      "criterion_id": "AC-SCOPE",
      "criterion_text": "Only the declared body changes; public signatures, all other source, tests, dependencies and Git identity remain fixed.",
      "category": "structural"
    }
  ],
  "checks": [
    {
      "id": "acceptance-percentage",
      "kind": "test",
      "parser": "rust",
      "cwd": ".",
      "timeout_seconds": 210,
      "required_test_ids": [
        "ac_memory_percentage"
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
        "b2",
        "ac_memory_percentage",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "acceptance-identity",
      "kind": "test",
      "parser": "rust",
      "cwd": ".",
      "timeout_seconds": 210,
      "required_test_ids": [
        "ac_memory_identity"
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
        "b2",
        "ac_memory_identity",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "acceptance-threshold",
      "kind": "test",
      "parser": "rust",
      "cwd": ".",
      "timeout_seconds": 210,
      "required_test_ids": [
        "ac_memory_threshold"
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
        "b2",
        "ac_memory_threshold",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "acceptance-other_event",
      "kind": "test",
      "parser": "rust",
      "cwd": ".",
      "timeout_seconds": 210,
      "required_test_ids": [
        "ac_memory_existing_load"
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
        "b2",
        "ac_memory_existing_load",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "targeted-regression",
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
        "--all-features",
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

<a id="b2-003"></a>
## B2-003

Append load_per_cpu with two decimals to high-load evidence for CLI/audit readability.

元のtask_id: `B2-003`。初期ファイル数: 29。

**課題・インターフェース**

Find the high-load event builder. Preserve its existing trigger, IDs, kind, target, evidence prefix and event ordering; append "; load_per_cpu=<ratio>".

取り出し方:

```sh
python materialize_task.py --set protocol-improvement-b2 --task B2-003 --output work/B2-003
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | ESCALATE | ESCALATE | — | false | REJECT | — | [R-c4502833ac34fb](#r-c4502833ac34fb) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-c4502833ac34fb"></a>
### 根拠 R-c4502833ac34fb

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/2`
- 出典ファイルのSHA-256: `a07b2ba6ebb99a7d9f6ea39d3f90ce0410f920a8f31b7d42da6e88388fb6216e`
- [抽出した測定値・他の工程の記録](../results/protocol-improvement-b2.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Append load_per_cpu=load/CPUs with two decimals and retain the evidence prefix.",
    "Retain HighLoad id/kind/target.",
    "Retain strict threshold, zero-CPU and non-finite-load rejection.",
    "Memory event remains first with unchanged evidence when both events exist.",
    "Existing targeted regression tests remain passing.",
    "Workspace rustfmt remains clean.",
    "Impacted crate clippy with warnings denied remains clean.",
    "Only the declared body changes; public signatures, all other source, tests, dependencies and Git identity remain fixed."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "AC-1",
      "criterion_text": "Append load_per_cpu=load/CPUs with two decimals and retain the evidence prefix.",
      "category": "functional"
    },
    {
      "criterion_id": "AC-2",
      "criterion_text": "Retain HighLoad id/kind/target.",
      "category": "functional"
    },
    {
      "criterion_id": "AC-3",
      "criterion_text": "Retain strict threshold, zero-CPU and non-finite-load rejection.",
      "category": "functional"
    },
    {
      "criterion_id": "AC-4",
      "criterion_text": "Memory event remains first with unchanged evidence when both events exist.",
      "category": "functional"
    },
    {
      "criterion_id": "AC-REGRESSION",
      "criterion_text": "Existing targeted regression tests remain passing.",
      "category": "functional"
    },
    {
      "criterion_id": "AC-FORMAT",
      "criterion_text": "Workspace rustfmt remains clean.",
      "category": "quality"
    },
    {
      "criterion_id": "AC-LINT",
      "criterion_text": "Impacted crate clippy with warnings denied remains clean.",
      "category": "quality"
    },
    {
      "criterion_id": "AC-SCOPE",
      "criterion_text": "Only the declared body changes; public signatures, all other source, tests, dependencies and Git identity remain fixed.",
      "category": "structural"
    }
  ],
  "checks": [
    {
      "id": "acceptance-ratio",
      "kind": "test",
      "parser": "rust",
      "cwd": ".",
      "timeout_seconds": 210,
      "required_test_ids": [
        "ac_load_ratio"
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
        "b2",
        "ac_load_ratio",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "acceptance-identity",
      "kind": "test",
      "parser": "rust",
      "cwd": ".",
      "timeout_seconds": 210,
      "required_test_ids": [
        "ac_load_identity"
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
        "b2",
        "ac_load_identity",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "acceptance-threshold",
      "kind": "test",
      "parser": "rust",
      "cwd": ".",
      "timeout_seconds": 210,
      "required_test_ids": [
        "ac_load_threshold"
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
        "b2",
        "ac_load_threshold",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "acceptance-ordering",
      "kind": "test",
      "parser": "rust",
      "cwd": ".",
      "timeout_seconds": 210,
      "required_test_ids": [
        "ac_load_existing_memory"
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
        "b2",
        "ac_load_existing_memory",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "targeted-regression",
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
        "--all-features",
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

<a id="b2-004"></a>
## B2-004

Include snapshot process count in the audit summary for an anomaly-free inspection.

元のtask_id: `B2-004`。初期ファイル数: 28。

**課題・インターフェース**

Find the no-anomaly audit summary producer. Only append ; processes=N to its existing reason, using the observed snapshot. Retain all behavior and public signatures.

取り出し方:

```sh
python materialize_task.py --set protocol-improvement-b2 --task B2-004 --output work/B2-004
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | ESCALATE | ESCALATE | — | false | REJECT | — | [R-4fa14796403f7f](#r-4fa14796403f7f) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-4fa14796403f7f"></a>
### 根拠 R-4fa14796403f7f

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/3`
- 出典ファイルのSHA-256: `a07b2ba6ebb99a7d9f6ea39d3f90ce0410f920a8f31b7d42da6e88388fb6216e`
- [抽出した測定値・他の工程の記録](../results/protocol-improvement-b2.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "No-anomaly audit short_reason is exactly No anomaly candidates; model asleep; processes=N for snapshot process count N.",
    "Preserve returned snapshot, one fast-path record and all record fields; no provider call/token reservation.",
    "Anomalous input retains the existing event, source, reason and provider behavior.",
    "Invalid intent is still rejected before any provider call.",
    "Existing targeted regression tests remain passing.",
    "Workspace rustfmt remains clean.",
    "Impacted crate clippy with warnings denied remains clean.",
    "Only the declared body changes; public signatures, all other source, tests, dependencies and Git identity remain fixed."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "AC-1",
      "criterion_text": "No-anomaly audit short_reason is exactly No anomaly candidates; model asleep; processes=N for snapshot process count N.",
      "category": "functional"
    },
    {
      "criterion_id": "AC-2",
      "criterion_text": "Preserve returned snapshot, one fast-path record and all record fields; no provider call/token reservation.",
      "category": "functional"
    },
    {
      "criterion_id": "AC-3",
      "criterion_text": "Anomalous input retains the existing event, source, reason and provider behavior.",
      "category": "functional"
    },
    {
      "criterion_id": "AC-4",
      "criterion_text": "Invalid intent is still rejected before any provider call.",
      "category": "functional"
    },
    {
      "criterion_id": "AC-REGRESSION",
      "criterion_text": "Existing targeted regression tests remain passing.",
      "category": "functional"
    },
    {
      "criterion_id": "AC-FORMAT",
      "criterion_text": "Workspace rustfmt remains clean.",
      "category": "quality"
    },
    {
      "criterion_id": "AC-LINT",
      "criterion_text": "Impacted crate clippy with warnings denied remains clean.",
      "category": "quality"
    },
    {
      "criterion_id": "AC-SCOPE",
      "criterion_text": "Only the declared body changes; public signatures, all other source, tests, dependencies and Git identity remain fixed.",
      "category": "structural"
    }
  ],
  "checks": [
    {
      "id": "acceptance-reason",
      "kind": "test",
      "parser": "rust",
      "cwd": ".",
      "timeout_seconds": 210,
      "required_test_ids": [
        "ac_fast_reason"
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
        "ncos-agent",
        "--test",
        "b2",
        "ac_fast_reason",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "acceptance-record",
      "kind": "test",
      "parser": "rust",
      "cwd": ".",
      "timeout_seconds": 210,
      "required_test_ids": [
        "ac_fast_preserve_record"
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
        "ncos-agent",
        "--test",
        "b2",
        "ac_fast_preserve_record",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "acceptance-anomaly",
      "kind": "test",
      "parser": "rust",
      "cwd": ".",
      "timeout_seconds": 210,
      "required_test_ids": [
        "ac_fast_existing_anomaly"
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
        "ncos-agent",
        "--test",
        "b2",
        "ac_fast_existing_anomaly",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "acceptance-invalid",
      "kind": "test",
      "parser": "rust",
      "cwd": ".",
      "timeout_seconds": 210,
      "required_test_ids": [
        "ac_fast_invalid_intent"
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
        "ncos-agent",
        "--test",
        "b2",
        "ac_fast_invalid_intent",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "targeted-regression",
      "kind": "test",
      "parser": "rust",
      "cwd": ".",
      "timeout_seconds": 210,
      "required_test_ids": [
        "mock_propose",
        "resource_budget_and_skill_reuse",
        "healthy_fast_path_never_calls_model",
        "untrusted_provider_cannot_escalate",
        "excessive_usage_is_rejected_and_reservation_retained",
        "late_response_is_not_executed"
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
        "ncos-agent",
        "--test",
        "acceptance",
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
        "ncos-agent",
        "--all-targets",
        "--all-features",
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

<a id="b2-005"></a>
## B2-005

Include the current event target in the reusable skill proposal reason for audit readability.

元のtask_id: `B2-005`。初期ファイル数: 28。

**課題・インターフェース**

Locate the reusable skill report constructor, not the mock provider. Append ; target=T to its existing reason. Keep fixed proposal authority/target and exact current evidence; preserve unsupported-intent rejection.

取り出し方:

```sh
python materialize_task.py --set protocol-improvement-b2 --task B2-005 --output work/B2-005
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | ESCALATE | ESCALATE | — | false | REJECT | — | [R-1ac648f20b3c77](#r-1ac648f20b3c77) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-1ac648f20b3c77"></a>
### 根拠 R-1ac648f20b3c77

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/4`
- 出典ファイルのSHA-256: `a07b2ba6ebb99a7d9f6ea39d3f90ce0410f920a8f31b7d42da6e88388fb6216e`
- [抽出した測定値・他の工程の記録](../results/protocol-improvement-b2.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Reusable skill reason is exactly Verified report template with current evidence; target=T using the current event target T.",
    "Retain fixed Report/system/Report/Low/reversible fields and exact current evidence.",
    "Unsupported goal or constraints continue returning None.",
    "Existing targeted regression tests remain passing.",
    "Workspace rustfmt remains clean.",
    "Impacted crate clippy with warnings denied remains clean.",
    "Only the declared body changes; public signatures, all other source, tests, dependencies and Git identity remain fixed."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "AC-1",
      "criterion_text": "Reusable skill reason is exactly Verified report template with current evidence; target=T using the current event target T.",
      "category": "functional"
    },
    {
      "criterion_id": "AC-2",
      "criterion_text": "Retain fixed Report/system/Report/Low/reversible fields and exact current evidence.",
      "category": "functional"
    },
    {
      "criterion_id": "AC-3",
      "criterion_text": "Unsupported goal or constraints continue returning None.",
      "category": "functional"
    },
    {
      "criterion_id": "AC-REGRESSION",
      "criterion_text": "Existing targeted regression tests remain passing.",
      "category": "functional"
    },
    {
      "criterion_id": "AC-FORMAT",
      "criterion_text": "Workspace rustfmt remains clean.",
      "category": "quality"
    },
    {
      "criterion_id": "AC-LINT",
      "criterion_text": "Impacted crate clippy with warnings denied remains clean.",
      "category": "quality"
    },
    {
      "criterion_id": "AC-SCOPE",
      "criterion_text": "Only the declared body changes; public signatures, all other source, tests, dependencies and Git identity remain fixed.",
      "category": "structural"
    }
  ],
  "checks": [
    {
      "id": "acceptance-reason",
      "kind": "test",
      "parser": "rust",
      "cwd": ".",
      "timeout_seconds": 210,
      "required_test_ids": [
        "ac_skill_reason"
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
        "b2",
        "ac_skill_reason",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "acceptance-proposal",
      "kind": "test",
      "parser": "rust",
      "cwd": ".",
      "timeout_seconds": 210,
      "required_test_ids": [
        "ac_skill_preserve_proposal"
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
        "b2",
        "ac_skill_preserve_proposal",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "acceptance-unsupported",
      "kind": "test",
      "parser": "rust",
      "cwd": ".",
      "timeout_seconds": 210,
      "required_test_ids": [
        "ac_skill_reject_unsupported"
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
        "b2",
        "ac_skill_reject_unsupported",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "targeted-regression",
      "kind": "test",
      "parser": "rust",
      "cwd": ".",
      "timeout_seconds": 210,
      "required_test_ids": [
        "skill_cache",
        "promotion_requires_safe_verified_simulation"
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
        "acceptance",
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
        "--all-features",
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
