# a = int(input("enter your value b/w 5 and 9: "))
# if a < 5 or a > 9:
#     raise ValueError("Value should be b/w 5 and 9")

a = (input("enter your value b/w 5 and 9 or quite "))

if a < 5 or a > 9 or a == 'quit':
    raise ValueError("value should be between 5 and 9 or quite")
