from colorama import Fore,Style,init
init(autoreset=True)

# P2: Calculatrice Simple

# fonction de calcul simple
def calculator():
    operator = {1: "+", 2: "-", 3: "*", 4: "/"}
    while True:
        print("\n","*"*60)
        print("\n=== Welcome Choose an operation ===")
        for i,op in operator.items():
            print(f"{i} - {op}")

        #choix de l'operation
        try :
            operation_choice = int(input(f"\n{Fore.YELLOW}Your choice: "))
            if operation_choice not in operator:
                raise ValueError
        except ValueError:
            print(f"\n{Fore.RED}Enter a Integer !{Style.RESET_ALL}")
            continue
        
        #entrer des deux valeurs
        try:
            first_value = float(input(f"\n{Fore.CYAN}Enter the first value: "))
            second_value = float(input(f"\n{Fore.CYAN}Enter the second value: "))
        except ValueError:
            print("\nEnter a float !")
            continue

        # opérations
        if operation_choice == 1 :
            result = first_value + second_value
            op = "+"
            break
        
        elif operation_choice == 2 :
            result = first_value - second_value 
            op = "-"
            break

        elif operation_choice == 3 :
            result = first_value * second_value
            op = "*"
            break

        elif operation_choice == 4 :
            op = "/"
            if second_value != 0 :
                result = first_value / second_value

            else :
                print(f"\n{Fore.RED}Division by Zero is impossible\n{Style.RESET_ALL}")

            continue

    # Affichage de l'opération
    print(f"{Fore.CYAN}{first_value} {op} {second_value} = {result}{Style.RESET_ALL}")

        
# Menu de la calculatrice
def menu():
    while True:
        print("\n","*"*60)
        print("===== Welcome in the simple calculator menu =====")
        print("1 -do a calcul")
        print("2 -leave")
        
        # choix de calcul ou pas
        try :
            choice = int(input("\nEnter your choice here: "))
        except ValueError:
            print(f"\n{Fore.RED}ERROR: Enter a figure!!{Style.RESET_ALL}")
            continue

        if choice == 1 :
            calculator()
            break

        elif choice == 2 :
            print("\nGoodbye\n")
            break

        else :
            print(f"{Fore.RED}Invalid Choice{Style.RESET_ALL}")
            continue

if __name__ == '__main__' :
    menu()

