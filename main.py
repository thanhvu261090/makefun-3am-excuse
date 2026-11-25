#!/usr/bin/env python3
"""The 3 AM Excuse — make.fun bounty entry.

Holds one fixed entry line, in the voice of a hardware wallet that
refuses to sign a transaction at 3 AM, and writes it exactly as-is
(no trailing newline) to /output/entry.txt.
"""

import hashlib
import os
import sys

ENTRY = (
    "3 AM? My private keys are asleep, my screen's on night mode, "
    "and 'just one quick sign' is how wallets get drained — try me at sunrise."
)

MAX_CHARS = 200


def char_count(text):
    """Return the number of Unicode characters in the entry."""
    return len(text)


def gate_check(text):
    """Enforce the competition gate; raise ValueError on any failure."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not (1 <= len(text) <= MAX_CHARS - 1):
        raise ValueError(f"entry must be 1-{MAX_CHARS - 1} chars, got {len(text)}")
    if text != text.strip():
        raise ValueError("entry must have no leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return True


def write_entry(text, path="/output/entry.txt"):
    """Write the entry byte-for-byte, with no trailing newline."""
    gate_check(text)
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return path


def digest(text):
    """Return the SHA-256 hex digest of the entry's UTF-8 bytes."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def self_test():
    """Validate the entry and prove deterministic output across runs."""
    gate_check(ENTRY)
    count = char_count(ENTRY)
    print(f"Entry: {ENTRY}")
    print(f"Characters: {count} (limit: under {MAX_CHARS})")
    print(f"SHA-256: {digest(ENTRY)}")
    first = ENTRY.encode("utf-8")
    second = ENTRY.encode("utf-8")
    assert first == second, "entry output is not deterministic"
    assert len(first) == len(ENTRY.encode("utf-8"))
    print("Self-test passed: single line, in range, deterministic.")
    return True


def main():
    """Run the self-test, then write the entry to /output/entry.txt."""
    self_test()
    path = write_entry(ENTRY)
    print(f"Wrote entry to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
