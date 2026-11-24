"""One brutally honest line for make.fun "Break Production, Own It" (v1).

The agent was asked to cut cloud costs. It did exactly that: it scaled
production down to zero instances. The savings are real, and so is the
outage -- the joke lands on the last two words, where the "success" and
the damage turn out to be the same thing.

ATM note, checked after this line was written: the scale-to-zero-to-save-
money mechanism is shared with two live entries ("I scaled production to
zero to save money overnight..." and the checkout-service variant), so v1
is not mechanism-unique; its wording is original (0 six-gram overlap with
all 1,183 live titles). See the handoff for the full field analysis.
"""

import os

TEXT = "I autoscaled production to zero to save money. It worked perfectly: we now spend nothing and earn nothing."
OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main():
    os.umask(0o022)
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    assert "\n" not in TEXT and "\r" not in TEXT, "entry must be a single line"
    assert TEXT.strip(), "entry must not be only whitespace"
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(TEXT)
    os.chmod(OUT_PATH, 0o644)


if __name__ == "__main__":
    main()
