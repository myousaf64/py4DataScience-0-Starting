"""Identify and print null-like objects."""

import math


def NULL_not_found(obj: any) -> int:
    """Print object type for null-like values; return 0 on match else 1."""

    if obj is None:
        print(f"Nothing: {obj} {type(obj)}")
        return 0
    if isinstance(obj, float) and math.isnan(obj):
        print(f"Cheese: nan {type(obj)}")
        return 0
    if obj is False:
        print(f"Fake: {obj} {type(obj)}")
        return 0
    if obj == 0 and isinstance(obj, int):
        print(f"Zero: {obj} {type(obj)}")
        return 0
    if isinstance(obj, str) and obj == "":
        print(f"Empty: {type(obj)}")
        return 0
    print("Type not Found")
    return 1


# from NULL_not_found import NULL_not_found
def main() -> None:
    """Do nothing when executed directly."""


if __name__ == "__main__":
    main()
