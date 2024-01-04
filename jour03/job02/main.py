class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Compte n°{self.__numero_compte} - {self.__nom} {self.__prenom}")
        print(f"Solde: {self.__solde} €")

    def afficherSolde(self):
        print(f"Solde actuel: {self.__solde} €")

    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant} € effectué. Nouveau solde: {self.__solde} €")

    def retrait(self, montant):
        if self.__decouvert or self.__solde >= montant:
            self.__solde -= montant
            print(f"Retrait de {montant} € effectué. Nouveau solde: {self.__solde} €")
        else:
            print("Opération impossible. Solde insuffisant.")

    def agios(self, taux_agios):
        if self.__solde < 0:
            agios_amount = abs(self.__solde) * taux_agios
            self.__solde -= agios_amount
            print(f"Des agios de {agios_amount} € ont été appliqués. Nouveau solde: {self.__solde} €")

    def virement(self, compte_destinataire, montant):
        if self.__solde >= montant:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant} € effectué vers le compte {compte_destinataire.__numero_compte}.")
        else:
            print("Opération impossible. Solde insuffisant.")

# Création d'un compte sans découvert initial
compte1 = CompteBancaire(1, "Dupont", "Jean", 1000)

# Affichage du compte
compte1.afficher()

# Versement
compte1.versement(500)

# Retrait
compte1.retrait(200)

# Création d'un compte avec découvert initial
compte2 = CompteBancaire(2, "Martin", "Sophie", -200, decouvert=True)

# Affichage du compte
compte2.afficher()

# Virement du compte1 vers le compte2
compte1.virement(compte2, 300)

# Affichage des soldes après le virement
compte1.afficherSolde()
compte2.afficherSolde()

# Application d'agios sur le compte2
compte2.agios(0.05)
compte2.afficherSolde()