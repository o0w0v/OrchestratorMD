# HumanEval_67_fruit_distribution

Implement the Rust function below. Preserve its signature and follow the documented behavior. Return the completed function as Rust code. Do not consult reference solutions or hidden evaluator tests.

```rust
/// In this task, you will be given a string that represents a number of apples and oranges 
/// that are distributed in a basket of fruit this basket contains 
/// apples, oranges, and mango fruits. Given the string that represents the total number of 
/// the oranges and apples and an integer that represent the total number of the fruits 
/// in the basket return the number of the mango fruits in the basket.
/// for examble:
/// >>> fruit_distribution(String::from("5 apples and 6 oranges"), 19)
/// 8
/// >>> fruit_distribution(String::from("0 apples and 1 oranges"), 3)
/// 2
/// >>> fruit_distribution(String::from("2 apples and 3 oranges"), 100)
/// 95
/// >>> fruit_distribution(String::from("100 apples and 1 oranges"), 120)
/// 19
fn fruit_distribution(s: String, n: isize) -> isize {
```
