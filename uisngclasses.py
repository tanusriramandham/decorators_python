class Decorator:
    def __init__(self,func):
        self.func=func
    def __call__(self,args):
        print("Before the function call")
        result=self.func(args)
        print("After the Function call")
        return result


@Decorator
def base_func(name):
    print(f"HELLO {name}! this is  Base Function")
 
base_func("Tanuja")