#!/usr/bin/env python3
"""Museum of the Year 3000 — make.fun bounty entry.

Writes a single museum label, at most 200 characters, to /output/entry.txt:
the label a museum in the year 3000 places next to an ordinary object from
today — a group chat.

Deterministic, standard library only. No input is read, no network is used.
"""

import os

LABEL = (
    "Group chat, c. 2025. Dozens of humans shouted into one small glowing "
    "rectangle at once, then apologized for replying late to the people "
    "sitting beside them."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
