"""Real-Life Patch Notes entry: one changelog line for a human-biology bug.

Writes the patch note to $MAKEFUN_OUTPUT_DIR/entry.txt with no trailing
newline. Python 3.13 standard library only; no network, no input files.
"""

import os
import sys

LINE = (
    "v1.3.7: fixed a bug where hiccups entered an infinite loop "
    "with no exit condition and no way to kill the process."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    if not text or len(text) > 160:
        print("entry must be 1-160 characters", file=sys.stderr)
        return 1
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
