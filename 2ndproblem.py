
"""2. How do you create a parameterized decorator? Write a decorator that takes an argument specifying how many times to retry a function upon failure.
Parameterized decorator

- means the decorator itself has some parameters
- here retry_decorator has the parameters as "retries"
"""
def retry_decorator(retries):
    def decorator(func):
        def wrapper():
            for attempt in range(retries):
                try:
                    return func()
                except Exception as e:
                    print(f"Attempt Number {attempt+1} Failed:{e}")
            print(f"Function failed after {retries} retries")
        return wrapper
    return decorator
@retry_decorator(retries=3)
def test_function():
    print("Trying...")
    raise ValueError("Something Went WRONG")
test_function()