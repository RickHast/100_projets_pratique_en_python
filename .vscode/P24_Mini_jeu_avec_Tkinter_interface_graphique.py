from tkinter import *
from P13_Jeux_du_Pierre_feuille_ciseaux import *

# Fenetre Principale

Window = Tk()
Window.title("Rock-Paper-Scissor Game")
Window.geometry("780x460")
Window.config(background='#5468A1')
Window.iconbitmap("P24_pierre_feuille_ciseaux.ico")
Window.minsize(480,360)

frame = Frame(Window, bg='#5468A1', bd=1, relief=SUNKEN)

Label_texte = Label(frame, text="Welcome in the Rock Paper Scissor Game Menu", font = ("Helvetica", 20), bg = '#5468A1', foreground = "White")
Label_texte.pack(expand=YES)

Label_pick = Label(frame, text="\nPick a Choice", font = ("Helvetica", 20), bg = '#5468A1', foreground = "White")
Label_pick.pack(expand=YES)

play_button = Button(frame, text="Play the Game", font = ("Arial", 15), bg = 'White', foreground = "#5468A1",command=Play_rps)
play_button.pack(padx= 20, side=LEFT)


leave_button = Button(frame, text="Leave the Game", font = ("Arial", 15), bg = 'White', foreground = "#5468A1",command=exit)
leave_button.pack(padx= 20, side=RIGHT)

# Affichage de la frame
frame.pack(expand=YES)


# fonction pour le jeux de piere feuille ciseaux
def Play_rps():
    rps_random = {1: f"{Fore.LIGHTBLACK_EX}Rock", 2: f"{Fore.WHITE}Paper", 3: f"{Fore.YELLOW}Scissor"}
    machine_score = 0
    user_score = 0
    round = 1
    game_Window = Tk()
    game_Window.title("Rock-Paper-Scissor Game")
    game_Window.geometry("780x460")
    game_Window.config(background='#5468A1')
    game_Window.iconbitmap("P24_pierre_feuille_ciseaux.ico")
    game_Window.minsize(480,360)


    game_frame = Frame(game_Window, bg='#5468A1')
    game_frame.pack(expand=YES)
    while True :
        mach_rand = randint(1,3)
        if mach_rand == 1 :
            mach_choice = "Rock"

        elif mach_rand == 2 :
            mach_choice = "Paper"

        elif mach_rand == 3 :
            mach_choice = "Scissor"


        Label_round = Label(game_frame, text=("\n","-"*40,f"Round {round}","-"*40), font = ("Helvetica", 20), bg = '#5468A1', foreground = "White")
        Label_round.pack(expand=YES)
        for x,rps_rand in rps_random.items() :
            Label_round = Label(game_frame, text=(f"\n\t{x} -{rps_rand}"), font = ("Helvetica", 20), bg = '#5468A1', foreground = "White")
            Label_round.pack(expand=YES)

            
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

    
    game_Window.mainloop()


# Affichage de la fenetre
Window.mainloop()

