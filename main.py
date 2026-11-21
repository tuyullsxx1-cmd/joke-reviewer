"""Write one one-line joke about working beside an AI coding agent."""

import os

JOKE = "I asked my agent to make the query faster. It cached the error. Now it fails instantly."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
# The joke is a fixed string: the same bytes on every run, no randomness.


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
