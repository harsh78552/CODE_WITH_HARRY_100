def greet(sx):
    def mfx():
        print("Good Morning")
        sx()
        print("Thanks for using these functions")

    return mfx()


@greet
def hello():
    print("Hello world")


hello()

# greet(hello)()


"""import logging


def log_function_call(func):
    print("hii")
    def decorated(*args, **kwargs):
        logging.info(f"Calling{func.__name__} with args={args},kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result

    return decorated


def my_function(a, b):
    return a + b


logged_my_fun = log_function_call(my_function)
result1 = logged_my_fun(1, 2)
print(result1)
# Example string
input_string = input("Enter yes: ")

# Case-insensitive comparison using case fold()
if input_string.casefold() == "yes":
    print("The strings match (case-insensitive)")
else:
    print("The strings do not match (case-insensitive)")"""
