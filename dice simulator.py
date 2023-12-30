import random
import time
import sys
from colorama import Fore, Back, Style


def rollthedice(r):
    if int(r) == 0:
        o = random.randint(1, 6)
    else:
        o = random.choice([random.randint(1, 6), r])
    return int(o)


def printthedice(p):
    n = 0
    while n < 3:
        sys.stdout.write(" ")
        for i in range(1, 9 + n):
            sys.stdout.write(" *")
        n += 1
        print()
        time.sleep(0.25)

    print("  * * *             *")
    time.sleep(0.25)
    l1 = [' ', ' ', ' ']
    l2 = [' ', ' ', ' ']
    for i in range(1, p + 1):
        if i <= 3:
            l1[i - 1] = '*'
        else:
            l2[i - 4] = '*'
    for i in range(2, 6):
        if i == 2:
            sys.stdout.write("  * * *   " + Fore.BLACK + Back.YELLOW + Style.BRIGHT + " " + ' '.join(
                l1) + " " + Style.RESET_ALL + "   *")
            print()
            time.sleep(0.25)
        elif i == 3:
            sys.stdout.write("  * * *   " + Fore.BLACK + Back.YELLOW + Style.BRIGHT + " " + ' '.join(
                l2) + " " + Style.RESET_ALL + "   *")
            print()
            time.sleep(0.25)
        elif i == 4:
            print("    * *             *")
            time.sleep(0.25)
        else:
            print("      * * * * * * * *")
            time.sleep(0.25)


print("Welcome to the dice simulator :-")
readytoplay = input("Kindly press 1 to roll the dice, 0 to exit the game.\n")
while int(readytoplay) != 0:
    biasedornot = input("Press 0 for unbiased draw.\nPress any digit from 1 to 6 to make a biased roll of that number.\nKindly enter your choice:\n")
    diceout = rollthedice(biasedornot)
    time.sleep(5)
    print("\n")
    printthedice(diceout)
    if int(biasedornot) == 0:
        print(Fore.LIGHTMAGENTA_EX + "\nYou have got a unbiased roll: " + Style.BRIGHT + str(diceout) + Style.NORMAL + Style.RESET_ALL)
    else:
        print(Fore.LIGHTMAGENTA_EX + "\nYou have got a biased roll with " + str(biasedornot) + ": " + Style.BRIGHT + str(diceout) + Style.NORMAL + Style.RESET_ALL)

    print("\n")
    readytoplay = input("Kindly press 1 to roll again, 0 to exit the game.\n")

print(Fore.LIGHTCYAN_EX + "\nThank you for playing. Have a nice day." + Style.RESET_ALL)




