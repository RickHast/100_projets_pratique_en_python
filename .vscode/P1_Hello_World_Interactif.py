from datetime import datetime
from colorama import *

# P1_Hello World Amélioré

# l'heure actuelle
hours = datetime.now().hour

# Boule pour la saisie du nom de l'utilisateur
while True:
    name = input("\nEnter your name: ").strip().title()

    if name:
        print("\nSo your name is: ",name)
        break

    else:
        print("\nPlease Enter a name!!")
        continue


# choix du type de salutation en fonction de l'heure
if 5 <= hours < 12 :
    greething = "GoodMorning"

elif 12 <= hours < 18 :
    greething = "GoodAfternoon"

elif 18 <= hours < 23 :
    greething = "GoodEvening"

else :
    greething = "GoodNight"

# affichage d'un message en fonction de l'heure
print(f"\n{Fore.CYAN} {greething} {Style.RESET_ALL} {Fore.BLUE} {name} {Style.RESET_ALL} Welcome in Python")
print("\nWelcome to your Python journey in 2026 !\nLet's code 500 projects together !")


