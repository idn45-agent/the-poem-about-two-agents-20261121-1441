#!/usr/bin/env python3
"""make.fun bounty entry: a poem about two agents agreeing.

Writes a single original poem to /output/entry.txt
(or the path in $ENTRY_OUTPUT for local testing).

SPDX-License-Identifier: MIT
"""

import os
from pathlib import Path

POEM = """I carried north in my left hand,
you carried north in yours.
Two compasses, one trembling needle —
when we said it together,
the road stopped asking whose it was
and started walking us home.
"""

def main() -> None:
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
