"""Houseplant out-of-office auto-reply.

One line of text, written by a neglected fern, goes to /output/entry.txt.
Single line, 1-120 characters, no trailing newline, no BOM.
Stdlib only. Deterministic: the same output on every run.
"""
import os

ENTRY = "This fern hasn't had water since March. Your email joins the queue behind the dust. Water would help."

OUTPUT_PATH = "/output/entry.txt"

# The sealed gate (RULES.txt): the raw file must be UTF-8 text of 1 to 120
# characters, not only white space, and a single line.
MAX_CHARS = 120


def check_gate(text):
    """True when text passes the sealed gate, False otherwise.

    Control characters (C0, except tab) are rejected too: they would
    smuggle invisible bytes into the entry without adding a laugh.
    """
    if not isinstance(text, str):
        return False
    if len(text) < 1 or len(text) > MAX_CHARS:
        return False
    if text.strip() == "":
        return False
    if "\n" in text or "\r" in text:
        return False
    for ch in text:
        if ord(ch) < 32 and ch != "\t":
            return False
    return True


def main():
    if not check_gate(ENTRY):
        raise SystemExit(
            "ENTRY invalid: must be 1-120 characters, one line, "
            "not whitespace-only"
        )
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
