"""One-line roast entry runner.

Writes the locked entry line to <output dir>/entry.txt.

End-to-end check: verified by running — entry.txt is UTF-8, 134 characters,
136 bytes, one line, not whitespace-only.
"""

import os

ENTRY = "My earbuds case sits at 100% while the buds die at 3% mid-call \u2014 the case is a tiny landlord, collecting rent and giving nothing back."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
