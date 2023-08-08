""" This is actually pretty crazy, you can add extra prebuilt steps into a 
function by using a decorator. By creating a function that accepts and returns a 
function you can then add extra functionality before executing the called 
function and then applying that to new functions as a decorator """


def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("********")
        func(*args, **kwargs)
        print("********")

    return wrap_func


@my_decorator
def hello(greeting, emoji=" :)"):
    print(greeting + emoji)


@my_decorator
def bye():
    print("byeeee")


hello("hello")
bye()
