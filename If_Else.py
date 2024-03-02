# age = int(input("enter your age: "))
# print(age)

# applePrice = 200
# budget = int(input("enter your number:"))
# if budget >= applePrice:
#     print("Alexa, add 1 kg apple on cart.")
# else:
#     print("Alexa, don't add apple on cart.")

Name = input("Enter your name please......\t")
import time

timestamp = time.strftime('%H:%M:%S:%p')
print(timestamp)
Hour = int(time.strftime('%H'))
Minute = int(time.strftime('%M'))
Second = int(time.strftime('%S'))
Str = time.strftime('%p')

if 5 <= Hour <= 11 and Str == "AM":
    print('"Good Morning",', Name)
elif 12 <= Hour <= 17 and Str == "PM":
    print('"Good afternoon",', Name)
else:
    print('"Good evening",', Name)
