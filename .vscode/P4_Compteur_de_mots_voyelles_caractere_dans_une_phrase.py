from colorama import Fore,Style,init
init(autoreset=True)

# P4_Compteur_de_mots_voyelles_caractere_dans_une_phrase

# Fonction Pour Compter les mots de la prhase
def word_counter():
    word_dict = {1: 'count the Words', 2: 'Go back to the menu', 3: 'Leave'}
    while True:
        print("\n","*"*60)
        print("===== Welcome in Word/Vowels/character counter")
        for i,wchoi in word_dict.items():
            print(f"{i} -{wchoi}")

        try :
            user_w_choice = int(input("\nWhat is your choice: "))
            if user_w_choice not in word_dict :
                raise ValueError
        except ValueError:
            print(f"\n{Fore.RED}ERROR: Enter a figure! ")
            continue

        if user_w_choice == 1 :
            word_sent = input("\nEnter Your sentence Here: ").split()
            len_word = len(word_sent)
            print(f"\nYour sentence {word_sent} \ncontains {Fore.CYAN}{len_word} Words")
            
        elif user_w_choice == 2 :
            menu()
            return

        else :
            break



# Fonction Pour Compter les Voyelles de la prhase
def vowels_counter():
    vow_dict = {1: 'count the Vowels', 2: 'Go back to the menu', 3: 'Leave'}
    while True:
        print("\n","*"*60)
        print("===== Welcome in Vowels counter")
        for i,vchoi in vow_dict.items():
            print(f"{i} -{vchoi}")

        try :
            user_v_choice = int(input("\nWhat is your choice: "))
            if user_v_choice not in vow_dict :
                raise ValueError
        except ValueError:
            print(f"\n{Fore.RED}ERROR: Enter a figure! ")
            continue

        if user_v_choice == 1 :
            vowels = set("aeiouyAEIOUY")
            vow_sent = input("\nEnter Your sentence Here: ")
            vow = sum(1 for letter in vow_sent if letter in vowels)
            print(f"\nYour sentence {vow_sent} \ncontains {Fore.CYAN}{vow} Vowels")


        elif user_v_choice == 2 :
            menu()
            return

        else :
            break


# Fonction Pour Compter les Caractères de la prhase
def char_counter():
    let_dict = {1: 'count the letters', 2: 'Go back to the menu', 3: 'Leave'}
    while True:
        print("\n","*"*60)
        print("===== Welcome in letters counter")
        for i,lchoi in let_dict.items():
            print(f"{i} -{lchoi}")

        try :
            user_l_choice = int(input("\nWhat is your choice: "))
            if user_l_choice not in let_dict :
                raise ValueError
        except ValueError:
            print(f"\n{Fore.RED}ERROR: Enter a figure! ")
            continue

        if user_l_choice == 1 :
            let_sent = input("\nEnter Your sentence Here: ")
            len_let = len(let_sent.isalpha())
            print(f"\nYour sentence {let_sent} \ncontains {Fore.CYAN}{len_let} Letters")


        elif user_l_choice == 2 :
            menu()
            return

        else :
            break

# Fonction menu Pour faire le choix entre les types de compteurs
def menu():
    counter = {1: "Word", 2: "Vowels", 3: "Character", 4: "Leave"}
    while True:
        print("\n","*"*60)
        print("===== Welcome in Word/Vowels/character counter")
        for i,count in counter.items():
            print(f"{i} -{count}")

        try :
            counter_choice = int(input("\nWhich counter will you choose: "))
            if counter_choice not in counter :
                print(f"\n{Fore.RED}Invalid Choice")
                raise ValueError
        except ValueError:
            print(f"\n{Fore.RED}ERROR: Enter a integer")

        if counter_choice == 1 :
            word_counter()
            break

        elif counter_choice == 2 :
            vowels_counter()
            break

        elif counter_choice == 3 :
            char_counter()
            break

        elif counter_choice == 4 :
            print("\nGood Bye!!\n")
            break

if __name__ == '__main__':
    menu()

