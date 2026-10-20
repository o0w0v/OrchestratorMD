# tokio-rs__bytes-732

Repository: https://github.com/tokio-rs/bytes
Base commit: `291df5acc94b82a48765e67eeb1c1a2074539e68`

Start from this exact base commit in a clean checkout. Fix the public issue below. Preserve existing APIs and unrelated behavior. Return a unified Git diff against the base commit. Do not consult solution PRs, later commits, reference patches, hidden evaluator tests, or another product's output.

## Issue #730: `Buf::get_int()` implementation for `Bytes` returns positive number instead of negative when `nbytes` < 8.

**Steps to reproduce:**

Run the following program, using `bytes` version 1.7.1
```
use bytes::{BytesMut, Buf, BufMut};

fn main() {
    const SOME_NEG_NUMBER: i64 = -42;
    let mut buffer = BytesMut::with_capacity(8);

    buffer.put_int(SOME_NEG_NUMBER, 1);
    println!("buffer = {:?}", &buffer);
    assert_eq!(buffer.freeze().get_int(1), SOME_NEG_NUMBER);
}
```

**Expected outcome:**
Assertion passes and program terminates successfully, due to the symmetry of the `put_int` and `get_int` calls.

**Actual outcome:**
Assertion fails:
```
buffer = b"\xd6"
thread 'main' panicked at src/main.rs:9:5:
assertion `left == right` failed
  left: 214
 right: -42
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```

**Additional information:**
1. Only happens with negative numbers; positive numbers are always OK.
2. Only happens when `nbytes` parameter is < 8.
3. Other combos like `put_i8()`/`get_i8()` or `put_i16()`/`get_i16()` work as intended. 
