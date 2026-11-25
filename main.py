"""Write the one-line meeting joke to /output/entry.txt."""

import os
from pathlib import Path


ENTRY = (
    "Everyone had already read the email; "
    "we met to pretend we hadn't."
)


def main() -> None:
    """Write ENTRY verbatim, with no trailing newline."""
    output_path = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(ENTRY.encode("utf-8"))


if __name__ == "__main__":
    main()
