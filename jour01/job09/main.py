class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        infos = f"Nom: {self.nom}, Prix HT: {self.prixHT}€, TVA: {self.TVA}%"
        print(infos)

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrixHT(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT

    def obtenirNom(self):
        return self.nom

    def obtenirPrixHT(self):
        return self.prixHT

# Création de plusieurs produits
produit1 = Produit("Ordinateur", 800, 20)
produit2 = Produit("Téléphone", 500, 10)
produit3 = Produit("Imprimante", 150, 15)

# Affichage initial
print("Affichage initial des produits :")
produit1.afficher()
produit2.afficher()
produit3.afficher()

# Calcul des prix TTC
prix_TTC_produit1 = produit1.CalculerPrixTTC()
prix_TTC_produit2 = produit2.CalculerPrixTTC()
prix_TTC_produit3 = produit3.CalculerPrixTTC()

# Affichage des prix TTC
print("\nPrix TTC des produits :")
print(f"{produit1.obtenirNom()}: {prix_TTC_produit1}€")
print(f"{produit2.obtenirNom()}: {prix_TTC_produit2}€")
print(f"{produit3.obtenirNom()}: {prix_TTC_produit3}€")

# Modification du nom et du prix de chaque produit
produit1.modifierNom("Nouvel Ordinateur")
produit2.modifierPrixHT(550)

# Affichage des nouveaux noms et prix HT
print("\nNouveaux noms et prix HT des produits :")
print(f"{produit1.obtenirNom()}: {produit1.obtenirPrixHT()}€")
print(f"{produit2.obtenirNom()}: {produit2.obtenirPrixHT()}€")
print(f"{produit3.obtenirNom()}: {produit3.obtenirPrixHT()}€")
