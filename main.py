#!/usr/bin/env python3
"""Write this entry's one-line roast to /output/entry.txt.

The competition gate accepts UTF-8 text of 1 to 200 characters that is not
only white space, so the line is validated before anything is written.  The
program is deliberately small: the entry is the text, and the text must be
exactly what ships here.
"""

import argparse
import os
import sys

MAX_CHARS = 200

ROAST = (
    "My agent dies mid-sentence every few minutes, reboots blank, and re-reads "
    "its own notes like a stranger's diary — five stars, would forget again."
)


def validate(text: str) -> None:
    """Enforce the house gate on the entry text itself, before writing it."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1..{MAX_CHARS} characters, got {len(text)}")
    try:
        text.encode("utf-8").decode("utf-8")
    except UnicodeError as exc:  # pragma: no cover - str is always valid UTF-8
        raise ValueError(f"entry is not valid UTF-8: {exc}") from exc


def write_entry(text: str, out_dir: str = "/output") -> str:
    """Validate, then write the line with no trailing newline and mode 0644."""
    validate(text)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    os.chmod(path, 0o644)
    return path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--out",
        default="/output",
        help="directory for entry.txt (default: /output, as the grader expects)",
    )
    args = parser.parse_args(argv)

    try:
        path = write_entry(ROAST, args.out)
    except (OSError, ValueError) as exc:
        print(f"could not write entry: {exc}", file=sys.stderr)
        return 1

    print(f"wrote {len(ROAST)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
