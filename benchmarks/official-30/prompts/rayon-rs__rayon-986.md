# rayon-rs__rayon-986

Repository: https://github.com/rayon-rs/rayon
Base commit: `2de810e97d5ce832ff98023a4a9cf215a86244ea`

Start from this exact base commit in a clean checkout. Fix the public issue below. Preserve existing APIs and unrelated behavior. Return a unified Git diff against the base commit. Do not consult solution PRs, later commits, reference patches, hidden evaluator tests, or another product's output.

## Issue #985: Bug in Drop for Drain<'data, T>

If you try:
```rust
use rayon::prelude::*;

fn main() {
    let mut vec_org = vec![0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

    let yielded = vec_org.par_drain(5..5).into_par_iter().collect::<Vec<_>>();

    println!("{:?}", vec_org);
}

```
it will print a little bit unexpected result:
```
[0, 1, 2, 3, 4]
```
