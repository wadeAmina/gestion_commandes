from dao.fournisseur_dao import FournisseurDAO


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
            print("1. Afficher tous les fournisseurs")
            print("2. Rechercher un fournisseur par ID")
            print("3. Supprimer un fournisseur")
            print("0. Retour")
            print("==================================")

            choix = input("Votre choix : ")

            match choix:

                case "1":
                    fournisseurs = self.fournisseur_dao.get_all()

                    if not fournisseurs:
                        print("Aucun fournisseur trouvé")
                    else:
                        for fournisseur in fournisseurs:
                            print(fournisseur)

                case "2":
                    id_fournisseur = int(input("ID : "))
                    fournisseur = self.fournisseur_dao.get_by_id(id_fournisseur)

                    if fournisseur:
                        fournisseur.afficher()
                    else:
                        print("Fournisseur introuvable")

                case "3":
                    id_fournisseur = int(input("ID du fournisseur : "))

                    if self.fournisseur_dao.delete_by_id(id_fournisseur):
                        print("Suppression effectuée")
                    else:
                        print("Suppression impossible")

                case "0":
                    break

                case _:
                    print("Choix invalide")