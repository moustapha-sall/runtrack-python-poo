class Operation:
    def __init__(self, nombre1=5, nombre2=4):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print(f"Résultat de l'addition : {resultat}")

# Instanciation de la classe
operation_instance = Operation()

# Appel de la méthode addition
operation_instance.addition()
