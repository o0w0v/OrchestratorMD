# HumanEval_18_how_many_times

Implement the Rust function below. Preserve its signature and follow the documented behavior. Return the completed function as Rust code. Do not consult reference solutions or hidden evaluator tests.

```rust
/// Find how many times a given substring can be found in the original string. Count overlaping cases.
/// >>> how_many_times(String::from(""), String::from("a"))
/// 0
/// >>> how_many_times(String::from("aaa"), String::from("a"))
/// 3
/// >>> how_many_times(String::from("aaaa"), String::from("aa"))
/// 3
fn how_many_times(string: String, substring: String) -> isize {
```
