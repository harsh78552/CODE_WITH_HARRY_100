def calculateGmean(num1, num2):
    mean = (num1 * num2) / (num1 + num2)
    print(mean)


def Greater(num1, num2):
    if (num1 > num2):
        print("Num1 is greater.")
    else:
        print("Num2 is greater.")


num1 = int(input("enter your number: "))
num2 = int(input("enter your number: "))
calculateGmean(num1, num2)
Greater(num1, num2)

a = 4
v = 6
calculateGmean(a, v)
Greater(num1, num2)
