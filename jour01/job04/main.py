class Personne:
    def __init__(self, nom="", prenom=""):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Je suis {self.nom} {self.prenom}"

# Instanciation de plusieurs personnes avec des valeurs de construction
personne1 = Personne("John", "Doe")
personne2 = Personne("Jean", "Dupont")

# Appel de la méthode SePresenter pour chaque personne
print(personne1.SePresenter())
print(personne2.SePresenter())

