# BurntSushi__ripgrep-2626

Repository: https://github.com/BurntSushi/ripgrep
Base commit: `7099e174acbcbd940f57e4ab4913fee4040c826e`

Start from this exact base commit in a clean checkout. Fix the public issue below. Preserve existing APIs and unrelated behavior. Return a unified Git diff against the base commit. Do not consult solution PRs, later commits, reference patches, hidden evaluator tests, or another product's output.

## Issue #1966: `rg --unknown-switch` panics on broken pipe error

#### What version of ripgrep are you using?

```console
$ ./target/debug/rg --version
ripgrep 13.0.0 (rev 9b01a8f9ae)
-SIMD -AVX (compiled)
+SIMD +AVX (runtime)
```

#### How did you install ripgrep?

Compiled from source.

```console
$ git rev-parse HEAD
9b01a8f9ae53ebcd05c27ec21843758c2c1e823f
```

#### What operating system are you using ripgrep on?

macOS Big Sur 11.5.1 (20G80)

#### Describe your bug.

ripgrep panics when printing a clap error to stderr if stderr is closed.

#### What are the steps to reproduce the behavior?

Apply this diff to ripgrep:

```diff
diff --git a/crates/core/main.rs b/crates/core/main.rs
index 47385de..f3d9889 100644
--- a/crates/core/main.rs
+++ b/crates/core/main.rs
@@ -46,10 +46,14 @@ static ALLOC: jemallocator::Jemalloc = jemallocator::Jemalloc;
 type Result<T> = ::std::result::Result<T, Box<dyn error::Error>>;

 fn main() {
-    if let Err(err) = Args::parse().and_then(try_main) {
-        eprintln!("{}", err);
-        process::exit(2);
-    }
+    let f = std::panic::catch_unwind(std::panic::AssertUnwindSafe(|| {
+        if let Err(err) = Args::parse().and_then(try_main) {
+            eprintln!("{}", err);
+            process::exit(2);
+        }
+    }));
+    println!("panicked? - {}", f.is_err());
+    process::exit(1);
 }

 fn try_main(args: Args) -> Result<()> {
```

Then:

```console
$ cargo build
$ ./target/debug/rg --unknown-switch 3>&1 1>&2 2>&3 | head -c 0 # swap stdout and stderr, close stdout
head: illegal byte count -- 0
panicked? - true
$ echo $?
1
```

I'm not sure how I could observe this panic without the patch since rust writes the panic to stderr. Maybe if ripgrep is compiled with `panic = abort`?

#### What is the actual behavior?

ripgrep panics if stderr is closed despite going to great lengths to avoid panicking when writing to stdout.

#### What is the expected behavior?

ripgrep does not panic.

