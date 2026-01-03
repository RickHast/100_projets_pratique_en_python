from datetime import datetime
from colorama import Fore,init
import time
init(autoreset=True)

#P15: Lire Ecrire un fichier test simple

# Fonction menu de choix
def newspaper_menu() :
    news_dict = {1: f"{Fore.LIGHTBLUE_EX}Write in the Newspaper", 2: f"{Fore.LIGHTYELLOW_EX}Read the Newspaper", 3: f"{Fore.LIGHTRED_EX}Leave the menu"}
    while True:
        print("\n","*"*60)
        print("===== Welcome in the Newspaper menu =====")
        for i,news in news_dict.items():
            print(f"{i} -{news}")

        try : 
            user_nc = int(input("\nEnter Your Choice: "))
            if user_nc not in news_dict :
                raise ValueError
        except ValueError:
            print(f"\n{Fore.RED}ERROR: Enter a figure from the top list !!")
            continue

        # Ecrire dans le Journal
        if user_nc == 1 :
            while True:
                try:
                    rep_a = int(input("\nHow many times will you write in the newspaper: "))
                except ValueError:
                    print(f"\n{Fore.RED}ERROR: Enter a integer !")
                    continue

                if rep_a :
                    break

                else : 
                    continue
                
            with open("Journal.txt", "a") as f:
                for i in range(rep_a) :

                    f.write(datetime.now().strftime("%d/%m/%Y"))
                    f.write(":\t")
                    user_w =input("\nWrite in the newspaper: ")
                    f.write(user_w)
                    f.write("\n")
                    
        #Lire le Journal
        elif user_nc == 2 :
            print("\n")
            with open("Journal.txt", "r") as f :
                for lines in f :
                    for letter in lines :
                        print(letter, end="", flush=True)
                        time.sleep(0.03)
                    print()
                    time.sleep(0.5)

        #Quitter le menu
        elif user_nc == 3 :
            print("Goodbye !")
            break


if __name__ == '__main__' :
    newspaper_menu()
