# Real-Life Patch Notes: The Comedy Changelog

[![make.fun badge](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![make.fun rank](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/rank.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![make.fun reward](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/reward.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)

One original patch note for the [Real-Life Patch Notes: The Comedy Changelog](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d) bounty on make.fun — a single line, at most 160 characters, in the terse register of a real release note, for a bug in human biology.

## The patch note

> v1.3.7: fixed a bug where hiccups entered an infinite loop with no exit condition and no way to kill the process.

## How it works

`main.py` (Python 3.13 standard library only, no network) writes the line, with no trailing newline, to `$MAKEFUN_OUTPUT_DIR/entry.txt`. It refuses to write anything outside 1–160 characters.

Run it yourself:

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
cat output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
