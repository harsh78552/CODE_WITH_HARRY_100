x = int(input("enter your number: "))
match x:
    case 0:
        print("X is zero.")
    case 4 if x % 2 == 0:
        print("X is even.")
    case _:
        print(x)
