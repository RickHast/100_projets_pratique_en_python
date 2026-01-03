from colorama import Fore,Style,init
init(autoreset=True)

# P5: convertion  de Temperature
# Fonction qui permet de faire la convertion de celcius en une autre grandeur
def celcius():
    celcius_dict = {1: f"Convert to {Fore.YELLOW}Kelvin", 2: f"Convert to {Fore.GREEN}farenheit", 3: f"{Fore.MAGENTA}go back to the menu", 4: "Leave"}
    while True:
        print("\n","*"*60)
        print("===== Welcome in th celcius convertisseur =====")
        for i,cel_item in celcius_dict.items() :
            print(f"{i} -{cel_item}")

        try :
            cel_choice = int(input("\nIn which greatness will you convert: "))
            if cel_choice not in celcius_dict :
                raise ValueError
        except ValueError:
            print(f"\n{Fore.RED}ERROR: enter a integer")
            continue

        if cel_choice == 1 or cel_choice == 2 :   
            while True: 
                try :
                    cel_val = int(input("\nEnter the value in °C: "))
                except ValueError:
                    print(f"\n{Fore.RED}ERROR: enter a integer")
                    continue

                if cel_val :
                    break

        if cel_choice == 1 :
            cel_kel_for = (32*cel_val)+273.15
            aff = f"{Fore.YELLOW}{cel_kel_for}"
            sym = "°K"
        
        elif cel_choice == 2 :
            cel_fah_for = ((32*cel_val)*9/5)+32
            aff = f"{Fore.GREEN}{cel_fah_for}"
            sym = "°F"

        elif cel_choice == 3 :
            temperature_menu()
            break

        else:
            print(f"\n{Fore.CYAN}Bye !!")
            break

        print(f"\nYou Convert {Fore.BLUE}{cel_val}{Style.RESET_ALL}°C to {aff}{Style.RESET_ALL}{sym}")


# Fonction qui permet de faire la convertion de kelvin en une autre grandeur
def kelvin():
    kelvin_dict = {1: f"Convert to {Fore.BLUE}Celcius", 2: f"Convert to {Fore.GREEN}farenheit", 3: f"{Fore.MAGENTA}go back to the menu", 4: "Leave"}
    while True:
        print("\n","*"*60)
        print("===== Welcome in the Kelvin converter =====")
        for i,kel_item in kelvin_dict.items() :
            print(f"{i} -{kel_item}")

        try :
            kel_choice = int(input("\nIn which greatness will you convert: "))
            if kel_choice not in kelvin_dict :
                raise ValueError
        except ValueError:
            print(f"\n{Fore.RED}ERROR: enter a integer")
            continue

        if kel_choice == 1 or kel_choice == 2 :   
            while True: 
                try :
                    kel_val = int(input("\nEnter the value in °K: "))
                except ValueError:
                    print(f"\n{Fore.RED}ERROR: enter a integer")
                    continue

                if kel_val :
                    break

        if kel_choice == 1 :
            kel_cel_for = (32*kel_val)-273.15
            aff = f"{Fore.BLUE}{kel_cel_for}"
            sym = "°C"
        
        elif kel_choice == 2 :
            kel_fah_for = (((32*kel_val)-273.15)*9/5)+32
            aff = f"{Fore.GREEN}{kel_fah_for}"
            sym = "°F"

        elif kel_choice == 3 :
            temperature_menu()
            break

        else:
            print(f"\n{Fore.CYAN}Bye !!")
            break

        print(f"\nYou Convert {Fore.YELLOW}{kel_val}{Style.RESET_ALL}°K to {aff}{Style.RESET_ALL}{sym}")


# Fonction qui permet de faire la convertion de Fahrenheit en une autre grandeur
def fahrenheit():
    farenheit_dict = {1: f"Convert to {Fore.BLUE}Celcius", 2: f"Convert to {Fore.YELLOW}Kelvin", 3: f"{Fore.MAGENTA}go back to the menu", 4: "Leave"}
    while True:
        print("\n","*"*60)
        print("===== Welcome in the Fahrenheit converter =====")
        for i,fah_item in farenheit_dict.items() :
            print(f"{i} -{fah_item}")

        try :
            fah_choice = int(input("\nn which greatness will you convert: "))
            if fah_choice not in farenheit_dict :
                raise ValueError
        except ValueError:
            print(f"\n{Fore.RED}ERROR: enter a integer")
            continue

        if fah_choice == 1 or fah_choice == 2 :   
            while True: 
                try :
                    fah_val = int(input("\nEnter the value in °F: "))
                except ValueError:
                    print(f"\n{Fore.RED}ERROR: enter a integer")
                    continue

                if fah_val :
                    break

        if fah_choice == 1 :
            fah_cel_for = ((32*fah_val)-32)*5/9
            aff = f"{Fore.BLUE}{fah_cel_for}"
            sym = "°C"
        
        elif fah_choice == 2 :
            fah_kel_for = (((32*fah_val)-32)*5/9)+273.15
            aff = f"{Fore.YELLOW}{fah_kel_for}"
            sym = "°K"

        elif fah_choice == 3 :
            temperature_menu()
            break

        else:
            print(f"\n{Fore.CYAN}Bye !!")
            break

        print(f"\nYou Convert {Fore.GREEN}{fah_val}{Style.RESET_ALL}°K to {aff}{Style.RESET_ALL}{sym}")



# Fonction menu qui permet de faire le choix du convertisseur
def temperature_menu():
    convertisor_dict = {1: f"{Fore.BLUE}Celcius", 2: f"{Fore.YELLOW}Kelvin", 3: f"{Fore.GREEN}farenheit", 4: "Leave"}
    while True:
        print("\n","*"*60)
        print("===== Welcome int the Temperature converter menu ====")
        for i,x in convertisor_dict.items():
            print(f"{i} -{x}")

        try :
            choix_convertisor = int(input("\nEnter Your Converter Choice: "))
            if choix_convertisor not in convertisor_dict :
                raise ValueError
        except ValueError:
            print(f"\n{Fore.RED}ERROR: Enter a integer!!")
            continue

        if choix_convertisor == 1 :
            celcius()
            break

        elif choix_convertisor == 2 :
            kelvin()
            break

        elif choix_convertisor == 3 :
            fahrenheit()
            break

        else :
            print(f"\n{Fore.CYAN}Goodbye !!")
            break


if __name__ == '__main__':
    temperature_menu()




