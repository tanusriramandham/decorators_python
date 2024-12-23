"""6. What happens when multiple decorators are applied to a single function?
we can add as many functionalities as our wish using as many decrators we want 
it is nothing but the multiple decorators
take 5th problem code and add another functionaloty to the double decorator futher to make the square of the result we got by double decorator
in this it follows a  structure
@decor1
@decor
first decor will apply on main function
secondly the outer decorator "decor1" will work on the result we got by first decor
"""
def triple_result(func):
    def wrapper(*args,**kwargs):
        res=func(*args,**kwargs)
        answer2=res*res
        print(f"the triple of the result of decorated function is {answer2}")
        return answer2
    print("Welcome to triple_result")
    return wrapper
def double_result(func):
    def wrapper(*args,**kwargs):
        res=func(*args,**kwargs)
        answer1=2*res
        print(f"the result is {res}")
        print(f"the double of the result of decorated function is {answer1}")
        return answer1
    print("Welcome to the double_result")
    return wrapper
@triple_result
@double_result
def add(x,y):
    return(x+y)
add(2,3)