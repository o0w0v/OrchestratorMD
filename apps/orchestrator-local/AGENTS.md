# Standalone Python application

This directory contains a Windows CSV/JSON application, separate from the historical Rust coding-worker rules at the repository root. It does not edit a user's source repository or implement the Production Router.

Run `python -X utf8 -B -m unittest discover -s tests -v` using the installed application dependencies. Tests must use the fake backend; do not add live inference, model downloads, paid Cloud calls, or changes to a user's actual MCP/Skill registration to the test suite. The public repository does not contain the historical Cargo workspace or `scripts/test_worker.py` mentioned by the root guidance.

Keep user settings, credentials, SQLite jobs, runtime logs, model files, virtual environments and installation receipts out of commits. Preserve existing results and unrelated MCP/Skill settings. Do not adopt a candidate until conversation review; usable output is accepted without optional rewrites. Changes to schemas or business requirements must come from the user, not a reviewer preference.
