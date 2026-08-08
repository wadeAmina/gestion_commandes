class Produit:

    def __init__(
        self,
        id=None,
        reference="",
        designation="",
        prix_unitaire=0,
        stock=0,
        date_creation=None
    ):
        self.id = id
        self.reference = reference
        self.designation = designation
        self.prix_unitaire = prix_unitaire
        self.stock = stock
        self.date_creation = date_creation

    def __str__(self):
        return (
            f"ID : {self.id} | "
            f"Référence : {self.reference} | "
            f"Désignation : {self.designation} | "
            f"Prix : {self.prix_unitaire} | "
            f"Stock : {self.stock} | "
            f"Date : {self.date_creation}"
        )

    def afficher(self):
        print(f"ID : {self.id}")
        print(f"Référence : {self.reference}")
        print(f"Désignation : {self.designation}")
        print(f"Prix unitaire : {self.prix_unitaire}")
        print(f"Stock : {self.stock}")
        print(f"Date de création : {self.date_creation}")