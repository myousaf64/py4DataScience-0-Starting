"""Count character categories in a provided string."""

import string
import sys


def count_categories(text: str) -> None:
    """Print counts of character categories in the text."""
    # your tests and your error handling

    length = len(text)
    upper = sum(1 for ch in text if ch.isupper())
    lower = sum(1 for ch in text if ch.islower())
    punct = sum(1 for ch in text if ch in string.punctuation)
    spaces = sum(1 for ch in text if ch.isspace())
    digits = sum(1 for ch in text if ch.isdigit())

    print(f"The text contains {length} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main() -> None:
    """Handle arguments, prompt if missing, and count characters."""

    args = sys.argv[1:]
    try:
        if len(args) > 1:
            raise AssertionError("more than one argument is provided")
        if len(args) == 1:
            text = args[0]
        else:
            print("What is the text to count?")
            text = sys.stdin.read()
        count_categories(text)
    except AssertionError as exc:
        print(f"AssertionError: {exc}")


if __name__ == "__main__":
    main()
