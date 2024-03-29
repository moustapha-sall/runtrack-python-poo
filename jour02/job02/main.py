class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages

    # Assesseurs (getters)
    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nb_pages(self):
        return self.__nb_pages

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

# Création d'un livre avec des valeurs initiales
mon_livre = Livre("Titre du livre", "Auteur du livre", 200)

# Affichage des valeurs initiales
print("Titre :", mon_livre.get_titre())
print("Auteur :", mon_livre.get_auteur())
print("Nombre de pages :", mon_livre.get_nb_pages())

# Modification des valeurs avec vérification pour le nombre de pages
mon_livre.set_titre("Nouveau titre du livre")
mon_livre.set_auteur("Nouvel auteur du livre")
mon_livre.set_nb_pages(300)  # Modification avec un nombre de pages valide
mon_livre.set_nb_pages(-50)  # Tentative de modification avec un nombre de pages invalide

# Affichage des valeurs modifiées
print("Nouveau titre :", mon_livre.get_titre())
print("Nouvel auteur :", mon_livre.get_auteur())
print("Nouveau nombre de pages :", mon_livre.get_nb_pages())
