from random import randint
from colorama import Fore,Style,init
init(autoreset=True)

# P13: Jeux du pierre Papier Ciseaux

# fonction pour le jeux de piere feuille ciseaux
def Play_rps():
    rps_random = {1: f"{Fore.LIGHTBLACK_EX}Rock", 2: f"{Fore.WHITE}Paper", 3: f"{Fore.YELLOW}Scissor"}
    machine_score = 0
    user_score = 0
    round = 1
    while True :
        mach_rand = randint(1,3)
        if mach_rand == 1 :
            mach_choice = "Rock"

        elif mach_rand == 2 :
            mach_choice = "Paper"

        elif mach_rand == 3 :
            mach_choice = "Scissor"

        print("\n","-"*40,f"Round {round}","-"*40)
        for x,rps_rand in rps_random.items() :
            print(f"\n\t{x} -{rps_rand}")

        try : 
            user_rps = int(input("\nEnter A figure in the list: "))
            if user_rps not in rps_random :
                raise ValueError
        except ValueError:
            print(f"\nERROR: Your choice didn't exist!")
            continue

        if user_rps < mach_rand :
            print(f"\n{Fore.LIGHTBLACK_EX}Machine:{Style.RESET_ALL} {mach_choice}")
            print(f"\n{Fore.LIGHTBLUE_EX}You:{Style.RESET_ALL} {user_rps}")
            print(f"\n{Fore.RED}You lose !!")
            machine_score += 1

        elif user_rps > mach_rand :
            print(f"\n{Fore.LIGHTBLACK_EX}Machine:{Style.RESET_ALL} {mach_choice}")
            print(f"\n{Fore.LIGHTBLUE_EX}You:{Style.RESET_ALL} {user_rps}")
            print(f"\n{Fore.GREEN}You Win !!")
            user_score += 1 

        elif user_rps == mach_rand :
            print(f"\n{Fore.LIGHTBLACK_EX}Machine:{Style.RESET_ALL} {mach_choice}")
            print(f"\n{Fore.LIGHTBLUE_EX}You:{Style.RESET_ALL} {user_rps}")
            print(f"\n{Fore.YELLOW}Same Choices !!!")

        if machine_score == 10  or user_score == 10 :
            print("\n\n\n\t*** The game is Finished ***\n")
            if machine_score > user_score :
                print(f"\n{Fore.LIGHTBLACK_EX}The Winner is The Macine, Her Score is:{Style.RESET_ALL} {machine_score}")
                print(f"\n{Fore.LIGHTBLUE_EX}You lose, Your score is:{Style.RESET_ALL} {user_score}")
                print("\nTry Again\n\n\n")
                break

            elif user_score > machine_score :
                print(f"\n{Fore.LIGHTBLUE_EX}You Win, Your score is:{Style.RESET_ALL} {user_score}")
                print(f"\n{Fore.LIGHTBLACK_EX}The Macine Lose, Her Score is:{Style.RESET_ALL} {machine_score}")
                print("\nTry Again If you want !")
                break

            else :
                print(f"\n{Fore.MAGENTA}It's a draw !")
                print(f"\n{Fore.LIGHTBLUE_EX}Your Score is: {user_score}")
                print(f"\n{Fore.LIGHTBLACK_EX}The Macine Score is: {machine_score}")
                break
        
        round += 1

    rock_paper_sissor_menu()

# Fonction menu pour le choix de jouer ou non
def rock_paper_sissor_menu() :
    rps_list = {1: f"{Fore.CYAN}Play the Game", 2: f"{Fore.YELLOW}Leave the game"}
    while True:
        print("\n","*"*60)
        print("===== Welcome in the Rock Paper Scissor Game Menu =====")
        for i,rps in rps_list.items() :
            print(f"{i} -{rps}")

        try : 
            rps_choice = int(input("\nEnter Your decision: "))
            if rps_choice not in rps_list :
                raise ValueError
        except ValueError:
            print(f"\n{Fore.RED}ERROR: You don't Enter the figure in the list !")
            continue

        if rps_choice == 1 :
            Play_rps()
            break

        elif rps_choice == 2 :
            print(f"\n{Fore.BLUE}GoodBye and look forward !!")
            break

if __name__ == '__main__' : 
    rock_paper_sissor_menu()


        

