# Given the below class:
class Cat:
    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("kyle", 2)
cat2 = Cat("pickles", 4)
cat3 = Cat("table", 1)


# 2 Create a function that finds the oldest cat
def findOldestCat(*cats):
    oldest_cat = Cat("none", 0)
    for cat in cats:
        if cat.age > oldest_cat.age:
            oldest_cat = cat

    return oldest_cat


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(findOldestCat(cat1, cat2, cat3).age)
