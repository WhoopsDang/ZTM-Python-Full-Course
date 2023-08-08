# By reading the python documentation, add 3 more magic/dunder methods of your choice to this Toy class.
class Toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            "name": "Yoyo",
            "has_pets": False,
        }

    def __str__(self):
        return f"{self.color}"

    def __len__(self):
        return 5

    def __del__(self):
        return "deleted"

    def __call__(self):
        return "yes??"

    def __getitem__(self, i):
        return self.my_dict[i]

    def __bytes__(self):
        return b"0b100"

    def __format__(self, format_spec):
        if format_spec == "":
            return "lmao you thought i was gonna format this"


action_figure = Toy("red", 0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure["name"])
print(bytes(action_figure))
print(format("hello", ""))
