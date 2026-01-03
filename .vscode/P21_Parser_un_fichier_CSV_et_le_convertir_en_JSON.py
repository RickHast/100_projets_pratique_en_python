from colorama import Fore,Style,init
init(autoreset=True)
import os
import json
import csv
import time

# P21_Parser_un_fichier_CSV_et_le_convertir_en_JSON

def csv_json() :
    csv_file_name = "etudiants.csv"
    if os.path.exists(csv_file_name) :
        enc_print = f"Convertion En Cours......."
        for i in enc_print :
            print(i, end="",flush=True)
            time.sleep(0.1)

        with open(csv_file_name, "r") as f :
            reader = csv.reader(f)
            data = []
            next(reader)
            for row in reader :
                if len(row) > 0 :
                    data.append(
                        {
                            "Nom": row[0],
                            "Age": row[1],
                            "Ville": row[2],
                            "Note": row[3]
                        }
                    )

        with open("etudiants.json", "w") as j :
            json.dump(data, j, indent=4, ensure_ascii=False)

        print(f"\n\n\tConvertion du Fichier CSV en Fichier JSON Terminé !!\n")

    else :
        print(f"\n\n\tVotre Fichier {csv_file_name} N'existe pas !!!\n")
        csv_json_menu()

def csv_json_menu() :
    csv_json_dict = {1: "Convertir un Ficher CSV en JSON", 2: "Quitter"}
    while True:
        print("\n","*"*60)
        print("===== Bienvenue dans le menu de choix de convertion d'un fichier CSV =====")
        for i,cj in csv_json_dict.items() :
            print(f"{i} -{cj}")

        try : 
            user_cjc = int(input("\nEntrez votre Choix ici: "))
            if user_cjc not in csv_json_dict :
                raise ValueError
        except ValueError:
            print(f"\nERREUR: Votre choix ne figure pas dans la liste ci-dessus !!")
            continue

        if user_cjc == 1 :
            csv_json()
            break

        elif user_cjc == 2 :
            print("\nAu Revoir at a bientot !!\n\n")
            break

if __name__ == '__main__' :
    csv_json_menu()