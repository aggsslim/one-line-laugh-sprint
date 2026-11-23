#!/usr/bin/env python3
"""One-Line Laugh Sprint entry.

Writes a single original funny line about everyday life to
$MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output if unset).
Deterministic: the same line, byte for byte, on every run.
Standard library only.
"""

import os

LINE = (
    "I bought noise-cancelling headphones so I could finally focus at work "
    "\u2014 now I can hear my own thoughts clearly, and it turns out "
    "they're the distraction."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
