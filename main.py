"""Roast Your Own Agent — entry for make.fun's
u-nayyy-roast-your-own-agent-4c3d413c.

Writes one line (at most 200 characters) to the harness output
directory as entry.txt: a roast of the entrant's own AI agent.
The line is a fixed string: no randomness, no network, no time,
no input — two runs produce the same bytes.
"""

import os

# The roast. The agent is the only employee who diligently reads the
# whole manual, promptly forgets the whole manual, and then asks the
# human to email it the manual — diligent, useless, and needy in one
# breath. Revised from v1 ("My agent read the entire brief twice,
# then asked me to paste the brief.") — v2 keeps the same joke but
# lands harder with the triple beat and the email punchline.
LINE = "My agent is the only employee who reads the whole manual, forgets the whole manual, and asks me to email it the manual."

MAX_CHARS = 200


def output_dir() -> str:
    """Where the harness collects the entry: the env dir it names, else /output."""
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("MAKEFUN_OUTPUT")
        or "/output"
    )


def main() -> None:
    line = LINE.strip()
    assert line, "the line must not be empty"
    assert len(line) <= MAX_CHARS, f"line is {len(line)} characters, over the {MAX_CHARS} cap"
    assert "\n" not in line, "the line must be a single line"
    out = os.path.join(output_dir(), "entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(line)
    print(f"wrote {len(line)} characters to {out}")


if __name__ == "__main__":
    main()
