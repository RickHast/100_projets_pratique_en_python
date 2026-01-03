from tkinter import *
from random import randint
from colorama import Fore,Style,init
init(autoreset=True)


def play_rps():
    rps_random = {1: f"{Fore.LIGHTBLACK_EX}Rock", 2: f"{Fore.WHITE}Paper", 3: f"{Fore.YELLOW}Scissor"}
    machine_score = 0
    user_score = 0
    round = 1

    second_window = Toplevel()
    second_window.title("Rock Paper Scissor Game")
    second_window.geometry("780x460")
    second_window.config(background='#5468A1')
    second_window.minsize(480,360)
    second_window.iconbitmap("P24_pierre_feuille_ciseaux.ico")


    second_frame = Frame(second_window, bg='#5468A1', bd=1, relief=SUNKEN)
    second_frame.pack(fill=BOTH, expand=True)


    second_scrollbar = Scrollbar(second_frame)
    second_scrollbar.pack(side=RIGHT, fill=Y)


    print_label = Label(second_frame, text="Welcome in the Rock Paper Scissor Game Menu", font=("Helvetica", 20), bg='#5468A1', fg='White')
    welcome_label.pack(expand=YES)


    while True :
        mach_rand = randint(1,3)
        if mach_rand == 1 :
            mach_choice = "Rock"

        elif mach_rand == 2 :
            mach_choice = "Paper"

        elif mach_rand == 3 :
            mach_choice = "Scissor"

        print_label = Label(second_frame, text=("\n","-"*40,f"Round {round}","-"*40), font=("Helvetica", 20), bg='#5468A1', fg='White')
        print_label.pack(expand=YES)

        for x,rps_rand in rps_random.items() :
            print_label = Label(second_frame, text=(f"\n\t{x} -{rps_rand}"), font=("Helvetica", 20), bg='#5468A1', fg='White')
            print_label.pack(expand=YES)


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




principal_window = Tk()
principal_window.title("Rock Paper Scissor Game")
principal_window.geometry("780x460")
principal_window.config(background='#5468A1')
principal_window.minsize(480,360)
principal_window.iconbitmap("P24_pierre_feuille_ciseaux.ico")


principal_frame = Frame(principal_window, bg='#5468A1', bd=1, relief=SUNKEN)
principal_frame.pack(expand=YES)


welcome_label = Label(principal_frame, text="Welcome in the Rock Paper Scissor Game Menu", font=("Helvetica", 20), bg='#5468A1', fg='White')
welcome_label.pack(expand=YES)


welcome_label = Label(principal_frame, text="Pick a Choice", font=("Helvetica", 15), bg='#5468A1', fg='White')
welcome_label.pack(expand=YES)


play_button = Button(principal_frame, text="Play the Game", font=("Arial", 15), bg='White', fg='#5468A1', command=play_rps)
play_button.pack(side=LEFT, padx=20)


leave_button = Button(principal_frame, text="Leave", font=("Arial", 15), bg='White', fg='#5468A1', command=exit)
leave_button.pack(side=RIGHT, padx=20)





principal_window.mainloop()
