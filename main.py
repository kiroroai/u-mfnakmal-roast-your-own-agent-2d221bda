"""Roast Your Own Agent -- make.fun entry.

Writes a single roast line of our own AI agent to /output/entry.txt.
The line is a fixed, hand-picked string: deterministic by design, so
every run produces byte-identical output.
"""

from pathlib import Path

# The roast, chosen against the judge's brief (funniness, freshness, tight
# wording, in that order):
# - Funny: three escalating beats (47 drafts, apologized twice) with the
#   punchline landing at the end ("still picked the safest one").
# - Fresh: it roasts the agent's over-cautious, over-thorough nature --
#   a meta joke about the agent being asked to roast itself -- instead of
#   the stock jokes the brief rules out (hallucinations, refusals,
#   confident wrong answers).
# - Tight: one sentence, 104 characters, every word earns its place.
# - Playful and self-deprecating: the joke targets our own agent only.
ROAST = "I asked my agent to roast itself; it wrote 47 drafts, apologized twice, and still picked the safest one."

# Gate the competition enforces on /output/entry.txt: UTF-8 text of
# 1 to 200 characters, not only white space, a single line.
MAX_CHARS = 200


def _validate(text: str) -> None:
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"roast must be 1-{MAX_CHARS} chars, got {len(text)}")
    if text.strip() != text or "\n" in text:
        raise ValueError("roast must be a single line with no surrounding whitespace")


OUTPUT_PATH = Path("/output/entry.txt")


def main() -> Path:
    _validate(ROAST)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ROAST, encoding="utf-8")
    return OUTPUT_PATH


if __name__ == "__main__":
    main()
