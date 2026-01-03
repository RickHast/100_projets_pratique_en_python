from colorama import Fore,Style,init
from math import factorial
init(autoreset=True)

# P10: Calcul de Factorielle

def fact_menu():
    fact_dict = {1: f"{Fore.GREEN}Do a Factorielle", 2: f"{Fore.RED}Leave"}
    while True:
        print("\n","*"*60)
        print("======  Welcome in the Factoriel menu =====")
        for i,fact in fact_dict.items() :
            print(f"{i} -{fact}")

        try : 
            fact_choice = int(input(f"{Fore.CYAN}\nEnter Your menu choice here: {Style.RESET_ALL}"))
            if fact_choice not in fact_dict :
                raise ValueError
        except ValueError:
            print(f"\n{Fore.RED}ERROR: Enter 1 or 2!")
            continue

        if fact_choice == 1 :
            while True:
                try:
                    user_number = int(input(f"{Fore.CYAN}\nEnter A Number: {Style.RESET_ALL}"))
                    if user_number < 0 or user_number > 1000 :
                        raise ValueError
                except ValueError:
                    print(f"\n{Fore.RED}ERROR: Please Enter an Integer ( 0 < integer < 1000) ")
                    continue

                if user_number :
                    break

                elif user_number == 0 :

                    break


                

            fact_num = factorial(user_number)
            
            print(f"\nLa Factoriel de {Fore.YELLOW}{user_number}{Style.RESET_ALL} est: {Fore.RED}{fact_num}\n")
            print(f"Expression: Fact[{Fore.YELLOW}{user_number}{Style.RESET_ALL}] = {Fore.RED}{fact_num}\n")


        elif fact_choice == 2 :
            print(f"{Fore.BLUE}Goodbye and look forward !!\n")
            break


if __name__ == '__main__' :
    fact_menu()

