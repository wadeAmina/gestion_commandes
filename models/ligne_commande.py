class LigneCommande:

    def __init__(
        self,
        id=None,
        commande_id=None,
        produit_id=None,
        quantite=0,
        prix_unitaire=0
    ):
        self.id = id
        self.commande_id = commande_id
        self.produit_id = produit_id
        self.quantite = quantite
        self.prix_unitaire = prix_unitaire

    def __str__(self):
        return (
            f"ID : {self.id} | "
            f"Commande : {self.commande_id} | "
            f"Produit : {self.produit_id} | "
            f"Quantité : {self.quantite} | "
            f"Prix unitaire : {self.prix_unitaire}"
        )

    def sous_total(self):
        return self.quantite * self.prix_unitaire