class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)
        print(f"Tâche '{tache.titre}' ajoutée à la liste.")

    def supprimerTache(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                self.taches.remove(tache)
                print(f"Tâche '{tache.titre}' supprimée de la liste.")
                return
        print(f"Tâche '{titre}' introuvable.")

    def marquerCommeFinie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.statut = "terminée"
                print(f"Tâche '{tache.titre}' marquée comme terminée.")
                return
        print(f"Tâche '{titre}' introuvable.")

    def afficherListe(self):
        print("Liste des tâches :")
        for tache in self.taches:
            print(f"- {tache.titre} ({tache.statut}): {tache.description}")

    def filterListe(self, statut):
        filtered_list = [tache for tache in self.taches if tache.statut == statut]
        return filtered_list

# Tester le code
# Création d'instances de Tache
tache1 = Tache("Faire les courses", "Acheter des fruits et légumes")
tache2 = Tache("Réviser pour l'examen", "Chapitres 1 à 3", "à faire")
tache3 = Tache("Faire du sport", "30 minutes de jogging", "à faire")

# Création d'une instance de ListeDeTaches
liste_taches = ListeDeTaches()

# Ajout de tâches à la liste
liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)

# Affichage de la liste initiale
liste_taches.afficherListe()

# Marquer une tâche comme terminée
liste_taches.marquerCommeFinie("Faire les courses")

# Affichage de la liste après la modification
liste_taches.afficherListe()

# Supprimer une tâche
liste_taches.supprimerTache("Réviser pour l'examen")

# Affichage de la liste après la suppression
liste_taches.afficherListe()

# Filtrer les tâches à faire
taches_a_faire = liste_taches.filterListe("à faire")
print("\nTâches à faire :")
for tache in taches_a_faire:
    print(f"- {tache.titre} ({tache.statut}): {tache.description}")