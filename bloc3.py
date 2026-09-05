def ecrire_liste_courses(chemin, articles):
    with open(chemin, "w", encoding="utf-8") as fichier:
        for article in articles:
            fichier.write(article + "\n")


def ajouter_article(chemin, article):
    with open(chemin, "a", encoding="utf-8") as fichier:
        fichier.write(article + "\n")


def lire_fichier(chemin):
    with open(chemin, "r", encoding="utf-8") as fichier:
        return fichier.readlines()


def compter_lignes(chemin):
    compteur = 0

    with open(chemin, "r", encoding="utf-8") as fichier:
        for ligne in fichier:
            compteur += 1

    print(f"Nombre de lignes : {compteur}")

articles = ["pommes", "lait", "pain"]

ecrire_liste_courses("courses.txt", articles)

ajouter_article("courses.txt", "oeufs")

print(lire_fichier("courses.txt"))

compter_lignes("courses.txt")