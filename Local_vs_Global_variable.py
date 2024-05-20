x = 4


"""def hello():
    x = 20
    global y
    y = 50
    print(f"The global x is: {x}")
    print("Hello world")


print(f"The global x is: {x}")
hello()
print(f"The global x is: {x}")"""


# change value of global variable
def my_function():
    global x
    x = 20
    y = 40
    print(y)


my_function()
print(x)
