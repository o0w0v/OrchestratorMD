# sharkdp__bat-3189

Repository: https://github.com/sharkdp/bat
Base commit: `f8c6e90647221d8a5142bc50c7ea972562f6cdcd`

Start from this exact base commit in a clean checkout. Fix the public issue below. Preserve existing APIs and unrelated behavior. Return a unified Git diff against the base commit. Do not consult solution PRs, later commits, reference patches, hidden evaluator tests, or another product's output.

## Issue #3188: Default theme info is still printed on piped stdout

I believe this is the same issue reported in #3073 and apparently fixed in #3075.

Am I doing something wrong?

**What steps will reproduce the bug?**

Running `$ bat --no-config --list-themes | cat`

The `--no-config` part is optional, it's just to clear my settings for this run.

**What happens?**

This is the output:

```txt
1337
Coldark-Cold
Coldark-Dark
DarkNeon
Dracula
GitHub
Monokai Extended (default dark)
Monokai Extended Bright
Monokai Extended Light (default light)
Monokai Extended Origin
Nord
OneHalfDark
OneHalfLight
Solarized (dark)
Solarized (light)
Sublime Snazzy
TwoDark
Visual Studio Dark+
ansi
base16
base16-256
custom16
gruvbox-dark
gruvbox-light
zenburn
```

Monokai Extended and Extended Light include default theme annotations.

**What did you expect to happen instead?**

The same list / output but without `(default dark)` and `(default light)` information.

**How did you install `bat`?**

Via Cargo.

**Side note**

Probably unrelated but when I run `$ bat --list-themes --color=never` I get the same output but with `(default)` instead of `(default dark)`.

---

**bat version and environment**

#### Software version

bat 0.25.0

#### Operating system

- OS: Linux (Ubuntu 23.10)
- Kernel: 6.5.0-44-generic

#### Command-line

```bash
bat --diagnostic 
```

#### Environment variables

```bash
BAT_CACHE_PATH=<not set>
BAT_CONFIG_PATH=<not set>
BAT_OPTS=<not set>
BAT_PAGER='less -R'
BAT_PAGING=<not set>
BAT_STYLE=<not set>
BAT_TABS=<not set>
BAT_THEME=<not set>
COLORTERM=truecolor
LANG=en_US.UTF-8
LC_ALL=<not set>
LESS=<not set>
MANPAGER='sh -c '\''col -bx | bat -p --language=man --theme=custom16'\'''
NO_COLOR=<not set>
PAGER=less
SHELL=/usr/bin/zsh
TERM=xterm-256color
XDG_CACHE_HOME=<not set>
XDG_CONFIG_HOME=<not set>
```

#### System Config file

Could not read contents of '/etc/bat/config': No such file or directory (os error 2).

#### Config file

```
# This is `bat`s configuration file. Each line either contains a comment or
# a command-line option that you want to pass to `bat` by default. You can
# run `bat --help` to get a list of all possible configuration options.

--theme="Dracula"
--italic-text=always
--color=always
```

#### Custom assets metadata

```
bat_version: 0.25.0
creation_time:
  secs_since_epoch: 1736608946
  nanos_since_epoch: 486389724
```

#### Custom assets

- metadata.yaml, 97 bytes
- syntaxes.bin, 973899 bytes
- themes.bin, 41464 bytes

#### Compile time information

- Profile: release
- Target triple: x86_64-unknown-linux-gnu
- Family: unix
- OS: linux
- Architecture: x86_64
- Pointer width: 64
- Endian: little
- CPU features: fxsr,sse,sse2
- Host: x86_64-unknown-linux-gnu

#### Less version

```
> less --version 
less 590 (GNU regular expressions)
Copyright (C) 1984-2021  Mark Nudelman

less comes with NO WARRANTY, to the extent permitted by law.
For information about the terms of redistribution,
see the file named README in the less distribution.
Home page: https://greenwoodsoftware.com/less
```
