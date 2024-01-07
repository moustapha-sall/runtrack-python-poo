import math

class Forme:
    def aire(self):
        return 0


class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur


class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        return math.pi * self.radius**2


# Instanciation de la classe Rectangle
rectangle = Rectangle(largeur=7, hauteur=3)

# Utilisation de la méthode aire de la classe Rectangle
resultat_aire_rectangle = rectangle.aire()

# Affichage du résultat
print("L'aire du rectangle est:", resultat_aire_rectangle)

# Instanciation de la classe Cercle
cercle = Cercle(radius=4)

# Utilisation de la méthode aire de la classe Cercle
resultat_aire_cercle = cercle.aire()

# Affichage du résultat
print("L'aire du cercle est:", resultat_aire_cercle)
