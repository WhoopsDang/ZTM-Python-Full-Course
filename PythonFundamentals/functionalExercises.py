from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ["sisi", "bibi", "titi", "carla"]

print(list(map(str.capitalize, my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ["a", "b", "c", "d", "e"]
my_numbers = [5, 4, 3, 2, 1]

my_numbers.sort()

print(list(zip(my_strings, my_numbers)))
# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
print(list(filter(lambda item: item > 50, scores)))

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
numbers = list(zip(my_numbers, scores))


def combine(acc, number):
    return acc + number[0] + number[1]


print(reduce(combine, numbers, 0))
