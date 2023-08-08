n = input()


def factorial(n):
    a = 1
    b = 2
    for i in range(n):
        yield a
        a = a * b
        b += 1


for i in factorial(int(n)):
    print(f"{i},", end="")
