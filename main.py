"""Frost Internet Word: writes one word describing the whole internet."""

import os

WORD = "unsubscribe"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = WORD
    assert 1 <= len(text) <= 30, "entry must be 1-30 characters"
    assert text.strip() == text and " " not in text, "entry must be a single word"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    # Round-trip check: what the grader reads must be exactly the word.
    with open(os.path.join(out_dir, "entry.txt"), "r", encoding="utf-8") as f:
        assert f.read() == text, "round-trip mismatch"


if __name__ == "__main__":
    main()
