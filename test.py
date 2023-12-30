import sys
from colorama import Fore, Back, Style
n = 0
p = 1
while n < 3:
    sys.stdout.write(" ")
    for i in range(1, 9+n):
        sys.stdout.write(" *")
    n += 1
    print()

print("  * * *             *")
l1 = [' ', ' ', ' ']
l2 = [' ', ' ', ' ']
for i in range(1, p+1):
    if i<=3:
        l1[i-1]='*'
    else:
        l2[i-4]='*'
for i in range(2, 6):
    if i == 2:
        sys.stdout.write("  * * *   " + Fore.BLACK + Back.YELLOW + Style.BRIGHT + " " + ' '.join(l1) + " " + Style.RESET_ALL + "   *")
        print()
    elif i == 3:
        sys.stdout.write("  * * *   " + Fore.BLACK + Back.YELLOW + Style.BRIGHT + " " + ' '.join(l2) + " " +Style.RESET_ALL + "   *")
        print()
    elif i == 4:
        print("    * *             *")
    else:
        print("      * * * * * * * *")
