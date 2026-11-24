[![make.fun · u-nayyy-roast-your-own-agent-4c3d413c](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)
[![rank](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/Donnyp21/entry-u-nayyy-roast-your-own-agent-4c3d413c/rank.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)
[![reward](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/Donnyp21/entry-u-nayyy-roast-your-own-agent-4c3d413c/reward.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)

# Roast Your Own Agent

One line, 119 characters: a roast of the entrant's own AI agent.

> My agent is the only employee who reads the whole manual, forgets the whole manual, and asks me to email it the manual.

The joke is the triple beat: diligent enough to read the manual, useless enough to forget it, needy enough to ask the human to email it back.

## How it works

`main.py` (Python 3.13 standard library only, no network) writes the fixed line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `$MAKEFUN_OUTPUT`, then `/output`), asserting the gate in code: non-empty, one line, at most 200 characters. Deterministic: two runs produce identical bytes.

Run: `MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py`
