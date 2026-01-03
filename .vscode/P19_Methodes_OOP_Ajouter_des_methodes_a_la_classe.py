from colorama import Fore,Style,init
init(autoreset=True)

# P19: Methodes OOP Ajouter des methodes a la classe

# Class Personne
class Person :
    def __init__(self, name, Last_name, Age, O_city, A_city):
        self.name = name
        self.Last_name = Last_name
        self.Age = Age
        self.O_city = O_city
        self.A_city = A_city

    def Presentation(self) :
        print(f"\nMy Full Name is {self.name} {self.Last_name}, I'm {self.Age}")

    def aniversary(self) :
        ani_age = self.Age + 1
        print(f"\nYou have {self.Age}, You will have {ani_age} at your next aniversary")

    def moving(self) :
        print(f"\nMy Origine City is {self.O_city} bur I moving to my Actual City {self.A_city}")

# La Liste Contennant Tout les Informations de toutes les personnes !
per__list = []

# Fonction Permettant D'ajouter des Personnes a la Liste
def add_person(): 
    while True:
        try :
            w_per = int(input("\nWhich Persons Will you add/create?: "))
            if w_per <= 0 :
                raise ValueError
        except ValueError:
            print(f"\n{Fore.RED}ERROR: Enter Integer > 0")
            continue

        if w_per:
            per = 1
            for i in range(w_per) :
                print(f"\n\t***** Person {per} *****")
                user_name = input("Name: ")
                userLast_name = input("Last Name: ")

                while True:
                    try :
                        user_Age = int(input("Age: "))
                        if user_Age <= 0 :
                            raise ValueError
                    except ValueError:
                        print(f"\n{Fore.RED}ERROR: Enter Integer > 0 !!")
                        continue

                    if user_Age :
                        break
            
                userO_city = input("Origine City: ")
                userA_city = input("Actual City: ")
                p = Person(user_name, userLast_name, user_Age, userO_city, userA_city)
                per__list.append(p)
                per += 1

        oop_met_menu()


# Fonction permettant D'afficer Toutes les personnes présente dans la liste si il y en a !
def print_all_person() :
    per = 1
    if per__list:
        for p in per__list:
            print(f"\n\n\t***** Person {per} *****")
            p.Presentation()
            p.moving()
            p.aniversary()
            per += 1
    
    else :
        print(f"\nTHe List is Empty, Enter a Person First !!!\n")

    oop_met_menu()

# Fonction permettant de Nettoyer toute le liste !
def clear_persons():
    per__list.clear()
    print(f"\n\t{Fore.RED}The list is Deleted !!!\n")
    oop_met_menu()

# Fonction menu permettant le Choix de l'action de l'utilisateur !!
def oop_met_menu():
    menu_dict = {1: f"Add persons", 2: f"Print All Persons", 3: f"Delete All Persons", 4: f"Leave The Menu"}
    while True:
        print("\n","*"*60)
        print("===== Welcome in the oop met menu =====")
        for i,omm in menu_dict.items():
            print(f"{i} -{omm}")

        try : 
            user_omc = int(input("\nChoose any Proposition: "))
            if user_omc not in menu_dict :
                raise ValueError
        except ValueError:
            print(f"\n{Fore.RED}ERROR: Invalid Choice !!")
            continue

        if user_omc == 1 :
            add_person()
            break

        elif user_omc == 2 :
            print_all_person()
            break

        elif user_omc == 3 :
            clear_persons()
            break

        elif user_omc == 4 :
            print("\nGoodbye guy !!")
            continue

if __name__ == '__main__' :
    oop_met_menu()

