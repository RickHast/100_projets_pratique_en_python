from tkinter import *
from P13_Jeux_du_Pierre_feuille_ciseaux import *
def rps_game():
    pass

    



# Nous devons créer une Frame dans laquelle l'on va placer nos éléments pour pouvoir bien les positionner comme on le souhaite


# créer la fenetre
window = Tk()

# personaliser cette fenetre
#**le titre de la fenetre
window.title("Rock-Paper-Scissor Game")


#**les dimensions de cette fenetre (longeur,largeur)
window.geometry("740x480")


#** Taille minimum de la fenetre
window.minsize(480, 360)


#** Le logo de la fenetre
    #**convertir l'image d'abord en image.ico
window.iconbitmap("P24_pierre_feuille_ciseaux.ico")


#** changer la couleur de fond de la fenetre
window.config(background='#5468A1')



#** Créer la frame
    #pour voir la frame on peut lui donner des argument , bd = 1 (pour la bordure); relief = SUNKEN (pour changer le relief de la frame pour quelle soit plus visible )
frame = Frame(window, bg='#5468A1')


#Ajoueter un premier texte
    #foreground (Couleur du texte); pour le '.pack()' on peut ajouter une ou plusieurs paramètres tels que: 'side' EX: (side = LEFT; side = BOTTOM); EXPEND = YES (qui placera toujour notre texte au milieu qu'importe comment l'on dimensionne la fenetre)
label_title = Label(frame, text="Welcome in the Rock-Paper-Scissor Game Application", font=("Helvetica", 20), bg='#5468A1',foreground="White")
label_title.pack(expand=YES)



#Ajoueter un second texte
    #foreground (Couleur du texte); pour le '.pack()' on peut ajouter une ou plusieurs paramètres tels que: 'side' EX: (side = LEFT; side = BOTTOM); EXPEND = YES (qui placera toujour notre texte au milieu qu'importe comment l'on dimensionne la fenetre)
label_subtitle = Label(frame, text="Hey les gars", font=("Arial", 15), bg='#5468A1',foreground="White")
label_subtitle.pack(expand=YES)


# Ajouter un premier boutton 
play_button = Button(frame, text="Play Game", font=("Arial", 15), bg='White',foreground="#5468A1")
play_button.pack(pady=25, fill=X)

#** Afficher la frame
frame.pack(expand=YES)



# afficher la fenetre
window.mainloop()