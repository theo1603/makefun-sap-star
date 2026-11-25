#!/usr/bin/env python3
"""One Star, Written in Sap.

Writes a single one-line 1-star review, in the voice of a houseplant
reviewing the human who owns it, to /output/entry.txt.

Deterministic: the same review text is written on every run.
Standard library only; no network, no environment secrets.
"""

import os

REVIEW = (
    "One star. He spins me a quarter-turn every Sunday 'for even growth', "
    "like I'm a rotisserie chicken, then acts betrayed when I lean toward "
    "the window instead of him. I am a fern, not a kebab."
)


def main() -> None:
    text = REVIEW.strip()
    if not 1 <= len(text) <= 279:
        raise ValueError(f"review must be 1-279 chars, got {len(text)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
