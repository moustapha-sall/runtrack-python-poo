
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

# Création d'un élève
eleve = Eleve()

# Dire bonjour à l'élève
eleve.bonjour()

# Aller en cours
eleve.allerEnCours()

# Redéfinir l'âge de l'élève à 15 ans
eleve.modifierAge(15)
eleve.afficherAge()

# Création d'un professeur
professeur = Professeur(matiereEnseignee="Mathématiques", age=40)

# Dire bonjour au professeur
professeur.bonjour()

# Commencer le cours grâce à la méthode enseigner
professeur.enseigner()
