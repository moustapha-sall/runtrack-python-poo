import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

class Jeu:
    def __init__(self):
        self.paquet = self.creer_paquet()
        self.main_joueur = []
        self.main_croupier = []

    def creer_paquet(self):
        valeurs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        couleurs = ['Coeurs', 'Carreaux', 'Trèfles', 'Piques']
        paquet = [Carte(v, c) for v in valeurs for c in couleurs]
        random.shuffle(paquet)
        return paquet

    def distribuer_cartes(self):
        self.main_joueur = [self.paquet.pop(), self.paquet.pop()]
        self.main_croupier = [self.paquet.pop(), self.paquet.pop()]

    def calculer_points(self, main):
        total = sum(carte.valeur for carte in main)
        as_present = any(carte.valeur == 11 for carte in main)

        while total > 21 and as_present:
            total -= 10
            as_present = any(carte.valeur == 11 for carte in main)

        return total

    def afficher_main(self, main, joueur):
        print(f"Main {joueur}: {[str(carte) for carte in main]}")

    def jouer(self):
        self.distribuer_cartes()

        while True:
            self.afficher_main(self.main_joueur, "Joueur")
            choix = input("Voulez-vous prendre une carte de plus? (Oui/Non): ").lower()

            if choix == 'oui':
                self.main_joueur.append(self.paquet.pop())
                points_joueur = self.calculer_points(self.main_joueur)

                if points_joueur > 21:
                    print("Vous avez dépassé 21 points. Vous avez perdu!")
                    return
            else:
                break

        while self.calculer_points(self.main_croupier) < 17:
            self.main_croupier.append(self.paquet.pop())

        self.afficher_main(self.main_joueur, "Joueur")
        self.afficher_main(self.main_croupier, "Croupier")

        points_joueur = self.calculer_points(self.main_joueur)
        points_croupier = self.calculer_points(self.main_croupier)

        if points_joueur > 21 or (points_croupier <= 21 and points_croupier > points_joueur):
            print("Le croupier gagne!")
        else:
            print("Vous gagnez!")

# Jouer une partie
jeu_blackjack = Jeu()
jeu_blackjack.jouer()