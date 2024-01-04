class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = 0
        self.__level = self.__student_eval()  # Initialisation du niveau lors de la création

    # Mutateur pour ajouter des crédits (vérifie que la valeur est supérieure à zéro)
    def add_credits(self, amount):
        if amount > 0:
            self.__credits += amount
            self.__level = self.__student_eval()  # Mise à jour du niveau après l'ajout de crédits
            print(f"{amount} crédits ajoutés avec succès.")
        else:
            print("Erreur : Le nombre de crédits ajouté doit être supérieur à zéro.")

    # Méthode privée pour évaluer le niveau de l'étudiant
    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    # Méthode pour afficher les informations de l'étudiant
    def student_info(self):
        print(f"Nom = {self.__nom}, Prenom = {self.__prenom}, Id = {self.__numero_etudiant}, Niveau = {self.__level}")

# Instanciation de l'objet représentant l'étudiant John Doe
john_doe = Student("John", "Doe", 145)

# Ajout de crédits à trois reprises
john_doe.add_credits(30)
john_doe.add_credits(25)
john_doe.add_credits(20)

# Affichage des informations de l'étudiant
john_doe.student_info()
