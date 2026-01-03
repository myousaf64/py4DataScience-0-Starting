#!.venv/bin/python

"""Format current epoch time and date."""

from datetime import datetime
import time


def main() -> None:
    now = time.time()
    print(
        f"Seconds since January 1, 1970: {now:,.4f} or {now:.2e} in scientific notation"
    )
    print(datetime.fromtimestamp(now).strftime("%b %d %Y"))


if __name__ == "__main__":
    main()
