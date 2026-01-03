from colorama import Fore, Style, init
init(autoreset=True)

#P11: Conversion de secondes heures minutes

def secondes_conversion():
    while True:
        try:
            secondes = int(input(f"{Fore.CYAN}\nEntrez un nombre de secondes : {Style.RESET_ALL}"))
            if secondes < 0:
                print(f"{Fore.RED}Entrez un nombre positif !")
                continue
            break
        except ValueError:
            print(f"{Fore.RED}Entrez un nombre entier valide !")

    heures = secondes // 3600
    minutes = (secondes % 3600) // 60
    secondes_restantes = secondes % 60

    print(f"\n{Fore.MAGENTA}{secondes}{Style.RESET_ALL} secondes = ", end="")
    if heures > 0:
        print(f"{Fore.YELLOW}{heures}{Style.RESET_ALL} heure(s), ", end="")
    if minutes > 0:
        print(f"{Fore.GREEN}{minutes}{Style.RESET_ALL} minute(s) et ", end="")
    print(f"{Fore.CYAN}{secondes_restantes}{Style.RESET_ALL} seconde(s)")

if __name__ == '__main__':
    secondes_conversion()
# menu du choix de conversion
def converter_menu():
    conver_dict = {1: f"{Fore.GREEN}Convert Second", 2: "Leave"}
    while True:
        print("\n","*"*60)
        print("===== Welcome in the Second convertion menu =====")
        for i,time in conver_dict.items():
            print(f"{i} -{time}")

        try :
            time_choice = int(input("\nEnter Your choice here: "))
            if time_choice not in conver_dict :
                raise ValueError
        except ValueError:
            print("\nERROR: Your choice not in the menu choice !")
            continue
        if time_choice == 1 :
            secondes_conversion()
            break

        elif time_choice == 2 :
            print("\nGoodbye and look forward !!\n")
            break      


if __name__ == '__main__' :
    converter_menu()

