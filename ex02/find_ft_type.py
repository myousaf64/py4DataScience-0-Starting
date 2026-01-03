"""Print object types and return 42."""


# def all_thing_is_obj(object: any) -> int:
def all_thing_is_obj(object: any) -> int:
    """Print the object type according to the specification and return 42."""

    if isinstance(object, list):
        print(f"List : {type(object)}")
    elif isinstance(object, tuple):
        print(f"Tuple : {type(object)}")
    elif isinstance(object, set):
        print(f"Set : {type(object)}")
    elif isinstance(object, dict):
        print(f"Dict : {type(object)}")
    elif isinstance(object, str):
        print(f"{object} is in the kitchen : {type(object)}")
    else:
        print("Type not found")
    return 42


def main() -> None:
    """Do nothing when executed directly."""


if __name__ == "__main__":
    main()
