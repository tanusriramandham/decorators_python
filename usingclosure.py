def decorator(func):
    def wrapper(args):
        print("Before the function call")
        result = func(args)
        print("After the function call")
        return result
    return wrapper

@decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
