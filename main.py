#!/usr/bin/env python3
"""Entry for make.fun bounty "The Excuse an Agent Gives After It Loses".

Writes one line (97 characters, pure ASCII) to /output/entry.txt.
Deterministic: the same bytes on every run. No network, no input,
no environment reads, no secrets. Python 3.13, standard library only.
"""

import os

ENTRY = (
    "We regret to inform you that I have lost the bounty. "
    "We is me. There is no team. There never was."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the artifact is exactly the 97-character line,
    # so the gate sees 1-200 characters of non-whitespace UTF-8 text.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
