#!../.venv/bin/python

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[1] = "World!"
ft_tuple = (ft_tuple[0], "UAE!")

# This will raise a KeyError if "tutu!" is not found
# ft_set.remove("tutu!")

ft_set.discard("tutu!")
ft_set.add("Abu Dhabi!")

ft_dict["Hello"] = "42 Abu Dhabi!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
