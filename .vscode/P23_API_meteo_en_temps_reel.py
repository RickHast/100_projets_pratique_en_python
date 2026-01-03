import requests
from colorama import Fore,Style,init
init(autoreset=True)

# P23_API_meteo_en_temps_reel


ma_cle_api = "31e93e9a84392bd5bece54e4da44191e"
def meteo(city) :
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={ma_cle_api}&units=metric&lang=fr"
    response = requests.get(url)
    
    if response.status_code == 200 :
        data_meteo = response.json()
        
        print(f"\n\t----- {Fore.MAGENTA}Affichage de la météo{Style.RESET_ALL} -----\n")
        print(f"City Name:  {data_meteo["name"]}\n")
        print(f"Longitude:  {data_meteo["coord"]["lon"]}\n")
        print(f"Latitude:   {data_meteo["coord"]["lat"]}\n")
        print(f"Description:  {data_meteo["weather"][0]["description"]}\n")
        print(f"Humidity:   {data_meteo["main"]["humidity"]}\n")
        print(f"Dregrees:   {data_meteo["wind"]["deg"]}°C \n\n\n\n")

        meteo_menu()

    else:
        print(f"\n\t{Fore.RED}The URL is not working !!\n\n\n\n\n")
        


def meteo_menu() :
    mm_dict = {1: f"{Fore.MAGENTA}Météo Data", 2: f"{Fore.RED}Leave"}
    while True:
        print("\n","*"*60)
        print("===== Welcome In the Météo Menu =====")
        for i, m in mm_dict.items() :
            print(f"{i} -{m}")

        try :
            user_mc = int(input("\nEnter Your Decision: "))
            if user_mc not  in mm_dict :
                raise ValueError
        except ValueError:
            print(f"\n{Fore.RED}ERROR: Enter integer in the list from the top !!!")
            continue

        if user_mc == 1 :
            while True:
                city_name = input("\nEnter a City name: ").capitalize()

                if city_name :
                    break

                
            meteo(city_name)
            break

        elif user_mc == 2 :
            print(f"{Fore.GREEN}Goodbye !!\n\n")
            break


if __name__ == '__main__' :
    meteo_menu()