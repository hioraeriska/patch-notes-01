"""Real-Life Patch Notes entry: one changelog line for a human-biology bug.

Writes the patch note to $MAKEFUN_OUTPUT_DIR/entry.txt with no trailing
newline. Python 3.13 standard library only; no network, no input files.
"""

import os
import sys

PATCH_LINE = (
    "v1.3.7: fixed a bug where hiccups entered an infinite loop "
    "with no exit condition and no way to kill the process."
)

MAX_CHARS = 160


def validate_line(line: str) -> str:
    """Return the line if it is a single line within the char limit."""
    text = line.strip()
    if not text:
        raise ValueError("entry must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if len(text) > MAX_CHARS:
        raise ValueError("entry must be 1-160 characters")
    return text


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    try:
        text = validate_line(PATCH_LINE)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
