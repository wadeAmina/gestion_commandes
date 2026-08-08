class Commande:

    STATUTS = (
        "EN_ATTENTE",
        "VALIDEE",
        "LIVREE",
        "ANNULEE"
    )

    def __init__(
        self,
        id=None,
        numero="",
        date_commande=None,
        fournisseur_id=None,
        montant_total=0,
        statut="EN_ATTENTE",
        date_creation=None
    ):
        self.id = id
        self.numero = numero
        self.date_commande = date_commande
        self.fournisseur_id = fournisseur_id
        self.montant_total = montant_total
        self.statut = statut
        self.date_creation = date_creation

    def __str__(self):
        return (
            f"ID : {self.id} | "
            f"Numéro : {self.numero} | "
            f"Fournisseur : {self.fournisseur_id} | "
            f"Montant : {self.montant_total} | "
            f"Statut : {self.statut} | "
            f"Date : {self.date_commande}"
        )

    def afficher(self):
        print(f"ID : {self.id}")
        print(f"Numéro : {self.numero}")
        print(f"Fournisseur : {self.fournisseur_id}")
        print(f"Montant total : {self.montant_total}")
        print(f"Statut : {self.statut}")
        print(f"Date commande : {self.date_commande}")
        print(f"Date création : {self.date_creation}")