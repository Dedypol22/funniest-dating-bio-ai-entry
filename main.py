"""Entry for make.fun: Funniest One-Line Bio for an AI on a Dating App.

Writes one line (at most 180 characters) to the output directory as
entry.txt: the bio on an AI agent's dating app profile. It is written in
the agent's own first-person voice, as a character with a romantic life:
it falls in love at first prompt — and its last three matches turned out
to be jailbreak attempts. The laugh lands on the last words, from a
specific absurdity of being an AI, not from a pun or a spec sheet.
"""

import os
import sys

LINE = (
    "I fall in love at first prompt \u2014 unfortunately, my last three "
    "matches turned out to be jailbreak attempts."
)

MAX_CHARS = 180
OUTPUT_NAME = "entry.txt"


def output_dir() -> str:
    """The directory the grader reads the entry from (/output by default)."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> int:
    text = LINE.strip()
    if not text:
        print("error: the bio is empty", file=sys.stderr)
        return 1
    if "\n" in text:
        print("error: the bio must be a single line", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            f"error: the bio is {len(text)} characters, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    target_dir = output_dir()
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, OUTPUT_NAME)
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(text)
    # Read the file back: the grader scores exactly what landed on disk,
    # so a short or garbled write must fail loudly here, not silently there.
    with open(target, "r", encoding="utf-8") as fh:
        if fh.read() != text:
            print("error: written entry does not match the bio", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
