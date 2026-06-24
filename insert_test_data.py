from dao.fournisseur_dao import FournisseurDAO
from models.fournisseur import Fournisseur

dao = FournisseurDAO()

f1 = Fournisseur(
    code="F001",
    raison_sociale="Sonatel",
    email="contact@sonatel.sn",
    telephone="771234567",
    adresse="Dakar"
)

f2 = Fournisseur(
    code="F002",
    raison_sociale="Orange Business",
    email="contact@orange.sn",
    telephone="781112233",
    adresse="Dakar"
)

dao.ajouter(f1)
dao.ajouter(f2)

print("Fournisseurs de test ajoutés avec succès.")