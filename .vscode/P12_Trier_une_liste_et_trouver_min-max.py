from colorama import Fore,init,Style
init(autoreset=True)

# P12: trie d'une liste pour trouver le max

numbers_list = []
def Ordered_choice():
    sort_dict = {1: f"{Fore.GREEN}Ascending Order", 2: f"{Fore.BLUE}Descending Order", 3: f"{Fore.MAGENTA}All Sort Order", 4: "Leave"}
    
    while True:
        print("\n\n\n","*"*60)
        print("===== Welcome in the Sort Order Choice =====")
        try :
            which_time = int(input(f"\n{Fore.CYAN}Which value will you enter?: "))
        except ValueError:
            print(f"\n{Fore.RED}ERROR: Please Enter a Integer !!")
            continue

        for i in range(which_time) :
            while True :
                try :
                    values = float(input(f"\n{Fore.CYAN}Enter Your Values: "))
                except ValueError :
                    print(f"\n{Fore.RED}ERROR: Enter numeric Value !")
                    continue

                numbers_list.append(values)

                if values:
                    break

        for i,sort_choice in sort_dict.items() :
            print(f"{i} -{sort_choice}")

        while True:
            try :
                user_sort_choice = int(input(f"\n{Fore.CYAN}Enter your Sort Order Choice here: "))
                if user_sort_choice not in sort_dict :
                    raise ValueError 
            except ValueError :
                print(f"\n{Fore.RED}ERROR: Your Choice is'nt in the list !!")
                continue
            
            if user_sort_choice :
                break

        if user_sort_choice == 1 :
            Ascending_Order()


        elif user_sort_choice == 2 :
            Descending_Order()
            

        elif user_sort_choice == 3 :
            All_Sort_Order()
           
           
        elif user_sort_choice == 4 : 
            print(f"\n{Fore.CYAN}Goodbye and look forward !!")
            break

    


def Ascending_Order():
    print("\n","-"*60)
    print(f"\n===== Welcome in the {Fore.GREEN}Ascending Order{Style.RESET_ALL} =====")
    Ascend = sorted(numbers_list)
    print(f"\n{Fore.GREEN}The Ascend Order is:{Style.RESET_ALL} {Ascend}")

    


def Descending_Order():
    print("\n","-"*60)
    print(f"\n===== Welcome in the {Fore.BLUE}Descending Order{Style.RESET_ALL} =====")
    Descend = sorted(numbers_list, reverse=True)
    print(f"\n{Fore.BLUE}The Descending Order is:{Style.RESET_ALL} {Descend}")




def All_Sort_Order():
    Ascending_Order()

    Descending_Order()



def sort_menu():
    sort_dict = {1: "Ordered your numbers", 2: "Leave"}
    while True:
        print("\n","*"*60)
        print("===== Welcome in the Sort Menu Choice =====")
        for i,sort in sort_dict.items() :
            print(f"{i} -{sort}")

        try :
            sort_choice = int(input(f"\n{Fore.CYAN}Which Sort do you choose: "))
            if sort_choice not in sort_dict :
                raise ValueError
        except ValueError:
            print(f"\n{Fore.RED}ERROR: Pick your choice in the list !!")
            continue

        if sort_choice == 1 :
            Ordered_choice()
            break

        elif sort_choice == 2 :
            print(f"\n{Fore.CYAN}Goodbye and look Forward !!")
            break

if __name__ == '__main__' :
    sort_menu()

