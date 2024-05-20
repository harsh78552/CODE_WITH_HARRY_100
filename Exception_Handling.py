"""num = input("enter your number: ")
print(f"Multiplication table of {num} is:")
try:
    for i in range(1, 11):
        print(f"{int(num)} X {i} = {int(num) * i}")
except Exception as e:
    print(e)
print("important code...")
print("Thankyou..")"""
try:
    num = int(input("enter number:"))
    List = [5, 6]
    print(List[num])
except ValueError as v:
    print(v)
except IndexError as e:
    print(e)
