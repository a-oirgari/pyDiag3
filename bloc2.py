def verifier_age(age):

    if age < 0:
        raise ValueError(f"l’age ne peut pas etre negatif ({age}).")
    print(f"Age valide : {age}")

verifier_age(25)

def traiter_liste_de_valeurs(valeurs):
    for valeur in valeurs:
        try:
            nombre = int(valeur)

        except ValueError:
            print(f'Log : valeur "{valeur}" invalide, 'f'exception relancee.')
            raise

class StockInsuffisantError(Exception):
    pass


def retirer_stock(stock, produit, quantite):
    if produit not in stock:
        raise KeyError(f'le produit "{produit}" n’existe pas.')
    disponible = stock[produit]

    if quantite > disponible:
        raise StockInsuffisantError(f'stock insuffisant pour "{produit}" 'f'(demande : {quantite}, 'f'disponible : {disponible})')
    stock[produit] -= quantite

    print(f"Retrait effectue : {quantite} {produit}.")


stock = {
    "pommes": 20,
    "bananes": 4
}

retirer_stock(stock, "pommes", 5)
