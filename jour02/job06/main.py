class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}
        self.__statut_commande = "En cours"  # Statut initial

    # Méthode pour ajouter un plat à la commande
    def ajouter_plat(self, nom_plat, prix_plat):
        if nom_plat not in self.__plats_commandes:
            self.__plats_commandes[nom_plat] = {"prix": prix_plat, "statut": "En cours"}
            print(f"Plat '{nom_plat}' ajouté à la commande.")
        else:
            print(f"Le plat '{nom_plat}' est déjà dans la commande.")

    # Méthode pour annuler la commande
    def annuler_commande(self):
        self.__statut_commande = "Annulée"
        for plat in self.__plats_commandes:
            self.__plats_commandes[plat]["statut"] = "Annulé"
        print("La commande a été annulée.")

    # Méthode privée pour calculer le total de la commande
    def __calculer_total(self):
        total = sum(plat["prix"] for plat in self.__plats_commandes.values())
        return total

    # Méthode pour afficher la commande avec son total
    def afficher_commande(self):
        print(f"Numéro de commande : {self.__numero_commande}")
        print("Plats commandés:")
        for plat, info in self.__plats_commandes.items():
            print(f" - {plat}: {info['prix']} € ({info['statut']})")
        print(f"Total à payer : {self.__calculer_total()} €")

    # Méthode pour calculer la TVA (20% du total)
    def calculer_tva(self):
        tva = 0.2 * self.__calculer_total()
        return tva

# Exemple d'utilisation de la classe Commande
ma_commande = Commande(123)

# Ajout de plats à la commande
ma_commande.ajouter_plat("Pizza", 12)
ma_commande.ajouter_plat("Salade", 8)
ma_commande.ajouter_plat("Pâtes", 10)

# Affichage de la commande
ma_commande.afficher_commande()

# Annulation de la commande
ma_commande.annuler_commande()

# Affichage de la commande annulée
ma_commande.afficher_commande()

# Calcul de la TVA
tva = ma_commande.calculer_tva()
print(f"TVA à payer : {tva} €")
