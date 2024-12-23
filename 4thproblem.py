"""4. Create a decorator call_counter that tracks how many times a function is called. 
Use it with a function say_hello that prints "Hello!".
"""
def call_counter(func):
    c=0
    def wrapper():
        nonlocal c
        c+=1
        func()
        print(f"{func.__name__} executed {c} times")
    return wrapper
@call_counter
def say_hello():
    print("HELLO WORLD")
say_hello()
say_hello()
say_hello()
