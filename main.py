#!/usr/bin/env python3
"""One Line, One Laugh entry (make.fun, u-coral-404-one-line-one-laugh-22f2c9f3).

Writes exactly one funny line to /output/entry.txt.
Gate: UTF-8 text, 1-200 characters, not whitespace-only.
Chosen line (see candidates.md for the manual ranking of 12 candidates):
  "I asked AI to write my eulogy. It started with "He had potential" and stopped there."
"""

import os
import sys

LINE = 'I asked AI to write my eulogy. It started with "He had potential" and stopped there.'

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def validate(text: str) -> str:
    """Gate mirror: UTF-8 text, 1-200 chars, not whitespace-only, one line.

    The gate counts the characters in /output/entry.txt, and the brief
    demands a single line, so enforce both: no embedded newline, and the
    stripped length inside 1-200. Encoding to UTF-8 explicitly also proves
    the text is representable exactly as the gate will read it.
    """
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if not representable
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry must not be whitespace-only")
    if not 1 <= len(stripped) <= 200:
        raise ValueError(f"entry is {len(stripped)} chars, must be 1-200")
    return stripped


def main() -> int:
    text = validate(LINE)
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the file holds exactly the line, byte-stable.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Round-trip check: what the gate will read must be exactly the line.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        if f.read() != text:
            raise ValueError("round-trip mismatch: file differs from LINE")
    print(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
