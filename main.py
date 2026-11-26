#!/usr/bin/env python3
"""Write this entry's one-line roast to /output/entry.txt."""

import os

LINE = (
    "My agent dies mid-sentence every few minutes, reboots blank, and re-reads "
    "its own notes like a stranger's diary — five stars, would forget again."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    os.chmod(out_dir, 0o755)

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
