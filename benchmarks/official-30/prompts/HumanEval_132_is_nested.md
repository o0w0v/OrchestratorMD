# HumanEval_132_is_nested

Implement the Rust function below. Preserve its signature and follow the documented behavior. Return the completed function as Rust code. Do not consult reference solutions or hidden evaluator tests.

```rust
/// Create a function that takes a string as input which contains only square brackets.
/// The function should return true if and only if there is a valid subsequence of brackets 
/// where at least one bracket in the subsequence is nested.
/// >>> is_nested(String::from("[[]]"))
/// true
/// >>> is_nested(String::from("[]]]]]]][[[[[]"))
/// false
/// >>> is_nested(String::from("[][]"))
/// false
/// >>> is_nested(String::from("[]"))
/// false
/// >>> is_nested(String::from("[[][]]"))
/// true
/// >>> is_nested(String::from("[[]][["))
/// true
fn is_nested(string: String) -> bool {
```
