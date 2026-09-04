def division_securisee(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        print("Erreur : division par zero impossible.")


print(division_securisee(10, 2))
division_securisee(10, 0)


def convertir_entier(valeur):
    try:
        return int(valeur)

    except ValueError:
        print(f'Erreur : "{valeur}" n’est pas un entier valide.')


print(convertir_entier("42"))
convertir_entier("abc")


def acceder_element(liste, index):
    try:
        return liste[index]

    except IndexError:
        print(
            f"Erreur : index {index} hors limites "
            f"(taille de la liste : {len(liste)})."
        )


notes = [12, 15, 9]

print(acceder_element(notes, 1))
acceder_element(notes, 10)


def acceder_cle(dictionnaire, cle):
    try:
        return dictionnaire[cle]

    except KeyError:
        print(f'Erreur : la cle "{cle}" n’existe pas.')


eleve = {
    "nom": "Sara",
    "age": 20
}

print(acceder_cle(eleve, "nom"))
acceder_cle(eleve, "email")


def traiter_valeur(valeur):
    try:
        nombre = int(valeur)

    except ValueError:
        print(f'Erreur : "{valeur}" n’est pas convertible.')

    else:
        print(f"Conversion reussie : {nombre}")

    finally:
        print("Traitement termine.")


traiter_valeur("8")
traiter_valeur("x")