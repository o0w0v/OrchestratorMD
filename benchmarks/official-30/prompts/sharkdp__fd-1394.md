# sharkdp__fd-1394

Repository: https://github.com/sharkdp/fd
Base commit: `93cdb2628e89dd5831eee22b8df697aea00eca3b`

Start from this exact base commit in a clean checkout. Fix the public issue below. Preserve existing APIs and unrelated behavior. Return a unified Git diff against the base commit. Do not consult solution PRs, later commits, reference patches, hidden evaluator tests, or another product's output.

## Issue #1393: [BUG] unintended behavior when using "-1"

### Checks

- [X] I have read the troubleshooting section and still think this is a bug.

### Describe the bug you encountered:

Thanks for fd, it comes in handy!

Attempts to use the shorthand `-1` alias instead of `--max-results` with exec or batch exec are not prevented, and the operations will be performed on every object which matches the query instead of the first hit. Depending on what one was trying to achieve the impact of this can be quite significant.


The alias does not have the relevant `conflicts_with`

https://github.com/sharkdp/fd/blob/93cdb2628e89dd5831eee22b8df697aea00eca3b/src/cli.rs#L513-L522


Using long option `--max-results=1` would yield immediate abort and explanation that options conflict:

https://github.com/sharkdp/fd/blob/93cdb2628e89dd5831eee22b8df697aea00eca3b/src/cli.rs#L20-L30


Finally `-1` overrides_with `--max-results`, but not the other way around so `fd --max-results=1 -1 -X prog query` will launch prog against all objects matching query.

### Describe what you expected to happen:

Consistent behavior: if mixing `max-results` with exec-type functions is refused, same should be true for aliases.

### What version of `fd` are you using?

8.7.0

### Which operating system / distribution are you on?

```shell
Linux
```

