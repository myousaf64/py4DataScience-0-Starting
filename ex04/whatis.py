"""Check whether an argument is odd or even."""

import sys


def describe_number(value: str) -> None:
    """Print whether the given string represents an odd or even integer."""

    if value.strip().lstrip("-+").isdigit() is False:
        raise AssertionError("argument is not an integer")
    number = int(value)
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


def main() -> None:
    """Validate CLI arguments and report parity."""

    args = sys.argv[1:]
    try:
        if len(args) == 0:
            return
        if len(args) > 1:
            raise AssertionError("more than one argument is provided")
        describe_number(args[0])
    except AssertionError as exc:
        print(f"AssertionError: {exc}")


if __name__ == "__main__":
    main()
