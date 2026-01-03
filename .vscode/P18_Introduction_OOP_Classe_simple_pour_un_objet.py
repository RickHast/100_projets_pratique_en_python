
# P18_Introduction_OOP_Classe_simple_pour_un_objet

class person:
    def __init__(self, first_name, Last_name, age, city):
        self.first_name = first_name
        self.last_name = Last_name
        self.age = age 
        self.city = city

    def se_presenter(self) :
        print(f"My name is {self.first_name} {self.last_name}, I'm {self.age} and I'm live in {self.city} !!")

p_list = []
def Create_Person() :
    while True:
        try:
            w_persons = int(input("Which Persons do you want to Create?: "))
            if w_persons <= 0 :
                raise ValueError
        except ValueError:
            print("ERROR: Enter integer > 0 !!")

        if w_persons:
            per = 1
            for i in range(w_persons) :
                print(f"\n\n\t***** Person {per} *****")
                userf_name = input("First name: ")
                userl_name = input("Last name: ")

                while True:
                    try:    
                        user_age = int(input("Age: "))
                    except ValueError:
                        print("ERROR: The Age Isn't a numeric value !!")
                        continue
                    
                    if user_age:
                        break

                user_city = input("City: ")
                per += 1
                p = person(userf_name, userl_name, user_age, user_city)
                p_list.append(p)

            poo_menu()
             
def print_all_persons() :
    if p_list:
        for p in p_list:
            p.se_presenter()
    
    else :
        print("Your List is Empty, add Person First !!!")
        poo_menu()
        



def poo_menu() :
    poo_dict = {1: "Create a Person", 2: "Print All Persons", 3: "Leave"}
    while True:
        print("\n","*"*60)
        print("==== Welcome in the Persons Informations menu ====")
        for i,poo in poo_dict.items() :
            print(f"{i} -{poo}")

        try :
            user_pooc = int(input("Put any option here: "))
            if user_pooc not in poo_dict:
                raise ValueError
        except ValueError:
            print(f"ERROR: Your Value isn't in the list from the top !!")

        if user_pooc == 1 :
            Create_Person()
            break

        elif user_pooc == 2 :
            print_all_persons()
            break

        elif user_pooc == 3 :
            print("Goodbye !")
            break

if __name__ == '__main__' :
    poo_menu()
