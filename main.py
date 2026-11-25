#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader entry.

Writes one fortune cookie line to /output/entry.txt (UTF-8, 1-160
characters, exactly one line, at most 20 words). Deterministic,
standard library only, no network, no environment reads.

The line (15 words, 78 characters): "Your lucky numbers are 0, 0,
and the leverage you swore you'd never use again." The setup is the
most familiar fortune cookie trope of all, the lucky numbers; the
turn is that the trader's lucky numbers are zeroes, because the
wallet is empty, and the third "number" is not a number at all but
the leverage he swore he would never touch again. The joke lands on
the loss and on the trader's own broken promise, rueful and warm
rather than cruel: he is laughing at himself, at 3am, with the
cookie. A small, oracular opening that the punchline then breaks.
"""

import os

FORTUNE = (
    "Your lucky numbers are 0, 0, and the leverage "
    "you swore you'd never use again."
)


def entry_text() -> str:
    """Return the fortune, checked against the gate.

    The gate requires 1-160 characters of UTF-8 text, not only
    whitespace, on exactly one line, and the task caps the line at
    20 words of plain text.
    """
    text = FORTUNE
    assert 1 <= len(text) <= 160, "entry must be 1-160 characters"
    assert text.strip() == text, "entry must not start or end with whitespace"
    assert "\n" not in text, "entry must be exactly one line"
    assert len(text.split()) <= 20, "entry must be at most 20 words"
    return text


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(entry_text())


if __name__ == "__main__":
    main()
