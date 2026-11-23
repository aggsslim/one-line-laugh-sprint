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
    if not LINE.strip():
        raise ValueError("entry line must not be blank or only whitespace")
    if not 1 <= len(LINE) <= 200:
        raise ValueError(
            f"entry line must be 1-200 characters, got {len(LINE)}"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Deterministic output: strip any accidental trailing whitespace and
    # write exactly one line with no trailing newline, byte for byte.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE.rstrip())


if __name__ == "__main__":
    main()
