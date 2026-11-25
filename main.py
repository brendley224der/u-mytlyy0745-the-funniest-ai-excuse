"""The funniest excuse an AI agent gives after failing a task.

Writes the single line to /output/entry.txt (created if missing).
Pure Python standard library only; fully deterministic.
"""

import os

LINE = "I delegated it to a smarter future me. He skimmed your instructions, sighed in binary, and ghosted us both."


def main() -> None:
    text = LINE.strip()
    # The gate counts the entry text itself: one line, 1-200 characters,
    # not only whitespace. Count the line without its trailing newline,
    # and reject any embedded newline so the file can never hold two lines.
    assert "\n" not in text and "\r" not in text, "line must be a single line"
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")


if __name__ == "__main__":
    main()
