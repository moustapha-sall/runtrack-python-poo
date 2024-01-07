class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur

    # Assesseurs et mutateurs pour longueur
    def getLongueur(self):
        return self._longueur

    def setLongueur(self, longueur):
        self._longueur = longueur

    # Assesseurs et mutateurs pour largeur
    def getLargeur(self):
        return self._largeur

    def setLargeur(self, largeur):
        self._largeur = largeur

    def perimetre(self):
        return 2 * (self._longueur + self._largeur)

    def surface(self):
        return self._longueur * self._largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self._hauteur = hauteur

    # Assesseur et mutateur pour hauteur
    def getHauteur(self):
        return self._hauteur

    def setHauteur(self, hauteur):
        self._hauteur = hauteur

    def volume(self):
        return self._longueur * self._largeur * self._hauteur


# Instanciation de la classe Rectangle
rectangle = Rectangle(longueur=5, largeur=3)

# Utilisation des méthodes de la classe Rectangle
print("Perimètre du rectangle:", rectangle.perimetre())
print("Surface du rectangle:", rectangle.surface())

# Instanciation de la classe Parallelepipede
parallelepipede = Parallelepipede(longueur=4, largeur=2, hauteur=6)

# Utilisation des méthodes de la classe Parallelepipede et héritées de Rectangle
print("Perimètre du parallélépipède:", parallelepipede.perimetre())
print("Surface du parallélépipède:", parallelepipede.surface())
print("Volume du parallélépipède:", parallelepipede.volume())
