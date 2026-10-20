# 実装委譲の検証 / 手順-v2.2.6-fresh-tasks

セットID: `router-shadow-pilot-v2.2.6-fresh-tasks`

課題数: 11。個別記録あり: 11、個別記録未確認: 0。

[全セット一覧](../INDEX.md) / [課題定義JSON](router-shadow-pilot-v2.2.6-fresh-tasks.json) / [結果と根拠のJSON](../results/router-shadow-pilot-v2.2.6-fresh-tasks.json) / [判定の読み方](../README.md#判定の読み方)

各結果はこのセットの保存記録に対応します。収録外の別runの結果を新たに代入していません。SHA-256が記録されている結果は課題定義と照合し、それ以外は実行キー・ディレクトリ・同一セット内の一意のIDによる対応として表示しています。元の記録が過去の工程を再利用している場合、独立した再実行の結果とは扱わないでください。

参考の実験レポート: [RESULTS_JA.md](../reports/router-shadow-pilot-v2.2.6-fresh-tasks/RESULTS_JA.md)

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
  },
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
| [PFT-001](#pft-001) | CLIの累積inference時間を整数演算で秒表示 | 記録あり |
| [PFT-002](#pft-002) | 重複抑制auditが現在event IDを示す | 記録あり |
| [PFT-003](#pft-003) | CLIに実行結果DryRun/Blockedの固定labelを表示 | 記録あり |
| [PFT-004](#pft-004) | MockProviderの不足token数を診断する | 記録あり |
| [PFT-005](#pft-005) | telemetry readのUTF-8エラーをI/O欠測と区別 | 記録あり |
| [PFT-006](#pft-006) | TCP欠測warningが失敗したIP familyを列挙 | 記録あり |
| [PFT-007](#pft-007) | CLI引数エラーへinspect基準のindexを追加 | 記録あり |
| [PFT-008](#pft-008) | policy評価済みauditがproposal由来を説明 | 記録あり |
| [PFT-009](#pft-009) | proc directory識別が符号付き/zero名を受理する不具合 | 記録あり |
| [PFT-010](#pft-010) | Runtime constructorの固定容量と初期化契約をtyped抽出 | 記録あり |
| [PFT-011](#pft-011) | 長期audit閲覧におけるrecord grouping方針を決定 | 記録あり |

<a id="pft-001"></a>
## PFT-001

CLIの累積inference時間を整数演算で秒表示

元のtask_id: `PFT-001`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Implement elapsed_seconds(ms: u128) -> String. Render elapsed milliseconds as seconds with exactly three fractional digits and suffix s: 0 => 0.000 s, 1 => 0.001 s, 1001 => 1.001 s. Use exact integer quotient/remainder by 1000, supporting all u128 including MAX without overflow or floating-point precision loss. No time reading or usage mutation.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.6-fresh-tasks --task PFT-001 --output work/PFT-001
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | model=gemma4:26b | — | PASS | — | — | ACCEPT_NO_CHANGE | — | [R-d1c95b43264447](#r-d1c95b43264447) |
| コードの検証 | model=gemma4:26b | PASS | — | — | — | workspace/records/router-v2.2/PFT-001/review.json | — | [R-4b1e43b1afddea](#r-4b1e43b1afddea) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-d1c95b43264447"></a>
### 根拠 R-d1c95b43264447

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/0`
- 出典ファイルのSHA-256: `9b0ae77d9072e9d69785288674c1590e057257b3739233661f78867611283931`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.6-fresh-tasks.json)

<a id="r-4b1e43b1afddea"></a>
### 根拠 R-4b1e43b1afddea

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/0`
- 出典ファイルのSHA-256: `d229293fe33b21ace3526c27b05d93266a911b737e7efc27cb3a822a2cd64963`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.6-fresh-tasks.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Implement elapsed_seconds(ms: u128) -> String. Render elapsed milliseconds as seconds with exactly three fractional digits and suffix s: 0 => 0.000 s, 1 => 0.001 s, 1001 => 1.001 s.",
    "Use exact integer quotient/remainder by 1000, supporting all u128 including MAX without overflow or floating-point precision loss. No time reading or usage mutation.",
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
      "criterion_text": "Implement elapsed_seconds(ms: u128) -> String. Render elapsed milliseconds as seconds with exactly three fractional digits and suffix s: 0 => 0.000 s, 1 => 0.001 s, 1001 => 1.001 s.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Use exact integer quotient/remainder by 1000, supporting all u128 including MAX without overflow or floating-point precision loss. No time reading or usage mutation.",
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
      "cwd": "units/PFT-001",
      "timeout_seconds": 330,
      "required_test_ids": [
        "fresh_pft_001"
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
        "ncos-cli",
        "--bin",
        "ncos",
        "fresh_pft_001",
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
      "cwd": "units/PFT-001",
      "timeout_seconds": 330,
      "required_test_ids": [
        "demo_audit_and_refusal_to_overwrite"
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
        "ncos-cli",
        "--test",
        "cli",
        "demo_audit_and_refusal_to_overwrite",
        "--",
        "--exact"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/PFT-001",
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
      "cwd": "units/PFT-001",
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
      "cwd": "units/PFT-001",
      "timeout_seconds": 330,
      "required_test_ids": [
        "demo_audit_and_refusal_to_overwrite"
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
      "cwd": "units/PFT-001",
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
      "cwd": "units/PFT-001",
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

<a id="pft-002"></a>
## PFT-002

重複抑制auditが現在event IDを示す

元のtask_id: `PFT-002`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Locate the deduplicated audit reason argument in Runtime::handle. Append ; event_id=ID to Duplicate kind/target in bounded session window, using the current event.id exactly. The record helper expects &str for reason: borrow a formatted String if needed. Preserve dedup key/ordering, source, cloned current event, time, usage, provider calls and every other audit reason. Do not show the first-seen event ID.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.6-fresh-tasks --task PFT-002 --output work/PFT-002
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | model=gemma4:26b | — | ESCALATE | — | — | REJECT | — | [R-bc99faaaa3d819](#r-bc99faaaa3d819) |
| コードの検証 | model=gemma4:26b | ESCALATE | — | — | — | workspace/records/router-v2.2/PFT-002/review.json | — | [R-1ee7f2b0beaff3](#r-1ee7f2b0beaff3) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-bc99faaaa3d819"></a>
### 根拠 R-bc99faaaa3d819

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/1`
- 出典ファイルのSHA-256: `9b0ae77d9072e9d69785288674c1590e057257b3739233661f78867611283931`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.6-fresh-tasks.json)

<a id="r-1ee7f2b0beaff3"></a>
### 根拠 R-1ee7f2b0beaff3

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/1`
- 出典ファイルのSHA-256: `d229293fe33b21ace3526c27b05d93266a911b737e7efc27cb3a822a2cd64963`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.6-fresh-tasks.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Locate the deduplicated audit reason argument in Runtime::handle. Append ; event_id=ID to Duplicate kind/target in bounded session window, using the current event.id exactly.",
    "The record helper expects &str for reason: borrow a formatted String if needed. Preserve dedup key/ordering, source, cloned current event, time, usage, provider calls and every other audit reason. Do not show the first-seen event ID.",
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
      "criterion_text": "Locate the deduplicated audit reason argument in Runtime::handle. Append ; event_id=ID to Duplicate kind/target in bounded session window, using the current event.id exactly.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "The record helper expects &str for reason: borrow a formatted String if needed. Preserve dedup key/ordering, source, cloned current event, time, usage, provider calls and every other audit reason. Do not show the first-seen event ID.",
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
      "cwd": "units/PFT-002",
      "timeout_seconds": 330,
      "required_test_ids": [
        "fresh_pft_002"
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
        "ncos-agent",
        "--lib",
        "fresh_pft_002",
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
      "cwd": "units/PFT-002",
      "timeout_seconds": 330,
      "required_test_ids": [
        "healthy_fast_path_never_calls_model"
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
        "ncos-agent",
        "--test",
        "acceptance",
        "healthy_fast_path_never_calls_model",
        "--",
        "--exact"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/PFT-002",
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
      "cwd": "units/PFT-002",
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
      "cwd": "units/PFT-002",
      "timeout_seconds": 330,
      "required_test_ids": [
        "healthy_fast_path_never_calls_model"
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
      "cwd": "units/PFT-002",
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
      "cwd": "units/PFT-002",
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

<a id="pft-003"></a>
## PFT-003

CLIに実行結果DryRun/Blockedの固定labelを表示

元のtask_id: `PFT-003`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Implement execution_label(status: &ncos_core::ExecutionStatus) -> &'static str: DryRun returns DRY_RUN, Blocked returns BLOCKED. This labels recorded execution status only; never derive it from policy, change execution, or use debug-format/heap allocation. Keep record.detail and all audit bytes unchanged.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.6-fresh-tasks --task PFT-003 --output work/PFT-003
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | model=gemma4:26b | — | PASS | — | — | ACCEPT_NO_CHANGE | — | [R-a56070a37d74b6](#r-a56070a37d74b6) |
| コードの検証 | model=gemma4:26b | PASS | — | — | — | workspace/records/router-v2.2/PFT-003/review.json | — | [R-35b578c446c906](#r-35b578c446c906) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-a56070a37d74b6"></a>
### 根拠 R-a56070a37d74b6

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/2`
- 出典ファイルのSHA-256: `9b0ae77d9072e9d69785288674c1590e057257b3739233661f78867611283931`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.6-fresh-tasks.json)

<a id="r-35b578c446c906"></a>
### 根拠 R-35b578c446c906

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/2`
- 出典ファイルのSHA-256: `d229293fe33b21ace3526c27b05d93266a911b737e7efc27cb3a822a2cd64963`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.6-fresh-tasks.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Implement execution_label(status: &ncos_core::ExecutionStatus) -> &'static str: DryRun returns DRY_RUN, Blocked returns BLOCKED.",
    "This labels recorded execution status only; never derive it from policy, change execution, or use debug-format/heap allocation. Keep record.detail and all audit bytes unchanged.",
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
      "criterion_text": "Implement execution_label(status: &ncos_core::ExecutionStatus) -> &'static str: DryRun returns DRY_RUN, Blocked returns BLOCKED.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "This labels recorded execution status only; never derive it from policy, change execution, or use debug-format/heap allocation. Keep record.detail and all audit bytes unchanged.",
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
      "cwd": "units/PFT-003",
      "timeout_seconds": 330,
      "required_test_ids": [
        "fresh_pft_003"
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
        "ncos-cli",
        "--bin",
        "ncos",
        "fresh_pft_003",
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
      "cwd": "units/PFT-003",
      "timeout_seconds": 330,
      "required_test_ids": [
        "demo_audit_and_refusal_to_overwrite"
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
        "ncos-cli",
        "--test",
        "cli",
        "demo_audit_and_refusal_to_overwrite",
        "--",
        "--exact"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/PFT-003",
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
      "cwd": "units/PFT-003",
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
      "cwd": "units/PFT-003",
      "timeout_seconds": 330,
      "required_test_ids": [
        "demo_audit_and_refusal_to_overwrite"
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
      "cwd": "units/PFT-003",
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
      "cwd": "units/PFT-003",
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

<a id="pft-004"></a>
## PFT-004

MockProviderの不足token数を診断する

元のtask_id: `PFT-004`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Locate the MockProvider::propose insufficient-token error. For token_limit below 16, return exactly insufficient mock token budget: required=16; available=N; shortfall=D, where N=token_limit and D=16-token_limit. Preserve existing threshold, validation precedence, call-counter charging, overflow error, tokens_used and proposal. No authority or budget policy change; no addition of provider inference.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.6-fresh-tasks --task PFT-004 --output work/PFT-004
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | model=gemma4:26b | — | PASS | — | — | ACCEPT_NO_CHANGE | — | [R-d143fb52ca81f4](#r-d143fb52ca81f4) |
| コードの検証 | model=gemma4:26b | PASS | — | — | — | workspace/records/router-v2.2/PFT-004/review.json | — | [R-01a1d38b588e50](#r-01a1d38b588e50) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-d143fb52ca81f4"></a>
### 根拠 R-d143fb52ca81f4

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/3`
- 出典ファイルのSHA-256: `9b0ae77d9072e9d69785288674c1590e057257b3739233661f78867611283931`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.6-fresh-tasks.json)

<a id="r-01a1d38b588e50"></a>
### 根拠 R-01a1d38b588e50

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/3`
- 出典ファイルのSHA-256: `d229293fe33b21ace3526c27b05d93266a911b737e7efc27cb3a822a2cd64963`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.6-fresh-tasks.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Locate the MockProvider::propose insufficient-token error. For token_limit below 16, return exactly insufficient mock token budget: required=16; available=N; shortfall=D, where N=token_limit and D=16-token_limit.",
    "Preserve existing threshold, validation precedence, call-counter charging, overflow error, tokens_used and proposal. No authority or budget policy change; no addition of provider inference.",
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
      "criterion_text": "Locate the MockProvider::propose insufficient-token error. For token_limit below 16, return exactly insufficient mock token budget: required=16; available=N; shortfall=D, where N=token_limit and D=16-token_limit.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve existing threshold, validation precedence, call-counter charging, overflow error, tokens_used and proposal. No authority or budget policy change; no addition of provider inference.",
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
      "cwd": "units/PFT-004",
      "timeout_seconds": 330,
      "required_test_ids": [
        "fresh_pft_004"
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
        "ncos-agent",
        "--lib",
        "fresh_pft_004",
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
      "cwd": "units/PFT-004",
      "timeout_seconds": 330,
      "required_test_ids": [
        "healthy_fast_path_never_calls_model"
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
        "ncos-agent",
        "--test",
        "acceptance",
        "healthy_fast_path_never_calls_model",
        "--",
        "--exact"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/PFT-004",
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
      "cwd": "units/PFT-004",
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
      "cwd": "units/PFT-004",
      "timeout_seconds": 330,
      "required_test_ids": [
        "healthy_fast_path_never_calls_model"
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
      "cwd": "units/PFT-004",
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
      "cwd": "units/PFT-004",
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

<a id="pft-005"></a>
## PFT-005

telemetry readのUTF-8エラーをI/O欠測と区別

元のtask_id: `PFT-005`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Implement telemetry_read_error(error: std::io::Error) -> String. If error.kind() is std::io::ErrorKind::InvalidData return telemetry invalid UTF-8, otherwise telemetry unavailable. Do not reveal the OS error message/path, retry reads, change the 65536-byte bound, or change parsers. This helper is wired solely into read_bounded error mapping.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.6-fresh-tasks --task PFT-005 --output work/PFT-005
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | model=gemma4:26b | — | PASS | — | — | ACCEPT_NO_CHANGE | — | [R-c0e3aaad02fe9d](#r-c0e3aaad02fe9d) |
| コードの検証 | model=gemma4:26b | PASS | — | — | — | workspace/records/router-v2.2/PFT-005/review.json | — | [R-8dc5b7a61e7d8d](#r-8dc5b7a61e7d8d) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-c0e3aaad02fe9d"></a>
### 根拠 R-c0e3aaad02fe9d

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/4`
- 出典ファイルのSHA-256: `9b0ae77d9072e9d69785288674c1590e057257b3739233661f78867611283931`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.6-fresh-tasks.json)

<a id="r-8dc5b7a61e7d8d"></a>
### 根拠 R-8dc5b7a61e7d8d

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/4`
- 出典ファイルのSHA-256: `d229293fe33b21ace3526c27b05d93266a911b737e7efc27cb3a822a2cd64963`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.6-fresh-tasks.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Implement telemetry_read_error(error: std::io::Error) -> String. If error.kind() is std::io::ErrorKind::InvalidData return telemetry invalid UTF-8, otherwise telemetry unavailable.",
    "Do not reveal the OS error message/path, retry reads, change the 65536-byte bound, or change parsers. This helper is wired solely into read_bounded error mapping.",
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
      "criterion_text": "Implement telemetry_read_error(error: std::io::Error) -> String. If error.kind() is std::io::ErrorKind::InvalidData return telemetry invalid UTF-8, otherwise telemetry unavailable.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Do not reveal the OS error message/path, retry reads, change the 65536-byte bound, or change parsers. This helper is wired solely into read_bounded error mapping.",
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
      "cwd": "units/PFT-005",
      "timeout_seconds": 330,
      "required_test_ids": [
        "fresh_pft_005"
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
        "ncos-observer-linux",
        "--lib",
        "fresh_pft_005",
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
      "cwd": "units/PFT-005",
      "timeout_seconds": 330,
      "required_test_ids": [
        "memory_parse"
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
        "ncos-observer-linux",
        "--test",
        "acceptance",
        "memory_parse",
        "--",
        "--exact"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/PFT-005",
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
      "cwd": "units/PFT-005",
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
      "cwd": "units/PFT-005",
      "timeout_seconds": 330,
      "required_test_ids": [
        "memory_parse"
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
      "cwd": "units/PFT-005",
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
      "cwd": "units/PFT-005",
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

<a id="pft-006"></a>
## PFT-006

TCP欠測warningが失敗したIP familyを列挙

元のtask_id: `PFT-006`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Locate the TCP unavailable diagnostic helper tcp_unavailable(ipv4_failed: bool, ipv6_failed: bool) -> String. Return TCP inventory unavailable: IPv4 for (true,false), TCP inventory unavailable: IPv6 for (false,true), TCP inventory unavailable: IPv4, IPv6 for (true,true). For (false,false), retain TCP inventory unavailable. Do not alter process warnings, TCP counting, Option presence, I/O attempts or partial-inventory policy. This is one diagnostic selector.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.6-fresh-tasks --task PFT-006 --output work/PFT-006
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | model=gemma4:26b | — | PASS | — | — | ACCEPT_NO_CHANGE | — | [R-ac9a84c8bf7849](#r-ac9a84c8bf7849) |
| コードの検証 | model=gemma4:26b | PASS | — | — | — | workspace/records/router-v2.2/PFT-006/review.json | — | [R-d8737fa96c2718](#r-d8737fa96c2718) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-ac9a84c8bf7849"></a>
### 根拠 R-ac9a84c8bf7849

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/5`
- 出典ファイルのSHA-256: `9b0ae77d9072e9d69785288674c1590e057257b3739233661f78867611283931`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.6-fresh-tasks.json)

<a id="r-d8737fa96c2718"></a>
### 根拠 R-d8737fa96c2718

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/5`
- 出典ファイルのSHA-256: `d229293fe33b21ace3526c27b05d93266a911b737e7efc27cb3a822a2cd64963`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.6-fresh-tasks.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Locate the TCP unavailable diagnostic helper tcp_unavailable(ipv4_failed: bool, ipv6_failed: bool) -> String. Return TCP inventory unavailable: IPv4 for (true,false), TCP inventory unavailable: IPv6 for (false,true), TCP inventory unavailable: IPv4, IPv6 for (true,true).",
    "For (false,false), retain TCP inventory unavailable. Do not alter process warnings, TCP counting, Option presence, I/O attempts or partial-inventory policy. This is one diagnostic selector.",
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
      "criterion_text": "Locate the TCP unavailable diagnostic helper tcp_unavailable(ipv4_failed: bool, ipv6_failed: bool) -> String. Return TCP inventory unavailable: IPv4 for (true,false), TCP inventory unavailable: IPv6 for (false,true), TCP inventory unavailable: IPv4, IPv6 for (true,true).",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "For (false,false), retain TCP inventory unavailable. Do not alter process warnings, TCP counting, Option presence, I/O attempts or partial-inventory policy. This is one diagnostic selector.",
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
      "cwd": "units/PFT-006",
      "timeout_seconds": 330,
      "required_test_ids": [
        "fresh_pft_006"
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
        "ncos-observer-linux",
        "--lib",
        "fresh_pft_006",
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
      "cwd": "units/PFT-006",
      "timeout_seconds": 330,
      "required_test_ids": [
        "memory_parse"
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
        "ncos-observer-linux",
        "--test",
        "acceptance",
        "memory_parse",
        "--",
        "--exact"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/PFT-006",
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
      "cwd": "units/PFT-006",
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
      "cwd": "units/PFT-006",
      "timeout_seconds": 330,
      "required_test_ids": [
        "memory_parse"
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
      "cwd": "units/PFT-006",
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
      "cwd": "units/PFT-006",
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

<a id="pft-007"></a>
## PFT-007

CLI引数エラーへinspect基準のindexを追加

元のtask_id: `PFT-007`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Implement argument_error(index: usize) -> String: return exactly unknown, duplicate or incomplete argument at index N; see --help where N is index in unsigned decimal. Index is supplied by the existing parser (inspect is index 0); do not increment it or echo the argument value. Preserve all parsing rules and side effects; support 0 and usize::MAX.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.6-fresh-tasks --task PFT-007 --output work/PFT-007
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | model=gemma4:26b | — | ESCALATE | — | — | REJECT | — | [R-be9970f26d7938](#r-be9970f26d7938) |
| コードの検証 | model=gemma4:26b | ESCALATE | — | — | — | workspace/records/router-v2.2/PFT-007/review.json | — | [R-711bf0c4665ac2](#r-711bf0c4665ac2) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-be9970f26d7938"></a>
### 根拠 R-be9970f26d7938

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/6`
- 出典ファイルのSHA-256: `9b0ae77d9072e9d69785288674c1590e057257b3739233661f78867611283931`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.6-fresh-tasks.json)

<a id="r-711bf0c4665ac2"></a>
### 根拠 R-711bf0c4665ac2

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/6`
- 出典ファイルのSHA-256: `d229293fe33b21ace3526c27b05d93266a911b737e7efc27cb3a822a2cd64963`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.6-fresh-tasks.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Implement argument_error(index: usize) -> String: return exactly unknown, duplicate or incomplete argument at index N; see --help where N is index in unsigned decimal.",
    "Index is supplied by the existing parser (inspect is index 0); do not increment it or echo the argument value. Preserve all parsing rules and side effects; support 0 and usize::MAX.",
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
      "criterion_text": "Implement argument_error(index: usize) -> String: return exactly unknown, duplicate or incomplete argument at index N; see --help where N is index in unsigned decimal.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Index is supplied by the existing parser (inspect is index 0); do not increment it or echo the argument value. Preserve all parsing rules and side effects; support 0 and usize::MAX.",
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
      "cwd": "units/PFT-007",
      "timeout_seconds": 330,
      "required_test_ids": [
        "fresh_pft_007"
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
        "ncos-cli",
        "--bin",
        "ncos",
        "fresh_pft_007",
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
      "cwd": "units/PFT-007",
      "timeout_seconds": 330,
      "required_test_ids": [
        "demo_audit_and_refusal_to_overwrite"
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
        "ncos-cli",
        "--test",
        "cli",
        "demo_audit_and_refusal_to_overwrite",
        "--",
        "--exact"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/PFT-007",
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
      "cwd": "units/PFT-007",
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
      "cwd": "units/PFT-007",
      "timeout_seconds": 330,
      "required_test_ids": [
        "demo_audit_and_refusal_to_overwrite"
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
      "cwd": "units/PFT-007",
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
      "cwd": "units/PFT-007",
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

<a id="pft-008"></a>
## PFT-008

policy評価済みauditがproposal由来を説明

元のtask_id: `PFT-008`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Locate the evaluated-proposal audit reason in Runtime::handle. Use Proposal evaluated by deterministic policy; origin=cached-template when source == skill, otherwise Proposal evaluated by deterministic policy; origin=provider. Change only this reason string argument. Preserve policy/execution/verification, original source field, provider reservation and calls, cache promotion, denied-content handling, dedup and all early-return reasons.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.6-fresh-tasks --task PFT-008 --output work/PFT-008
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | model=gemma4:26b | — | ESCALATE | — | — | REJECT | — | [R-eb872a428729c5](#r-eb872a428729c5) |
| コードの検証 | model=gemma4:26b | ESCALATE | — | — | — | workspace/records/router-v2.2/PFT-008/review.json | — | [R-37c30c7bc9a94d](#r-37c30c7bc9a94d) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-eb872a428729c5"></a>
### 根拠 R-eb872a428729c5

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/7`
- 出典ファイルのSHA-256: `9b0ae77d9072e9d69785288674c1590e057257b3739233661f78867611283931`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.6-fresh-tasks.json)

<a id="r-37c30c7bc9a94d"></a>
### 根拠 R-37c30c7bc9a94d

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/7`
- 出典ファイルのSHA-256: `d229293fe33b21ace3526c27b05d93266a911b737e7efc27cb3a822a2cd64963`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.6-fresh-tasks.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Locate the evaluated-proposal audit reason in Runtime::handle. Use Proposal evaluated by deterministic policy; origin=cached-template when source == skill, otherwise Proposal evaluated by deterministic policy; origin=provider.",
    "Change only this reason string argument. Preserve policy/execution/verification, original source field, provider reservation and calls, cache promotion, denied-content handling, dedup and all early-return reasons.",
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
      "criterion_text": "Locate the evaluated-proposal audit reason in Runtime::handle. Use Proposal evaluated by deterministic policy; origin=cached-template when source == skill, otherwise Proposal evaluated by deterministic policy; origin=provider.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Change only this reason string argument. Preserve policy/execution/verification, original source field, provider reservation and calls, cache promotion, denied-content handling, dedup and all early-return reasons.",
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
      "cwd": "units/PFT-008",
      "timeout_seconds": 330,
      "required_test_ids": [
        "fresh_pft_008"
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
        "ncos-agent",
        "--lib",
        "fresh_pft_008",
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
      "cwd": "units/PFT-008",
      "timeout_seconds": 330,
      "required_test_ids": [
        "healthy_fast_path_never_calls_model"
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
        "ncos-agent",
        "--test",
        "acceptance",
        "healthy_fast_path_never_calls_model",
        "--",
        "--exact"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/PFT-008",
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
      "cwd": "units/PFT-008",
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
      "cwd": "units/PFT-008",
      "timeout_seconds": 330,
      "required_test_ids": [
        "healthy_fast_path_never_calls_model"
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
      "cwd": "units/PFT-008",
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
      "cwd": "units/PFT-008",
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

<a id="pft-009"></a>
## PFT-009

proc directory識別が符号付き/zero名を受理する不具合

元のtask_id: `PFT-009`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Debug process_directory_pid(name: &str) -> Option<u32>, extracted unchanged from LinuxObserver directory selection. Accept iff name is nonempty ASCII decimal digits and its u32 value is nonzero. Leading zeros are permitted. Reject +1, -1, 0/00, Unicode digits, whitespace, suffixes and u32 overflow. Return None without panic. This is only directory-name selection, not /proc/status parsing or PID validation elsewhere.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.6-fresh-tasks --task PFT-009 --output work/PFT-009
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | model=qwen3-coder-next:latest | — | ESCALATE | — | — | REJECT | — | [R-58ea89af65b7b8](#r-58ea89af65b7b8) |
| コードの検証 | model=qwen3-coder-next:latest | ESCALATE | — | — | — | workspace/records/router-v2.2/PFT-009/review.json | — | [R-a6f54e4bd7e37c](#r-a6f54e4bd7e37c) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-58ea89af65b7b8"></a>
### 根拠 R-58ea89af65b7b8

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/8`
- 出典ファイルのSHA-256: `9b0ae77d9072e9d69785288674c1590e057257b3739233661f78867611283931`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.6-fresh-tasks.json)

<a id="r-a6f54e4bd7e37c"></a>
### 根拠 R-a6f54e4bd7e37c

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/8`
- 出典ファイルのSHA-256: `d229293fe33b21ace3526c27b05d93266a911b737e7efc27cb3a822a2cd64963`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.6-fresh-tasks.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Debug process_directory_pid(name: &str) -> Option<u32>, extracted unchanged from LinuxObserver directory selection. Accept iff name is nonempty ASCII decimal digits and its u32 value is nonzero. Leading zeros are permitted.",
    "Reject +1, -1, 0/00, Unicode digits, whitespace, suffixes and u32 overflow. Return None without panic. This is only directory-name selection, not /proc/status parsing or PID validation elsewhere.",
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
      "criterion_text": "Debug process_directory_pid(name: &str) -> Option<u32>, extracted unchanged from LinuxObserver directory selection. Accept iff name is nonempty ASCII decimal digits and its u32 value is nonzero. Leading zeros are permitted.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Reject +1, -1, 0/00, Unicode digits, whitespace, suffixes and u32 overflow. Return None without panic. This is only directory-name selection, not /proc/status parsing or PID validation elsewhere.",
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
      "cwd": "units/PFT-009",
      "timeout_seconds": 330,
      "required_test_ids": [
        "fresh_pft_009"
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
        "ncos-observer-linux",
        "--lib",
        "fresh_pft_009",
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
      "cwd": "units/PFT-009",
      "timeout_seconds": 330,
      "required_test_ids": [
        "memory_parse"
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
        "ncos-observer-linux",
        "--test",
        "acceptance",
        "memory_parse",
        "--",
        "--exact"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/PFT-009",
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
      "cwd": "units/PFT-009",
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
      "cwd": "units/PFT-009",
      "timeout_seconds": 330,
      "required_test_ids": [
        "memory_parse"
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
      "cwd": "units/PFT-009",
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
      "cwd": "units/PFT-009",
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

<a id="pft-010"></a>
## PFT-010

Runtime constructorの固定容量と初期化契約をtyped抽出

元のtask_id: `PFT-010`。初期ファイル数: 1。

**課題・インターフェース**

From the supplied Runtime::new source, extract dedup_capacity, skill_capacity, report_only (PolicyEngine capabilities consist exactly of Report), usage_defaulted (ResourceUsage::default), budget_preserved (the supplied budget is stored unchanged). Return source facts only.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.6-fresh-tasks --task PFT-010 --output work/PFT-010
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | model=gemma4:26b | — | PASS | — | — | ACCEPT_NO_CHANGE | — | [R-4f726a13446f9f](#r-4f726a13446f9f) |
| コードの検証 | model=gemma4:26b | PASS | — | — | — | workspace/records/router-v2.2/PFT-010/review.json | — | [R-9f38c9db33d56c](#r-9f38c9db33d56c) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-4f726a13446f9f"></a>
### 根拠 R-4f726a13446f9f

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/9`
- 出典ファイルのSHA-256: `9b0ae77d9072e9d69785288674c1590e057257b3739233661f78867611283931`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.6-fresh-tasks.json)

<a id="r-9f38c9db33d56c"></a>
### 根拠 R-9f38c9db33d56c

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/9`
- 出典ファイルのSHA-256: `d229293fe33b21ace3526c27b05d93266a911b737e7efc27cb3a822a2cd64963`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.6-fresh-tasks.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Extract both cache capacities and all three initialization facts exactly from Runtime::new.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "Extract both cache capacities and all three initialization facts exactly from Runtime::new.",
      "category": "functional"
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
      "kind": "structured",
      "argv": null,
      "portability_note": "Original adapter-specific check; use the declared acceptance contract and fixture tests."
    }
  ]
}
```

</details>

<a id="pft-011"></a>
## PFT-011

長期audit閲覧におけるrecord grouping方針を決定

元のtask_id: `PFT-011`。初期ファイル数: 1。

**課題・インターフェース**

Open product decision: whether a future audit viewer groups records by inspection session, event kind or time; decide human-facing tradeoffs without changing schema, retention, policy or implementing UI.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.6-fresh-tasks --task PFT-011 --output work/PFT-011
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実行状態・対照条件 | source=report_table | CODEX_ONLY | — | — | — | — | — | [R-b0d132d8982fb8](#r-b0d132d8982fb8) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-b0d132d8982fb8"></a>
### 根拠 R-b0d132d8982fb8

- 対応方法: 同一セット・課題IDによる対応
- 出典: `RESULTS_JA.md` / 位置: `markdown-line:33`
- 出典ファイルのSHA-256: `25ca55298756a66e10457df67dad6d78e91ad062b261d3a0b257b40cd3259675`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.6-fresh-tasks.json)

出典の表の該当行:

```text
| PFT-011 | audit viewerのrecord grouping方針 | Codex boundary | N/A | CODEX_ONLY・Local dispatch 0 | 実装なし |
```

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Free product specification remains Codex-owned with zero Local dispatch.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "Free product specification remains Codex-owned with zero Local dispatch.",
      "category": "functional"
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
      "kind": "structured",
      "argv": null,
      "portability_note": "Original adapter-specific check; use the declared acceptance contract and fixture tests."
    }
  ]
}
```

</details>
