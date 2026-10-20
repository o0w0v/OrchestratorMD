# ローカルモデルへの委譲にかかる費用の検証

セットID: `local-specialist-economics`

課題数: 14。個別記録あり: 14、個別記録未確認: 0。

[全セット一覧](../INDEX.md) / [課題定義JSON](local-specialist-economics.json) / [結果と根拠のJSON](../results/local-specialist-economics.json) / [判定の読み方](../README.md#判定の読み方)

各結果はこのセットの保存記録に対応します。収録外の別runの結果を新たに代入していません。SHA-256が記録されている結果は課題定義と照合し、それ以外は実行キー・ディレクトリ・同一セット内の一意のIDによる対応として表示しています。元の記録が過去の工程を再利用している場合、独立した再実行の結果とは扱わないでください。

参考の実験レポート: [RESULTS_LOCAL_SPECIALIST_ECONOMICS_DEVELOPMENT_JA.md](../reports/local-specialist-economics/RESULTS_LOCAL_SPECIALIST_ECONOMICS_DEVELOPMENT_JA.md) / [RESULTS_LOCAL_SPECIALIST_ECONOMICS_FINAL_JA.md](../reports/local-specialist-economics/RESULTS_LOCAL_SPECIALIST_ECONOMICS_FINAL_JA.md) / [RESULTS_LOCAL_SPECIALIST_ECONOMICS_JA.md](../reports/local-specialist-economics/RESULTS_LOCAL_SPECIALIST_ECONOMICS_JA.md)

**実験で固定した設定**（実際の結果・モデル情報は各記録を参照）

```json
[
  {
    "generation_options": {
      "temperature": 0,
      "seed": 20260926,
      "num_ctx": 8192,
      "num_predict": 2048
    }
  }
]
```

| 課題ID | 内容 | 個別記録 |
| --- | --- | --- |
| [LSE-001](#lse-001) | Escape event identity for pipe-delimited audit export | 記録あり |
| [LSE-002](#lse-002) | List recorded blocked proposal targets | 記録あり |
| [LSE-003](#lse-003) | Summarize sample warnings with stable empty/nonempty groups | 記録あり |
| [LSE-004](#lse-004) | Replace repeated event keys in their first-seen display positions | 記録あり |
| [LSE-005](#lse-005) | Remove overflow in rounded-up audit elapsed seconds | 記録あり |
| [LSE-006](#lse-006) | Compute affordable future recorded calls from two independent limits | 記録あり |
| [LSE-007](#lse-007) | Consolidate risk rendering through the existing helper | 記録あり |
| [LSE-008](#lse-008) | Serialize a process sample as an exact line manifest | 記録あり |
| [LSE-009](#lse-009) | Collect dry-run proposals lacking successful verification | 記録あり |
| [LSE-010](#lse-010) | Separate sampled process IDs with self-parent anomalies | 記録あり |
| [LSE-011](#lse-011) | Preview cooldown admissions without refreshing rejected timestamps | 記録あり |
| [LSE-012](#lse-012) | Preserve signed TCP sample decreases and unknown samples | 記録あり |
| [LSE-013](#lse-013) | Select an ordered evidence prefix under a byte allowance | 記録あり |
| [LSE-014](#lse-014) | Centralize paired action display labels | 記録あり |

<a id="lse-001"></a>
## LSE-001

Escape event identity for pipe-delimited audit export

元のtask_id: `LSE-001`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Return id|target with exactly one literal pipe separator. Independently escape percent as %25, pipe as %7C, CR as %0D and LF as %0A in both original strings; all other characters unchanged. One pass only, never double-escape generated percent sequences. Empty strings are valid. Preserve Unicode, whitespace, kind and evidence; no trimming, newline or extra text.

取り出し方:

```sh
python materialize_task.py --set local-specialist-economics --task LSE-001 --output work/LSE-001
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| コードの検証 | model_key=gemma26 / partition=development | ESCALATE | — | — | — | — | — | [R-9b4d1530dfb414](#r-9b4d1530dfb414) |
| コードの検証 | model_key=qwen14 / partition=development | PASS | — | — | — | — | — | [R-73380c08782503](#r-73380c08782503) |
| ローカル実装 | local_condition=gemma26 / model=gemma4:26b | ESCALATE | ESCALATE | — | — | — | — | [R-53dd9da3ceff2f](#r-53dd9da3ceff2f) |
| ローカル実装 | local_condition=qwen14 / model=qwen2.5-Coder:14b | PASS | PASS | — | — | — | — | [R-e2d77e376eda59](#r-e2d77e376eda59) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-9b4d1530dfb414"></a>
### 根拠 R-9b4d1530dfb414

- 対応方法: 同一セット・課題IDによる対応
- 出典: `summaries/development-local-terminal-001.json` / 位置: `/models/gemma26/development/0`
- 出典ファイルのSHA-256: `5de0e6e03c550e6ba2aecff5c6da7dc9eba39d17d33d744e81c61761f4eb64e5`
- [抽出した測定値・他の工程の記録](../results/local-specialist-economics.json)

<a id="r-73380c08782503"></a>
### 根拠 R-73380c08782503

- 対応方法: 同一セット・課題IDによる対応
- 出典: `summaries/development-local-terminal-001.json` / 位置: `/models/qwen14/development/0`
- 出典ファイルのSHA-256: `5de0e6e03c550e6ba2aecff5c6da7dc9eba39d17d33d744e81c61761f4eb64e5`
- [抽出した測定値・他の工程の記録](../results/local-specialist-economics.json)

<a id="r-53dd9da3ceff2f"></a>
### 根拠 R-53dd9da3ceff2f

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `local/gemma26/development/workspace/records/router-v2.2/LSE-001/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `2100439cc8b00e21626b190504c0065eb05d8bb88e0b57757252fc648eac2d83`
- [抽出した測定値・他の工程の記録](../results/local-specialist-economics.json)

<a id="r-e2d77e376eda59"></a>
### 根拠 R-e2d77e376eda59

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `local/qwen14/development/workspace/records/router-v2.2/LSE-001/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `1250314b9bfcc56c236c58f5aae191a48d5f19ca08a34ca73b797436ae4ee51e`
- [抽出した測定値・他の工程の記録](../results/local-specialist-economics.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Return id|target with exactly one literal pipe separator. Independently escape percent as %25, pipe as %7C, CR as %0D and LF as %0A in both original strings; all other characters unchanged. One pass only, never double-escape generated percent sequences.",
    "Empty strings are valid. Preserve Unicode, whitespace, kind and evidence; no trimming, newline or extra text.",
    "Existing workspace behavior remains valid.",
    "Rust formatting remains clean.",
    "No clippy warnings.",
    "All workspace tests remain valid.",
    "Workspace type checking succeeds.",
    "Workspace build succeeds.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "Return id|target with exactly one literal pipe separator. Independently escape percent as %25, pipe as %7C, CR as %0D and LF as %0A in both original strings; all other characters unchanged. One pass only, never double-escape generated percent sequences.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Empty strings are valid. Preserve Unicode, whitespace, kind and evidence; no trimming, newline or extra text.",
      "category": "functional"
    },
    {
      "criterion_id": "REGRESSION",
      "criterion_text": "Existing workspace behavior remains valid.",
      "category": "quality"
    },
    {
      "criterion_id": "FORMAT",
      "criterion_text": "Rust formatting remains clean.",
      "category": "quality"
    },
    {
      "criterion_id": "CLIPPY",
      "criterion_text": "No clippy warnings.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-TEST",
      "criterion_text": "All workspace tests remain valid.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-CHECK",
      "criterion_text": "Workspace type checking succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-BUILD",
      "criterion_text": "Workspace build succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "SCOPE",
      "criterion_text": "Only declared editable regions change; protected source and tests remain identical.",
      "category": "structural"
    }
  ],
  "checks": [
    {
      "id": "acceptance",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-001",
      "timeout_seconds": 330,
      "required_test_ids": [
        "economic_lse_001"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--lib",
        "economic_lse_001",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "regression",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-001",
      "timeout_seconds": 330,
      "required_test_ids": [
        "event_detect"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--test",
        "acceptance",
        "event_detect",
        "--",
        "--exact"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/LSE-001",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "fmt",
        "--check"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "clippy",
      "kind": "lint",
      "cwd": "units/LSE-001",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "clippy",
        "--offline",
        "--all-targets",
        "--all-features",
        "--",
        "-D",
        "warnings"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-test",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-001",
      "timeout_seconds": 330,
      "required_test_ids": [
        "event_detect"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--workspace",
        "--offline",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-check",
      "kind": "typecheck",
      "cwd": "units/LSE-001",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "check",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-build",
      "kind": "build",
      "cwd": "units/LSE-001",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "build",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    }
  ]
}
```

</details>

<a id="lse-002"></a>
## LSE-002

List recorded blocked proposal targets

元のtask_id: `LSE-002`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Return proposal.target for each record with a present proposal and a present execution whose status is Blocked. Preserve row order and duplicates, including empty targets. Ignore policy, event and execution.changed. Clone target strings without mutating any record; missing proposal or execution and DryRun execution are omitted.

取り出し方:

```sh
python materialize_task.py --set local-specialist-economics --task LSE-002 --output work/LSE-002
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| コードの検証 | model_key=qwen14 / partition=development | ESCALATE | — | — | — | — | — | [R-9c02e8c7ecd7b3](#r-9c02e8c7ecd7b3) |
| ローカル実装 | local_condition=qwen14 / model=qwen2.5-Coder:14b | ESCALATE | ESCALATE | — | — | — | — | [R-d1e297d69703f9](#r-d1e297d69703f9) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-9c02e8c7ecd7b3"></a>
### 根拠 R-9c02e8c7ecd7b3

- 対応方法: 同一セット・課題IDによる対応
- 出典: `summaries/development-local-terminal-001.json` / 位置: `/models/qwen14/development/1`
- 出典ファイルのSHA-256: `5de0e6e03c550e6ba2aecff5c6da7dc9eba39d17d33d744e81c61761f4eb64e5`
- [抽出した測定値・他の工程の記録](../results/local-specialist-economics.json)

<a id="r-d1e297d69703f9"></a>
### 根拠 R-d1e297d69703f9

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `local/qwen14/development/workspace/records/router-v2.2/LSE-002/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `1117971e3fcb698bdf5fb9f02c5c2216c3cf599437aa8b6be1ade718a6e14216`
- [抽出した測定値・他の工程の記録](../results/local-specialist-economics.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Return proposal.target for each record with a present proposal and a present execution whose status is Blocked. Preserve row order and duplicates, including empty targets. Ignore policy, event and execution.changed.",
    "Clone target strings without mutating any record; missing proposal or execution and DryRun execution are omitted.",
    "Existing workspace behavior remains valid.",
    "Rust formatting remains clean.",
    "No clippy warnings.",
    "All workspace tests remain valid.",
    "Workspace type checking succeeds.",
    "Workspace build succeeds.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "Return proposal.target for each record with a present proposal and a present execution whose status is Blocked. Preserve row order and duplicates, including empty targets. Ignore policy, event and execution.changed.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Clone target strings without mutating any record; missing proposal or execution and DryRun execution are omitted.",
      "category": "functional"
    },
    {
      "criterion_id": "REGRESSION",
      "criterion_text": "Existing workspace behavior remains valid.",
      "category": "quality"
    },
    {
      "criterion_id": "FORMAT",
      "criterion_text": "Rust formatting remains clean.",
      "category": "quality"
    },
    {
      "criterion_id": "CLIPPY",
      "criterion_text": "No clippy warnings.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-TEST",
      "criterion_text": "All workspace tests remain valid.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-CHECK",
      "criterion_text": "Workspace type checking succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-BUILD",
      "criterion_text": "Workspace build succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "SCOPE",
      "criterion_text": "Only declared editable regions change; protected source and tests remain identical.",
      "category": "structural"
    }
  ],
  "checks": [
    {
      "id": "acceptance",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-002",
      "timeout_seconds": 330,
      "required_test_ids": [
        "economic_lse_002"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--lib",
        "economic_lse_002",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "regression",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-002",
      "timeout_seconds": 330,
      "required_test_ids": [
        "event_detect"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--test",
        "acceptance",
        "event_detect",
        "--",
        "--exact"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/LSE-002",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "fmt",
        "--check"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "clippy",
      "kind": "lint",
      "cwd": "units/LSE-002",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "clippy",
        "--offline",
        "--all-targets",
        "--all-features",
        "--",
        "-D",
        "warnings"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-test",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-002",
      "timeout_seconds": 330,
      "required_test_ids": [
        "event_detect"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--workspace",
        "--offline",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-check",
      "kind": "typecheck",
      "cwd": "units/LSE-002",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "check",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-build",
      "kind": "build",
      "cwd": "units/LSE-002",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "build",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    }
  ]
}
```

</details>

<a id="lse-003"></a>
## LSE-003

Summarize sample warnings with stable empty/nonempty groups

元のtask_id: `LSE-003`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Return (nonempty warnings in original order, number of exactly empty warning strings). Preserve duplicates and whitespace-only warnings; empty means byte length zero, not trimmed empty. Use only state.warnings; do not mutate state, deduplicate, infer errors or consult processes_truncated.

取り出し方:

```sh
python materialize_task.py --set local-specialist-economics --task LSE-003 --output work/LSE-003
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| コードの検証 | model_key=qwen14 / partition=development | PASS | — | — | — | — | — | [R-5ccb53488a8e80](#r-5ccb53488a8e80) |
| ローカル実装 | local_condition=qwen14 / model=qwen2.5-Coder:14b | PASS | PASS | — | — | — | — | [R-ec447baf868b50](#r-ec447baf868b50) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-5ccb53488a8e80"></a>
### 根拠 R-5ccb53488a8e80

- 対応方法: 同一セット・課題IDによる対応
- 出典: `summaries/development-local-terminal-001.json` / 位置: `/models/qwen14/development/2`
- 出典ファイルのSHA-256: `5de0e6e03c550e6ba2aecff5c6da7dc9eba39d17d33d744e81c61761f4eb64e5`
- [抽出した測定値・他の工程の記録](../results/local-specialist-economics.json)

<a id="r-ec447baf868b50"></a>
### 根拠 R-ec447baf868b50

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `local/qwen14/development/workspace/records/router-v2.2/LSE-003/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `bf495e2ccb0aa2d7c3819b2fe150dab17b195168acd0719f165cc3903b1fda7b`
- [抽出した測定値・他の工程の記録](../results/local-specialist-economics.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Return (nonempty warnings in original order, number of exactly empty warning strings). Preserve duplicates and whitespace-only warnings; empty means byte length zero, not trimmed empty.",
    "Use only state.warnings; do not mutate state, deduplicate, infer errors or consult processes_truncated.",
    "Existing workspace behavior remains valid.",
    "Rust formatting remains clean.",
    "No clippy warnings.",
    "All workspace tests remain valid.",
    "Workspace type checking succeeds.",
    "Workspace build succeeds.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "Return (nonempty warnings in original order, number of exactly empty warning strings). Preserve duplicates and whitespace-only warnings; empty means byte length zero, not trimmed empty.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Use only state.warnings; do not mutate state, deduplicate, infer errors or consult processes_truncated.",
      "category": "functional"
    },
    {
      "criterion_id": "REGRESSION",
      "criterion_text": "Existing workspace behavior remains valid.",
      "category": "quality"
    },
    {
      "criterion_id": "FORMAT",
      "criterion_text": "Rust formatting remains clean.",
      "category": "quality"
    },
    {
      "criterion_id": "CLIPPY",
      "criterion_text": "No clippy warnings.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-TEST",
      "criterion_text": "All workspace tests remain valid.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-CHECK",
      "criterion_text": "Workspace type checking succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-BUILD",
      "criterion_text": "Workspace build succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "SCOPE",
      "criterion_text": "Only declared editable regions change; protected source and tests remain identical.",
      "category": "structural"
    }
  ],
  "checks": [
    {
      "id": "acceptance",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-003",
      "timeout_seconds": 330,
      "required_test_ids": [
        "economic_lse_003"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--lib",
        "economic_lse_003",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "regression",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-003",
      "timeout_seconds": 330,
      "required_test_ids": [
        "event_detect"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--test",
        "acceptance",
        "event_detect",
        "--",
        "--exact"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/LSE-003",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "fmt",
        "--check"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "clippy",
      "kind": "lint",
      "cwd": "units/LSE-003",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "clippy",
        "--offline",
        "--all-targets",
        "--all-features",
        "--",
        "-D",
        "warnings"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-test",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-003",
      "timeout_seconds": 330,
      "required_test_ids": [
        "event_detect"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--workspace",
        "--offline",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-check",
      "kind": "typecheck",
      "cwd": "units/LSE-003",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "check",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-build",
      "kind": "build",
      "cwd": "units/LSE-003",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "build",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    }
  ]
}
```

</details>

<a id="lse-004"></a>
## LSE-004

Replace repeated event keys in their first-seen display positions

元のtask_id: `LSE-004`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Each (kind,target) exact pair owns its first-seen output position. A later matching pair replaces that entire stored Event with the later clone, without changing slot order. Distinct kinds sharing a target are separate keys. Do not merge evidence, sort, refresh positions, or mutate input. Empty input returns empty. Preserve sampled_warning_total behavior.

取り出し方:

```sh
python materialize_task.py --set local-specialist-economics --task LSE-004 --output work/LSE-004
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| コードの検証 | model_key=qwen14 / partition=development | ESCALATE | — | — | — | — | — | [R-5d15a80a318786](#r-5d15a80a318786) |
| ローカル実装 | local_condition=qwen14 / model=qwen2.5-Coder:14b | ESCALATE | ESCALATE | — | — | — | — | [R-9a16e5806debd0](#r-9a16e5806debd0) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-5d15a80a318786"></a>
### 根拠 R-5d15a80a318786

- 対応方法: 同一セット・課題IDによる対応
- 出典: `summaries/development-local-terminal-001.json` / 位置: `/models/qwen14/development/3`
- 出典ファイルのSHA-256: `5de0e6e03c550e6ba2aecff5c6da7dc9eba39d17d33d744e81c61761f4eb64e5`
- [抽出した測定値・他の工程の記録](../results/local-specialist-economics.json)

<a id="r-9a16e5806debd0"></a>
### 根拠 R-9a16e5806debd0

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `local/qwen14/development/workspace/records/router-v2.2/LSE-004/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `ac9e64513836fa361bd5580bf2c758d233f26a3f428e6849cb689308a267d218`
- [抽出した測定値・他の工程の記録](../results/local-specialist-economics.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Each (kind,target) exact pair owns its first-seen output position. A later matching pair replaces that entire stored Event with the later clone, without changing slot order. Distinct kinds sharing a target are separate keys.",
    "Do not merge evidence, sort, refresh positions, or mutate input. Empty input returns empty. Preserve sampled_warning_total behavior.",
    "Existing workspace behavior remains valid.",
    "Rust formatting remains clean.",
    "No clippy warnings.",
    "All workspace tests remain valid.",
    "Workspace type checking succeeds.",
    "Workspace build succeeds.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "Each (kind,target) exact pair owns its first-seen output position. A later matching pair replaces that entire stored Event with the later clone, without changing slot order. Distinct kinds sharing a target are separate keys.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Do not merge evidence, sort, refresh positions, or mutate input. Empty input returns empty. Preserve sampled_warning_total behavior.",
      "category": "functional"
    },
    {
      "criterion_id": "REGRESSION",
      "criterion_text": "Existing workspace behavior remains valid.",
      "category": "quality"
    },
    {
      "criterion_id": "FORMAT",
      "criterion_text": "Rust formatting remains clean.",
      "category": "quality"
    },
    {
      "criterion_id": "CLIPPY",
      "criterion_text": "No clippy warnings.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-TEST",
      "criterion_text": "All workspace tests remain valid.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-CHECK",
      "criterion_text": "Workspace type checking succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-BUILD",
      "criterion_text": "Workspace build succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "SCOPE",
      "criterion_text": "Only declared editable regions change; protected source and tests remain identical.",
      "category": "structural"
    }
  ],
  "checks": [
    {
      "id": "acceptance",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-004",
      "timeout_seconds": 330,
      "required_test_ids": [
        "economic_lse_004"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--lib",
        "economic_lse_004",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "regression",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-004",
      "timeout_seconds": 330,
      "required_test_ids": [
        "event_detect"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--test",
        "acceptance",
        "event_detect",
        "--",
        "--exact"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/LSE-004",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "fmt",
        "--check"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "clippy",
      "kind": "lint",
      "cwd": "units/LSE-004",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "clippy",
        "--offline",
        "--all-targets",
        "--all-features",
        "--",
        "-D",
        "warnings"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-test",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-004",
      "timeout_seconds": 330,
      "required_test_ids": [
        "event_detect"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--workspace",
        "--offline",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-check",
      "kind": "typecheck",
      "cwd": "units/LSE-004",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "check",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-build",
      "kind": "build",
      "cwd": "units/LSE-004",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "build",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    }
  ]
}
```

</details>

<a id="lse-005"></a>
## LSE-005

Remove overflow in rounded-up audit elapsed seconds

元のtask_id: `LSE-005`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Fix the existing overflow while preserving ceil(elapsed_ms/1000) for every u128 input, including u128::MAX. Integer exact result, no floats or saturating numerator that loses a final second. Zero returns zero; exact multiples do not round up. Preserve the signature and all surrounding behavior.

取り出し方:

```sh
python materialize_task.py --set local-specialist-economics --task LSE-005 --output work/LSE-005
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| コードの検証 | model_key=qwen14 / partition=development | ESCALATE | — | — | — | — | — | [R-4b5928d7a6fcf3](#r-4b5928d7a6fcf3) |
| ローカル実装 | local_condition=qwen14 / model=qwen2.5-Coder:14b | ESCALATE | ESCALATE | — | — | — | — | [R-875fc3a90bd593](#r-875fc3a90bd593) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-4b5928d7a6fcf3"></a>
### 根拠 R-4b5928d7a6fcf3

- 対応方法: 同一セット・課題IDによる対応
- 出典: `summaries/development-local-terminal-001.json` / 位置: `/models/qwen14/development/4`
- 出典ファイルのSHA-256: `5de0e6e03c550e6ba2aecff5c6da7dc9eba39d17d33d744e81c61761f4eb64e5`
- [抽出した測定値・他の工程の記録](../results/local-specialist-economics.json)

<a id="r-875fc3a90bd593"></a>
### 根拠 R-875fc3a90bd593

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `local/qwen14/development/workspace/records/router-v2.2/LSE-005/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `a8bbf3a0d6cb0a1c3f7e3cf6705b3de63f771994678bfd2935dc21e1bfca77d7`
- [抽出した測定値・他の工程の記録](../results/local-specialist-economics.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Fix the existing overflow while preserving ceil(elapsed_ms/1000) for every u128 input, including u128::MAX. Integer exact result, no floats or saturating numerator that loses a final second.",
    "Zero returns zero; exact multiples do not round up. Preserve the signature and all surrounding behavior.",
    "Existing workspace behavior remains valid.",
    "Rust formatting remains clean.",
    "No clippy warnings.",
    "All workspace tests remain valid.",
    "Workspace type checking succeeds.",
    "Workspace build succeeds.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "Fix the existing overflow while preserving ceil(elapsed_ms/1000) for every u128 input, including u128::MAX. Integer exact result, no floats or saturating numerator that loses a final second.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Zero returns zero; exact multiples do not round up. Preserve the signature and all surrounding behavior.",
      "category": "functional"
    },
    {
      "criterion_id": "REGRESSION",
      "criterion_text": "Existing workspace behavior remains valid.",
      "category": "quality"
    },
    {
      "criterion_id": "FORMAT",
      "criterion_text": "Rust formatting remains clean.",
      "category": "quality"
    },
    {
      "criterion_id": "CLIPPY",
      "criterion_text": "No clippy warnings.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-TEST",
      "criterion_text": "All workspace tests remain valid.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-CHECK",
      "criterion_text": "Workspace type checking succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-BUILD",
      "criterion_text": "Workspace build succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "SCOPE",
      "criterion_text": "Only declared editable regions change; protected source and tests remain identical.",
      "category": "structural"
    }
  ],
  "checks": [
    {
      "id": "acceptance",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-005",
      "timeout_seconds": 330,
      "required_test_ids": [
        "economic_lse_005"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--lib",
        "economic_lse_005",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "regression",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-005",
      "timeout_seconds": 330,
      "required_test_ids": [
        "event_detect"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--test",
        "acceptance",
        "event_detect",
        "--",
        "--exact"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/LSE-005",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "fmt",
        "--check"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "clippy",
      "kind": "lint",
      "cwd": "units/LSE-005",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "clippy",
        "--offline",
        "--all-targets",
        "--all-features",
        "--",
        "-D",
        "warnings"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-test",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-005",
      "timeout_seconds": 330,
      "required_test_ids": [
        "event_detect"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--workspace",
        "--offline",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-check",
      "kind": "typecheck",
      "cwd": "units/LSE-005",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "check",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-build",
      "kind": "build",
      "cwd": "units/LSE-005",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "build",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    }
  ]
}
```

</details>

<a id="lse-006"></a>
## LSE-006

Compute affordable future recorded calls from two independent limits

元のtask_id: `LSE-006`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Return the smaller of remaining inference-call slots and floor(remaining token allowance/tokens_per_call). Subtraction saturates independently. Zero per-call token price imposes no token limit, so only remaining call slots apply. Ignore latency and preferred model class. Use only supplied counters, never grant execution authority or mutate them. Avoid overflow/narrowing for every u64/u32 input.

取り出し方:

```sh
python materialize_task.py --set local-specialist-economics --task LSE-006 --output work/LSE-006
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| コードの検証 | model_key=qwen14 / partition=development | ESCALATE | — | — | — | — | — | [R-614e6c5a0e5f3d](#r-614e6c5a0e5f3d) |
| ローカル実装 | local_condition=qwen14 / model=qwen2.5-Coder:14b | ESCALATE | ESCALATE | — | — | — | — | [R-1db15c3cd6baf0](#r-1db15c3cd6baf0) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-614e6c5a0e5f3d"></a>
### 根拠 R-614e6c5a0e5f3d

- 対応方法: 同一セット・課題IDによる対応
- 出典: `summaries/development-local-terminal-001.json` / 位置: `/models/qwen14/development/5`
- 出典ファイルのSHA-256: `5de0e6e03c550e6ba2aecff5c6da7dc9eba39d17d33d744e81c61761f4eb64e5`
- [抽出した測定値・他の工程の記録](../results/local-specialist-economics.json)

<a id="r-1db15c3cd6baf0"></a>
### 根拠 R-1db15c3cd6baf0

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `local/qwen14/development/workspace/records/router-v2.2/LSE-006/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `123d10d5e3d08a03232492ac3b065a0657a8b6f68fa0054f1eb17466afcba763`
- [抽出した測定値・他の工程の記録](../results/local-specialist-economics.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Return the smaller of remaining inference-call slots and floor(remaining token allowance/tokens_per_call). Subtraction saturates independently. Zero per-call token price imposes no token limit, so only remaining call slots apply.",
    "Ignore latency and preferred model class. Use only supplied counters, never grant execution authority or mutate them. Avoid overflow/narrowing for every u64/u32 input.",
    "Existing workspace behavior remains valid.",
    "Rust formatting remains clean.",
    "No clippy warnings.",
    "All workspace tests remain valid.",
    "Workspace type checking succeeds.",
    "Workspace build succeeds.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "Return the smaller of remaining inference-call slots and floor(remaining token allowance/tokens_per_call). Subtraction saturates independently. Zero per-call token price imposes no token limit, so only remaining call slots apply.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Ignore latency and preferred model class. Use only supplied counters, never grant execution authority or mutate them. Avoid overflow/narrowing for every u64/u32 input.",
      "category": "functional"
    },
    {
      "criterion_id": "REGRESSION",
      "criterion_text": "Existing workspace behavior remains valid.",
      "category": "quality"
    },
    {
      "criterion_id": "FORMAT",
      "criterion_text": "Rust formatting remains clean.",
      "category": "quality"
    },
    {
      "criterion_id": "CLIPPY",
      "criterion_text": "No clippy warnings.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-TEST",
      "criterion_text": "All workspace tests remain valid.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-CHECK",
      "criterion_text": "Workspace type checking succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-BUILD",
      "criterion_text": "Workspace build succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "SCOPE",
      "criterion_text": "Only declared editable regions change; protected source and tests remain identical.",
      "category": "structural"
    }
  ],
  "checks": [
    {
      "id": "acceptance",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-006",
      "timeout_seconds": 330,
      "required_test_ids": [
        "economic_lse_006"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--lib",
        "economic_lse_006",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "regression",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-006",
      "timeout_seconds": 330,
      "required_test_ids": [
        "event_detect"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--test",
        "acceptance",
        "event_detect",
        "--",
        "--exact"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/LSE-006",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "fmt",
        "--check"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "clippy",
      "kind": "lint",
      "cwd": "units/LSE-006",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "clippy",
        "--offline",
        "--all-targets",
        "--all-features",
        "--",
        "-D",
        "warnings"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-test",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-006",
      "timeout_seconds": 330,
      "required_test_ids": [
        "event_detect"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--workspace",
        "--offline",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-check",
      "kind": "typecheck",
      "cwd": "units/LSE-006",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "check",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-build",
      "kind": "build",
      "cwd": "units/LSE-006",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "build",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    }
  ]
}
```

</details>

<a id="lse-007"></a>
## LSE-007

Consolidate risk rendering through the existing helper

元のtask_id: `LSE-007`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact before->after lowercase risk rendering for every Risk pair. Refactor the two duplicated match tables to the existing protected risk_word helper for both values. No match expression or duplicate risk-label literals may remain inside the editable body. Do not change the helper, interface, markers or other source.

取り出し方:

```sh
python materialize_task.py --set local-specialist-economics --task LSE-007 --output work/LSE-007
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| コードの検証 | model_key=qwen14 / partition=development | ESCALATE | — | — | — | — | — | [R-5af3f7610722f6](#r-5af3f7610722f6) |
| ローカル実装 | local_condition=qwen14 / model=qwen2.5-Coder:14b | ESCALATE | ESCALATE | — | — | — | — | [R-64c9470ba23d08](#r-64c9470ba23d08) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-5af3f7610722f6"></a>
### 根拠 R-5af3f7610722f6

- 対応方法: 同一セット・課題IDによる対応
- 出典: `summaries/development-local-terminal-001.json` / 位置: `/models/qwen14/development/6`
- 出典ファイルのSHA-256: `5de0e6e03c550e6ba2aecff5c6da7dc9eba39d17d33d744e81c61761f4eb64e5`
- [抽出した測定値・他の工程の記録](../results/local-specialist-economics.json)

<a id="r-64c9470ba23d08"></a>
### 根拠 R-64c9470ba23d08

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `local/qwen14/development/workspace/records/router-v2.2/LSE-007/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `61fb490ecf1cea34754931b947b96d6bcaab6be28bb6e6dc579c285a1cae5ff1`
- [抽出した測定値・他の工程の記録](../results/local-specialist-economics.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact before->after lowercase risk rendering for every Risk pair. Refactor the two duplicated match tables to the existing protected risk_word helper for both values.",
    "No match expression or duplicate risk-label literals may remain inside the editable body. Do not change the helper, interface, markers or other source.",
    "Existing workspace behavior remains valid.",
    "Rust formatting remains clean.",
    "No clippy warnings.",
    "All workspace tests remain valid.",
    "Workspace type checking succeeds.",
    "Workspace build succeeds.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "Preserve exact before->after lowercase risk rendering for every Risk pair. Refactor the two duplicated match tables to the existing protected risk_word helper for both values.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "No match expression or duplicate risk-label literals may remain inside the editable body. Do not change the helper, interface, markers or other source.",
      "category": "functional"
    },
    {
      "criterion_id": "REGRESSION",
      "criterion_text": "Existing workspace behavior remains valid.",
      "category": "quality"
    },
    {
      "criterion_id": "FORMAT",
      "criterion_text": "Rust formatting remains clean.",
      "category": "quality"
    },
    {
      "criterion_id": "CLIPPY",
      "criterion_text": "No clippy warnings.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-TEST",
      "criterion_text": "All workspace tests remain valid.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-CHECK",
      "criterion_text": "Workspace type checking succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-BUILD",
      "criterion_text": "Workspace build succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "SCOPE",
      "criterion_text": "Only declared editable regions change; protected source and tests remain identical.",
      "category": "structural"
    }
  ],
  "checks": [
    {
      "id": "acceptance",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-007",
      "timeout_seconds": 330,
      "required_test_ids": [
        "economic_lse_007"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--lib",
        "economic_lse_007",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "regression",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-007",
      "timeout_seconds": 330,
      "required_test_ids": [
        "event_detect"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--test",
        "acceptance",
        "event_detect",
        "--",
        "--exact"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/LSE-007",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "fmt",
        "--check"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "clippy",
      "kind": "lint",
      "cwd": "units/LSE-007",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "clippy",
        "--offline",
        "--all-targets",
        "--all-features",
        "--",
        "-D",
        "warnings"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-test",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-007",
      "timeout_seconds": 330,
      "required_test_ids": [
        "event_detect"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--workspace",
        "--offline",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-check",
      "kind": "typecheck",
      "cwd": "units/LSE-007",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "check",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-build",
      "kind": "build",
      "cwd": "units/LSE-007",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "build",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    }
  ]
}
```

</details>

<a id="lse-008"></a>
## LSE-008

Serialize a process sample as an exact line manifest

元のtask_id: `LSE-008`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Emit each supplied row as pid@parent_pid=rss_kib followed by one LF, unsigned decimal with no leading zeros or spaces. Preserve input order and duplicate rows; include zero values. Empty slice returns empty string. No headers, units, CR, sorting, truncation or input mutation. Include the final LF for nonempty input.

取り出し方:

```sh
python materialize_task.py --set local-specialist-economics --task LSE-008 --output work/LSE-008
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| コードの検証 | 記録に条件の明記なし | ESCALATE | — | — | — | — | — | [R-114a15ef8e7e2a](#r-114a15ef8e7e2a) |
| ローカル実装 | local_condition=qwen14 / model=qwen2.5-Coder:14b | ESCALATE | ESCALATE | — | — | — | — | [R-5b075b324408d7](#r-5b075b324408d7) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-114a15ef8e7e2a"></a>
### 根拠 R-114a15ef8e7e2a

- 対応方法: 同一セット・課題IDによる対応
- 出典: `summaries/held-out-local-terminal-001.json` / 位置: `/native_results/0`
- 出典ファイルのSHA-256: `9b8f061fbc358096a542b3b67818d6a474b24ffdc059a300e7732077936f5782`
- [抽出した測定値・他の工程の記録](../results/local-specialist-economics.json)

<a id="r-5b075b324408d7"></a>
### 根拠 R-5b075b324408d7

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `local/qwen14/held_out/workspace/records/router-v2.2/LSE-008/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `512aba994a123e1ec5d4e3fe7b599c60cb6d019920af4d1b52e62bdc228b3b36`
- [抽出した測定値・他の工程の記録](../results/local-specialist-economics.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Emit each supplied row as pid@parent_pid=rss_kib followed by one LF, unsigned decimal with no leading zeros or spaces. Preserve input order and duplicate rows; include zero values. Empty slice returns empty string.",
    "No headers, units, CR, sorting, truncation or input mutation. Include the final LF for nonempty input.",
    "Existing workspace behavior remains valid.",
    "Rust formatting remains clean.",
    "No clippy warnings.",
    "All workspace tests remain valid.",
    "Workspace type checking succeeds.",
    "Workspace build succeeds.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "Emit each supplied row as pid@parent_pid=rss_kib followed by one LF, unsigned decimal with no leading zeros or spaces. Preserve input order and duplicate rows; include zero values. Empty slice returns empty string.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "No headers, units, CR, sorting, truncation or input mutation. Include the final LF for nonempty input.",
      "category": "functional"
    },
    {
      "criterion_id": "REGRESSION",
      "criterion_text": "Existing workspace behavior remains valid.",
      "category": "quality"
    },
    {
      "criterion_id": "FORMAT",
      "criterion_text": "Rust formatting remains clean.",
      "category": "quality"
    },
    {
      "criterion_id": "CLIPPY",
      "criterion_text": "No clippy warnings.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-TEST",
      "criterion_text": "All workspace tests remain valid.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-CHECK",
      "criterion_text": "Workspace type checking succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-BUILD",
      "criterion_text": "Workspace build succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "SCOPE",
      "criterion_text": "Only declared editable regions change; protected source and tests remain identical.",
      "category": "structural"
    }
  ],
  "checks": [
    {
      "id": "acceptance",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-008",
      "timeout_seconds": 330,
      "required_test_ids": [
        "economic_lse_008"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--lib",
        "economic_lse_008",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "regression",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-008",
      "timeout_seconds": 330,
      "required_test_ids": [
        "event_detect"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--test",
        "acceptance",
        "event_detect",
        "--",
        "--exact"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/LSE-008",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "fmt",
        "--check"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "clippy",
      "kind": "lint",
      "cwd": "units/LSE-008",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "clippy",
        "--offline",
        "--all-targets",
        "--all-features",
        "--",
        "-D",
        "warnings"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-test",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-008",
      "timeout_seconds": 330,
      "required_test_ids": [
        "event_detect"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--workspace",
        "--offline",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-check",
      "kind": "typecheck",
      "cwd": "units/LSE-008",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "check",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-build",
      "kind": "build",
      "cwd": "units/LSE-008",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "build",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    }
  ]
}
```

</details>

<a id="lse-009"></a>
## LSE-009

Collect dry-run proposals lacking successful verification

元のtask_id: `LSE-009`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Return a clone of the entire proposal for each record with proposal present, execution present with DryRun status, and verification absent or passed=false. Preserve order and duplicates; Blocked or absent execution is omitted. Ignore execution.changed, policy, event and verification.scope/detail. Preserve all proposal fields and input records.

取り出し方:

```sh
python materialize_task.py --set local-specialist-economics --task LSE-009 --output work/LSE-009
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| コードの検証 | 記録に条件の明記なし | ESCALATE | — | — | — | — | — | [R-ef22a86e33362f](#r-ef22a86e33362f) |
| ローカル実装 | local_condition=qwen14 / model=qwen2.5-Coder:14b | ESCALATE | ESCALATE | — | — | — | — | [R-7c2d609f366bff](#r-7c2d609f366bff) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-ef22a86e33362f"></a>
### 根拠 R-ef22a86e33362f

- 対応方法: 同一セット・課題IDによる対応
- 出典: `summaries/held-out-local-terminal-001.json` / 位置: `/native_results/1`
- 出典ファイルのSHA-256: `9b8f061fbc358096a542b3b67818d6a474b24ffdc059a300e7732077936f5782`
- [抽出した測定値・他の工程の記録](../results/local-specialist-economics.json)

<a id="r-7c2d609f366bff"></a>
### 根拠 R-7c2d609f366bff

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `local/qwen14/held_out/workspace/records/router-v2.2/LSE-009/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `d928c6b82b843aec50c7b6abd9b6edc6a1d7bc02b7858fb4638e42c29b25a05a`
- [抽出した測定値・他の工程の記録](../results/local-specialist-economics.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Return a clone of the entire proposal for each record with proposal present, execution present with DryRun status, and verification absent or passed=false. Preserve order and duplicates; Blocked or absent execution is omitted.",
    "Ignore execution.changed, policy, event and verification.scope/detail. Preserve all proposal fields and input records.",
    "Existing workspace behavior remains valid.",
    "Rust formatting remains clean.",
    "No clippy warnings.",
    "All workspace tests remain valid.",
    "Workspace type checking succeeds.",
    "Workspace build succeeds.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "Return a clone of the entire proposal for each record with proposal present, execution present with DryRun status, and verification absent or passed=false. Preserve order and duplicates; Blocked or absent execution is omitted.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Ignore execution.changed, policy, event and verification.scope/detail. Preserve all proposal fields and input records.",
      "category": "functional"
    },
    {
      "criterion_id": "REGRESSION",
      "criterion_text": "Existing workspace behavior remains valid.",
      "category": "quality"
    },
    {
      "criterion_id": "FORMAT",
      "criterion_text": "Rust formatting remains clean.",
      "category": "quality"
    },
    {
      "criterion_id": "CLIPPY",
      "criterion_text": "No clippy warnings.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-TEST",
      "criterion_text": "All workspace tests remain valid.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-CHECK",
      "criterion_text": "Workspace type checking succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-BUILD",
      "criterion_text": "Workspace build succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "SCOPE",
      "criterion_text": "Only declared editable regions change; protected source and tests remain identical.",
      "category": "structural"
    }
  ],
  "checks": [
    {
      "id": "acceptance",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-009",
      "timeout_seconds": 330,
      "required_test_ids": [
        "economic_lse_009"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--lib",
        "economic_lse_009",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "regression",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-009",
      "timeout_seconds": 330,
      "required_test_ids": [
        "event_detect"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--test",
        "acceptance",
        "event_detect",
        "--",
        "--exact"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/LSE-009",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "fmt",
        "--check"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "clippy",
      "kind": "lint",
      "cwd": "units/LSE-009",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "clippy",
        "--offline",
        "--all-targets",
        "--all-features",
        "--",
        "-D",
        "warnings"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-test",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-009",
      "timeout_seconds": 330,
      "required_test_ids": [
        "event_detect"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--workspace",
        "--offline",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-check",
      "kind": "typecheck",
      "cwd": "units/LSE-009",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "check",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-build",
      "kind": "build",
      "cwd": "units/LSE-009",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "build",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    }
  ]
}
```

</details>

<a id="lse-010"></a>
## LSE-010

Separate sampled process IDs with self-parent anomalies

元のtask_id: `LSE-010`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Return PIDs for rows whose pid equals parent_pid and pid is nonzero. Preserve original order and duplicates. A 0/0 sentinel row is not an anomaly. Do not infer graph cycles, ancestors, missing parents or deduplicate; this is a direct sample projection. Do not mutate input.

取り出し方:

```sh
python materialize_task.py --set local-specialist-economics --task LSE-010 --output work/LSE-010
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| コードの検証 | 記録に条件の明記なし | ESCALATE | — | — | — | — | — | [R-11beb4b82f6b44](#r-11beb4b82f6b44) |
| ローカル実装 | local_condition=qwen14 / model=qwen2.5-Coder:14b | ESCALATE | ESCALATE | — | — | — | — | [R-c0ce8efcb12f79](#r-c0ce8efcb12f79) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-11beb4b82f6b44"></a>
### 根拠 R-11beb4b82f6b44

- 対応方法: 同一セット・課題IDによる対応
- 出典: `summaries/held-out-local-terminal-001.json` / 位置: `/native_results/2`
- 出典ファイルのSHA-256: `9b8f061fbc358096a542b3b67818d6a474b24ffdc059a300e7732077936f5782`
- [抽出した測定値・他の工程の記録](../results/local-specialist-economics.json)

<a id="r-c0ce8efcb12f79"></a>
### 根拠 R-c0ce8efcb12f79

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `local/qwen14/held_out/workspace/records/router-v2.2/LSE-010/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `4eacd40c9bc6125e951aceb8133cf21bc0c1a090b7b8cb356e15187a72a53c27`
- [抽出した測定値・他の工程の記録](../results/local-specialist-economics.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Return PIDs for rows whose pid equals parent_pid and pid is nonzero. Preserve original order and duplicates. A 0/0 sentinel row is not an anomaly.",
    "Do not infer graph cycles, ancestors, missing parents or deduplicate; this is a direct sample projection. Do not mutate input.",
    "Existing workspace behavior remains valid.",
    "Rust formatting remains clean.",
    "No clippy warnings.",
    "All workspace tests remain valid.",
    "Workspace type checking succeeds.",
    "Workspace build succeeds.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "Return PIDs for rows whose pid equals parent_pid and pid is nonzero. Preserve original order and duplicates. A 0/0 sentinel row is not an anomaly.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Do not infer graph cycles, ancestors, missing parents or deduplicate; this is a direct sample projection. Do not mutate input.",
      "category": "functional"
    },
    {
      "criterion_id": "REGRESSION",
      "criterion_text": "Existing workspace behavior remains valid.",
      "category": "quality"
    },
    {
      "criterion_id": "FORMAT",
      "criterion_text": "Rust formatting remains clean.",
      "category": "quality"
    },
    {
      "criterion_id": "CLIPPY",
      "criterion_text": "No clippy warnings.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-TEST",
      "criterion_text": "All workspace tests remain valid.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-CHECK",
      "criterion_text": "Workspace type checking succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-BUILD",
      "criterion_text": "Workspace build succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "SCOPE",
      "criterion_text": "Only declared editable regions change; protected source and tests remain identical.",
      "category": "structural"
    }
  ],
  "checks": [
    {
      "id": "acceptance",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-010",
      "timeout_seconds": 330,
      "required_test_ids": [
        "economic_lse_010"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--lib",
        "economic_lse_010",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "regression",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-010",
      "timeout_seconds": 330,
      "required_test_ids": [
        "event_detect"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--test",
        "acceptance",
        "event_detect",
        "--",
        "--exact"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/LSE-010",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "fmt",
        "--check"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "clippy",
      "kind": "lint",
      "cwd": "units/LSE-010",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "clippy",
        "--offline",
        "--all-targets",
        "--all-features",
        "--",
        "-D",
        "warnings"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-test",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-010",
      "timeout_seconds": 330,
      "required_test_ids": [
        "event_detect"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--workspace",
        "--offline",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-check",
      "kind": "typecheck",
      "cwd": "units/LSE-010",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "check",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-build",
      "kind": "build",
      "cwd": "units/LSE-010",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "build",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    }
  ]
}
```

</details>

<a id="lse-011"></a>
## LSE-011

Preview cooldown admissions without refreshing rejected timestamps

元のtask_id: `LSE-011`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Return one boolean per input timestamp. First timestamp is accepted. Later timestamps are accepted only when >= last accepted timestamp and their elapsed difference >= gap. Only accepted timestamps update the remembered timestamp; rejected or backward observations do not. Gap zero accepts equal/forward times but still rejects backward ones. Empty input -> empty. Avoid overflow at u128::MAX; no clock query, global state or input mutation. Preserve sampled_warning_total behavior.

取り出し方:

```sh
python materialize_task.py --set local-specialist-economics --task LSE-011 --output work/LSE-011
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| コードの検証 | 記録に条件の明記なし | ESCALATE | — | — | — | — | — | [R-d89089fa70e187](#r-d89089fa70e187) |
| ローカル実装 | local_condition=qwen14 / model=qwen2.5-Coder:14b | ESCALATE | ESCALATE | — | — | — | — | [R-56072cfa96b1ca](#r-56072cfa96b1ca) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-d89089fa70e187"></a>
### 根拠 R-d89089fa70e187

- 対応方法: 同一セット・課題IDによる対応
- 出典: `summaries/held-out-local-terminal-001.json` / 位置: `/native_results/3`
- 出典ファイルのSHA-256: `9b8f061fbc358096a542b3b67818d6a474b24ffdc059a300e7732077936f5782`
- [抽出した測定値・他の工程の記録](../results/local-specialist-economics.json)

<a id="r-56072cfa96b1ca"></a>
### 根拠 R-56072cfa96b1ca

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `local/qwen14/held_out/workspace/records/router-v2.2/LSE-011/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `4e5c63bd1c8370c11d2c5a3eac3046ea99af769c12127390200c031215d893cd`
- [抽出した測定値・他の工程の記録](../results/local-specialist-economics.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Return one boolean per input timestamp. First timestamp is accepted. Later timestamps are accepted only when >= last accepted timestamp and their elapsed difference >= gap. Only accepted timestamps update the remembered timestamp; rejected or backward observations do not.",
    "Gap zero accepts equal/forward times but still rejects backward ones. Empty input -> empty. Avoid overflow at u128::MAX; no clock query, global state or input mutation. Preserve sampled_warning_total behavior.",
    "Existing workspace behavior remains valid.",
    "Rust formatting remains clean.",
    "No clippy warnings.",
    "All workspace tests remain valid.",
    "Workspace type checking succeeds.",
    "Workspace build succeeds.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "Return one boolean per input timestamp. First timestamp is accepted. Later timestamps are accepted only when >= last accepted timestamp and their elapsed difference >= gap. Only accepted timestamps update the remembered timestamp; rejected or backward observations do not.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Gap zero accepts equal/forward times but still rejects backward ones. Empty input -> empty. Avoid overflow at u128::MAX; no clock query, global state or input mutation. Preserve sampled_warning_total behavior.",
      "category": "functional"
    },
    {
      "criterion_id": "REGRESSION",
      "criterion_text": "Existing workspace behavior remains valid.",
      "category": "quality"
    },
    {
      "criterion_id": "FORMAT",
      "criterion_text": "Rust formatting remains clean.",
      "category": "quality"
    },
    {
      "criterion_id": "CLIPPY",
      "criterion_text": "No clippy warnings.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-TEST",
      "criterion_text": "All workspace tests remain valid.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-CHECK",
      "criterion_text": "Workspace type checking succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-BUILD",
      "criterion_text": "Workspace build succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "SCOPE",
      "criterion_text": "Only declared editable regions change; protected source and tests remain identical.",
      "category": "structural"
    }
  ],
  "checks": [
    {
      "id": "acceptance",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-011",
      "timeout_seconds": 330,
      "required_test_ids": [
        "economic_lse_011"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--lib",
        "economic_lse_011",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "regression",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-011",
      "timeout_seconds": 330,
      "required_test_ids": [
        "event_detect"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--test",
        "acceptance",
        "event_detect",
        "--",
        "--exact"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/LSE-011",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "fmt",
        "--check"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "clippy",
      "kind": "lint",
      "cwd": "units/LSE-011",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "clippy",
        "--offline",
        "--all-targets",
        "--all-features",
        "--",
        "-D",
        "warnings"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-test",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-011",
      "timeout_seconds": 330,
      "required_test_ids": [
        "event_detect"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--workspace",
        "--offline",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-check",
      "kind": "typecheck",
      "cwd": "units/LSE-011",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "check",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-build",
      "kind": "build",
      "cwd": "units/LSE-011",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "build",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    }
  ]
}
```

</details>

<a id="lse-012"></a>
## LSE-012

Preserve signed TCP sample decreases and unknown samples

元のtask_id: `LSE-012`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Fix the existing loss of negative change. Return after-before as signed i128 when both samples are Some, including decreases and equal values. None in either position returns None. No saturation, wrapping, float conversion or interpreting unknown as zero. Full usize range must be representable exactly. This is a display delta only.

取り出し方:

```sh
python materialize_task.py --set local-specialist-economics --task LSE-012 --output work/LSE-012
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| コードの検証 | 記録に条件の明記なし | ESCALATE | — | — | — | — | — | [R-328ea0dca7fcad](#r-328ea0dca7fcad) |
| ローカル実装 | local_condition=qwen14 / model=qwen2.5-Coder:14b | ESCALATE | ESCALATE | — | — | — | — | [R-f802c984336149](#r-f802c984336149) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-328ea0dca7fcad"></a>
### 根拠 R-328ea0dca7fcad

- 対応方法: 同一セット・課題IDによる対応
- 出典: `summaries/held-out-local-terminal-001.json` / 位置: `/native_results/4`
- 出典ファイルのSHA-256: `9b8f061fbc358096a542b3b67818d6a474b24ffdc059a300e7732077936f5782`
- [抽出した測定値・他の工程の記録](../results/local-specialist-economics.json)

<a id="r-f802c984336149"></a>
### 根拠 R-f802c984336149

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `local/qwen14/held_out/workspace/records/router-v2.2/LSE-012/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `5112809ef3ff08f88840c8c7d12667704ac6e239c821ce07741c4e7e43538162`
- [抽出した測定値・他の工程の記録](../results/local-specialist-economics.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Fix the existing loss of negative change. Return after-before as signed i128 when both samples are Some, including decreases and equal values. None in either position returns None.",
    "No saturation, wrapping, float conversion or interpreting unknown as zero. Full usize range must be representable exactly. This is a display delta only.",
    "Existing workspace behavior remains valid.",
    "Rust formatting remains clean.",
    "No clippy warnings.",
    "All workspace tests remain valid.",
    "Workspace type checking succeeds.",
    "Workspace build succeeds.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "Fix the existing loss of negative change. Return after-before as signed i128 when both samples are Some, including decreases and equal values. None in either position returns None.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "No saturation, wrapping, float conversion or interpreting unknown as zero. Full usize range must be representable exactly. This is a display delta only.",
      "category": "functional"
    },
    {
      "criterion_id": "REGRESSION",
      "criterion_text": "Existing workspace behavior remains valid.",
      "category": "quality"
    },
    {
      "criterion_id": "FORMAT",
      "criterion_text": "Rust formatting remains clean.",
      "category": "quality"
    },
    {
      "criterion_id": "CLIPPY",
      "criterion_text": "No clippy warnings.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-TEST",
      "criterion_text": "All workspace tests remain valid.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-CHECK",
      "criterion_text": "Workspace type checking succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-BUILD",
      "criterion_text": "Workspace build succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "SCOPE",
      "criterion_text": "Only declared editable regions change; protected source and tests remain identical.",
      "category": "structural"
    }
  ],
  "checks": [
    {
      "id": "acceptance",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-012",
      "timeout_seconds": 330,
      "required_test_ids": [
        "economic_lse_012"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--lib",
        "economic_lse_012",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "regression",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-012",
      "timeout_seconds": 330,
      "required_test_ids": [
        "event_detect"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--test",
        "acceptance",
        "event_detect",
        "--",
        "--exact"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/LSE-012",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "fmt",
        "--check"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "clippy",
      "kind": "lint",
      "cwd": "units/LSE-012",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "clippy",
        "--offline",
        "--all-targets",
        "--all-features",
        "--",
        "-D",
        "warnings"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-test",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-012",
      "timeout_seconds": 330,
      "required_test_ids": [
        "event_detect"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--workspace",
        "--offline",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-check",
      "kind": "typecheck",
      "cwd": "units/LSE-012",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "check",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-build",
      "kind": "build",
      "cwd": "units/LSE-012",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "build",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    }
  ]
}
```

</details>

<a id="lse-013"></a>
## LSE-013

Select an ordered evidence prefix under a byte allowance

元のtask_id: `LSE-013`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Return the largest prefix length whose cumulative byte lengths do not exceed capacity. Stop at the first item that does not fit; never skip it to include later small items. Zero-length items consume no capacity and count if reached. Use exact unsigned accounting without overflow, including usize::MAX entries/capacity. Empty input -> 0. Do not reorder or mutate lengths.

取り出し方:

```sh
python materialize_task.py --set local-specialist-economics --task LSE-013 --output work/LSE-013
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| コードの検証 | 記録に条件の明記なし | ESCALATE | — | — | — | — | — | [R-901c85807382a7](#r-901c85807382a7) |
| ローカル実装 | local_condition=qwen14 / model=qwen2.5-Coder:14b | ESCALATE | ESCALATE | — | — | — | — | [R-78a6a6337bd5bc](#r-78a6a6337bd5bc) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-901c85807382a7"></a>
### 根拠 R-901c85807382a7

- 対応方法: 同一セット・課題IDによる対応
- 出典: `summaries/held-out-local-terminal-001.json` / 位置: `/native_results/5`
- 出典ファイルのSHA-256: `9b8f061fbc358096a542b3b67818d6a474b24ffdc059a300e7732077936f5782`
- [抽出した測定値・他の工程の記録](../results/local-specialist-economics.json)

<a id="r-78a6a6337bd5bc"></a>
### 根拠 R-78a6a6337bd5bc

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `local/qwen14/held_out/workspace/records/router-v2.2/LSE-013/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `ef36a99a4875f37e130c36e58babcb90d35418e27917e8d4da1f07c9a7693fa9`
- [抽出した測定値・他の工程の記録](../results/local-specialist-economics.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Return the largest prefix length whose cumulative byte lengths do not exceed capacity. Stop at the first item that does not fit; never skip it to include later small items. Zero-length items consume no capacity and count if reached.",
    "Use exact unsigned accounting without overflow, including usize::MAX entries/capacity. Empty input -> 0. Do not reorder or mutate lengths.",
    "Existing workspace behavior remains valid.",
    "Rust formatting remains clean.",
    "No clippy warnings.",
    "All workspace tests remain valid.",
    "Workspace type checking succeeds.",
    "Workspace build succeeds.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "Return the largest prefix length whose cumulative byte lengths do not exceed capacity. Stop at the first item that does not fit; never skip it to include later small items. Zero-length items consume no capacity and count if reached.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Use exact unsigned accounting without overflow, including usize::MAX entries/capacity. Empty input -> 0. Do not reorder or mutate lengths.",
      "category": "functional"
    },
    {
      "criterion_id": "REGRESSION",
      "criterion_text": "Existing workspace behavior remains valid.",
      "category": "quality"
    },
    {
      "criterion_id": "FORMAT",
      "criterion_text": "Rust formatting remains clean.",
      "category": "quality"
    },
    {
      "criterion_id": "CLIPPY",
      "criterion_text": "No clippy warnings.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-TEST",
      "criterion_text": "All workspace tests remain valid.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-CHECK",
      "criterion_text": "Workspace type checking succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-BUILD",
      "criterion_text": "Workspace build succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "SCOPE",
      "criterion_text": "Only declared editable regions change; protected source and tests remain identical.",
      "category": "structural"
    }
  ],
  "checks": [
    {
      "id": "acceptance",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-013",
      "timeout_seconds": 330,
      "required_test_ids": [
        "economic_lse_013"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--lib",
        "economic_lse_013",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "regression",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-013",
      "timeout_seconds": 330,
      "required_test_ids": [
        "event_detect"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--test",
        "acceptance",
        "event_detect",
        "--",
        "--exact"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/LSE-013",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "fmt",
        "--check"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "clippy",
      "kind": "lint",
      "cwd": "units/LSE-013",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "clippy",
        "--offline",
        "--all-targets",
        "--all-features",
        "--",
        "-D",
        "warnings"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-test",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-013",
      "timeout_seconds": 330,
      "required_test_ids": [
        "event_detect"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--workspace",
        "--offline",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-check",
      "kind": "typecheck",
      "cwd": "units/LSE-013",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "check",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-build",
      "kind": "build",
      "cwd": "units/LSE-013",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "build",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    }
  ]
}
```

</details>

<a id="lse-014"></a>
## LSE-014

Centralize paired action display labels

元のtask_id: `LSE-014`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact [left, right] rendering for every action pair, using the protected action_word helper for both labels instead of duplicated match tables. No match expression or duplicate label literals inside the editable body. Preserve protected helper/interface/source. This is display only, never execute any action.

取り出し方:

```sh
python materialize_task.py --set local-specialist-economics --task LSE-014 --output work/LSE-014
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| コードの検証 | 記録に条件の明記なし | ESCALATE | — | — | — | — | — | [R-7c6d2d8346a5d5](#r-7c6d2d8346a5d5) |
| ローカル実装 | local_condition=qwen14 / model=qwen2.5-Coder:14b | ESCALATE | ESCALATE | — | — | — | — | [R-faf8bfdd480250](#r-faf8bfdd480250) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-7c6d2d8346a5d5"></a>
### 根拠 R-7c6d2d8346a5d5

- 対応方法: 同一セット・課題IDによる対応
- 出典: `summaries/held-out-local-terminal-001.json` / 位置: `/native_results/6`
- 出典ファイルのSHA-256: `9b8f061fbc358096a542b3b67818d6a474b24ffdc059a300e7732077936f5782`
- [抽出した測定値・他の工程の記録](../results/local-specialist-economics.json)

<a id="r-faf8bfdd480250"></a>
### 根拠 R-faf8bfdd480250

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `local/qwen14/held_out/workspace/records/router-v2.2/LSE-014/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `cdb7eadb3b4015f63555f81c738efade69a741976a622f9be1315dfc82dee8d1`
- [抽出した測定値・他の工程の記録](../results/local-specialist-economics.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact [left, right] rendering for every action pair, using the protected action_word helper for both labels instead of duplicated match tables.",
    "No match expression or duplicate label literals inside the editable body. Preserve protected helper/interface/source. This is display only, never execute any action.",
    "Existing workspace behavior remains valid.",
    "Rust formatting remains clean.",
    "No clippy warnings.",
    "All workspace tests remain valid.",
    "Workspace type checking succeeds.",
    "Workspace build succeeds.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "Preserve exact [left, right] rendering for every action pair, using the protected action_word helper for both labels instead of duplicated match tables.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "No match expression or duplicate label literals inside the editable body. Preserve protected helper/interface/source. This is display only, never execute any action.",
      "category": "functional"
    },
    {
      "criterion_id": "REGRESSION",
      "criterion_text": "Existing workspace behavior remains valid.",
      "category": "quality"
    },
    {
      "criterion_id": "FORMAT",
      "criterion_text": "Rust formatting remains clean.",
      "category": "quality"
    },
    {
      "criterion_id": "CLIPPY",
      "criterion_text": "No clippy warnings.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-TEST",
      "criterion_text": "All workspace tests remain valid.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-CHECK",
      "criterion_text": "Workspace type checking succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-BUILD",
      "criterion_text": "Workspace build succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "SCOPE",
      "criterion_text": "Only declared editable regions change; protected source and tests remain identical.",
      "category": "structural"
    }
  ],
  "checks": [
    {
      "id": "acceptance",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-014",
      "timeout_seconds": 330,
      "required_test_ids": [
        "economic_lse_014"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--lib",
        "economic_lse_014",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "regression",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-014",
      "timeout_seconds": 330,
      "required_test_ids": [
        "event_detect"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--test",
        "acceptance",
        "event_detect",
        "--",
        "--exact"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/LSE-014",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "fmt",
        "--check"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "clippy",
      "kind": "lint",
      "cwd": "units/LSE-014",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "clippy",
        "--offline",
        "--all-targets",
        "--all-features",
        "--",
        "-D",
        "warnings"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-test",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/LSE-014",
      "timeout_seconds": 330,
      "required_test_ids": [
        "event_detect"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--workspace",
        "--offline",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-check",
      "kind": "typecheck",
      "cwd": "units/LSE-014",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "check",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-build",
      "kind": "build",
      "cwd": "units/LSE-014",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "build",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    }
  ]
}
```

</details>
