class Ville:
    def __init__(self, nom, nombre_habitants):
        self.__nom = nom
        self.__nombre_habitants = nombre_habitants

    def get_nom(self):
        return self.__nom

    def get_nombre_habitants(self):
        return self.__nombre_habitants

    def augmenter_population(self):
        self.__nombre_habitants += 1


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def ajouterPopulation(self):
        self.__ville.augmenter_population()


# Créer un objet Ville avec comme arguments “Paris” et 1000000.
paris = Ville("Paris", 1000000)
# Afficher en console le nombre d’habitants de la ville de Paris.
print(f"Nombre d'habitants à {paris.get_nom()}: {paris.get_nombre_habitants()}")

# Créer un autre objet Ville avec comme arguments “Marseille” et 861635.
marseille = Ville("Marseille", 861635)
# Afficher en console le nombre d’habitants de la ville de Marseille.
print(f"Nombre d'habitants à {marseille.get_nom()}: {marseille.get_nombre_habitants()}")

# Créer les objets suivants :
# - John, 45 ans, habitant à Paris
john = Personne("John", 45, paris)
john.ajouterPopulation()

# - Myrtille, 4 ans, habitant à Paris.
myrtille = Personne("Myrtille", 4, paris)
myrtille.ajouterPopulation()

# - Chloé, 18 ans, habitant à Marseille.
chloe = Personne("Chloé", 18, marseille)
chloe.ajouterPopulation()

# Afficher le nombre d’habitants de Paris et de Marseille après l’arrivée de ces nouvelles personnes.
print(f"Nombre d'habitants à {paris.get_nom()} après l'arrivée de nouvelles personnes: {paris.get_nombre_habitants()}")
print(f"Nombre d'habitants à {marseille.get_nom()} après l'arrivée de nouvelles personnes: {marseille.get_nombre_habitants()}")
