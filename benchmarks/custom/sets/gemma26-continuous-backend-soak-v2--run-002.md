# Gemma26の同一プロセスでの連続稼働（52課題）

セットID: `gemma26-continuous-backend-soak-v2--run-002`

課題数: 52。個別記録あり: 52、個別記録未確認: 0。

[全セット一覧](../INDEX.md) / [課題定義JSON](gemma26-continuous-backend-soak-v2--run-002.json) / [結果と根拠のJSON](../results/gemma26-continuous-backend-soak-v2--run-002.json) / [判定の読み方](../README.md#判定の読み方)

各結果はこのセットの保存記録に対応します。収録外の別runの結果を新たに代入していません。SHA-256が記録されている結果は課題定義と照合し、それ以外は実行キー・ディレクトリ・同一セット内の一意のIDによる対応として表示しています。元の記録が過去の工程を再利用している場合、独立した再実行の結果とは扱わないでください。

参考の実験レポート: [RESULTS_JA.md](../reports/gemma26-continuous-backend-soak-v2--run-002/RESULTS_JA.md)

**実験で固定した設定**（実際の結果・モデル情報は各記録を参照）

```json
[
  {
    "model": "gemma4:26b",
    "digest": "08ae7ec1744bd7f451c4a530afb39d2673ad9d07a8369b8a33a3613b41212a68",
    "codex_model": "gpt-6-sol",
    "quantization": "Q4_K_M",
    "effort": "xhigh",
    "speed": "Standard",
    "Local_repairs": 0
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
| [GCB228-001](#gcb228-001) | Refactor root pids to its protected typed helper without changing behavior | 記録あり |
| [GCB228-002](#gcb228-002) | Refactor nonroot pids to its protected typed helper without changing behavior | 記録あり |
| [GCB228-003](#gcb228-003) | Refactor positive rss pids to its protected typed helper without changing behavior | 記録あり |
| [GCB228-004](#gcb228-004) | Refactor even pids to its protected typed helper without changing behavior | 記録あり |
| [GCB228-005](#gcb228-005) | Refactor odd pids to its protected typed helper without changing behavior | 記録あり |
| [GCB228-006](#gcb228-006) | Refactor blank warning indices to its protected typed helper without changing behavior | 記録あり |
| [GCB228-007](#gcb228-007) | Refactor multiline warning indices to its protected typed helper without changing behavior | 記録あり |
| [GCB228-008](#gcb228-008) | Refactor nonascii warning indices to its protected typed helper without changing behavior | 記録あり |
| [GCB228-009](#gcb228-009) | Refactor nonempty warning indices to its protected typed helper without changing behavior | 記録あり |
| [GCB228-010](#gcb228-010) | Refactor constraint byte sizes to its protected typed helper without changing behavior | 記録あり |
| [GCB228-011](#gcb228-011) | Refactor constraint char sizes to its protected typed helper without changing behavior | 記録あり |
| [GCB228-012](#gcb228-012) | Refactor uppercase constraints to its protected typed helper without changing behavior | 記録あり |
| [GCB228-013](#gcb228-013) | Refactor trimmed constraints to its protected typed helper without changing behavior | 記録あり |
| [GCB228-014](#gcb228-014) | Refactor remaining token headroom to its protected typed helper without changing behavior | 記録あり |
| [GCB228-015](#gcb228-015) | Refactor remaining call headroom to its protected typed helper without changing behavior | 記録あり |
| [GCB228-016](#gcb228-016) | Refactor latency overrun flag to its protected typed helper without changing behavior | 記録あり |
| [GCB228-017](#gcb228-017) | Refactor elapsed complete seconds to its protected typed helper without changing behavior | 記録あり |
| [GCB228-018](#gcb228-018) | Refactor elapsed complete hours to its protected typed helper without changing behavior | 記録あり |
| [GCB228-019](#gcb228-019) | Refactor token low byte to its protected typed helper without changing behavior | 記録あり |
| [GCB228-020](#gcb228-020) | Refactor call saturation flag to its protected typed helper without changing behavior | 記録あり |
| [GCB228-021](#gcb228-021) | Refactor memory unused bytes to its protected typed helper without changing behavior | 記録あり |
| [GCB228-022](#gcb228-022) | Refactor memory unavailable kib to its protected typed helper without changing behavior | 記録あり |
| [GCB228-023](#gcb228-023) | Refactor rss whole mebibytes to its protected typed helper without changing behavior | 記録あり |
| [GCB228-024](#gcb228-024) | Refactor parent identity distance to its protected typed helper without changing behavior | 記録あり |
| [GCB228-025](#gcb228-025) | Refactor observation second remainder to its protected typed helper without changing behavior | 記録あり |
| [GCB228-026](#gcb228-026) | Refactor observation day bucket to its protected typed helper without changing behavior | 記録あり |
| [GCB228-027](#gcb228-027) | Refactor intent goal preview to its protected typed helper without changing behavior | 記録あり |
| [GCB228-028](#gcb228-028) | Refactor intent id uppercase to its protected typed helper without changing behavior | 記録あり |
| [GCB228-029](#gcb228-029) | Refactor source lowercase to its protected typed helper without changing behavior | 記録あり |
| [GCB228-030](#gcb228-030) | Refactor short reason preview to its protected typed helper without changing behavior | 記録あり |
| [GCB228-031](#gcb228-031) | Refactor event target uppercase to its protected typed helper without changing behavior | 記録あり |
| [GCB228-032](#gcb228-032) | Refactor event id lowercase to its protected typed helper without changing behavior | 記録あり |
| [GCB228-033](#gcb228-033) | Refactor intent constraint csv to its protected typed helper without changing behavior | 記録あり |
| [GCB228-034](#gcb228-034) | Refactor evidence semicolon text to its protected typed helper without changing behavior | 記録あり |
| [GCB228-035](#gcb228-035) | Refactor pid binary label to its protected typed helper without changing behavior | 記録あり |
| [GCB228-036](#gcb228-036) | Refactor parent hex label to its protected typed helper without changing behavior | 記録あり |
| [GCB228-037](#gcb228-037) | Refactor tokens decimal label to its protected typed helper without changing behavior | 記録あり |
| [GCB228-038](#gcb228-038) | Refactor calls decimal label to its protected typed helper without changing behavior | 記録あり |
| [GCB228-039](#gcb228-039) | Refactor schema decimal label to its protected typed helper without changing behavior | 記録あり |
| [GCB228-040](#gcb228-040) | Refactor logical cpu receipt to its protected typed helper without changing behavior | 記録あり |
| [GCB228-041](#gcb228-041) | Refactor disk known receipt to its protected typed helper without changing behavior | 記録あり |
| [GCB228-042](#gcb228-042) | Refactor service known receipt to its protected typed helper without changing behavior | 記録あり |
| [GCB228-043](#gcb228-043) | Refactor tcp known receipt to its protected typed helper without changing behavior | 記録あり |
| [GCB228-044](#gcb228-044) | Refactor truncated receipt to its protected typed helper without changing behavior | 記録あり |
| [GCB228-045](#gcb228-045) | Refactor warning byte total receipt to its protected typed helper without changing behavior | 記録あり |
| [GCB228-046](#gcb228-046) | Refactor warning scalar total receipt to its protected typed helper without changing behavior | 記録あり |
| [GCB228-047](#gcb228-047) | Refactor rss row count receipt to its protected typed helper without changing behavior | 記録あり |
| [GCB228-048](#gcb228-048) | Refactor memory total receipt to its protected typed helper without changing behavior | 記録あり |
| [GCB228-049](#gcb228-049) | Refactor available memory receipt to its protected typed helper without changing behavior | 記録あり |
| [GCB228-050](#gcb228-050) | Refactor observed millis receipt to its protected typed helper without changing behavior | 記録あり |
| [GCB228-051](#gcb228-051) | Refactor nonblank warning receipt to its protected typed helper without changing behavior | 記録あり |
| [GCB228-052](#gcb228-052) | Refactor root count receipt to its protected typed helper without changing behavior | 記録あり |

<a id="gcb228-001"></a>
## GCB228-001

Refactor root pids to its protected typed helper without changing behavior

元のtask_id: `GCB228-001`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_root_pids(state: &SystemState) -> Vec<u32>. Preserve filter, recorded order and duplicate rows exactly; empty input returns empty. Replace the inline body with a direct call to protected continuous_ref_root_pids, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-001 --output work/GCB228-001
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-a66442faab56c3](#r-a66442faab56c3) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-a66442faab56c3"></a>
### 根拠 R-a66442faab56c3

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/44`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_root_pids(state: &SystemState) -> Vec<u32>.",
    "Preserve filter, recorded order and duplicate rows exactly; empty input returns empty.",
    "Replace the inline body with a direct call to protected continuous_ref_root_pids, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_root_pids(state: &SystemState) -> Vec<u32>.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve filter, recorded order and duplicate rows exactly; empty input returns empty.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_root_pids, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-001",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_001"
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
        "continuous_gcb228_001",
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
      "cwd": "units/GCB228-001",
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
      "cwd": "units/GCB228-001",
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
      "cwd": "units/GCB228-001",
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
      "cwd": "units/GCB228-001",
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
      "cwd": "units/GCB228-001",
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
      "cwd": "units/GCB228-001",
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

<a id="gcb228-002"></a>
## GCB228-002

Refactor nonroot pids to its protected typed helper without changing behavior

元のtask_id: `GCB228-002`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_nonroot_pids(state: &SystemState) -> Vec<u32>. Preserve filter, recorded order and duplicate rows exactly; empty input returns empty. Replace the inline body with a direct call to protected continuous_ref_nonroot_pids, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-002 --output work/GCB228-002
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-af7afc580723ae](#r-af7afc580723ae) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-af7afc580723ae"></a>
### 根拠 R-af7afc580723ae

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/16`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_nonroot_pids(state: &SystemState) -> Vec<u32>.",
    "Preserve filter, recorded order and duplicate rows exactly; empty input returns empty.",
    "Replace the inline body with a direct call to protected continuous_ref_nonroot_pids, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_nonroot_pids(state: &SystemState) -> Vec<u32>.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve filter, recorded order and duplicate rows exactly; empty input returns empty.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_nonroot_pids, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-002",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_002"
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
        "continuous_gcb228_002",
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
      "cwd": "units/GCB228-002",
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
      "cwd": "units/GCB228-002",
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
      "cwd": "units/GCB228-002",
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
      "cwd": "units/GCB228-002",
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
      "cwd": "units/GCB228-002",
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
      "cwd": "units/GCB228-002",
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

<a id="gcb228-003"></a>
## GCB228-003

Refactor positive rss pids to its protected typed helper without changing behavior

元のtask_id: `GCB228-003`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_positive_rss_pids(state: &SystemState) -> Vec<u32>. Preserve filter, recorded order and duplicate rows exactly; empty input returns empty. Replace the inline body with a direct call to protected continuous_ref_positive_rss_pids, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-003 --output work/GCB228-003
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-e65fe9c7e50862](#r-e65fe9c7e50862) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-e65fe9c7e50862"></a>
### 根拠 R-e65fe9c7e50862

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/32`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_positive_rss_pids(state: &SystemState) -> Vec<u32>.",
    "Preserve filter, recorded order and duplicate rows exactly; empty input returns empty.",
    "Replace the inline body with a direct call to protected continuous_ref_positive_rss_pids, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_positive_rss_pids(state: &SystemState) -> Vec<u32>.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve filter, recorded order and duplicate rows exactly; empty input returns empty.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_positive_rss_pids, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-003",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_003"
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
        "continuous_gcb228_003",
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
      "cwd": "units/GCB228-003",
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
      "cwd": "units/GCB228-003",
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
      "cwd": "units/GCB228-003",
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
      "cwd": "units/GCB228-003",
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
      "cwd": "units/GCB228-003",
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
      "cwd": "units/GCB228-003",
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

<a id="gcb228-004"></a>
## GCB228-004

Refactor even pids to its protected typed helper without changing behavior

元のtask_id: `GCB228-004`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_even_pids(state: &SystemState) -> Vec<u32>. Preserve filter, recorded order and duplicate rows exactly; empty input returns empty. Replace the inline body with a direct call to protected continuous_ref_even_pids, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-004 --output work/GCB228-004
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-6477ae95660ed9](#r-6477ae95660ed9) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-6477ae95660ed9"></a>
### 根拠 R-6477ae95660ed9

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/36`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_even_pids(state: &SystemState) -> Vec<u32>.",
    "Preserve filter, recorded order and duplicate rows exactly; empty input returns empty.",
    "Replace the inline body with a direct call to protected continuous_ref_even_pids, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_even_pids(state: &SystemState) -> Vec<u32>.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve filter, recorded order and duplicate rows exactly; empty input returns empty.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_even_pids, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-004",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_004"
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
        "continuous_gcb228_004",
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
      "cwd": "units/GCB228-004",
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
      "cwd": "units/GCB228-004",
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
      "cwd": "units/GCB228-004",
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
      "cwd": "units/GCB228-004",
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
      "cwd": "units/GCB228-004",
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
      "cwd": "units/GCB228-004",
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

<a id="gcb228-005"></a>
## GCB228-005

Refactor odd pids to its protected typed helper without changing behavior

元のtask_id: `GCB228-005`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_odd_pids(state: &SystemState) -> Vec<u32>. Preserve filter, recorded order and duplicate rows exactly; empty input returns empty. Replace the inline body with a direct call to protected continuous_ref_odd_pids, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-005 --output work/GCB228-005
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-ffb2b4814fbd30](#r-ffb2b4814fbd30) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-ffb2b4814fbd30"></a>
### 根拠 R-ffb2b4814fbd30

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/48`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_odd_pids(state: &SystemState) -> Vec<u32>.",
    "Preserve filter, recorded order and duplicate rows exactly; empty input returns empty.",
    "Replace the inline body with a direct call to protected continuous_ref_odd_pids, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_odd_pids(state: &SystemState) -> Vec<u32>.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve filter, recorded order and duplicate rows exactly; empty input returns empty.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_odd_pids, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-005",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_005"
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
        "continuous_gcb228_005",
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
      "cwd": "units/GCB228-005",
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
      "cwd": "units/GCB228-005",
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
      "cwd": "units/GCB228-005",
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
      "cwd": "units/GCB228-005",
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
      "cwd": "units/GCB228-005",
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
      "cwd": "units/GCB228-005",
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

<a id="gcb228-006"></a>
## GCB228-006

Refactor blank warning indices to its protected typed helper without changing behavior

元のtask_id: `GCB228-006`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_blank_warning_indices(state: &SystemState) -> Vec<usize>. Keep exact existing warning predicate and occurrence indices in input order; preserve strings. Replace the inline body with a direct call to protected continuous_ref_blank_warning_indices, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-006 --output work/GCB228-006
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-794546546f00d7](#r-794546546f00d7) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-794546546f00d7"></a>
### 根拠 R-794546546f00d7

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/20`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_blank_warning_indices(state: &SystemState) -> Vec<usize>.",
    "Keep exact existing warning predicate and occurrence indices in input order; preserve strings.",
    "Replace the inline body with a direct call to protected continuous_ref_blank_warning_indices, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_blank_warning_indices(state: &SystemState) -> Vec<usize>.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Keep exact existing warning predicate and occurrence indices in input order; preserve strings.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_blank_warning_indices, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-006",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_006"
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
        "continuous_gcb228_006",
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
      "cwd": "units/GCB228-006",
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
      "cwd": "units/GCB228-006",
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
      "cwd": "units/GCB228-006",
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
      "cwd": "units/GCB228-006",
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
      "cwd": "units/GCB228-006",
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
      "cwd": "units/GCB228-006",
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

<a id="gcb228-007"></a>
## GCB228-007

Refactor multiline warning indices to its protected typed helper without changing behavior

元のtask_id: `GCB228-007`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_multiline_warning_indices(state: &SystemState) -> Vec<usize>. Keep exact existing warning predicate and occurrence indices in input order; preserve strings. Replace the inline body with a direct call to protected continuous_ref_multiline_warning_indices, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-007 --output work/GCB228-007
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-38175b1044eb5b](#r-38175b1044eb5b) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-38175b1044eb5b"></a>
### 根拠 R-38175b1044eb5b

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/4`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_multiline_warning_indices(state: &SystemState) -> Vec<usize>.",
    "Keep exact existing warning predicate and occurrence indices in input order; preserve strings.",
    "Replace the inline body with a direct call to protected continuous_ref_multiline_warning_indices, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_multiline_warning_indices(state: &SystemState) -> Vec<usize>.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Keep exact existing warning predicate and occurrence indices in input order; preserve strings.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_multiline_warning_indices, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-007",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_007"
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
        "continuous_gcb228_007",
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
      "cwd": "units/GCB228-007",
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
      "cwd": "units/GCB228-007",
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
      "cwd": "units/GCB228-007",
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
      "cwd": "units/GCB228-007",
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
      "cwd": "units/GCB228-007",
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
      "cwd": "units/GCB228-007",
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

<a id="gcb228-008"></a>
## GCB228-008

Refactor nonascii warning indices to its protected typed helper without changing behavior

元のtask_id: `GCB228-008`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_nonascii_warning_indices(state: &SystemState) -> Vec<usize>. Keep exact existing warning predicate and occurrence indices in input order; preserve strings. Replace the inline body with a direct call to protected continuous_ref_nonascii_warning_indices, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-008 --output work/GCB228-008
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-5efa275594d83b](#r-5efa275594d83b) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-5efa275594d83b"></a>
### 根拠 R-5efa275594d83b

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/40`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_nonascii_warning_indices(state: &SystemState) -> Vec<usize>.",
    "Keep exact existing warning predicate and occurrence indices in input order; preserve strings.",
    "Replace the inline body with a direct call to protected continuous_ref_nonascii_warning_indices, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_nonascii_warning_indices(state: &SystemState) -> Vec<usize>.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Keep exact existing warning predicate and occurrence indices in input order; preserve strings.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_nonascii_warning_indices, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-008",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_008"
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
        "continuous_gcb228_008",
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
      "cwd": "units/GCB228-008",
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
      "cwd": "units/GCB228-008",
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
      "cwd": "units/GCB228-008",
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
      "cwd": "units/GCB228-008",
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
      "cwd": "units/GCB228-008",
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
      "cwd": "units/GCB228-008",
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

<a id="gcb228-009"></a>
## GCB228-009

Refactor nonempty warning indices to its protected typed helper without changing behavior

元のtask_id: `GCB228-009`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_nonempty_warning_indices(state: &SystemState) -> Vec<usize>. Keep exact existing warning predicate and occurrence indices in input order; preserve strings. Replace the inline body with a direct call to protected continuous_ref_nonempty_warning_indices, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-009 --output work/GCB228-009
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-8268cb11d47656](#r-8268cb11d47656) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-8268cb11d47656"></a>
### 根拠 R-8268cb11d47656

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/12`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_nonempty_warning_indices(state: &SystemState) -> Vec<usize>.",
    "Keep exact existing warning predicate and occurrence indices in input order; preserve strings.",
    "Replace the inline body with a direct call to protected continuous_ref_nonempty_warning_indices, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_nonempty_warning_indices(state: &SystemState) -> Vec<usize>.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Keep exact existing warning predicate and occurrence indices in input order; preserve strings.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_nonempty_warning_indices, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-009",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_009"
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
        "continuous_gcb228_009",
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
      "cwd": "units/GCB228-009",
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
      "cwd": "units/GCB228-009",
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
      "cwd": "units/GCB228-009",
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
      "cwd": "units/GCB228-009",
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
      "cwd": "units/GCB228-009",
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
      "cwd": "units/GCB228-009",
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

<a id="gcb228-010"></a>
## GCB228-010

Refactor constraint byte sizes to its protected typed helper without changing behavior

元のtask_id: `GCB228-010`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_constraint_byte_sizes(intent: &ncos_core::Intent) -> Vec<usize>. Keep per-entry Unicode/byte transformation exactly, including empty entries and order. Replace the inline body with a direct call to protected continuous_ref_constraint_byte_sizes, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-010 --output work/GCB228-010
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-047bf6075851c2](#r-047bf6075851c2) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-047bf6075851c2"></a>
### 根拠 R-047bf6075851c2

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/8`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_constraint_byte_sizes(intent: &ncos_core::Intent) -> Vec<usize>.",
    "Keep per-entry Unicode/byte transformation exactly, including empty entries and order.",
    "Replace the inline body with a direct call to protected continuous_ref_constraint_byte_sizes, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_constraint_byte_sizes(intent: &ncos_core::Intent) -> Vec<usize>.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Keep per-entry Unicode/byte transformation exactly, including empty entries and order.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_constraint_byte_sizes, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-010",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_010"
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
        "continuous_gcb228_010",
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
      "cwd": "units/GCB228-010",
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
      "cwd": "units/GCB228-010",
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
      "cwd": "units/GCB228-010",
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
      "cwd": "units/GCB228-010",
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
      "cwd": "units/GCB228-010",
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
      "cwd": "units/GCB228-010",
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

<a id="gcb228-011"></a>
## GCB228-011

Refactor constraint char sizes to its protected typed helper without changing behavior

元のtask_id: `GCB228-011`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_constraint_char_sizes(intent: &ncos_core::Intent) -> Vec<usize>. Keep per-entry Unicode/byte transformation exactly, including empty entries and order. Replace the inline body with a direct call to protected continuous_ref_constraint_char_sizes, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-011 --output work/GCB228-011
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-bdccf532a2b00a](#r-bdccf532a2b00a) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-bdccf532a2b00a"></a>
### 根拠 R-bdccf532a2b00a

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/0`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_constraint_char_sizes(intent: &ncos_core::Intent) -> Vec<usize>.",
    "Keep per-entry Unicode/byte transformation exactly, including empty entries and order.",
    "Replace the inline body with a direct call to protected continuous_ref_constraint_char_sizes, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_constraint_char_sizes(intent: &ncos_core::Intent) -> Vec<usize>.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Keep per-entry Unicode/byte transformation exactly, including empty entries and order.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_constraint_char_sizes, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-011",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_011"
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
        "continuous_gcb228_011",
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
      "cwd": "units/GCB228-011",
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
      "cwd": "units/GCB228-011",
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
      "cwd": "units/GCB228-011",
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
      "cwd": "units/GCB228-011",
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
      "cwd": "units/GCB228-011",
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
      "cwd": "units/GCB228-011",
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

<a id="gcb228-012"></a>
## GCB228-012

Refactor uppercase constraints to its protected typed helper without changing behavior

元のtask_id: `GCB228-012`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_uppercase_constraints(intent: &ncos_core::Intent) -> Vec<String>. Keep per-entry Unicode/byte transformation exactly, including empty entries and order. Replace the inline body with a direct call to protected continuous_ref_uppercase_constraints, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-012 --output work/GCB228-012
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-b6ec1f7943f915](#r-b6ec1f7943f915) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-b6ec1f7943f915"></a>
### 根拠 R-b6ec1f7943f915

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/24`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_uppercase_constraints(intent: &ncos_core::Intent) -> Vec<String>.",
    "Keep per-entry Unicode/byte transformation exactly, including empty entries and order.",
    "Replace the inline body with a direct call to protected continuous_ref_uppercase_constraints, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_uppercase_constraints(intent: &ncos_core::Intent) -> Vec<String>.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Keep per-entry Unicode/byte transformation exactly, including empty entries and order.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_uppercase_constraints, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-012",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_012"
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
        "continuous_gcb228_012",
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
      "cwd": "units/GCB228-012",
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
      "cwd": "units/GCB228-012",
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
      "cwd": "units/GCB228-012",
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
      "cwd": "units/GCB228-012",
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
      "cwd": "units/GCB228-012",
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
      "cwd": "units/GCB228-012",
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

<a id="gcb228-013"></a>
## GCB228-013

Refactor trimmed constraints to its protected typed helper without changing behavior

元のtask_id: `GCB228-013`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_trimmed_constraints(intent: &ncos_core::Intent) -> Vec<String>. Keep per-entry Unicode/byte transformation exactly, including empty entries and order. Replace the inline body with a direct call to protected continuous_ref_trimmed_constraints, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-013 --output work/GCB228-013
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-e6dba720b11dbd](#r-e6dba720b11dbd) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-e6dba720b11dbd"></a>
### 根拠 R-e6dba720b11dbd

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/28`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_trimmed_constraints(intent: &ncos_core::Intent) -> Vec<String>.",
    "Keep per-entry Unicode/byte transformation exactly, including empty entries and order.",
    "Replace the inline body with a direct call to protected continuous_ref_trimmed_constraints, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_trimmed_constraints(intent: &ncos_core::Intent) -> Vec<String>.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Keep per-entry Unicode/byte transformation exactly, including empty entries and order.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_trimmed_constraints, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-013",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_013"
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
        "continuous_gcb228_013",
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
      "cwd": "units/GCB228-013",
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
      "cwd": "units/GCB228-013",
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
      "cwd": "units/GCB228-013",
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
      "cwd": "units/GCB228-013",
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
      "cwd": "units/GCB228-013",
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
      "cwd": "units/GCB228-013",
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

<a id="gcb228-014"></a>
## GCB228-014

Refactor remaining token headroom to its protected typed helper without changing behavior

元のtask_id: `GCB228-014`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_remaining_token_headroom(usage: &ncos_core::ResourceUsage, budget: &ncos_core::ResourceBudget) -> u64. Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields. Replace the inline body with a direct call to protected continuous_ref_remaining_token_headroom, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-014 --output work/GCB228-014
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-2228e7f11a1ebf](#r-2228e7f11a1ebf) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-2228e7f11a1ebf"></a>
### 根拠 R-2228e7f11a1ebf

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/33`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_remaining_token_headroom(usage: &ncos_core::ResourceUsage, budget: &ncos_core::ResourceBudget) -> u64.",
    "Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields.",
    "Replace the inline body with a direct call to protected continuous_ref_remaining_token_headroom, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_remaining_token_headroom(usage: &ncos_core::ResourceUsage, budget: &ncos_core::ResourceBudget) -> u64.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_remaining_token_headroom, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-014",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_014"
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
        "continuous_gcb228_014",
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
      "cwd": "units/GCB228-014",
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
      "cwd": "units/GCB228-014",
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
      "cwd": "units/GCB228-014",
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
      "cwd": "units/GCB228-014",
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
      "cwd": "units/GCB228-014",
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
      "cwd": "units/GCB228-014",
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

<a id="gcb228-015"></a>
## GCB228-015

Refactor remaining call headroom to its protected typed helper without changing behavior

元のtask_id: `GCB228-015`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_remaining_call_headroom(usage: &ncos_core::ResourceUsage, budget: &ncos_core::ResourceBudget) -> u32. Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields. Replace the inline body with a direct call to protected continuous_ref_remaining_call_headroom, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-015 --output work/GCB228-015
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-0b152c54b5806f](#r-0b152c54b5806f) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-0b152c54b5806f"></a>
### 根拠 R-0b152c54b5806f

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/45`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_remaining_call_headroom(usage: &ncos_core::ResourceUsage, budget: &ncos_core::ResourceBudget) -> u32.",
    "Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields.",
    "Replace the inline body with a direct call to protected continuous_ref_remaining_call_headroom, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_remaining_call_headroom(usage: &ncos_core::ResourceUsage, budget: &ncos_core::ResourceBudget) -> u32.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_remaining_call_headroom, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-015",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_015"
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
        "continuous_gcb228_015",
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
      "cwd": "units/GCB228-015",
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
      "cwd": "units/GCB228-015",
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
      "cwd": "units/GCB228-015",
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
      "cwd": "units/GCB228-015",
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
      "cwd": "units/GCB228-015",
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
      "cwd": "units/GCB228-015",
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

<a id="gcb228-016"></a>
## GCB228-016

Refactor latency overrun flag to its protected typed helper without changing behavior

元のtask_id: `GCB228-016`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_latency_overrun_flag(usage: &ncos_core::ResourceUsage, budget: &ncos_core::ResourceBudget) -> bool. Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields. Replace the inline body with a direct call to protected continuous_ref_latency_overrun_flag, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-016 --output work/GCB228-016
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-c5b0552ce7056c](#r-c5b0552ce7056c) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-c5b0552ce7056c"></a>
### 根拠 R-c5b0552ce7056c

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/25`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_latency_overrun_flag(usage: &ncos_core::ResourceUsage, budget: &ncos_core::ResourceBudget) -> bool.",
    "Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields.",
    "Replace the inline body with a direct call to protected continuous_ref_latency_overrun_flag, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_latency_overrun_flag(usage: &ncos_core::ResourceUsage, budget: &ncos_core::ResourceBudget) -> bool.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_latency_overrun_flag, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-016",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_016"
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
        "continuous_gcb228_016",
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
      "cwd": "units/GCB228-016",
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
      "cwd": "units/GCB228-016",
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
      "cwd": "units/GCB228-016",
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
      "cwd": "units/GCB228-016",
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
      "cwd": "units/GCB228-016",
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
      "cwd": "units/GCB228-016",
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

<a id="gcb228-017"></a>
## GCB228-017

Refactor elapsed complete seconds to its protected typed helper without changing behavior

元のtask_id: `GCB228-017`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_elapsed_complete_seconds(usage: &ncos_core::ResourceUsage) -> u128. Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields. Replace the inline body with a direct call to protected continuous_ref_elapsed_complete_seconds, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-017 --output work/GCB228-017
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-de52550df603cd](#r-de52550df603cd) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-de52550df603cd"></a>
### 根拠 R-de52550df603cd

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/1`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_elapsed_complete_seconds(usage: &ncos_core::ResourceUsage) -> u128.",
    "Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields.",
    "Replace the inline body with a direct call to protected continuous_ref_elapsed_complete_seconds, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_elapsed_complete_seconds(usage: &ncos_core::ResourceUsage) -> u128.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_elapsed_complete_seconds, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-017",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_017"
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
        "continuous_gcb228_017",
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
      "cwd": "units/GCB228-017",
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
      "cwd": "units/GCB228-017",
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
      "cwd": "units/GCB228-017",
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
      "cwd": "units/GCB228-017",
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
      "cwd": "units/GCB228-017",
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
      "cwd": "units/GCB228-017",
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

<a id="gcb228-018"></a>
## GCB228-018

Refactor elapsed complete hours to its protected typed helper without changing behavior

元のtask_id: `GCB228-018`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_elapsed_complete_hours(usage: &ncos_core::ResourceUsage) -> u128. Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields. Replace the inline body with a direct call to protected continuous_ref_elapsed_complete_hours, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-018 --output work/GCB228-018
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-2388da3b3e0292](#r-2388da3b3e0292) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-2388da3b3e0292"></a>
### 根拠 R-2388da3b3e0292

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/9`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_elapsed_complete_hours(usage: &ncos_core::ResourceUsage) -> u128.",
    "Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields.",
    "Replace the inline body with a direct call to protected continuous_ref_elapsed_complete_hours, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_elapsed_complete_hours(usage: &ncos_core::ResourceUsage) -> u128.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_elapsed_complete_hours, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-018",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_018"
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
        "continuous_gcb228_018",
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
      "cwd": "units/GCB228-018",
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
      "cwd": "units/GCB228-018",
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
      "cwd": "units/GCB228-018",
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
      "cwd": "units/GCB228-018",
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
      "cwd": "units/GCB228-018",
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
      "cwd": "units/GCB228-018",
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

<a id="gcb228-019"></a>
## GCB228-019

Refactor token low byte to its protected typed helper without changing behavior

元のtask_id: `GCB228-019`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_token_low_byte(usage: &ncos_core::ResourceUsage) -> u64. Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields. Replace the inline body with a direct call to protected continuous_ref_token_low_byte, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-019 --output work/GCB228-019
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-1739396e9033a7](#r-1739396e9033a7) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-1739396e9033a7"></a>
### 根拠 R-1739396e9033a7

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/17`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_token_low_byte(usage: &ncos_core::ResourceUsage) -> u64.",
    "Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields.",
    "Replace the inline body with a direct call to protected continuous_ref_token_low_byte, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_token_low_byte(usage: &ncos_core::ResourceUsage) -> u64.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_token_low_byte, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-019",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_019"
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
        "continuous_gcb228_019",
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
      "cwd": "units/GCB228-019",
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
      "cwd": "units/GCB228-019",
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
      "cwd": "units/GCB228-019",
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
      "cwd": "units/GCB228-019",
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
      "cwd": "units/GCB228-019",
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
      "cwd": "units/GCB228-019",
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

<a id="gcb228-020"></a>
## GCB228-020

Refactor call saturation flag to its protected typed helper without changing behavior

元のtask_id: `GCB228-020`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_call_saturation_flag(usage: &ncos_core::ResourceUsage) -> bool. Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields. Replace the inline body with a direct call to protected continuous_ref_call_saturation_flag, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-020 --output work/GCB228-020
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-e3429f8288fac3](#r-e3429f8288fac3) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-e3429f8288fac3"></a>
### 根拠 R-e3429f8288fac3

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/49`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_call_saturation_flag(usage: &ncos_core::ResourceUsage) -> bool.",
    "Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields.",
    "Replace the inline body with a direct call to protected continuous_ref_call_saturation_flag, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_call_saturation_flag(usage: &ncos_core::ResourceUsage) -> bool.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_call_saturation_flag, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-020",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_020"
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
        "continuous_gcb228_020",
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
      "cwd": "units/GCB228-020",
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
      "cwd": "units/GCB228-020",
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
      "cwd": "units/GCB228-020",
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
      "cwd": "units/GCB228-020",
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
      "cwd": "units/GCB228-020",
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
      "cwd": "units/GCB228-020",
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

<a id="gcb228-021"></a>
## GCB228-021

Refactor memory unused bytes to its protected typed helper without changing behavior

元のtask_id: `GCB228-021`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_memory_unused_bytes(memory: &ncos_core::Memory) -> u64. Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields. Replace the inline body with a direct call to protected continuous_ref_memory_unused_bytes, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-021 --output work/GCB228-021
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-9b837baa73eb87](#r-9b837baa73eb87) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-9b837baa73eb87"></a>
### 根拠 R-9b837baa73eb87

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/37`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_memory_unused_bytes(memory: &ncos_core::Memory) -> u64.",
    "Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields.",
    "Replace the inline body with a direct call to protected continuous_ref_memory_unused_bytes, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_memory_unused_bytes(memory: &ncos_core::Memory) -> u64.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_memory_unused_bytes, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-021",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_021"
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
        "continuous_gcb228_021",
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
      "cwd": "units/GCB228-021",
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
      "cwd": "units/GCB228-021",
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
      "cwd": "units/GCB228-021",
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
      "cwd": "units/GCB228-021",
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
      "cwd": "units/GCB228-021",
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
      "cwd": "units/GCB228-021",
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

<a id="gcb228-022"></a>
## GCB228-022

Refactor memory unavailable kib to its protected typed helper without changing behavior

元のtask_id: `GCB228-022`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_memory_unavailable_kib(memory: &ncos_core::Memory) -> u64. Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields. Replace the inline body with a direct call to protected continuous_ref_memory_unavailable_kib, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-022 --output work/GCB228-022
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-5421cb3a6b78aa](#r-5421cb3a6b78aa) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-5421cb3a6b78aa"></a>
### 根拠 R-5421cb3a6b78aa

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/5`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_memory_unavailable_kib(memory: &ncos_core::Memory) -> u64.",
    "Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields.",
    "Replace the inline body with a direct call to protected continuous_ref_memory_unavailable_kib, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_memory_unavailable_kib(memory: &ncos_core::Memory) -> u64.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_memory_unavailable_kib, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-022",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_022"
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
        "continuous_gcb228_022",
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
      "cwd": "units/GCB228-022",
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
      "cwd": "units/GCB228-022",
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
      "cwd": "units/GCB228-022",
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
      "cwd": "units/GCB228-022",
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
      "cwd": "units/GCB228-022",
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
      "cwd": "units/GCB228-022",
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

<a id="gcb228-023"></a>
## GCB228-023

Refactor rss whole mebibytes to its protected typed helper without changing behavior

元のtask_id: `GCB228-023`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_rss_whole_mebibytes(process: &ncos_core::Process) -> u64. Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields. Replace the inline body with a direct call to protected continuous_ref_rss_whole_mebibytes, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-023 --output work/GCB228-023
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-04374273d105f5](#r-04374273d105f5) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-04374273d105f5"></a>
### 根拠 R-04374273d105f5

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/41`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_rss_whole_mebibytes(process: &ncos_core::Process) -> u64.",
    "Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields.",
    "Replace the inline body with a direct call to protected continuous_ref_rss_whole_mebibytes, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_rss_whole_mebibytes(process: &ncos_core::Process) -> u64.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_rss_whole_mebibytes, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-023",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_023"
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
        "continuous_gcb228_023",
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
      "cwd": "units/GCB228-023",
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
      "cwd": "units/GCB228-023",
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
      "cwd": "units/GCB228-023",
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
      "cwd": "units/GCB228-023",
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
      "cwd": "units/GCB228-023",
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
      "cwd": "units/GCB228-023",
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

<a id="gcb228-024"></a>
## GCB228-024

Refactor parent identity distance to its protected typed helper without changing behavior

元のtask_id: `GCB228-024`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_parent_identity_distance(process: &ncos_core::Process) -> u32. Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields. Replace the inline body with a direct call to protected continuous_ref_parent_identity_distance, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-024 --output work/GCB228-024
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-51856be4b477d8](#r-51856be4b477d8) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-51856be4b477d8"></a>
### 根拠 R-51856be4b477d8

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/13`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_parent_identity_distance(process: &ncos_core::Process) -> u32.",
    "Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields.",
    "Replace the inline body with a direct call to protected continuous_ref_parent_identity_distance, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_parent_identity_distance(process: &ncos_core::Process) -> u32.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_parent_identity_distance, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-024",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_024"
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
        "continuous_gcb228_024",
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
      "cwd": "units/GCB228-024",
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
      "cwd": "units/GCB228-024",
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
      "cwd": "units/GCB228-024",
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
      "cwd": "units/GCB228-024",
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
      "cwd": "units/GCB228-024",
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
      "cwd": "units/GCB228-024",
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

<a id="gcb228-025"></a>
## GCB228-025

Refactor observation second remainder to its protected typed helper without changing behavior

元のtask_id: `GCB228-025`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_observation_second_remainder(state: &SystemState) -> u128. Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields. Replace the inline body with a direct call to protected continuous_ref_observation_second_remainder, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-025 --output work/GCB228-025
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-c3722e44c87afc](#r-c3722e44c87afc) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-c3722e44c87afc"></a>
### 根拠 R-c3722e44c87afc

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/21`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_observation_second_remainder(state: &SystemState) -> u128.",
    "Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields.",
    "Replace the inline body with a direct call to protected continuous_ref_observation_second_remainder, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_observation_second_remainder(state: &SystemState) -> u128.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_observation_second_remainder, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-025",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_025"
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
        "continuous_gcb228_025",
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
      "cwd": "units/GCB228-025",
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
      "cwd": "units/GCB228-025",
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
      "cwd": "units/GCB228-025",
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
      "cwd": "units/GCB228-025",
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
      "cwd": "units/GCB228-025",
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
      "cwd": "units/GCB228-025",
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

<a id="gcb228-026"></a>
## GCB228-026

Refactor observation day bucket to its protected typed helper without changing behavior

元のtask_id: `GCB228-026`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_observation_day_bucket(state: &SystemState) -> u128. Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields. Replace the inline body with a direct call to protected continuous_ref_observation_day_bucket, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-026 --output work/GCB228-026
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-0dc8e5458bb084](#r-0dc8e5458bb084) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-0dc8e5458bb084"></a>
### 根拠 R-0dc8e5458bb084

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/29`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_observation_day_bucket(state: &SystemState) -> u128.",
    "Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields.",
    "Replace the inline body with a direct call to protected continuous_ref_observation_day_bucket, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_observation_day_bucket(state: &SystemState) -> u128.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve existing full-width arithmetic, saturation/equality boundaries and unrelated fields.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_observation_day_bucket, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-026",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_026"
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
        "continuous_gcb228_026",
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
      "cwd": "units/GCB228-026",
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
      "cwd": "units/GCB228-026",
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
      "cwd": "units/GCB228-026",
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
      "cwd": "units/GCB228-026",
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
      "cwd": "units/GCB228-026",
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
      "cwd": "units/GCB228-026",
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

<a id="gcb228-027"></a>
## GCB228-027

Refactor intent goal preview to its protected typed helper without changing behavior

元のtask_id: `GCB228-027`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_intent_goal_preview(intent: &ncos_core::Intent) -> String. Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes. Replace the inline body with a direct call to protected continuous_ref_intent_goal_preview, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-027 --output work/GCB228-027
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-eb65904ca97cb5](#r-eb65904ca97cb5) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-eb65904ca97cb5"></a>
### 根拠 R-eb65904ca97cb5

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/18`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_intent_goal_preview(intent: &ncos_core::Intent) -> String.",
    "Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes.",
    "Replace the inline body with a direct call to protected continuous_ref_intent_goal_preview, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_intent_goal_preview(intent: &ncos_core::Intent) -> String.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_intent_goal_preview, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-027",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_027"
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
        "continuous_gcb228_027",
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
      "cwd": "units/GCB228-027",
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
      "cwd": "units/GCB228-027",
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
      "cwd": "units/GCB228-027",
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
      "cwd": "units/GCB228-027",
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
      "cwd": "units/GCB228-027",
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
      "cwd": "units/GCB228-027",
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

<a id="gcb228-028"></a>
## GCB228-028

Refactor intent id uppercase to its protected typed helper without changing behavior

元のtask_id: `GCB228-028`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_intent_id_uppercase(intent: &ncos_core::Intent) -> String. Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes. Replace the inline body with a direct call to protected continuous_ref_intent_id_uppercase, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-028 --output work/GCB228-028
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-1ed4291ef69e85](#r-1ed4291ef69e85) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-1ed4291ef69e85"></a>
### 根拠 R-1ed4291ef69e85

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/46`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_intent_id_uppercase(intent: &ncos_core::Intent) -> String.",
    "Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes.",
    "Replace the inline body with a direct call to protected continuous_ref_intent_id_uppercase, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_intent_id_uppercase(intent: &ncos_core::Intent) -> String.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_intent_id_uppercase, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-028",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_028"
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
        "continuous_gcb228_028",
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
      "cwd": "units/GCB228-028",
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
      "cwd": "units/GCB228-028",
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
      "cwd": "units/GCB228-028",
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
      "cwd": "units/GCB228-028",
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
      "cwd": "units/GCB228-028",
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
      "cwd": "units/GCB228-028",
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

<a id="gcb228-029"></a>
## GCB228-029

Refactor source lowercase to its protected typed helper without changing behavior

元のtask_id: `GCB228-029`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_source_lowercase(record: &ncos_core::AuditRecord) -> String. Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes. Replace the inline body with a direct call to protected continuous_ref_source_lowercase, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-029 --output work/GCB228-029
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-cf5f2c8bc7fab9](#r-cf5f2c8bc7fab9) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-cf5f2c8bc7fab9"></a>
### 根拠 R-cf5f2c8bc7fab9

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/2`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_source_lowercase(record: &ncos_core::AuditRecord) -> String.",
    "Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes.",
    "Replace the inline body with a direct call to protected continuous_ref_source_lowercase, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_source_lowercase(record: &ncos_core::AuditRecord) -> String.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_source_lowercase, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-029",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_029"
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
        "continuous_gcb228_029",
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
      "cwd": "units/GCB228-029",
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
      "cwd": "units/GCB228-029",
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
      "cwd": "units/GCB228-029",
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
      "cwd": "units/GCB228-029",
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
      "cwd": "units/GCB228-029",
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
      "cwd": "units/GCB228-029",
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

<a id="gcb228-030"></a>
## GCB228-030

Refactor short reason preview to its protected typed helper without changing behavior

元のtask_id: `GCB228-030`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_short_reason_preview(record: &ncos_core::AuditRecord) -> String. Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes. Replace the inline body with a direct call to protected continuous_ref_short_reason_preview, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-030 --output work/GCB228-030
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-416ceb42d6eebd](#r-416ceb42d6eebd) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-416ceb42d6eebd"></a>
### 根拠 R-416ceb42d6eebd

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/50`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_short_reason_preview(record: &ncos_core::AuditRecord) -> String.",
    "Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes.",
    "Replace the inline body with a direct call to protected continuous_ref_short_reason_preview, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_short_reason_preview(record: &ncos_core::AuditRecord) -> String.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_short_reason_preview, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-030",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_030"
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
        "continuous_gcb228_030",
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
      "cwd": "units/GCB228-030",
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
      "cwd": "units/GCB228-030",
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
      "cwd": "units/GCB228-030",
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
      "cwd": "units/GCB228-030",
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
      "cwd": "units/GCB228-030",
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
      "cwd": "units/GCB228-030",
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

<a id="gcb228-031"></a>
## GCB228-031

Refactor event target uppercase to its protected typed helper without changing behavior

元のtask_id: `GCB228-031`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_event_target_uppercase(event: &ncos_core::Event) -> String. Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes. Replace the inline body with a direct call to protected continuous_ref_event_target_uppercase, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-031 --output work/GCB228-031
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-5b1ef78b3cd0cc](#r-5b1ef78b3cd0cc) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-5b1ef78b3cd0cc"></a>
### 根拠 R-5b1ef78b3cd0cc

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/38`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_event_target_uppercase(event: &ncos_core::Event) -> String.",
    "Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes.",
    "Replace the inline body with a direct call to protected continuous_ref_event_target_uppercase, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_event_target_uppercase(event: &ncos_core::Event) -> String.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_event_target_uppercase, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-031",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_031"
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
        "continuous_gcb228_031",
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
      "cwd": "units/GCB228-031",
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
      "cwd": "units/GCB228-031",
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
      "cwd": "units/GCB228-031",
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
      "cwd": "units/GCB228-031",
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
      "cwd": "units/GCB228-031",
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
      "cwd": "units/GCB228-031",
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

<a id="gcb228-032"></a>
## GCB228-032

Refactor event id lowercase to its protected typed helper without changing behavior

元のtask_id: `GCB228-032`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_event_id_lowercase(event: &ncos_core::Event) -> String. Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes. Replace the inline body with a direct call to protected continuous_ref_event_id_lowercase, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-032 --output work/GCB228-032
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-dd15c9f8ba5755](#r-dd15c9f8ba5755) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-dd15c9f8ba5755"></a>
### 根拠 R-dd15c9f8ba5755

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/6`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_event_id_lowercase(event: &ncos_core::Event) -> String.",
    "Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes.",
    "Replace the inline body with a direct call to protected continuous_ref_event_id_lowercase, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_event_id_lowercase(event: &ncos_core::Event) -> String.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_event_id_lowercase, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-032",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_032"
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
        "continuous_gcb228_032",
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
      "cwd": "units/GCB228-032",
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
      "cwd": "units/GCB228-032",
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
      "cwd": "units/GCB228-032",
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
      "cwd": "units/GCB228-032",
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
      "cwd": "units/GCB228-032",
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
      "cwd": "units/GCB228-032",
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

<a id="gcb228-033"></a>
## GCB228-033

Refactor intent constraint csv to its protected typed helper without changing behavior

元のtask_id: `GCB228-033`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_intent_constraint_csv(intent: &ncos_core::Intent) -> String. Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes. Replace the inline body with a direct call to protected continuous_ref_intent_constraint_csv, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-033 --output work/GCB228-033
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-53c804cffea06a](#r-53c804cffea06a) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-53c804cffea06a"></a>
### 根拠 R-53c804cffea06a

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/34`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_intent_constraint_csv(intent: &ncos_core::Intent) -> String.",
    "Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes.",
    "Replace the inline body with a direct call to protected continuous_ref_intent_constraint_csv, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_intent_constraint_csv(intent: &ncos_core::Intent) -> String.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_intent_constraint_csv, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-033",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_033"
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
        "continuous_gcb228_033",
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
      "cwd": "units/GCB228-033",
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
      "cwd": "units/GCB228-033",
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
      "cwd": "units/GCB228-033",
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
      "cwd": "units/GCB228-033",
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
      "cwd": "units/GCB228-033",
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
      "cwd": "units/GCB228-033",
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

<a id="gcb228-034"></a>
## GCB228-034

Refactor evidence semicolon text to its protected typed helper without changing behavior

元のtask_id: `GCB228-034`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_evidence_semicolon_text(event: &ncos_core::Event) -> String. Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes. Replace the inline body with a direct call to protected continuous_ref_evidence_semicolon_text, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-034 --output work/GCB228-034
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-739d538f41aaaf](#r-739d538f41aaaf) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-739d538f41aaaf"></a>
### 根拠 R-739d538f41aaaf

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/30`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_evidence_semicolon_text(event: &ncos_core::Event) -> String.",
    "Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes.",
    "Replace the inline body with a direct call to protected continuous_ref_evidence_semicolon_text, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_evidence_semicolon_text(event: &ncos_core::Event) -> String.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_evidence_semicolon_text, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-034",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_034"
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
        "continuous_gcb228_034",
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
      "cwd": "units/GCB228-034",
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
      "cwd": "units/GCB228-034",
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
      "cwd": "units/GCB228-034",
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
      "cwd": "units/GCB228-034",
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
      "cwd": "units/GCB228-034",
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
      "cwd": "units/GCB228-034",
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

<a id="gcb228-035"></a>
## GCB228-035

Refactor pid binary label to its protected typed helper without changing behavior

元のtask_id: `GCB228-035`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_pid_binary_label(process: &ncos_core::Process) -> String. Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes. Replace the inline body with a direct call to protected continuous_ref_pid_binary_label, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-035 --output work/GCB228-035
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-e5eed04c666c5e](#r-e5eed04c666c5e) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-e5eed04c666c5e"></a>
### 根拠 R-e5eed04c666c5e

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/42`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_pid_binary_label(process: &ncos_core::Process) -> String.",
    "Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes.",
    "Replace the inline body with a direct call to protected continuous_ref_pid_binary_label, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_pid_binary_label(process: &ncos_core::Process) -> String.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_pid_binary_label, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-035",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_035"
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
        "continuous_gcb228_035",
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
      "cwd": "units/GCB228-035",
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
      "cwd": "units/GCB228-035",
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
      "cwd": "units/GCB228-035",
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
      "cwd": "units/GCB228-035",
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
      "cwd": "units/GCB228-035",
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
      "cwd": "units/GCB228-035",
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

<a id="gcb228-036"></a>
## GCB228-036

Refactor parent hex label to its protected typed helper without changing behavior

元のtask_id: `GCB228-036`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_parent_hex_label(process: &ncos_core::Process) -> String. Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes. Replace the inline body with a direct call to protected continuous_ref_parent_hex_label, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-036 --output work/GCB228-036
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-9d49f057cbd652](#r-9d49f057cbd652) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-9d49f057cbd652"></a>
### 根拠 R-9d49f057cbd652

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/14`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_parent_hex_label(process: &ncos_core::Process) -> String.",
    "Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes.",
    "Replace the inline body with a direct call to protected continuous_ref_parent_hex_label, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_parent_hex_label(process: &ncos_core::Process) -> String.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_parent_hex_label, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-036",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_036"
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
        "continuous_gcb228_036",
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
      "cwd": "units/GCB228-036",
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
      "cwd": "units/GCB228-036",
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
      "cwd": "units/GCB228-036",
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
      "cwd": "units/GCB228-036",
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
      "cwd": "units/GCB228-036",
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
      "cwd": "units/GCB228-036",
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

<a id="gcb228-037"></a>
## GCB228-037

Refactor tokens decimal label to its protected typed helper without changing behavior

元のtask_id: `GCB228-037`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_tokens_decimal_label(usage: &ncos_core::ResourceUsage) -> String. Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes. Replace the inline body with a direct call to protected continuous_ref_tokens_decimal_label, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-037 --output work/GCB228-037
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-5f1afdef0fe7e8](#r-5f1afdef0fe7e8) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-5f1afdef0fe7e8"></a>
### 根拠 R-5f1afdef0fe7e8

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/22`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_tokens_decimal_label(usage: &ncos_core::ResourceUsage) -> String.",
    "Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes.",
    "Replace the inline body with a direct call to protected continuous_ref_tokens_decimal_label, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_tokens_decimal_label(usage: &ncos_core::ResourceUsage) -> String.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_tokens_decimal_label, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-037",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_037"
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
        "continuous_gcb228_037",
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
      "cwd": "units/GCB228-037",
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
      "cwd": "units/GCB228-037",
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
      "cwd": "units/GCB228-037",
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
      "cwd": "units/GCB228-037",
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
      "cwd": "units/GCB228-037",
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
      "cwd": "units/GCB228-037",
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

<a id="gcb228-038"></a>
## GCB228-038

Refactor calls decimal label to its protected typed helper without changing behavior

元のtask_id: `GCB228-038`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_calls_decimal_label(usage: &ncos_core::ResourceUsage) -> String. Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes. Replace the inline body with a direct call to protected continuous_ref_calls_decimal_label, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-038 --output work/GCB228-038
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-bc613d09f14101](#r-bc613d09f14101) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-bc613d09f14101"></a>
### 根拠 R-bc613d09f14101

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/10`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_calls_decimal_label(usage: &ncos_core::ResourceUsage) -> String.",
    "Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes.",
    "Replace the inline body with a direct call to protected continuous_ref_calls_decimal_label, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_calls_decimal_label(usage: &ncos_core::ResourceUsage) -> String.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_calls_decimal_label, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-038",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_038"
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
        "continuous_gcb228_038",
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
      "cwd": "units/GCB228-038",
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
      "cwd": "units/GCB228-038",
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
      "cwd": "units/GCB228-038",
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
      "cwd": "units/GCB228-038",
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
      "cwd": "units/GCB228-038",
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
      "cwd": "units/GCB228-038",
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

<a id="gcb228-039"></a>
## GCB228-039

Refactor schema decimal label to its protected typed helper without changing behavior

元のtask_id: `GCB228-039`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_schema_decimal_label(record: &ncos_core::AuditRecord) -> String. Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes. Replace the inline body with a direct call to protected continuous_ref_schema_decimal_label, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-039 --output work/GCB228-039
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | ESCALATE | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | false | [R-9ceb6e53c5ae2d](#r-9ceb6e53c5ae2d) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-9ceb6e53c5ae2d"></a>
### 根拠 R-9ceb6e53c5ae2d

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/26`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_schema_decimal_label(record: &ncos_core::AuditRecord) -> String.",
    "Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes.",
    "Replace the inline body with a direct call to protected continuous_ref_schema_decimal_label, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_schema_decimal_label(record: &ncos_core::AuditRecord) -> String.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve the exact existing Unicode, separator and field selection behavior; no trimming or extra bytes.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_schema_decimal_label, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-039",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_039"
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
        "continuous_gcb228_039",
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
      "cwd": "units/GCB228-039",
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
      "cwd": "units/GCB228-039",
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
      "cwd": "units/GCB228-039",
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
      "cwd": "units/GCB228-039",
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
      "cwd": "units/GCB228-039",
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
      "cwd": "units/GCB228-039",
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

<a id="gcb228-040"></a>
## GCB228-040

Refactor logical cpu receipt to its protected typed helper without changing behavior

元のtask_id: `GCB228-040`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_logical_cpu_receipt(state: &SystemState) -> String. Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics. Replace the inline body with a direct call to protected continuous_ref_logical_cpu_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-040 --output work/GCB228-040
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-fa9e6f317660e1](#r-fa9e6f317660e1) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-fa9e6f317660e1"></a>
### 根拠 R-fa9e6f317660e1

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/15`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_logical_cpu_receipt(state: &SystemState) -> String.",
    "Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics.",
    "Replace the inline body with a direct call to protected continuous_ref_logical_cpu_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_logical_cpu_receipt(state: &SystemState) -> String.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_logical_cpu_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-040",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_040"
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
        "continuous_gcb228_040",
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
      "cwd": "units/GCB228-040",
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
      "cwd": "units/GCB228-040",
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
      "cwd": "units/GCB228-040",
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
      "cwd": "units/GCB228-040",
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
      "cwd": "units/GCB228-040",
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
      "cwd": "units/GCB228-040",
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

<a id="gcb228-041"></a>
## GCB228-041

Refactor disk known receipt to its protected typed helper without changing behavior

元のtask_id: `GCB228-041`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_disk_known_receipt(state: &SystemState) -> String. Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics. Replace the inline body with a direct call to protected continuous_ref_disk_known_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-041 --output work/GCB228-041
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-2d73c108df8d40](#r-2d73c108df8d40) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-2d73c108df8d40"></a>
### 根拠 R-2d73c108df8d40

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/43`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_disk_known_receipt(state: &SystemState) -> String.",
    "Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics.",
    "Replace the inline body with a direct call to protected continuous_ref_disk_known_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_disk_known_receipt(state: &SystemState) -> String.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_disk_known_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-041",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_041"
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
        "continuous_gcb228_041",
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
      "cwd": "units/GCB228-041",
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
      "cwd": "units/GCB228-041",
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
      "cwd": "units/GCB228-041",
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
      "cwd": "units/GCB228-041",
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
      "cwd": "units/GCB228-041",
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
      "cwd": "units/GCB228-041",
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

<a id="gcb228-042"></a>
## GCB228-042

Refactor service known receipt to its protected typed helper without changing behavior

元のtask_id: `GCB228-042`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_service_known_receipt(state: &SystemState) -> String. Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics. Replace the inline body with a direct call to protected continuous_ref_service_known_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-042 --output work/GCB228-042
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-7f58715cdbf3ce](#r-7f58715cdbf3ce) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-7f58715cdbf3ce"></a>
### 根拠 R-7f58715cdbf3ce

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/27`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_service_known_receipt(state: &SystemState) -> String.",
    "Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics.",
    "Replace the inline body with a direct call to protected continuous_ref_service_known_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_service_known_receipt(state: &SystemState) -> String.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_service_known_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-042",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_042"
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
        "continuous_gcb228_042",
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
      "cwd": "units/GCB228-042",
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
      "cwd": "units/GCB228-042",
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
      "cwd": "units/GCB228-042",
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
      "cwd": "units/GCB228-042",
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
      "cwd": "units/GCB228-042",
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
      "cwd": "units/GCB228-042",
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

<a id="gcb228-043"></a>
## GCB228-043

Refactor tcp known receipt to its protected typed helper without changing behavior

元のtask_id: `GCB228-043`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_tcp_known_receipt(state: &SystemState) -> String. Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics. Replace the inline body with a direct call to protected continuous_ref_tcp_known_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-043 --output work/GCB228-043
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-e0ca820555b36f](#r-e0ca820555b36f) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-e0ca820555b36f"></a>
### 根拠 R-e0ca820555b36f

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/11`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_tcp_known_receipt(state: &SystemState) -> String.",
    "Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics.",
    "Replace the inline body with a direct call to protected continuous_ref_tcp_known_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_tcp_known_receipt(state: &SystemState) -> String.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_tcp_known_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-043",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_043"
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
        "continuous_gcb228_043",
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
      "cwd": "units/GCB228-043",
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
      "cwd": "units/GCB228-043",
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
      "cwd": "units/GCB228-043",
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
      "cwd": "units/GCB228-043",
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
      "cwd": "units/GCB228-043",
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
      "cwd": "units/GCB228-043",
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

<a id="gcb228-044"></a>
## GCB228-044

Refactor truncated receipt to its protected typed helper without changing behavior

元のtask_id: `GCB228-044`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_truncated_receipt(state: &SystemState) -> String. Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics. Replace the inline body with a direct call to protected continuous_ref_truncated_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-044 --output work/GCB228-044
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-2af03b8c7cb595](#r-2af03b8c7cb595) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-2af03b8c7cb595"></a>
### 根拠 R-2af03b8c7cb595

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/7`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_truncated_receipt(state: &SystemState) -> String.",
    "Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics.",
    "Replace the inline body with a direct call to protected continuous_ref_truncated_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_truncated_receipt(state: &SystemState) -> String.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_truncated_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-044",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_044"
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
        "continuous_gcb228_044",
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
      "cwd": "units/GCB228-044",
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
      "cwd": "units/GCB228-044",
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
      "cwd": "units/GCB228-044",
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
      "cwd": "units/GCB228-044",
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
      "cwd": "units/GCB228-044",
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
      "cwd": "units/GCB228-044",
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

<a id="gcb228-045"></a>
## GCB228-045

Refactor warning byte total receipt to its protected typed helper without changing behavior

元のtask_id: `GCB228-045`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_warning_byte_total_receipt(state: &SystemState) -> String. Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics. Replace the inline body with a direct call to protected continuous_ref_warning_byte_total_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-045 --output work/GCB228-045
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-d3dfd61d0945a6](#r-d3dfd61d0945a6) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-d3dfd61d0945a6"></a>
### 根拠 R-d3dfd61d0945a6

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/39`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_warning_byte_total_receipt(state: &SystemState) -> String.",
    "Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics.",
    "Replace the inline body with a direct call to protected continuous_ref_warning_byte_total_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_warning_byte_total_receipt(state: &SystemState) -> String.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_warning_byte_total_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-045",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_045"
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
        "continuous_gcb228_045",
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
      "cwd": "units/GCB228-045",
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
      "cwd": "units/GCB228-045",
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
      "cwd": "units/GCB228-045",
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
      "cwd": "units/GCB228-045",
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
      "cwd": "units/GCB228-045",
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
      "cwd": "units/GCB228-045",
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

<a id="gcb228-046"></a>
## GCB228-046

Refactor warning scalar total receipt to its protected typed helper without changing behavior

元のtask_id: `GCB228-046`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_warning_scalar_total_receipt(state: &SystemState) -> String. Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics. Replace the inline body with a direct call to protected continuous_ref_warning_scalar_total_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-046 --output work/GCB228-046
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-9d08852a251418](#r-9d08852a251418) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-9d08852a251418"></a>
### 根拠 R-9d08852a251418

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/19`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_warning_scalar_total_receipt(state: &SystemState) -> String.",
    "Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics.",
    "Replace the inline body with a direct call to protected continuous_ref_warning_scalar_total_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_warning_scalar_total_receipt(state: &SystemState) -> String.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_warning_scalar_total_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-046",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_046"
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
        "continuous_gcb228_046",
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
      "cwd": "units/GCB228-046",
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
      "cwd": "units/GCB228-046",
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
      "cwd": "units/GCB228-046",
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
      "cwd": "units/GCB228-046",
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
      "cwd": "units/GCB228-046",
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
      "cwd": "units/GCB228-046",
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

<a id="gcb228-047"></a>
## GCB228-047

Refactor rss row count receipt to its protected typed helper without changing behavior

元のtask_id: `GCB228-047`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_rss_row_count_receipt(state: &SystemState) -> String. Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics. Replace the inline body with a direct call to protected continuous_ref_rss_row_count_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-047 --output work/GCB228-047
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-a4cbeb52e33d40](#r-a4cbeb52e33d40) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-a4cbeb52e33d40"></a>
### 根拠 R-a4cbeb52e33d40

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/47`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_rss_row_count_receipt(state: &SystemState) -> String.",
    "Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics.",
    "Replace the inline body with a direct call to protected continuous_ref_rss_row_count_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_rss_row_count_receipt(state: &SystemState) -> String.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_rss_row_count_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-047",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_047"
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
        "continuous_gcb228_047",
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
      "cwd": "units/GCB228-047",
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
      "cwd": "units/GCB228-047",
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
      "cwd": "units/GCB228-047",
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
      "cwd": "units/GCB228-047",
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
      "cwd": "units/GCB228-047",
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
      "cwd": "units/GCB228-047",
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

<a id="gcb228-048"></a>
## GCB228-048

Refactor memory total receipt to its protected typed helper without changing behavior

元のtask_id: `GCB228-048`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_memory_total_receipt(state: &SystemState) -> String. Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics. Replace the inline body with a direct call to protected continuous_ref_memory_total_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-048 --output work/GCB228-048
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-d56cb9ddd77bff](#r-d56cb9ddd77bff) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-d56cb9ddd77bff"></a>
### 根拠 R-d56cb9ddd77bff

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/35`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_memory_total_receipt(state: &SystemState) -> String.",
    "Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics.",
    "Replace the inline body with a direct call to protected continuous_ref_memory_total_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_memory_total_receipt(state: &SystemState) -> String.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_memory_total_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-048",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_048"
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
        "continuous_gcb228_048",
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
      "cwd": "units/GCB228-048",
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
      "cwd": "units/GCB228-048",
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
      "cwd": "units/GCB228-048",
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
      "cwd": "units/GCB228-048",
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
      "cwd": "units/GCB228-048",
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
      "cwd": "units/GCB228-048",
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

<a id="gcb228-049"></a>
## GCB228-049

Refactor available memory receipt to its protected typed helper without changing behavior

元のtask_id: `GCB228-049`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_available_memory_receipt(state: &SystemState) -> String. Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics. Replace the inline body with a direct call to protected continuous_ref_available_memory_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-049 --output work/GCB228-049
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-5ad7ce327c04d1](#r-5ad7ce327c04d1) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-5ad7ce327c04d1"></a>
### 根拠 R-5ad7ce327c04d1

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/3`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_available_memory_receipt(state: &SystemState) -> String.",
    "Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics.",
    "Replace the inline body with a direct call to protected continuous_ref_available_memory_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_available_memory_receipt(state: &SystemState) -> String.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_available_memory_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-049",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_049"
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
        "continuous_gcb228_049",
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
      "cwd": "units/GCB228-049",
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
      "cwd": "units/GCB228-049",
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
      "cwd": "units/GCB228-049",
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
      "cwd": "units/GCB228-049",
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
      "cwd": "units/GCB228-049",
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
      "cwd": "units/GCB228-049",
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

<a id="gcb228-050"></a>
## GCB228-050

Refactor observed millis receipt to its protected typed helper without changing behavior

元のtask_id: `GCB228-050`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_observed_millis_receipt(state: &SystemState) -> String. Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics. Replace the inline body with a direct call to protected continuous_ref_observed_millis_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-050 --output work/GCB228-050
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-c0c477793d06b1](#r-c0c477793d06b1) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-c0c477793d06b1"></a>
### 根拠 R-c0c477793d06b1

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/31`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_observed_millis_receipt(state: &SystemState) -> String.",
    "Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics.",
    "Replace the inline body with a direct call to protected continuous_ref_observed_millis_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_observed_millis_receipt(state: &SystemState) -> String.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_observed_millis_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-050",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_050"
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
        "continuous_gcb228_050",
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
      "cwd": "units/GCB228-050",
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
      "cwd": "units/GCB228-050",
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
      "cwd": "units/GCB228-050",
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
      "cwd": "units/GCB228-050",
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
      "cwd": "units/GCB228-050",
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
      "cwd": "units/GCB228-050",
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

<a id="gcb228-051"></a>
## GCB228-051

Refactor nonblank warning receipt to its protected typed helper without changing behavior

元のtask_id: `GCB228-051`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_nonblank_warning_receipt(state: &SystemState) -> String. Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics. Replace the inline body with a direct call to protected continuous_ref_nonblank_warning_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-051 --output work/GCB228-051
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-5e8e42a232dede](#r-5e8e42a232dede) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-5e8e42a232dede"></a>
### 根拠 R-5e8e42a232dede

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/23`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_nonblank_warning_receipt(state: &SystemState) -> String.",
    "Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics.",
    "Replace the inline body with a direct call to protected continuous_ref_nonblank_warning_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_nonblank_warning_receipt(state: &SystemState) -> String.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_nonblank_warning_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-051",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_051"
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
        "continuous_gcb228_051",
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
      "cwd": "units/GCB228-051",
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
      "cwd": "units/GCB228-051",
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
      "cwd": "units/GCB228-051",
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
      "cwd": "units/GCB228-051",
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
      "cwd": "units/GCB228-051",
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
      "cwd": "units/GCB228-051",
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

<a id="gcb228-052"></a>
## GCB228-052

Refactor root count receipt to its protected typed helper without changing behavior

元のtask_id: `GCB228-052`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn continuous_root_count_receipt(state: &SystemState) -> String. Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics. Replace the inline body with a direct call to protected continuous_ref_root_count_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass. Do not mutate input, modify the helper, tests or any other source.

取り出し方:

```sh
python materialize_task.py --set gemma26-continuous-backend-soak-v2--run-002 --task GCB228-052 --output work/GCB228-052
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | 記録に条件の明記なし | COMPLETE | PASS | MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | — | — | true | [R-d0ce7e334e1171](#r-d0ce7e334e1171) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-d0ce7e334e1171"></a>
### 根拠 R-d0ce7e334e1171

- 対応方法: 同一セット・課題IDによる対応
- 出典: `FINAL_SUMMARY.json` / 位置: `/tasks/51`
- 出典ファイルのSHA-256: `4dc0fa1ac352ef554e1a37068155d9a8bbb64ae8a7943f38ae342da8119605ee`
- [抽出した測定値・他の工程の記録](../results/gemma26-continuous-backend-soak-v2--run-002.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn continuous_root_count_receipt(state: &SystemState) -> String.",
    "Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics.",
    "Replace the inline body with a direct call to protected continuous_ref_root_count_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
    "Do not mutate input, modify the helper, tests or any other source.",
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
      "criterion_text": "Preserve exact signature: pub fn continuous_root_count_receipt(state: &SystemState) -> String.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve exact single-LF receipt, decimal value, existing field/predicate and empty/extreme semantics.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Replace the inline body with a direct call to protected continuous_ref_root_count_receipt, forwarding the declared parameters in their original order. Do not duplicate its computation or retain the inline implementation. This refactor requirement is independently contract-reviewed; pristine behavioral tests intentionally already pass.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-4",
      "criterion_text": "Do not mutate input, modify the helper, tests or any other source.",
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
      "cwd": "units/GCB228-052",
      "timeout_seconds": 330,
      "required_test_ids": [
        "continuous_gcb228_052"
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
        "continuous_gcb228_052",
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
      "cwd": "units/GCB228-052",
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
      "cwd": "units/GCB228-052",
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
      "cwd": "units/GCB228-052",
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
      "cwd": "units/GCB228-052",
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
      "cwd": "units/GCB228-052",
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
      "cwd": "units/GCB228-052",
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
