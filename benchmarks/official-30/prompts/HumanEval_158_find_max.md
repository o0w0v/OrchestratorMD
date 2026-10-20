# HumanEval_158_find_max

Implement the Rust function below. Preserve its signature and follow the documented behavior. Return the completed function as Rust code. Do not consult reference solutions or hidden evaluator tests.

```rust
/// Write a function that accepts a vector of strings.
/// The vector contains different words. Return the word with maximum number
/// of unique characters. If multiple strings have maximum number of unique
/// characters, return the one which comes first in lexicographical order.
/// >>> find_max(vec![String::from("name"), String::from("of"), String::from("string")])
/// String::from("string")
/// >>> find_max(vec![String::from("name"), String::from("enam"), String::from("game")])
/// String::from("enam")
/// >>> find_max(vec![String::from("aaaaaaa"), String::from("bb"), String::from("cc")])
/// String::from("aaaaaaa")
fn find_max(words: Vec<String>) -> String {
```
