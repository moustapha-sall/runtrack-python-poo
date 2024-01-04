class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = True

    # Assesseurs (getters)
    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nb_pages(self):
        return self.__nb_pages

    def get_disponible(self):
        return self.__disponible

    # Mutateurs (setters)
    def set_titre(self, titre):
        self.__titre = titre

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def set_nb_pages(self, nb_pages):
        # Vérification que nb_pages est un nombre entier positif
        if isinstance(nb_pages, int) and nb_pages > 0:
            self.__nb_pages = nb_pages
        else:
            print("Erreur : Le nombre de pages doit être un nombre entier positif.")

    # Méthode pour vérifier si le livre est disponible
    def verification(self):
        return self.__disponible

    # Méthode pour emprunter le livre
    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print("Le livre a été emprunté avec succès.")
        else:
            print("Le livre n'est pas disponible pour l'emprunt.")

    # Méthode pour rendre le livre
    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print("Le livre a été rendu avec succès.")
        else:
            print("Le livre est déjà disponible.")

# Exemple d'utilisation
mon_livre = Livre("Titre du livre", "Auteur du livre", 200)

# Vérification de la disponibilité initiale du livre
print("Le livre est disponible :", mon_livre.verification())

# Emprunt du livre
mon_livre.emprunter()

# Tentative de réemprunter le livre (ne devrait pas être possible)
mon_livre.emprunter()

# Rendre le livre
mon_livre.rendre()

# Tentative de rendre le livre à nouveau (ne devrait pas être possible)
mon_livre.rendre()
