from dao.fournisseur_dao import FournisseurDAO
from models.fournisseur import Fournisseur

dao = FournisseurDAO()

fournisseurs = [
    Fournisseur(
        code="F001",
        raison_sociale="Sonatel",
        email="contact@sonatel.sn",
        telephone="771234567",
        adresse="Dakar"
    ),
    Fournisseur(
        code="F002",
        raison_sociale="Orange Business",
        email="contact@orange.sn",
        telephone="781112233",
        adresse="Dakar"
    ),
    Fournisseur(
        code="F003",
        raison_sociale="SenTech",
        email="contact@sentech.sn",
        telephone="771111111",
        adresse="Thiès"
    )
]

for fournisseur in fournisseurs:
    if dao.ajouter(fournisseur):
        print(f"{fournisseur.code} ajouté avec succès")
    else:
        print(f"Erreur lors de l'ajout de {fournisseur.code}")

print("Insertion des données de test terminée.")