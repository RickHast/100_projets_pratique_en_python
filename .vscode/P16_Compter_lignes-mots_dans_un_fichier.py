import os
from colorama import Fore,Style,init
init(autoreset=True)
lfile_name = 'Journal.txt'

#P16: Compteur de ligne et de mots dans un Fichier

#Fonction pour compter le nombre de ligne
def lines_counter() :
    l_dict = {1: f"{Fore.LIGHTBLUE_EX}count lines", 2: f"{Fore.LIGHTBLACK_EX}Back to menu", 3: f"{Fore.RED}Leave"}
    while True:
        print("\n","-"*60)
        print("*** Welcome in the Line Counter ***")
        for i,l in l_dict.items() :
            print(f"{i} -{l}")

        try :
            l_choice = int(input("\nEnter your own choice here: "))
            if l_choice not in l_dict :
                raise ValueError
        except ValueError:
            print(f"{Fore.RED}\nERROR: Your Choice not in the List From the top !!")
            continue

        if l_choice == 1 :
            if os.path.exists(lfile_name) :
                print(f"{Fore.GREEN}\nLe Fichier {lfile_name} existe")
            else :
                print(f"{Fore.RED}\nLe Fichier {lfile_name} N'existe pas!")
                continue

            with open(lfile_name, "r") as f :
                lines = f.readlines()
                nb_lines = len(lines)
                print(f"Your File Contains: {Fore.LIGHTBLUE_EX}{nb_lines} Lines")
            

        elif l_choice == 2 :
            line_word_counter_menu()
            return
        
        elif l_choice == 3 :
            print(f"{Fore.GREEN}\nThanks for your visits !!\n\n")
            break


#Fonction pour compter de mots
def word_counter() :
    w_dict = {1: f"{Fore.LIGHTYELLOW_EX}count Word", 2: f"{Fore.LIGHTBLACK_EX}Back to menu", 3: f"{Fore.RED}Leave"}
    while True:
        print("\n","-"*60)
        print("*** Welcome in the Word Counter ***")
        for i,w in w_dict.items() :
            print(f"{i} -{w}")

        try :
            w_choice = int(input("\nEnter your own choice here: "))
            if w_choice not in w_dict :
                raise ValueError
        except ValueError:
            print(f"{Fore.RED}\nERROR: Your Choice not in the List From the top !!")
            continue

        if w_choice == 1 :
            if os.path.exists(lfile_name) :
                print(f"{Fore.GREEN}\nLe Fichier {lfile_name} existe")
            else :
                print(f"{Fore.RED}\nLe Fichier {lfile_name} N'existe pas!")
                continue

            with open(lfile_name, "r") as f :
                words = f.read()
                nb_words = len(words.split())
                print(f"Your File Contains: {Fore.LIGHTYELLOW_EX}{nb_words} Words")
            

        elif w_choice == 2 :
            line_word_counter_menu()
            return
        
        elif w_choice == 3 :
            print(f"{Fore.GREEN}\nThanks for your visits !!\n\n")
            break


#Fonction pour compter le nombre de ligne et de mots en meme temp
def l_w_counter() :
    lw_dict = {1: f"{Fore.LIGHTMAGENTA_EX}count Lines and Words", 2: f"{Fore.LIGHTBLACK_EX}Back to menu", 3: f"{Fore.RED}Leave"}
    while True:
        print("\n","-"*60)
        print("*** Welcome in the Lines and Words Counter ***")
        for i,lw in lw_dict.items() :
            print(f"{i} -{lw}")

        try :
            lw_choice = int(input("\nEnter your own choice here: "))
            if lw_choice not in lw_dict :
                raise ValueError
        except ValueError:
            print(f"{Fore.RED}\nERROR: Your Choice not in the List From the top !!")
            continue

        if lw_choice == 1 :
            if os.path.exists(lfile_name) :
                print(f"{Fore.GREEN}\nLe Fichier {lfile_name} existe")
            else :
                print(f"{Fore.RED}\nLe Fichier {lfile_name} N'existe pas!")
                continue
            
            
            with open(lfile_name, "r") as f :
                # Lignes
                lines = f.readlines()
                nb_lines = len(lines)

                f.seek(0)  # remet le curseur au début
                # Mots
                words = f.read()
                nb_words = len(words.split())
                print(f"\nYour File Contains: {Fore.LIGHTBLUE_EX}{nb_lines} Lines{Style.RESET_ALL} and {Fore.LIGHTYELLOW_EX}{nb_words} Words\n")
            

        elif lw_choice == 2 :
            line_word_counter_menu()
            return
        
        elif lw_choice == 3 :
            print(f"{Fore.GREEN}\nThanks for your visits !!\n\n")
            break


#Fonction menu pour le Choix du type de compteur 
def line_word_counter_menu() :
    lwc_dict = {1: f"{Fore.LIGHTBLUE_EX}lines counter", 2: f"{Fore.LIGHTYELLOW_EX}Word Counter", 3: f"{Fore.LIGHTMAGENTA_EX}Lines-Word Counters", 4: f"{Fore.RED}Leave the menu"}
    while True:
        print("\n","*"*60)
        print("===== Welcomme in the Lines/Word Counter Menu =====")
        for i,lwc in lwc_dict.items():
            print(f"{i} -{lwc}")

        try :
            user_lwcc = int(input("Put any Option here: "))
            if user_lwcc not in lwc_dict :
                raise ValueError
        except ValueError:
            print(f"{Fore.RED}\nERROR: This Option didn't exist!")
            continue

        if user_lwcc == 1 :
            lines_counter()
            break

        elif user_lwcc == 2 :
            word_counter()
            break

        elif user_lwcc == 3 :
            l_w_counter()
            break

        elif user_lwcc == 4 :
            print("\nBye human !!\n\n")
            break

        
if __name__ == '__main__' :
    line_word_counter_menu()

