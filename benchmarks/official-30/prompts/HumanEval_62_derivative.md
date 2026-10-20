# HumanEval_62_derivative

Implement the Rust function below. Preserve its signature and follow the documented behavior. Return the completed function as Rust code. Do not consult reference solutions or hidden evaluator tests.

```rust
/// xs represent coefficients of a polynomial.
/// xs[0] + xs[1] * x + xs[2] * x^2 + ....
/// Return derivative of this polynomial in the same form.
/// >>> derivative(vec![3, 1, 2, 4, 5])
/// vec![1, 4, 12, 20]
/// >>> derivative(vec![1, 2, 3])
/// vec![2, 6]
fn derivative(xs: Vec<isize>) -> Vec<isize> {
```
