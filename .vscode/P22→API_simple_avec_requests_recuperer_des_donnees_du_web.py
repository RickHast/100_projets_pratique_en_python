import requests

# P22 Python → API simple avec requests (récupérer des données du web)

# url de base
base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name) :
    # url de la page
    url = f"{base_url}/pokemon/{name}"
    # requests.get(url) vérifie si l'url existe ou est fontionnelle et renvoie une valeur spécifique en fonction de son état
    response = requests.get(url)
    
    # si le résultat issue de la vérification est égale à 200
    if response.status_code == 200 :
        # respose.json() transforme les infos reçues en dictionnaires
        pokemon_data = response.json()
        # retourne les données sous forme de dictionnaire
        return pokemon_data 
    else:
        print(f"Failed to retrieve data {response.status_code}")


pokemon_name = "pikachu".lower()
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    need_info_list = ["name", "id", "height", "weight"]
    for i in need_info_list :
        print(f"\n{i}: {pokemon_info[i]}")
    
    print("\n\n")


# pour des Info sur la vérification de lien HTTP, consulter mdn(response status-code)