import time

time.sleep(1)
print(
    "                                Welcome in Snake_Water_Gun_Game                           "
)

print(
    """
                    0-----> Snake
                    1-----> Water
                    2-----> Gun
                          """
)

import random

List = []
Num1 = [0, 1, 2]

Num = random.randint(0, 2)
Start = input("You wants play this game: ")
match Start.upper():
    case "YES":
        Input = int(input("How many times you want to play this game :"))
        for i in range(0, Input):

            Times = int(input("\nEnter your number: "))
            print(f"Player move {Times}")
            if Times in Num1:
                print(f"Computer move  {Num}")
                if Times == Num:
                    print("It's a tie!")
                elif Times == 0 and Num == 1:
                    print("Snake drink Water. Player Win!")
                elif Times == 1 and Num == 2:
                    print(" Water extinguishes Gun.  Player Win!")
                elif Times == 2 and Num == 1:
                    print("Gun shoot Snakes.  Player Win")
                else:
                    print("Computer Win!")
            else:
                print(f"Warning!!...wrong input...{Times}")
                break
    case _:
        print("Quit")
