from colorama import Fore,Style,init
init(autoreset=True)
from random import randint, choice
import time

# P21:Heritage oop

class car :
    def __init__(self, mark, model, color, fabrication_year, actual_speed):
        self.mark = mark
        self.model = model
        self.color = color
        self.fab_year = fabrication_year
        self.act_speed = actual_speed
    
    def car_presentation(self) :
        print_car =f"{self.color} {self.mark} model{self.model}, fabrication year: {self.fab_year}, actual speed: {self.act_speed}"
        for i in print_car :
            print(i, end="",flush=True)
            time.sleep(0.2,0.05)

class camion(car) :
    def __init__(self, mark, model, color, fabrication_year, actual_speed):
        super().__init__(mark, model, color, fabrication_year, actual_speed)

    def weigth(self, weigths):
        self.weigths = weigths
        

car_list = []
def create_car():
    while True:
        try :
            user_cars = int(input("\nHow Many Cars Will You want to create: "))
        except ValueError:
            print("\nERROR: Your Value isn't a Integer !!")
            continue

        if user_cars:
            cars = 1
            for i in range(user_cars) :
                print(f"\n\t***** Car N°{cars} *****")
                car_mark = input("Car Mark: ")
                car_model = input("Car Type: ")
                car_color = input("Car Color: ")
                car_fabrication_year = input("Car fabrication_year: ")
                while True:
                    try :
                        car_actual_speed = int(input("Car Actual Speed: "))
                        if car_actual_speed <= 0:
                            raise ValueError
                    except ValueError:
                        print("\nInvalid Input!!\n")
                        continue

                    if car_actual_speed:
                        break

                c = car(car_mark, car_model, car_color, car_color, car_fabrication_year, car_actual_speed)
                car_list.append(c)
                cars += 1
            
            oop_car_menu()

def print_car():
    nub_car = 1
    for c in car_list:
        print(f"\n\t----- car N°{nub_car} Présentation -----")
        c.car_presentation()

    oop_car_menu()

def accelerate_car():
    rand_acc = randint(10, 70)
    print_rand = f"\nAll Car Recieve {rand_acc} m/s Accelerate Speed"
    for i in print_rand :
        print(i, end="", flush=True)
        time.sleep(0.2, 0.04) 

    oop_car_menu()


def Car_honk():
    honk_list = ["tut tut", "Bip Bip", "Nip Nip", "Tboum Tboum"]
    choi_honk = choice(honk_list)
    print_honk = f"\nCar Honk is '{choi_honk}' 🎺"
    for i in print_honk :
        print(i, end="", flush=True)
        time.sleep(0.2, 0.04) 

    oop_car_menu()



def oop_car_menu() :
    ocm_dict = {1: "Create a New car", 2: "Print All Cars", 3: "Accelerate a Car", 4: "Honk with a car", 5: "Leave"}
    while True:
        print("\n","*"*60)
        print("===== Welcome in the Car OOP manu =====")
        for i, ocm in ocm_dict.items():
            print(f"{i} -{ocm}")

        try : 
            user_ocmc = int(input("\nEnter Your Choice here: "))
            if user_ocmc not in ocm_dict :
                raise ValueError
        except ValueError:
            print(f"\nERROR: Enter a Figure who is in the list from the top !!")
            continue

        if user_ocmc == 1 :
            create_car()
            break 

        elif user_ocmc == 2 :
            print_car()
            break 

        elif user_ocmc == 3 :
            accelerate_car()
            break 

        elif user_ocmc == 4 :
            Car_honk()
            break

        elif user_ocmc == 5 :
            print("\nGoodbye !!\n\n")
            break

if __name__ == '__main__' :
    oop_car_menu()