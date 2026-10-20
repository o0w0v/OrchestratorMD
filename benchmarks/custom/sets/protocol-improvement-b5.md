# 実装・検証手順の比較 / protocol-improvement-b5

セットID: `protocol-improvement-b5`

課題数: 3。個別記録あり: 3、個別記録未確認: 0。

[全セット一覧](../INDEX.md) / [課題定義JSON](protocol-improvement-b5.json) / [結果と根拠のJSON](../results/protocol-improvement-b5.json) / [判定の読み方](../README.md#判定の読み方)

各結果はこのセットの保存記録に対応します。収録外の別runの結果を新たに代入していません。SHA-256が記録されている結果は課題定義と照合し、それ以外は実行キー・ディレクトリ・同一セット内の一意のIDによる対応として表示しています。元の記録が過去の工程を再利用している場合、独立した再実行の結果とは扱わないでください。

参考の実験レポート: [RESULTS_JA.md](../reports/protocol-improvement-b5/RESULTS_JA.md)

| 課題ID | 内容 | 個別記録 |
| --- | --- | --- |
| [B5-003](#b5-003) | Append load_per_cpu with two decimals to high-load evidence for CLI/audit readability. | 記録あり |
| [B5-004](#b5-004) | Include snapshot process count in the audit summary for an anomaly-free inspection. | 記録あり |
| [B5-005](#b5-005) | Include the current event target in the reusable skill proposal reason for audit readability. | 記録あり |

<a id="b5-003"></a>
## B5-003

Append load_per_cpu with two decimals to high-load evidence for CLI/audit readability.

元のtask_id: `B5-003`。初期ファイル数: 29。

**課題・インターフェース**

Find the high-load event builder. Preserve its existing trigger, IDs, kind, target, evidence prefix and event ordering; append "; load_per_cpu=<ratio>".

取り出し方:

```sh
python materialize_task.py --set protocol-improvement-b5 --task B5-003 --output work/B5-003
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | PASS | PASS | — | true | ACCEPT_NO_CHANGE | — | [R-5fbd5824aff323](#r-5fbd5824aff323) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-5fbd5824aff323"></a>
### 根拠 R-5fbd5824aff323

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/0`
- 出典ファイルのSHA-256: `3f4b05894248ae0fdd4417c54b9ce9d748ad18639f7b8f555c88e2f810da2c61`
- [抽出した測定値・他の工程の記録](../results/protocol-improvement-b5.json)

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

<a id="b5-004"></a>
## B5-004

Include snapshot process count in the audit summary for an anomaly-free inspection.

元のtask_id: `B5-004`。初期ファイル数: 28。

**課題・インターフェース**

Find the no-anomaly audit summary producer. Only append ; processes=N to its existing reason, using the observed snapshot. Retain all behavior and public signatures.

取り出し方:

```sh
python materialize_task.py --set protocol-improvement-b5 --task B5-004 --output work/B5-004
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | PASS | PASS | — | true | ACCEPT_NO_CHANGE | — | [R-c6c7e9a1d6db88](#r-c6c7e9a1d6db88) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-c6c7e9a1d6db88"></a>
### 根拠 R-c6c7e9a1d6db88

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/1`
- 出典ファイルのSHA-256: `3f4b05894248ae0fdd4417c54b9ce9d748ad18639f7b8f555c88e2f810da2c61`
- [抽出した測定値・他の工程の記録](../results/protocol-improvement-b5.json)

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

<a id="b5-005"></a>
## B5-005

Include the current event target in the reusable skill proposal reason for audit readability.

元のtask_id: `B5-005`。初期ファイル数: 28。

**課題・インターフェース**

Locate the reusable skill report constructor, not the mock provider. Append ; target=T to its existing reason. Keep fixed proposal authority/target and exact current evidence; preserve unsupported-intent rejection.

取り出し方:

```sh
python materialize_task.py --set protocol-improvement-b5 --task B5-005 --output work/B5-005
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | PASS | PASS | — | true | ACCEPT_NO_CHANGE | — | [R-2d632922fadb0d](#r-2d632922fadb0d) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-2d632922fadb0d"></a>
### 根拠 R-2d632922fadb0d

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/2`
- 出典ファイルのSHA-256: `3f4b05894248ae0fdd4417c54b9ce9d748ad18639f7b8f555c88e2f810da2c61`
- [抽出した測定値・他の工程の記録](../results/protocol-improvement-b5.json)

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
