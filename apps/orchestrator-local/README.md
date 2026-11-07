# Orchestrator Local 0.1.0 — Windows preview

> Keep asking your usual AI as before. Share some of the work with an AI on your PC to reduce Cloud AI consumption.

**[日本語の導入手順・使い方](README_JA.md)**

## Why use it?

The goal is to keep the familiar way of asking for work, receive results of the quality you need, and lower the cost of producing them. Handoffs, precise edits and file saving are the mechanisms behind that goal.

### What the 100-case comparison measured

The comparison included initial consultation/design and the final Sol review and partial corrections.

|Measure|Usual Sol|New approach, including Sol review/corrections|
|---|---:|---:|
|Reported-usage Credits subtotal|181.64328|122.10496|
|Adopted data correct|100/100 cases|100/100 cases|
|Mean active time, including consultation|63.10 seconds|247.32 seconds|

**The known subtotal fell by 59.53832 Credits, about 32.78%.** Both methods shared direct Sol execution for 14 small cases. The new approach used Gemma for the other 86; its subtotal includes all 86 Sol reviews and the 12 partial corrections made in those reviews. Processing took longer.

These are results for 100 synthetic business-data cases. Unmeasured consumption prevents an exact total or reduction percentage; those unknown amounts are in the shared consultation stage and cancel out of the difference when allocated equally. Prose equivalence was not independently audited across every case. See the [completion review](../../benchmarks/practical-review-100/2026-11-05/COMPLETION_REVIEW_JA.md) for conditions and evidence.

The public application does not yet measure conversation-side Credits. This measured study result and the savings achieved in each use of the application are separate questions.

### What happens behind the scenes

The conversation AI handles consultation/design and final review, while Gemma does some of the work. Usable output is kept; necessary corrections are saved as precise edits. The [internal design](DESIGN_JA.md) and the implementation notes below explain this workflow.

## Before installing

This is a source release for Windows users who already have Python 3.11+ and a working Ollama installation with `gemma4:26b`. Model weights, Ollama, Python, user configuration, job data and credentials are not included. This is not a one-click installer or a reviewed plugin-directory listing. macOS/Linux and other machines have not been acceptance tested.

The model creates candidates only. The conversation checks them against the original request, accepts usable output, or patches errors that affect use. It does not regenerate results to improve style. Files and SQLite jobs survive MCP reconnects; failed or interrupted generations are not retried automatically.

The local service talks only to a configured loopback Ollama endpoint. Inputs and candidates are also returned to the conversation for review, so this is not an entirely offline workflow. Conversation usage is not measured by this application, and cost savings are not guaranteed.

See [validation and scope](VALIDATION.md), [the design](DESIGN_JA.md), and the repository [license](LICENSE).
