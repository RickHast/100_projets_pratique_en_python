#P21: Heritage oop

# Simulateur de ville
# Créer 3 Classes: Supermarché, Banque, Immeuble
# Superclasse: Batiment
# 4: Immeubles, 2: supermarché, 1: banque

class Batiment:
    def __init__(self, nb_etage, adresse):
        self.etage = nb_etage
        self.adresse = adresse

    def nb_etage(self) :
        return self.etage

    def adresse(self) :
        return self.etage


class Immeuble(Batiment) :
    def __init__(self, nb_etage, adresse):
        super().__init__(nb_etage, adresse)

    def nb_de_chambre(self, nb_chambre) :
        nb




