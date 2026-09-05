import csv

def lire_fichier_securise(chemin):
    try:
        with open(chemin, "r", encoding="utf-8") as fichier:
            return fichier.readlines()

    except FileNotFoundError:
        print(f'Erreur : le fichier "{chemin}" n’existe pas.')

    except PermissionError:
        print(f'Erreur : permission refusee pour "{chemin}".')

print(lire_fichier_securise("courses.txt"))
# lire_fichier_securise("inexistant.txt")

# ====================================================================================

def calculer_moyenne_csv(chemin):
    notes = []

    try:
        with open(chemin, "r", encoding="utf-8") as fichier:
            lecteur = csv.DictReader(fichier)

            for ligne in lecteur:
                nom = ligne["nom"]
                valeur = ligne["note"]

                try:
                    note = float(valeur)
                    notes.append(note)

                except ValueError:
                    print(f'Attention : note invalide pour "{nom}" 'f'("{valeur}"), ligne ignoree.')

    except FileNotFoundError:
        print(f'Erreur : le fichier "{chemin}" n’existe pas.')
        return

    moyenne = sum(notes) / len(notes)

    print(f"Moyenne calculee ({len(notes)} notes valides) : "f"{moyenne:.2f}")

calculer_moyenne_csv("provisoire.csv")