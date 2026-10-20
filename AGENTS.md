# Repository guidance

## Repository and checks

- Rust workspace: eight `ncos-*` crates. Core owns contracts, policy authority, agent composition, CLI boundary. Preserve APIs, naming and dependencies. Application behavior remains strictly dry-run; development-worker tools do not grant authority to the Rust application.
- Before changes, read relevant docs/CI and Git status. Use a feature/fix branch; preserve user changes, existing logs and Phase 1/2 experiment artifacts. No force push/history rewrite or direct main/master push.
- Required checks: `python scripts/test_worker.py`, `cargo fmt --check`, `cargo clippy --all-targets --all-features -- -D warnings`, `cargo test --workspace`, `cargo check --workspace --locked`, `cargo build --workspace --locked`. On Windows use the verified WSL toolchain from parent AGENTS.md.

## Local Worker default: Router v2.1 shadow mode

- Read [LOCAL_WORKER.md](docs/LOCAL_WORKER.md), [MODEL_ROUTER.md](docs/MODEL_ROUTER.md) and [PROTOCOL_ROUTER.md](docs/PROTOCOL_ROUTER.md). New tasks use schema_version 3; legacy v2 specs/results keep their original Qwen path and are not silently migrated/reset.
- Codex owns architecture, types/interface/scaffold, acceptance meaning, risk, decomposition and final review. Local LLM implements one closed responsibility/behavior. Host/tests enforce limits. Optimize total Codex work, not local tokens or delegation rate. Direct Codex work is appropriate for infrastructure/security or when cheaper.
- Ready: explicit goal/interface/acceptance/validation, reviewed risk/sensitive areas, small file/read/tool scope. Default guard is 1-2 editable files and 80 added+deleted LOC; responsibility determines decomposition. Freeze contracts/tests outside editable regions. Never delegate a whole complex parser/state machine, ambiguous/security/auth/DB/public API redesign.
- Protocol and model are independent: known edit location -> FIXED_SLOT (host owns path/region/markers; model returns slot bodies only); unknown location -> bounded AGENTIC; no edit -> typed REASONING without edit tools. Do not choose AGENTIC when FIXED_SLOT suffices.
- Router v2.1 adds config/worker/operational_policy.json over the preserved v2 capability registry. Gemma12 is quarantined: never dispatch it, including probes. Gemma26 handles measured light/localized and normal coding; CoderNext retains debugging. Qwen14 remains experimental and is not an automatic fallback. Decisions retain preferred_model, selected_model and override_reason. High-risk/complex/unknown categories stay with Codex. BOUNDED_LOGIC requires reviewed decomposition and a parent ID. Free specification is Codex-owned; only typed extraction may be local.
- Before/after live local dispatch, use read-only GPU/API/backend/residency health checks, never a per-task generation probe. CUDA/backend failure or repeated GPU query timeout is INFRA_ERROR: preserve raw evidence and stop the cohort. Never retry infrastructure or change routes during a frozen cohort. Phase 3 evidence measures operational stability, not coding capability.
- No implicit model download/cloud/fallback. Model tools have no unrestricted shell, network, package installation, secret access, commit or push. Tests use trusted fixed argv/check IDs. The private Git copy is NOT an OS sandbox; untrusted generated code needs a separately verified containment boundary.

## Execution, review and accounting

- Local implementation -> targeted test/lint -> actual stdout/stderr to same model -> one repair -> targeted test. Maximum two code attempts; Codex does not participate in ordinary retry diagnosis/prompts. Never regenerate whole files or relax tests.
- OUTPUT_LIMIT -> immediate RESPLIT, no retry/continuation/budget increase. SCOPE_VIOLATION -> reject/review protocol. Two code failures -> evaluate decomposition before another model. No fixed model ladder. v3 GENERATION_FAILED is invalid model output; transport/persistence INFRA_ERROR is separate and excluded from capability metrics. v3 has no automatic infrastructure retry.
- Worker operates only on a private branch/index baseline in .worker-v2, returns evidence under records/router-v2, and never adopts to original source/main. Existing IDs/results cannot be reset. Resplit children keep parent_task_id.
- Gates: DESIGN READY -> UNIT READY -> INTEGRATION READY -> REVIEW READY -> commit/PR. Local PASS means UNIT READY only. Verify original base hashes before integration and rerun impacted checks after changes.
- Review task/decision/model/protocol, git diff/stat, checks/validation, attempts, short summary and risks; not entire conversation/reasoning history. 3-5 independent low-risk PASS tasks may be batched; sensitive scope/high risk/public API changes are excluded.
- Record local usage/time, first/repair outcome, escalation and supervisor review/modified-code/repair LOC/acceptance. router_metrics.py writes separate evidence-bound review annotations and KPI reports. Missing Codex planning/review/repair input/output tokens stay null; local tokens are not savings. Preserve failed results after later manual repair/adoption.
- Final report states changes, direct/delegated work, tests and dry runs, remaining limits, next KPI measurements, commit/branch/PR state. Do not claim production success from small synthetic fixtures.
