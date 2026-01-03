"""Simple manual tester for ex02/all_thing_is_obj."""

from find_ft_type import all_thing_is_obj


def run_demo() -> None:
    """Call all_thing_is_obj with the expected sample values."""

    samples = [
        ["Hello", "tata!"],
        ("Hello", "toto!"),
        {"Hello", "tutu!"},
        {"Hello": "titi!"},
        "Brian",
        10,
    ]

    for obj in samples:
        ret = all_thing_is_obj(obj)
        print(f"returned -> {ret}")


def main() -> None:
    ft_list = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "tutu!"}
    ft_dict = {"Hello" : "titi!"}
    all_thing_is_obj(ft_list)
    all_thing_is_obj(ft_tuple)
    all_thing_is_obj(ft_set)
    all_thing_is_obj(ft_dict)
    all_thing_is_obj("Brian")
    all_thing_is_obj("Toto")
    print(all_thing_is_obj(10))


if __name__ == "__main__":
    main()
    # run_demo()
