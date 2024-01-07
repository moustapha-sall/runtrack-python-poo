class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque: {self.marque}\nModèle: {self.modele}\nAnnée: {self.annee}\nPrix: {self.prix}")

    def demarrer(self):
        print("Attention, je roule")


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes: {self.portes}")


class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roues=2):
        super().__init__(marque, modele, annee, prix)
        self.roues = roues

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues: {self.roues}")

    def demarrer(self):
        print("Vroum vroum, je démarre !")


# Instanciation d'un objet Voiture
voiture = Voiture(marque="Toyota", modele="Corolla", annee=2022, prix=25000)

# Appel à la méthode informationsVehicule de la classe Voiture
voiture.informationsVehicule()

# Démarrage de la voiture
voiture.demarrer()

# Espacement entre les résultats
print("\n" + "=" * 40 + "\n")

# Instanciation d'un objet Moto
moto = Moto(marque="Harley-Davidson", modele="Sportster", annee=2022, prix=12000)

# Appel à la méthode informationsVehicule de la classe Moto
moto.informationsVehicule()

# Démarrage de la moto
moto.demarrer()
