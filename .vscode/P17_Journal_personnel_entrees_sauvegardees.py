from colorama import Fore,Style,init
import os
from datetime import datetime
import time
init(autoreset=True)
Jornal = "Journal.txt"

# P17: Journal Personnel entrées sauvegardes

def add_Write() :
    aw_dict = {1: f"{Fore.GREEN}Yes", 2: f"{Fore.RED}No"}
    while True:
        print("\n","_"*60)
        print(f"\nDo you want to {Fore.BLUE}WRITE{Style.RESET_ALL} in the Newspaper?")
        for i,aw in aw_dict.items() :
            print(f"{i} -{aw}")

        try : 
            user_wc = int(input("\nEnter Your Choice here: "))
            if user_wc not in aw_dict :
                raise ValueError
        except ValueError:
            print(f"\n{Fore.RED}ERROR: You didn't Enter 1 or 2 !!")
            continue

        if user_wc == 1 :
            while True:
                try :
                    write_time = int(input("\nHow many times will you Write: "))
                except ValueError:
                    print(f"\n{Fore.RED}ERROR: You didn't enter an Integer !")
                    continue

                if write_time :
                    break

            with open(Jornal, "a") as f :
                for x in range(write_time) :
                    date_ = datetime.now().strftime("\n%d/%m/%Y à %H:%M")
                    f.write(date_)
                    f.write("\n")
                    user_write = input("\nWrite Here: ")
                    f.write(user_write)

        elif user_wc == 2 :
            personal_newspapper_menu()
            return


def read() :
    r_dict = {1: f"{Fore.GREEN}Yes", 2: f"{Fore.RED}No"}
    while True:
        print("\n","_"*60)
        print(f"\nDo you want to {Fore.YELLOW}READ{Style.RESET_ALL} the Newspaper?")
        for i,r in r_dict.items() :
            print(f"{i} -{r}")

        try : 
            user_rc = int(input("\nEnter Your Choice here: "))
            if user_rc not in r_dict :
                raise ValueError
        except ValueError:
            print(f"\n{Fore.RED}ERROR: You didn't Enter 1 or 2 !!")
            continue

        if user_rc == 1 :
            if os.path.exists(Jornal) :
                print(f"\nYour Newspaper always Exist !!")
                with open(Jornal, "r") as f :
                    aff = f.read()
                    for u in aff :
                        print(u,end="",flush=True)
                        time.sleep(0.05)
                    

            else :
                print(f"\nYour Newspaper Don't Exist, Write Evrything First !!\n")
                while True :
                    print(f"\nDo you want to Write First ?")
                    for k,l in r_dict.items() :
                        print(f"{k} -{l}")

                    try:
                        dy_w = int(input("\nPut your Choice here bro: "))
                        if dy_w not in r_dict :
                            raise ValueError
                    except ValueError:
                        print(f"\n{Fore.RED}ERROR: Choose the options from the top !!")
                        continue
                    
                    if dy_w == 1 :
                        add_Write()
                        break
                
                    elif dy_w == 2 :
                        personal_newspapper_menu()
                        break

        elif user_rc == 2 :
            personal_newspapper_menu()
            return
        

def delete() :
    d_dict = {1: f"{Fore.RED}Yes", 2: f"{Fore.GREEN}No"}
    while True:
        print("\n","_"*60)
        print(f"\n\tDo you want to {Fore.MAGENTA}DELETE{Style.RESET_ALL} the Newspaper?")
        for i,d in d_dict.items() :
            print(f"{i} -{d}")

        try : 
            user_dc = int(input("\nEnter Your Choice here: "))
            if user_dc not in d_dict :
                raise ValueError
        except ValueError:
            print(f"\n{Fore.RED}ERROR: You didn't Enter 1 or 2 !!")
            continue

        if user_dc == 1 : 
            with open(Jornal, "w") as f :
                print(f"\n\t{Fore.RED}You Delete Your Newspaper !!!\n")

        elif user_dc == 2 :
            personal_newspapper_menu()
            return



def personal_newspapper_menu() :
    pn_dict = {1: f"{Fore.BLUE}Add Elements/Write in the NewsPaper", 2: f"{Fore.YELLOW}read The Newspaper", 3: f"{Fore.MAGENTA}Delete The Newspaper", 4: f"{Fore.RED}Leave the Menu"}
    while True:
        print("\n","*"*60)
        print("===== Welcome in the Personal Newspaper Menu =====")
        for i,pn in pn_dict.items() :
            print(f"{i} -{pn}")

        try :
            user_pn = int(input("\nEnter Your Choice here: "))
            if user_pn not in pn_dict :
                raise ValueError
        except ValueError:
            print(f"\n{Fore.RED}ERROR: Your Choice isn't good !!")
            continue

        if user_pn == 1 :
            add_Write()
            break   

        elif user_pn == 2 :
            read()
            break

        elif user_pn == 3 :
            delete()
            break

        elif user_pn == 4 :
            print("Good Bye !!!")
            break


if __name__ == '__main__' :
    personal_newspapper_menu()
