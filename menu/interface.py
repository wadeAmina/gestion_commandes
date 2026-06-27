from dao.fournisseur_dao import FournisseurDAO
from models.fournisseur import Fournisseur


class Menu:

    def __init__(self):
        self.fournisseur_dao = FournisseurDAO()

    def menu_principal(self):

        while True:
            print("\n========== GESTION DES COMMANDES ==========")
            print("1. Gestion des fournisseurs")
            print("2. Gestion des produits")
            print("3. Gestion des commandes")
            print("0. Quitter")
            print("===========================================")

            choix = input("Votre choix : ")

            match choix:

                case "1":
                    self.menu_fournisseurs()

                case "2":
                    print("Module Produit en cours de développement")

                case "3":
                    print("Module Commande en cours de développement")

                case "0":
                    print("Au revoir !")
                    break

                case _:
                    print("Choix invalide")

    def menu_fournisseurs(self):

        while True:

            print("\n========== FOURNISSEURS ==========")
            print("1. Ajouter un fournisseur")
            print("2. Afficher tous les fournisseurs")
            print("3. Rechercher un fournisseur par ID")
            print("4. Supprimer un fournisseur")
            print("5. Rechercher par code")
            print("6. Rechercher par raison sociale")
            print("7. Modifier un fournisseur")
            print("0. Retour")
            print("==================================")

            choix = input("Votre choix : ")

            match choix:

                # Ajouter
                case "1":

                    print("\n===== AJOUTER UN FOURNISSEUR =====")

                    code = input("Code : ")
                    raison_sociale = input("Raison sociale : ")
                    email = input("Email : ")
                    telephone = input("Téléphone : ")
                    adresse = input("Adresse : ")

                    fournisseur = Fournisseur(
                        code=code,
                        raison_sociale=raison_sociale,
                        email=email,
                        telephone=telephone,
                        adresse=adresse
                    )

                    if self.fournisseur_dao.ajouter(fournisseur):
                        print("Fournisseur ajouté avec succès.")
                    else:
                        print("Erreur lors de l'ajout du fournisseur.")

                # Afficher tous
                case "2":

                    fournisseurs = self.fournisseur_dao.get_all()

                    if not fournisseurs:
                        print("Aucun fournisseur trouvé")
                    else:
                        for fournisseur in fournisseurs:
                            print(fournisseur)

                # Rechercher par ID
                case "3":

                    id_fournisseur = int(input("ID : "))

                    fournisseur = self.fournisseur_dao.get_by_id(id_fournisseur)

                    if fournisseur:
                        fournisseur.afficher()
                    else:
                        print("Fournisseur introuvable")

                # Supprimer
                case "4":

                    id_fournisseur = int(input("ID du fournisseur : "))

                    if self.fournisseur_dao.delete_by_id(id_fournisseur):
                        print("Suppression effectuée")
                    else:
                        print("Suppression impossible")

                # Rechercher par code
                case "5":

                    code = input("Code du fournisseur : ")

                    fournisseur = self.fournisseur_dao.rechercher_par_code(code)

                    if fournisseur:
                        fournisseur.afficher()
                    else:
                        print("Aucun fournisseur trouvé")

                # Rechercher par raison sociale
                case "6":

                    raison = input("Raison sociale : ")

                    fournisseurs = self.fournisseur_dao.rechercher_par_raison_sociale(raison)

                    if not fournisseurs:
                        print("Aucun fournisseur trouvé")
                    else:
                        for fournisseur in fournisseurs:
                            fournisseur.afficher()

                # Modifier
                case "7":

                    id_fournisseur = int(input("ID du fournisseur à modifier : "))

                    fournisseur = self.fournisseur_dao.get_by_id(id_fournisseur)

                    if fournisseur is None:
                        print("Fournisseur introuvable")

                    else:

                        print("\nLaissez vide si vous ne souhaitez pas modifier un champ.")

                        code = input(f"Code ({fournisseur.code}) : ")
                        raison = input(f"Raison sociale ({fournisseur.raison_sociale}) : ")
                        email = input(f"Email ({fournisseur.email}) : ")
                        telephone = input(f"Téléphone ({fournisseur.telephone}) : ")
                        adresse = input(f"Adresse ({fournisseur.adresse}) : ")

                        if code != "":
                            fournisseur.code = code

                        if raison != "":
                            fournisseur.raison_sociale = raison

                        if email != "":
                            fournisseur.email = email

                        if telephone != "":
                            fournisseur.telephone = telephone

                        if adresse != "":
                            fournisseur.adresse = adresse

                        if self.fournisseur_dao.update(fournisseur):
                            print("Fournisseur modifié avec succès.")
                        else:
                            print("Erreur lors de la modification.")

                case "0":
                    break

                case _:
                    print("Choix invalide")