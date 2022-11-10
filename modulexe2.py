from colorama import Fore, Back, Style


number = input("Anna jokin numero:\n")
number = int(number)

if number >= 0:
    print(Fore.BLACK + Back.LIGHTGREEN_EX + "Isompi kuin nolla")

else:
    print(Fore.BLACK + Back.LIGHTRED_EX + "Senkin negis.")