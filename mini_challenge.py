class StockInsuffisantError(Exception):
    pass


def retirer_stock(stock, produit, quantite):
    if produit not in stock:
        raise KeyError(produit)

    disponible = stock[produit]

    if quantite > disponible:
        raise StockInsuffisantError(f"stock insuffisant "f"(demande {quantite}, dispo {disponible})")

    stock[produit] -= quantite


def traiter_commandes(stock, commandes_brutes, chemin_journal):
    with open(chemin_journal, "w", encoding="utf-8") as journal:

        for commande in commandes_brutes:
            produit, valeur = commande.split(",")

            try:
                quantite = int(valeur)

                retirer_stock(stock, produit, quantite)

                message = (f"[OK] {produit} :-{quantite} "f"(reste {stock[produit]})")

            except ValueError:
                message = (f'[ERREUR] {produit} : 'f'quantite invalide ("{valeur}")')

            except StockInsuffisantError:
                disponible = stock[produit]

                message = (f"[ERREUR] {produit} : stock insuffisant "f"(demande {quantite}, dispo {disponible})")

            except KeyError:
                message = f"[ERREUR] {produit} : produit inconnu"

            journal.write(message + "\n")

            print(message)

    with open(chemin_journal, "r", encoding="utf-8") as journal:
        contenu = journal.read()

    print("\n    Contenu du journal    ")
    print(contenu)




stock = {
    "pommes": 20,
    "bananes": 4,
    "oranges": 15
}

commandes_brutes = [
    "pommes,5",
    "bananes,10",
    "kiwis,2",
    "oranges,abc",
    "oranges,5",
]

traiter_commandes(stock, commandes_brutes, "journal.txt")