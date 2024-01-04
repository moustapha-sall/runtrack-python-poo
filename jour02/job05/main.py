class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50  # Attribut privé réservoir, initialisé à 50 par défaut

    # Assesseurs (getters)
    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee

    def get_kilometrage(self):
        return self.__kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def get_reservoir(self):
        return self.__reservoir

    # Mutateurs (setters)
    def set_marque(self, marque):
        self.__marque = marque

    def set_modele(self, modele):
        self.__modele = modele

    def set_annee(self, annee):
        self.__annee = annee

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def set_en_marche(self, en_marche):
        self.__en_marche = en_marche

    def set_reservoir(self, reservoir):
        self.__reservoir = reservoir

    # Méthode privée pour vérifier le niveau du réservoir
    def __verifier_plein(self):
        return self.__reservoir

    # Méthode pour démarrer la voiture
    def demarrer(self):
        niveau_reservoir = self.__verifier_plein()
        if niveau_reservoir > 5:
            self.__en_marche = True
            print("La voiture a démarré avec succès.")
        else:
            print("Erreur : Le réservoir est trop bas, la voiture ne peut pas démarrer.")

    # Méthode pour arrêter la voiture
    def arreter(self):
        self.__en_marche = False
        print("La voiture s'est arrêtée.")

# Exemple d'utilisation de la classe Voiture
ma_voiture = Voiture("Audi", "Camry", 2018, 30000)

# Affichage des informations initiales
print("Marque :", ma_voiture.get_marque())
print("Modèle :", ma_voiture.get_modele())
print("Année :", ma_voiture.get_annee())
print("Kilométrage :", ma_voiture.get_kilometrage())
print("En marche :", ma_voiture.get_en_marche())
print("Réservoir :", ma_voiture.get_reservoir())

# Démarrage de la voiture (le réservoir est suffisant)
ma_voiture.demarrer()

# Arrêt de la voiture
ma_voiture.arreter()

# Tentative de démarrage avec un faible niveau de réservoir (ne devrait pas démarrer)
ma_voiture.set_reservoir(3)
ma_voiture.demarrer()
