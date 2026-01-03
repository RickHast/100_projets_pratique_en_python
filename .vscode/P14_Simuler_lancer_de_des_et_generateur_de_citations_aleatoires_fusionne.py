from random import randint, choice
import time
from colorama import Fore, Style, init
init(autoreset=True)

# P14: Simuler un lancer de dés et Générateur de Citations

# Function to Throw 'one' or 'multiple' dice(s)
def dice():
    dice_dict = {1: f"{Fore.BLUE}Roll The dice", 2: f"{Fore.MAGENTA}Return to Menu", 3: f"{Fore.RED}Leave"}
    while True:
        print("\n","-"*60)
        print("=== Welcome in the dice roller menu ==")
        for a,b in dice_dict.items():
            print(f"{a} -{b}")

        try: 
            user_dc = int(input("\nYour Choice: "))
            if user_dc not in dice_dict :
                raise ValueError
        except ValueError:
            print(f"{Fore.RED}Invalid Choice !!")
            continue

        if user_dc == 1:
            while True :
                try: 
                    hmd = int(input("\nHow much Dice will you Throw: "))
                except ValueError:
                    print(f"{Fore.RED}Enter a numeric Interger !")
                    continue

                if hmd:
                    break
            
            t = 1
            d = 1
            res = 0
            for rd in range(hmd) :
                rd = randint(1,6)
                print(f"\n\t**** {Fore.LIGHTBLACK_EX}Throw {t}{Style.RESET_ALL} ****")
                print(f"{Fore.BLUE}\tDice {d}{Style.RESET_ALL} ---> {Fore.LIGHTGREEN_EX}{rd}\n")
                t += 1
                d += 1
                res += rd

            print(f"All Dice Throws value are: {Fore.LIGHTGREEN_EX}{res}\n")
            print("\n\t** The Throws are finished ! Do you want to restart? **\n")

        elif user_dc == 2 :
            dice_compliment_menu()
            return
        
        elif user_dc == 3 :
            print(f"{Fore.LIGHTGREEN_EX}Bye, thaks for your playing!\n")
            break



# Function to Générate a Citations
def citation():
    comp_dict = {1: f"{Fore.YELLOW}Générate a citation", 2: f"{Fore.MAGENTA}Return to Menu", 3: f"{Fore.RED}Leave"}

    gene_comp = ["David Goggins: Just Do it.", "Walt Disney: The way to get started is to quit talking and begin doing.", "Winston Churchill: Success is walking from failure to failure with no loss of enthusiasm.", "Nelson Mandela: It always seems impossible until it's done.", "Walt Disney: If you can dream it, you can do it.", "George Eliot: It is never too late to be what you might have .", "Theodore Roosevelt: Do what you can, with what you have, where you are.", "Chris Grosser: Opportunities don't happen, you create them.", "Bervely sills: You may be disappointed if you fail, but you are doomed if you don't try.", "Les Browns: Don't let someone else's opinion of you become your reality.", "Stephen R. Covey: I am not a product of my circumstances. I am a product of my decisions.", "Sheryl Sandberg: If you're offered a seat on a rocket ship, don't ask what seat! Just get on.", "Napoleon Hill: Whatever the mind of man can conceive and believe, it can .", "Dan Millman: The secret of change is to focus all of your energy; not on fighting the old, but on building the new.", "Unknown: If you think small, your world will be small.", "Debbi Fields: The important thing is not being afraid to take a chance. Remember, the greatest failure is to not try.", "Ralph Waldo Emerson: The only person you are destined to become is the person you decide to be.", "Love your family, work super hard, live your passion.", "Winston Churchill: Success is not final; failure is not fatal: It is the courage to continue that counts.", "Sometimes Even The Devil on my Shoulder Asks:'What the fuck are you doing.'" ]
    while True:
        print("\n","-"*60)
        print("=== Welcome in the citation Générator ===")
        for l,k in comp_dict.items():
            print(f"{l} -{k}")

        try : 
            user_cm = int(input("\nYour opinion: "))
            if user_cm not in comp_dict :
                raise ValueError
        except ValueError :
            print(f"\n{Fore.RED}Invalid Figure !!")
            continue

        if user_cm == 1 :
            print(f"\n\t!!! {Fore.LIGHTMAGENTA_EX}PS: 20 is the maximum citaion in this program{Style.RESET_ALL} !!!")
            while True :
                try :
                    hmc = int(input("\nHow much citation will you need: "))
                except ValueError:
                    print(f"\nERROR: Choose another figure !!")
                    continue
                
                print(f"\n\t**** Your Citations: ****")
                n = 1
                for w in range(hmc):
                    gc = choice(gene_comp)
                    for k in gc :
                        print(k, end="")
                        time.sleep(0.05)
                    print("\n")
                    n += 1
                break

            print("\n** You Want to restart Citation Generation? **\n")
            
        elif user_cm == 2 :
            dice_compliment_menu()
            return
        
        elif user_cm == 3 :
            print("Go, Go with the Dicipline !!")
            break
            
# Fonction menu permettant le choix entre le lancer de dés et le générateur de motivation
def dice_compliment_menu():
    menu_dict = {1: f"{Fore.LIGHTBLUE_EX}Roll a dice", 2: f"{Fore.LIGHTYELLOW_EX}Générate a citation", 3: f"{Fore.RED}Leave"}
    while True:
        print("\n","*"*60)
        print(f"===== Welcome in the {Fore.LIGHTBLUE_EX}Roll a dice{Style.RESET_ALL} and{Fore.LIGHTYELLOW_EX} Citation Générator{Style.RESET_ALL} menu =====")
        for i,m in menu_dict.items() :
            print(f"{i} -{m}")

        try :
            user_mc = int(input("\nEnter Your Decision: "))
            if user_mc not in menu_dict :
                raise ValueError
        except ValueError:
            print(f"\n{Fore.RED}This Choice didn't exist !!")
            continue

        if user_mc == 1 :
            dice()
            break

        elif user_mc == 2 :
            citation()
            break

        elif user_mc == 3 :
            print(f"\nGoodbye Man !\n")
            break




if __name__ == '__main__' :
    dice_compliment_menu()
