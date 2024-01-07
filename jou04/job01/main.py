class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(f"L'âge de la personne est : {self.age}")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.age} ans")


class Professeur(Personne):
    def __init__(self, matiereEnseignee, age=14):
        super().__init__(age)
        self.matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")


# Instanciation d'une personne et d'un élève
personne = Personne()
eleve = Eleve()

# Affichage de l'âge par défaut de l'élève
eleve.afficherAge()