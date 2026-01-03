from random import randint, choice
from string import ascii_letters, digits, punctuation
from colorama import Fore, init
init(autoreset=True)

# P3_Generateur de mot de passe

# Generateur de mot de passe faible
def weak_password():
    weak_pass_dict = {1: "Generate the Weak Password", 2: "Go back to the menu", 3: "Leave"}
    max_w_pass = 7
    w_list = []
    while True:
        print("\n","*"*60)
        print("==== Welcome in the Weak Password generator ====")
        for i,we_pass in weak_pass_dict.items():
            print(f"{i} -{we_pass}")

        try :
            weak_choice = int(input("\nDo you want a Password Generation: "))
            if weak_choice not in weak_pass_dict :
                raise ValueError
        except ValueError:
            print(f"\n{Fore.RED}ERROR: Enter a value in range 1 - 3")
            continue

        if weak_choice == 1 :
            for i in range(1,max_w_pass):
                sep_w_pass = choice(ascii_letters)
                w_list.append(sep_w_pass)
            
            weak_pass = "".join(w_list)
            print(f"\nYour weak password is: {Fore.GREEN}{weak_pass}")

        elif weak_choice == 2 :
            password_menu()

        else :
            print("\nBye !\n")
            break


# Generateur de mot de passe Moyen
def medium_password():
    med_pass_dict = {1: "Generate the Medium Password", 2: "Go back to the menu", 3: "Leave"}
    max_m_pass = 14
    m_list = []
    while True:
        print("\n","*"*60)
        print("==== Welcome in the Medium Password generator ====")
        for i,me_pass in med_pass_dict.items():
            print(f"{i} -{me_pass}")

        try :
            med_choice = int(input("\nDo you want a Password Generation: "))
            if med_choice not in med_pass_dict :
                raise ValueError
        except ValueError:
            print(f"\n{Fore.RED}ERROR: Enter a value in range 1 - 3")
            continue

        if med_choice == 1 :
            for i in range(1,max_m_pass):
                rand_med = randint(1,2)
                if rand_med == 1 :
                    char_m_pass = choice(ascii_letters)
                    m_list.append(char_m_pass)

                else :
                    dig_m_pass = choice(digits)
                    m_list.append(dig_m_pass)
            
            med_pass = "".join(m_list)
            print(f"\nYour Medium password is: {Fore.YELLOW} {med_pass}")

        elif med_choice == 2 :
            password_menu()

        else :
            print("\nBye !\n")
            break


# generateur de mot de passe fort
def strong_password():
    str_pass_dict = {1: "Generate the Strong Password", 2: "Go back to the menu", 3: "Leave"}
    max_s_pass = 25
    s_list = []
    while True:
        print("\n","*"*60)
        print("==== Welcome in the strong Password generator ====")
        for i,str_pass in str_pass_dict.items():
            print(f"{i} -{str_pass}")

        try :
            str_choice = int(input("\nDo you want a Password Generation: "))
            if str_choice not in str_pass_dict :
                raise ValueError
        except ValueError:
            print(f"\n{Fore.RED}ERROR: Enter a value in range 1 - 3")
            continue

        if str_choice == 1 :
            for i in range(1,max_s_pass):
                rand_str = randint(1,3)
                if rand_str == 1 :
                    char_s_pass = choice(ascii_letters)
                    s_list.append(char_s_pass)

                elif rand_str == 2 :
                    dig_s_pass = choice(digits)
                    s_list.append(dig_s_pass)

                else :
                    punc_s_pass = choice(punctuation)
                    s_list.append(punc_s_pass)
            
            str_pass = "".join(s_list)
            print(f"\nYour strong password is: {Fore.MAGENTA} {str_pass}")

        elif str_choice == 2 :
            password_menu()

        else :
            print("\nBye !\n")
            break


# menu du choix des generateurs de pot de passe
def password_menu():
    password_dict = {1: "Weak Password", 2: "Medium Password", 3: "Strong Password", 4: "Leave"}
    while True:
        print("\n","*"*60)
        print("==== Welcome in the password generator menu choice ====")
        for i,passw in password_dict.items():
            print(f"{i} -{passw}")

        try :
            generator_choice = int(input("\nYour Choice: "))
            if generator_choice not in password_dict :
                raise ValueError
        except ValueError:
            print(f"\n{Fore.RED}Enter a Figure !")
            continue

        if generator_choice == 1 :
            weak_password()
            break

        elif generator_choice == 2 :
            medium_password()
            break

        elif generator_choice == 3 :
            strong_password()
            break

        elif generator_choice == 4 :
            print("\nGoodBye !\n")
            break

if __name__ == '__main__':
    password_menu()





