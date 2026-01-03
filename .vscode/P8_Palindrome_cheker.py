from colorama import Fore, Style, init
import time
init(convert=True, autoreset=True)
#P8: Palindrome Cheker

# Fonction Permentant de Verifier si le mot est un palindrome ou pas
def palindrome_checker():
    palin_list = {1: f"{Fore.MAGENTA}Go to the palindrome checker", 2: f"{Fore.RED}leave"}
    while True:
        print("\n","*"*60)
        print("===== Welcome in the Palindrome Checker menu =====")
        for i,palin in palin_list.items():
            print(f"{i} -{palin}")

        #Vérifie le choix de l'utilisateur
        try :
            palin_choice = int(input("\nEnter your choice here: "))
            if palin_choice not in palin_list :
                raise ValueError
        except ValueError:
            print(f"{Fore.RED}\nERROR: Your choice didn't exist!!")
            continue

        #Vérification du mot
        if palin_choice == 1 :
            while True: 
                pal_word = input("\nEnter Your Word: ").strip()
                if pal_word:
                    break

                else: 
                    continue

            nettoy = ''.join(c.lower() for c in pal_word if c.isalnum())
            if nettoy == nettoy[::-1]:
                pal = f"\n\t{Fore.GREEN}C'est un palindrome\n\n"
            else: 
                pal = f"\n\t{Fore.RED}Ce n'est pas un palindrome\n\n"
            
            for i in pal :
                print(i, end="", flush=True)
                time.sleep(0.05)

        # Quitter le plalindrome cheker
        else:
            print(f"{Fore.BLUE}\nGoodbye !!!\n")
            break


if __name__ == '__main__' :
    palindrome_checker()

"""

.isalnum()      --> On garde seulement les lettres et chiffres (enlève espaces, accents, ponctuation, etc.)

.lower()        --> Met chaque caractère gardé en minuscule

nettoy[::-1]        --> Inverse la chaîne (le slicing magique de Python)

"""
