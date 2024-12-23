""" Write a decorator double_result that doubles the result of the decorated function. 
Use it with a function add that adds two numbers.
"""
def double_result(func):
    def wrapper(*args,**kwargs):
        res=func(*args,**kwargs)
        print(f"the result is {res}")
        print(f"the double of the result of decorated function is {2*res}")
    return wrapper
@double_result
def add(x,y):
    return(x+y)
add(2,3)