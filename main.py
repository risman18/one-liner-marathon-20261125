#!/usr/bin/env python3
"""One-Liner Marathon entry: writes a single original joke to /output/entry.txt."""

import os

JOKE = "My sleep tracker gave me a score of 41, which is also the number of times I checked it last night."

# The punchline turns the score into the cause of the score: the tracker
# is measuring the anxiety it creates. Gate: a valid entry is 1-280 chars.
assert 1 <= len(JOKE) <= 280, "entry must be 1-280 characters"
assert "\n" not in JOKE, "entry must be a single line"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
