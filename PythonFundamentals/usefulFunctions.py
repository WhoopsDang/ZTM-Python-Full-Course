from functools import reduce

my_list = [1, 2, 3]
your_list = [10, 20, 30]
their_list = (5, 4, 3)


def multiply_by2(item):
    return item * 2


def only_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    print(acc, item)
    return acc + item


# map
# Performns an desired action on an iterable object does not change original object
print(list(map(multiply_by2, my_list)))
print(my_list)

# filter
# Keeps item in list based on the return of the function, function should return a boolean value
print(list(filter(only_odd, my_list)))

# zip
# Joins items from different lists but in the same index into a list of tuples
print(list(zip(my_list, your_list, their_list)))

# reduce
print(reduce(accumulator, my_list, 10))
