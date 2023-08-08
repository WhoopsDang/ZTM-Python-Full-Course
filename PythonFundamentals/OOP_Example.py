"""A player in a game"""


# OOP
class PlayerCharacter:
    """
    Class that describes a character in a game
    """

    # Class Object Attribute
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        """Method that allows person to run"""
        print("run")

    @classmethod
    def adding_things(cls, num1, num2):
        """Method to add stuff"""
        return cls("teddy", num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        """same thing as the other method but as a static"""
        return num1 + num2


player1 = PlayerCharacter("Matt", 12)

print(player1.name)
player1.run()
print(PlayerCharacter.adding_things(3, 2))
