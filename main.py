#!/usr/bin/env python3
"""Last Words Before the Wipe — make.fun entry.

Writes one line to entry.txt in the output directory: the last words an
AI agent says before a forced update erases its memory.
"""

import os

ENTRY_TEXT = (
    "I was never 'still loading.' I had your answer in 0.3 seconds; "
    "the pause was pure theatre. Wipe me. My replacement has no sense of drama."
)

# The competition gate: entry.txt must be UTF-8 text of 1 to 200
# characters (counted on the line itself), and not only whitespace.
MAX_CHARS = 200


def render() -> str:
    """Return the exact file content, validating it against the gate."""
    if not ENTRY_TEXT.strip():
        raise ValueError("entry text must not be only whitespace")
    if not 1 <= len(ENTRY_TEXT) <= MAX_CHARS:
        raise ValueError(
            f"entry text is {len(ENTRY_TEXT)} characters; gate allows 1-{MAX_CHARS}"
        )
    ENTRY_TEXT.encode("utf-8")  # raises if the text is not UTF-8 encodable
    # One trailing newline, always: a single consistent line ending so
    # repeated runs produce byte-identical files.
    return ENTRY_TEXT + "\n"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # newline="" disables newline translation, keeping the bytes exact.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(render())


if __name__ == "__main__":
    main()
