class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom

# Instanciation de la classe Animal
mon_animal = Animal()

# Affichage de l'âge initial de l'animal
print(f"Âge initial de l'animal : {mon_animal.age}")

# Vieillissement de l'animal
mon_animal.vieillir()

# Affichage de l'âge après vieillissement
print(f"Âge après vieillissement : {mon_animal.age}")

# Nommer l'animal
mon_animal.nommer("Luna")

# Affichage du nom de l'animal
print(f"L'animal se nomme {mon_animal.prenom}")
