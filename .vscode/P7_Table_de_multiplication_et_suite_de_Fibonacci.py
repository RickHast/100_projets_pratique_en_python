from colorama import init, Fore, Style
import time
import random
init(autoreset=True)

# P7: Table de multiplication
ran = 13

# table de 2
def table_of_2() :
    print("\n*** Table of 2 ***")
    for i in range(ran) :
        cal = i * 2
        print(f"{i} x 2 = {cal}")

# table de 3
def table_of_3() :
    print("\n*** Table of 3 ***")
    for i in range(ran) :
        cal = i * 3
        print(f"{i} x 3 = {cal}")

# table de 4
def table_of_4() :
    print("\n*** Table of 4 ***")
    for i in range(ran) :
        cal = i * 4
        print(f"{i} x 4 = {cal}")

# table de 5
def table_of_5() :
    print("\n*** Table of 5 ***")
    for i in range(ran) :
        cal = i * 5
        print(f"{i} x 5 = {cal}")

# table de 6
def table_of_6() :
    print("\n*** Table of 6 ***")
    for i in range(ran) :
        cal = i * 6
        print(f"{i} x 6 = {cal}")

# table de 7
def table_of_7() :
    print("\n*** Table of 7 ***")
    for i in range(ran) :
        cal = i * 7
        print(f"{i} x 7 = {cal}")

# table de 8
def table_of_8() :
    print("\n*** Table of 8 ***")
    for i in range(ran) :
        cal = i * 8
        print(f"{i} x 8 = {cal}")

# table de 9
def table_of_9() :
    print("\n*** Table of 9 ***")
    for i in range(ran) :
        cal = i * 9
        print(f"{i} x 9 = {cal}")

# table de 10
def table_of_10() :
    print("\n*** Table of 10 ***")
    for i in range(ran) :
        cal = i * 10
        print(f"{i} x 10 = {cal}")

# table de 11
def table_of_11() :
    print("\n*** Table of 11 ***")
    for i in range(ran) :
        cal = i * 11
        print(f"{i} x 11 = {cal}")

# table de 12
def table_of_12() :
    print("\n*** Table of 12 ***")
    for i in range(ran) :
        cal = i * 12
        print(f"{i} x 12 = {cal}")


# Choix tu type de table
def multiplication_table():
    table_list = {1: "table of 2", 2: "table of 3", 3: "table of 4", 4: "table of 5", 5: "table of 6", 6: "table of 7", 7: "table of 8", 8: "table of 9", 9: "table of 10", 10: "table of 11",11: "table of 12",12: "All tables", 13: "go back to the menu", 14: "Leave"}
    while True:
        print("\n","*"*60)
        print("==== Welcome in the multiplication table menu ====")
        for i,tab in table_list.items():
            print(f"{i} -{Fore.YELLOW}{tab}")

        try: 
            choix_table = int(input("\nEnter a choice: "))
            if choix_table not in table_list :
                raise ValueError
        except ValueError:
            print(f"\n{Fore.RED}ERROR: Invalid Choice !!")
            continue

        if choix_table == 1 :
            table_of_2()

        elif choix_table == 2 :
            table_of_3()

        elif choix_table == 3 :
            table_of_4()

        elif choix_table == 4 :
            table_of_5()

        elif choix_table == 5 :
            table_of_6()

        elif choix_table == 6 :
            table_of_7()

        elif choix_table == 7 :
            table_of_8()

        elif choix_table == 8 :
            table_of_9()

        elif choix_table == 9 :
            table_of_10()

        elif choix_table == 10 :
            table_of_11()

        elif choix_table == 11 :
            table_of_12()

        elif choix_table == 12 :
            table_of_2()
            table_of_3()
            table_of_4()
            table_of_5()
            table_of_6()
            table_of_7()
            table_of_8()
            table_of_9()
            table_of_10()
            table_of_11()
            table_of_12()

        elif choix_table == 13 :
            menu_table_suite()
            return

        elif choix_table == 14 :
            print(f"\n{Fore.GREEN}Goodbye !!")
            break


# choix de la maniere de generation de la suite
def Fibonacci_recurrence():
    fibo_list = {1: "start to generate the reccurence at 0", 2: "Choose the reccurence start", 3: "go back to the menu", 4: "Leave"}
    while True:
        print("\n","*"*60)
        print("==== Welcome in the Fibonacci Recurrence menu ====")
        for i,fibo in fibo_list.items() :
            print(f"{i} -{Fore.BLACK}{fibo}")

        try :
            fibo_choice = int(input(f"\nChoose an option in the menu: "))
            if fibo_choice not in fibo_list :
                raise ValueError
        except ValueError:
            print(f"\n{Fore.RED}ERROR: your option not in the menu choice !!")
            continue

        if fibo_choice == 1 :
            a, b = 0, 1
            for i in range(20) :
                time.sleep(random.uniform(0.2, 0.6))
                print(a, end=" ")
                a, b = b, a + b

        elif fibo_choice == 2 :
            while True :
                try :
                    rec_start = int(input("\nEnter the reccurence start: "))
                    if rec_start <= 0 :
                        raise ValueError

                except ValueError:
                    print(f"\n{Fore.RED}ERROR: enter a positif number !!")
                    continue

                try :
                    max_rec = int(input("Enter max the reccurence value: "))
                    if rec_start <= 0 :
                        raise ValueError

                except ValueError:
                    print(f"\nERROR: enter a positif number !!")
                    continue

                a, b = rec_start, rec_start+1
                for i in range(max_rec) :
                    time.sleep(random.uniform(0.2, 0.6))
                    print(a, end=",")
                    a, b = b, a + b

                return
            
        elif fibo_choice == 3 :
            menu_table_suite()
            return
        
        else :
            print(f"\n{Fore.GREEN}Goodbye")
            break


#menu de choix entre la table et les suites
def menu_table_suite():
    menu_list = {1: "Multiplication table", 2: "Fibonacci recurrence", 3: "Leave"}
    while True:
        print("\n","*"*60)
        print("==== Welcome in the multiplication table and Fibonacci recurrence Menu ====")
        for i,menu in menu_list.items():
            print(f"{i} -{Fore.CYAN}{menu}")

        try:
            user_menu_choice = int(input("Enter your menu choice: "))
            if user_menu_choice not in menu_list:
                raise ValueError
        except ValueError:
            print(f"\n{Fore.RED}ERROR! Enter 1 or 2")
            continue

        if user_menu_choice == 1 :
            multiplication_table()
            break

        elif user_menu_choice == 2 :
            Fibonacci_recurrence()
            break

        elif user_menu_choice == 3 :
            print(f"\n{Fore.GREEN}Goodbye!!")
            break

if __name__ == '__main__' :
    menu_table_suite()

