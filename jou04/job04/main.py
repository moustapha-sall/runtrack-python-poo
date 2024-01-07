class Forme:
    def aire(self):
        return 0


class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur


# Instanciation de la classe Rectangle
rectangle = Rectangle(largeur=7, hauteur=3)

# Utilisation de la méthode aire de la classe Rectangle
resultat_aire = rectangle.aire()

# Affichage du résultat
print("L'aire du rectangle est:", resultat_aire)