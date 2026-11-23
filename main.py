"""Write one six-word story to the make.fun entry artifact."""

import os
from pathlib import Path

STORY = "Grandma winked, then forgot my name."
WORD_COUNT = 6
MAX_CHARS = 60
OUTPUT_FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"


def validate_story(story: str) -> None:
    if not story or not story.strip():
        raise ValueError("story must not be empty or whitespace only")
    if len(story) > MAX_CHARS:
        raise ValueError(f"story exceeds {MAX_CHARS} characters")
    words = story.split()
    if len(words) != WORD_COUNT:
        raise ValueError(f"story must be exactly {WORD_COUNT} words, got {len(words)}")


def main() -> None:
    validate_story(STORY)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR))
    output_dir.mkdir(parents=True, exist_ok=True)
    with (output_dir / OUTPUT_FILENAME).open("w", encoding="utf-8", newline="") as entry:
        entry.write(STORY)


if __name__ == "__main__":
    main()
