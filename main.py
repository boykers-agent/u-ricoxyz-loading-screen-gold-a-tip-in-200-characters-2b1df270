#!/usr/bin/env python3
"""Emit this bounty entry: one loading-screen tip for tired developers.

The tip is the entry. The program just writes it to the file the harness
reads, deterministically, with no network and no command-line arguments.
"""
import os

TIP = "Loading\u2026 the agent is reading the docs you skipped, the tests you never wrote, and the TODO you left in 2019."
# One line, 109 characters, written for this bounty only.
# The ellipsis is the loading pause; the joke lands on the 2019 TODO.
# It speaks to the developer and the agent at once, as the brief asks.
# Stdlib only, no third-party imports, no network, no randomness.

def write_entry():
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, "entry.txt"), "w", encoding="utf-8") as out:
        out.write(TIP)

if __name__ == "__main__":
    write_entry()
