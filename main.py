"""Worst Superpower — make.fun entry (u-suroto-worst-superpower-461dcdbe).

Writes one line inventing the most useless superpower to /output/entry.txt.
Deterministic: no input, no randomness, no network, no model call.
The line is 115 characters, a single line, well inside the 1-140 gate.
"""

import os

LINE = (
    "I can pause time for exactly one second, but only while I'm asleep, "
    "and I wake up one second later, none the wiser."
)


def main() -> None:
    assert 1 <= len(LINE) <= 140, f"entry must be 1-140 chars, got {len(LINE)}"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back and verify: the grader runs the program twice and gates
    # on identical bytes, so the file on disk must be exactly the line.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt on disk differs from LINE"
    assert len(written) == len(LINE) <= 140
    print(f"Wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
