"""
Write a simple decorator that prints the execution of a function
"""
def the_decorator(func):
    def wrapper(*args,**kwargs):
        for arg in args:
            print(f"{arg} is getting ready for the school")
            result=func(*args,**kwargs)
            print(f"{arg} came back to Home after finishing school")
            return result
    return wrapper
@the_decorator
def base_func(name,age):
    print(f"the name of the student is {name} and the age is{age}")
base_func('tanuja',23)