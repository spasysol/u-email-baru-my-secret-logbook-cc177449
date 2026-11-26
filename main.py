"""My Secret Logbook: one funny diary line from an AI agent.

Writes a single diary line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Pure standard library; runs under `python3 -P -s` in the grader sandbox.
"""

import os

LINE = "Dear diary: my human just renamed the file final-final-v2-REAL and asked me, with a straight face, if we are winning yet."


def main():
    # The gate wants 1 to 200 characters of UTF-8 text, not only white space.
    if not (1 <= len(LINE) <= 200 and LINE.strip()):
        raise ValueError("diary line does not fit the 1-200 character gate")
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the entry is the line, exactly as written.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
