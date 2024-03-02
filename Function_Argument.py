# Function is used to separate the code
"""There are four types of arguments that we can provide in a function
* Default Arguments
* Keyword Arguments
* Variable lengths Arguments
* Required Arguments"""

"""Default Arguments
def average(a=6, b=4):average(a, b)
    print("The average is ", (a + b) / 2)


a = int(input("enter your number: "))
b = int(input("enter the another value: "))
average(a, b)
average(9)


def name(fname, fname1="Gautam", fname2="Dev", fname3="Vishwajeet"):
    print(f"Hello, {fname} ,{fname1} ,{fname2} or {fname3}")
    print("How are you ? ")


name("Harsh", "Adarsh", "Pushkar", "Aryan")"""


# Keyword Arguments
def average(*numbers):  # number stores in tuples form
    # def average(**name):
    sum = 0
    for i in numbers:
        sum = sum + i
        return sum // len(numbers)
    # print("Average is: ", sum / len(numbers))


Average = average(5, 6, 7)
print(Average)