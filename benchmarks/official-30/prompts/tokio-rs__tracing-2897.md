# tokio-rs__tracing-2897

Repository: https://github.com/tokio-rs/tracing
Base commit: `908cc432a5994f6e17c8f36e13c217dc40085704`

Start from this exact base commit in a clean checkout. Fix the public issue below. Preserve existing APIs and unrelated behavior. Return a unified Git diff against the base commit. Do not consult solution PRs, later commits, reference patches, hidden evaluator tests, or another product's output.

## Issue #2857: `tracing::instrument(ret)` errors on function with `&mut` args returning `&`/`&mut`

## Bug Report

### Version

```
tracing v0.1.40
tracing-attributes v0.1.27 (proc-macro)
tracing-core v0.1.32
```

### Description

When using `instrument(ret)` (or `instrument(err)`), the closure in the generated code is inferred to be `Fn` or `FnMut`, which causes compile errors when trying to return a reference to an argument.

```rust
// error: lifetime may not live long enough
// note: closure implements `Fn`, so references to captured variables can't escape the closure
#[tracing::instrument(ret)]
fn foo(x: &mut ()) -> &() {
    x
}

// error: captured variable cannot escape `FnMut` closure body
#[tracing::instrument(ret)]
fn foo(x: &mut ()) -> &mut () {
    x
}
```

### Possible Solution

Force the generated closure to be `FnOnce`, either via a function:

```rust
fn force_fn_once<T, F: FnOnce() -> T>(f: F) -> F {
    f
}

force_fn_once(move || {
    // ...
})
```

Or by rebinding a captured variable

```rust
let outer = &mut ();
move || {
    { let inner = outer; }
    // ...
}
```
