from random import randint
from colorama import Fore,Style,init
init(autoreset=True)


# P9: Jeux du juste Nombre
# Menu du jeux
def game_menu():
    game_list = {1: f"{Fore.GREEN}Play the game", 2: f"{Fore.RED}Leave the game"}
    while True:
        print("\n","*"*60)
        for i,g in game_list.items():
            print(f"{i} -{g}")

        try: 
            decide = int(input("\nEnter your decision: "))
            if decide not in game_list :
                raise ValueError
        except ValueError: 
            print(f"\n{Fore.RED}ERROR: enter 1 or 2 !")
            continue

        if decide == 1 :
            just_number = randint(1,10000)
            round = 0
            while True:
                print("\n\t","*"*20, f"{Fore.LIGHTBLACK_EX}Round{round}{Style.RESET_ALL}", "*"*20)
                try:
                    user_number = int(input("\nEnter Your number: "))
                except ValueError:
                    print(f"\n{Fore.RED}ERROR: Enter Integer !!")
                    continue
                
                # L'utilisateur trouve le bon Nombre
                if user_number == just_number :
                    print(f"\n{Fore.GREEN}You Win !!")
                    print(f"You found it in {Fore.MAGENTA}{round}{Style.RESET_ALL} rounds !")
                    break
                    
                # le Nombre de L'utilisateur est superieur a celui de la machine
                elif user_number > just_number :
                    print(f"\n{Fore.YELLOW}It's less !")

                # le Nombre de L'utilisateur est Inferieur a celui de la machine
                elif user_number < just_number :
                    print(f"\n{Fore.RED}It's More !")

                round+=1

                if round == 20 :
                    print(f"\n\t{Fore.MAGENTA}Game Over Rounds = {round}\n")
                    break      

        else :
            print(f"\n{Fore.BLUE}Goodbye !!")
            break

if __name__ == '__main__' :
    game_menu()
                

            