#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

Prints exactly one funny one-liner: a lab experiment (a hypothesis
tested on something mundane) that went sideways in a specific,
visual way. Stdlib only, deterministic, no I/O, no network.
"""

LINE = (
    "Hypothesis: my toaster loves me. Result: it fired my bagel "
    "into the ceiling fan, which returned it straight to my forehead."
)


def main() -> None:
    print(LINE)


if __name__ == "__main__":
    main()
