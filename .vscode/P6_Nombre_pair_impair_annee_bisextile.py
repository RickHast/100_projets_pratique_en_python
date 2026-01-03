from colorama import Fore,Style,init
init(autoreset=True)

# P6: Nombre Pair/Impaire

def Pair_Impair_Number_menu():
    piab_list = {1: "Enter a number", 2: "Go back to the menu",3: "Leave"}
    while True:
        print("\n","*"*60)
        print("\n===== Welcome in the Pair_Impair number and Bissextile year menu")
        for i,pi in piab_list.items():
            print(f"{i} -{pi}")

        try :
            user_pi_choice = int(input("\nEnter your choice here: "))
            if user_pi_choice not in piab_list:
                raise ValueError
        except ValueError:
            print(f"\n{Fore.RED}ERROR: enter 1, 2 or 3 !!")
            continue

        if user_pi_choice == 1 :
            try: 
                number = float(input("\nEnter your number: "))
            except ValueError:
                print(f"\n{Fore.RED}Error: enter a float or a integer!!")
                continue

            result = number % 2
            if result == 0 :
                signe = 'Pair'
            else :
                signe = 'Impair'

            print(f"\nYour number {Fore.CYAN}{number}{Style.RESET_ALL} is {Fore.BLUE}{signe}")

        elif user_pi_choice == 2 :
            menu()
            return

        elif user_pi_choice == 3 :
            print("\nGoodbye")
            break


def Bissextile_year():
    year_list = {1: "Enter a Year", 2: "Go back to the menu",3: "Leave"}
    while True:
        print("\n","*"*60)
        print("\n===== Welcome in the Pair_Impair number and Bissextile year menu")
        for i,y in year_list.items():
            print(f"{i} -{y}")

        try :
            user_y_choice = int(input("\nEnter your choice here: "))
            if user_y_choice not in year_list:
                raise ValueError
        except ValueError:
            print(f"\n{Fore.RED}ERROR: enter 1, 2 or 3 !!")
            continue

        if user_y_choice == 1 :
            try: 
                year = int(input("\nEnter your Year: "))
            except ValueError:
                print(f"\n{Fore.RED}Error: enter a integer!!")
                continue

            result1 = year % 4
            result2 = year % 100
            result3 = year % 400

            if (result1 == 0) and ((result2 != 0) or (result3 == 0)):
                days = f'{Fore.BLUE}366'
                signe = 'Bissextile'
            else:
                days = f'{Fore.YELLOW}365'
                signe = 'Not Bissextile'

            print(f"\nthe year {Fore.MAGENTA}{year} is {signe}{Style.RESET_ALL} and he contains {days} days")

        elif user_y_choice == 2 :
            menu()
            return

        elif user_y_choice == 3 :
            print("\nGoodbye")
            break



def menu():
    menu_list = {1: "Pair/Impair Number menu", 2: "Bissextile year",3: "Leave"}
    while True:
        print("\n","*"*60)
        print("\n===== Welcome in the Pair_Impair number and Bissextile year menu")
        for i,piab in menu_list.items():
            print(f"{i} -{piab}")

        try :
            user_choice = int(input("\nEnter your choice here: "))
            if user_choice not in menu_list:
                raise ValueError
        except ValueError:
            print(f"\n{Fore.RED}ERROR: enter 1, 2 or 3 !!")
            continue

        if user_choice == 1 :
            Pair_Impair_Number_menu()
            break

        elif user_choice == 2 :
            Bissextile_year()
            break

        elif user_choice == 3 :
            print("\nGoodbye")
            break


if __name__ == '__main__' :
    menu()
