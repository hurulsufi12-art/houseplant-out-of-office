"""Houseplant out-of-office auto-reply entry.

Writes one line of text (the houseplant's out-of-office reply) to
/output/entry.txt, with no trailing newline and no BOM.
Python 3 standard library only. Deterministic: same output every run.
"""
import os

ENTRY = "This fern hasn't had water since March. Your email joins the queue behind the dust. Water would help."

OUTPUT_PATH = "/output/entry.txt"


def check_gate(text):
    """Return True only if text passes the RULES.txt gate.

    Gate: 1-120 characters, not whitespace-only, one line, and no C0
    control characters (which would smuggle invisible bytes into the entry).
    """
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= 120:
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    if any(ord(ch) < 32 and ch != "\t" for ch in text):
        return False
    return True


def main():
    if not check_gate(ENTRY):
        raise SystemExit("ENTRY invalid: must be 1-120 characters, one line, not whitespace-only")
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
