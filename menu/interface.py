from dao.fournisseur_dao import FournisseurDAO
from dao.produit_dao import ProduitDAO
from dao.commande_dao import CommandeDAO
from dao.rapport_dao import RapportDAO

from models.fournisseur import Fournisseur
from models.produit import Produit
from models.commande import Commande


class Menu:

    def __init__(self):
        self.fournisseur_dao = FournisseurDAO()
        self.produit_dao = ProduitDAO()
        self.commande_dao = CommandeDAO()
        self.rapport_dao = RapportDAO()

    # =========================================================
    # MENU PRINCIPAL
    # =========================================================

    def menu_principal(self):

        while True:

            print("\n========== GESTION DES COMMANDES ==========")
            print("1. Gestion des fournisseurs")
            print("2. Gestion des produits")
            print("3. Gestion des commandes")
            print("4. Rapports et statistiques")
            print("0. Quitter")
            print("===========================================")

            choix = input("Votre choix : ")

            match choix:

                case "1":
                    self.menu_fournisseurs()

                case "2":
                    self.menu_produits()

                case "3":
                    self.menu_commandes()

                case "4":
                    self.menu_rapports()

                case "0":
                    print("Au revoir !")
                    break

                case _:
                    print("Choix invalide.")

    # =========================================================
    # MENU FOURNISSEURS
    # =========================================================

    def menu_fournisseurs(self):

        while True:

            print("\n========== FOURNISSEURS ==========")
            print("1. Ajouter un fournisseur")
            print("2. Afficher tous les fournisseurs")
            print("3. Rechercher par ID")
            print("4. Supprimer un fournisseur")
            print("5. Rechercher par code")
            print("6. Rechercher par raison sociale")
            print("7. Modifier un fournisseur")
            print("0. Retour")
            print("==================================")

            choix = input("Votre choix : ")

            match choix:

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
                        print("Erreur lors de l'ajout.")

                case "2":

                    fournisseurs = self.fournisseur_dao.get_all()

                    if not fournisseurs:
                        print("Aucun fournisseur trouvé.")
                    else:

                        print("\n===== LISTE DES FOURNISSEURS =====")

                        for fournisseur in fournisseurs:
                            fournisseur.afficher()
                            print("--------------------------------")

                case "3":

                    try:

                        id_fournisseur = int(
                            input("ID du fournisseur : ")
                        )

                        fournisseur = (
                            self.fournisseur_dao
                            .get_by_id(id_fournisseur)
                        )

                        if fournisseur:
                            fournisseur.afficher()
                        else:
                            print("Fournisseur introuvable.")

                    except ValueError:
                        print("L'ID doit être un nombre.")

                case "4":

                    try:

                        id_fournisseur = int(
                            input("ID du fournisseur : ")
                        )

                        if self.fournisseur_dao.delete_by_id(
                            id_fournisseur
                        ):
                            print("Suppression effectuée.")
                        else:
                            print("Suppression impossible.")

                    except ValueError:
                        print("L'ID doit être un nombre.")

                case "5":

                    code = input("Code du fournisseur : ")

                    fournisseur = (
                        self.fournisseur_dao
                        .rechercher_par_code(code)
                    )

                    if fournisseur:
                        fournisseur.afficher()
                    else:
                        print("Aucun fournisseur trouvé.")

                case "6":

                    raison = input("Raison sociale : ")

                    fournisseurs = (
                        self.fournisseur_dao
                        .rechercher_par_raison_sociale(raison)
                    )

                    if not fournisseurs:
                        print("Aucun fournisseur trouvé.")
                    else:

                        for fournisseur in fournisseurs:
                            fournisseur.afficher()
                            print("--------------------------------")

                case "7":

                    try:

                        id_fournisseur = int(
                            input(
                                "ID du fournisseur à modifier : "
                            )
                        )

                        fournisseur = (
                            self.fournisseur_dao
                            .get_by_id(id_fournisseur)
                        )

                        if fournisseur is None:
                            print("Fournisseur introuvable.")
                            continue

                        print(
                            "\nLaissez vide pour conserver "
                            "l'ancienne valeur."
                        )

                        code = input(
                            f"Code ({fournisseur.code}) : "
                        )

                        raison = input(
                            f"Raison sociale "
                            f"({fournisseur.raison_sociale}) : "
                        )

                        email = input(
                            f"Email ({fournisseur.email}) : "
                        )

                        telephone = input(
                            f"Téléphone ({fournisseur.telephone}) : "
                        )

                        adresse = input(
                            f"Adresse ({fournisseur.adresse}) : "
                        )

                        if code:
                            fournisseur.code = code

                        if raison:
                            fournisseur.raison_sociale = raison

                        if email:
                            fournisseur.email = email

                        if telephone:
                            fournisseur.telephone = telephone

                        if adresse:
                            fournisseur.adresse = adresse

                        if self.fournisseur_dao.update(
                            fournisseur
                        ):
                            print(
                                "Fournisseur modifié avec succès."
                            )
                        else:
                            print(
                                "Erreur lors de la modification."
                            )

                    except ValueError:
                        print("L'ID doit être un nombre.")

                case "0":
                    break

                case _:
                    print("Choix invalide.")

    # =========================================================
    # MENU PRODUITS
    # =========================================================

    def menu_produits(self):

        while True:

            print("\n========== PRODUITS ==========")
            print("1. Ajouter un produit")
            print("2. Afficher tous les produits")
            print("3. Rechercher un produit")
            print("4. Rechercher par ID")
            print("5. Modifier un produit")
            print("6. Supprimer un produit")
            print("7. Alerte de stock")
            print("0. Retour")
            print("==============================")

            choix = input("Votre choix : ")

            match choix:

                case "1":

                    print("\n===== AJOUTER UN PRODUIT =====")

                    reference = input("Référence : ")
                    designation = input("Désignation : ")

                    try:

                        prix_unitaire = float(
                            input("Prix unitaire : ")
                        )

                        stock = int(
                            input("Stock : ")
                        )

                        if prix_unitaire <= 0:
                            print(
                                "Le prix doit être supérieur à 0."
                            )
                            continue

                        if stock < 0:
                            print(
                                "Le stock ne peut pas être négatif."
                            )
                            continue

                    except ValueError:

                        print(
                            "Le prix doit être un nombre "
                            "et le stock un entier."
                        )
                        continue

                    produit = Produit(
                        reference=reference,
                        designation=designation,
                        prix_unitaire=prix_unitaire,
                        stock=stock
                    )

                    if self.produit_dao.ajouter(produit):
                        print("Produit ajouté avec succès.")
                    else:
                        print("Erreur lors de l'ajout.")

                case "2":

                    produits = self.produit_dao.get_all()

                    if not produits:
                        print("Aucun produit trouvé.")
                    else:

                        print("\n===== LISTE DES PRODUITS =====")

                        for produit in produits:
                            produit.afficher()
                            print("--------------------------------")

                case "3":

                    print("\n===== RECHERCHER UN PRODUIT =====")
                    print("1. Par référence")
                    print("2. Par désignation")

                    type_recherche = input("Votre choix : ")

                    if type_recherche == "1":

                        reference = input("Référence : ")

                        produit = (
                            self.produit_dao
                            .rechercher_par_reference(reference)
                        )

                        if produit:
                            produit.afficher()
                        else:
                            print("Produit introuvable.")

                    elif type_recherche == "2":

                        designation = input(
                            "Désignation : "
                        )

                        produits = (
                            self.produit_dao
                            .rechercher_par_designation(
                                designation
                            )
                        )

                        if not produits:
                            print("Aucun produit trouvé.")
                        else:

                            for produit in produits:
                                produit.afficher()
                                print("--------------------------------")

                    else:
                        print("Choix invalide.")

                case "4":

                    try:

                        produit_id = int(
                            input("ID du produit : ")
                        )

                        produit = (
                            self.produit_dao
                            .get_by_id(produit_id)
                        )

                        if produit:
                            produit.afficher()
                        else:
                            print("Produit introuvable.")

                    except ValueError:
                        print("L'ID doit être un nombre.")

                case "5":

                    try:

                        produit_id = int(
                            input("ID du produit à modifier : ")
                        )

                        produit = (
                            self.produit_dao
                            .get_by_id(produit_id)
                        )

                        if produit is None:
                            print("Produit introuvable.")
                            continue

                        print(
                            "\nLaissez vide pour conserver "
                            "l'ancienne valeur."
                        )

                        reference = input(
                            f"Référence ({produit.reference}) : "
                        )

                        designation = input(
                            f"Désignation ({produit.designation}) : "
                        )

                        prix = input(
                            f"Prix unitaire "
                            f"({produit.prix_unitaire}) : "
                        )

                        stock = input(
                            f"Stock ({produit.stock}) : "
                        )

                        if reference:
                            produit.reference = reference

                        if designation:
                            produit.designation = designation

                        if prix:

                            try:
                                nouveau_prix = float(prix)

                                if nouveau_prix <= 0:
                                    print(
                                        "Le prix doit être "
                                        "supérieur à 0."
                                    )
                                    continue

                                produit.prix_unitaire = nouveau_prix

                            except ValueError:
                                print("Prix invalide.")
                                continue

                        if stock:

                            try:
                                nouveau_stock = int(stock)

                                if nouveau_stock < 0:
                                    print(
                                        "Le stock ne peut pas "
                                        "être négatif."
                                    )
                                    continue

                                produit.stock = nouveau_stock

                            except ValueError:
                                print("Stock invalide.")
                                continue

                        if self.produit_dao.update(produit):
                            print(
                                "Produit modifié avec succès."
                            )
                        else:
                            print(
                                "Erreur lors de la modification."
                            )

                    except ValueError:
                        print("L'ID doit être un nombre.")

                case "6":

                    try:

                        produit_id = int(
                            input("ID du produit : ")
                        )

                        if self.produit_dao.delete_by_id(
                            produit_id
                        ):
                            print(
                                "Produit supprimé avec succès."
                            )
                        else:
                            print(
                                "Suppression impossible."
                            )

                    except ValueError:
                        print("L'ID doit être un nombre.")

                case "7":

                    try:

                        seuil = int(
                            input("Seuil de stock : ")
                        )

                        produits = (
                            self.produit_dao
                            .alerte_stock(seuil)
                        )

                        if not produits:
                            print(
                                "Aucun produit sous ce seuil."
                            )
                        else:

                            print(
                                "\n===== ALERTE STOCK ====="
                            )

                            for produit in produits:
                                produit.afficher()
                                print("--------------------------------")

                    except ValueError:
                        print(
                            "Le seuil doit être un nombre."
                        )

                case "0":
                    break

                case _:
                    print("Choix invalide.")

    # =========================================================
    # MENU COMMANDES
    # =========================================================

    def menu_commandes(self):

        while True:

            print("\n========== COMMANDES ==========")
            print("1. Ajouter une commande")
            print("2. Afficher toutes les commandes")
            print("3. Rechercher une commande par ID")
            print("4. Ajouter une ligne de commande")
            print("5. Afficher le détail d'une commande")
            print("6. Calculer le montant total")
            print("7. Valider une commande")
            print("8. Livrer une commande")
            print("9. Annuler une commande")
            print("10. Supprimer une commande")
            print("11. Afficher les commandes en attente")
            print("12. Rechercher par fournisseur")
            print("0. Retour")
            print("===============================")

            choix = input("Votre choix : ")

            match choix:

                # -------------------------------------------------
                # AJOUTER UNE COMMANDE
                # -------------------------------------------------

                case "1":

                    print("\n===== AJOUTER UNE COMMANDE =====")

                    numero = input(
                        "Numéro de commande : "
                    )

                    if numero == "":
                        print(
                            "Le numéro de commande est obligatoire."
                        )
                        continue

                    try:

                        fournisseur_id = int(
                            input(
                                "ID du fournisseur : "
                            )
                        )

                    except ValueError:

                        print(
                            "L'ID du fournisseur doit être "
                            "un nombre."
                        )
                        continue

                    # Vérifier que le fournisseur existe
                    fournisseur = (
                        self.fournisseur_dao
                        .get_by_id(fournisseur_id)
                    )

                    if fournisseur is None:

                        print(
                            "Fournisseur introuvable."
                        )

                        print(
                            "Veuillez utiliser un ID "
                            "de fournisseur existant."
                        )

                        continue

                    # Les dates ne sont plus demandées.
                    # MySQL utilise CURRENT_DATE automatiquement.

                    commande = Commande(
                        numero=numero,
                        fournisseur_id=fournisseur_id,
                        montant_total=0,
                        statut="EN_ATTENTE"
                    )

                    if self.commande_dao.ajouter(
                        commande
                    ):

                        print(
                            "Commande ajoutée avec succès."
                        )

                        print(
                            "La date de commande et la date "
                            "de création sont automatiques."
                        )

                    else:

                        print(
                            "Erreur lors de l'ajout "
                            "de la commande."
                        )

                # -------------------------------------------------
                # AFFICHER TOUTES LES COMMANDES
                # -------------------------------------------------

                case "2":

                    commandes = (
                        self.commande_dao.get_all()
                    )

                    if not commandes:

                        print(
                            "Aucune commande trouvée."
                        )

                    else:

                        print(
                            "\n===== LISTE DES COMMANDES ====="
                        )

                        for commande in commandes:
                            commande.afficher()
                            print("--------------------------------")

                # -------------------------------------------------
                # RECHERCHER PAR ID
                # -------------------------------------------------

                case "3":

                    try:

                        commande_id = int(
                            input(
                                "ID de la commande : "
                            )
                        )

                        commande = (
                            self.commande_dao
                            .get_by_id(commande_id)
                        )

                        if commande:
                            commande.afficher()
                        else:
                            print(
                                "Commande introuvable."
                            )

                    except ValueError:
                        print(
                            "L'ID doit être un nombre."
                        )

                # -------------------------------------------------
                # AJOUTER UNE LIGNE DE COMMANDE
                # -------------------------------------------------

                case "4":

                    print(
                        "\n===== AJOUTER UNE LIGNE DE COMMANDE ====="
                    )

                    try:

                        commande_id = int(
                            input("ID commande : ")
                        )

                        produit_id = int(
                            input("ID produit : ")
                        )

                        quantite = int(
                            input("Quantité : ")
                        )

                        prix_unitaire = float(
                            input("Prix unitaire : ")
                        )

                        if quantite <= 0:
                            print(
                                "La quantité doit être "
                                "supérieure à 0."
                            )
                            continue

                        if prix_unitaire <= 0:
                            print(
                                "Le prix doit être "
                                "supérieur à 0."
                            )
                            continue

                    except ValueError:

                        print(
                            "Valeur invalide."
                        )
                        continue

                    commande = (
                        self.commande_dao
                        .get_by_id(commande_id)
                    )

                    if commande is None:

                        print(
                            "Commande introuvable."
                        )
                        continue

                    if commande.statut != "EN_ATTENTE":

                        print(
                            "Impossible d'ajouter une ligne "
                            "à une commande qui n'est plus "
                            "EN_ATTENTE."
                        )
                        continue

                    if self.commande_dao.ajouter_ligne_commande(
                        commande_id,
                        produit_id,
                        quantite,
                        prix_unitaire
                    ):

                        print(
                            "Ligne de commande ajoutée."
                        )

                    else:

                        print(
                            "Erreur lors de l'ajout "
                            "de la ligne."
                        )

                # -------------------------------------------------
                # DETAIL COMMANDE
                # -------------------------------------------------

                case "5":

                    try:

                        commande_id = int(
                            input(
                                "ID de la commande : "
                            )
                        )

                        lignes = (
                            self.commande_dao
                            .detail_commande(commande_id)
                        )

                        if not lignes:

                            print(
                                "Aucune ligne trouvée."
                            )

                        else:

                            print(
                                "\n===== DETAIL DE LA COMMANDE ====="
                            )

                            for ligne in lignes:

                                print(
                                    f"Référence : {ligne[0]}"
                                )

                                print(
                                    f"Désignation : {ligne[1]}"
                                )

                                print(
                                    f"Quantité : {ligne[2]}"
                                )

                                print(
                                    f"Prix unitaire : {ligne[3]}"
                                )

                                print(
                                    f"Sous-total : {ligne[4]}"
                                )

                                print("--------------------------------")

                    except ValueError:
                        print(
                            "L'ID doit être un nombre."
                        )

                # -------------------------------------------------
                # CALCULER LE MONTANT TOTAL
                # -------------------------------------------------

                case "6":

                    try:

                        commande_id = int(
                            input(
                                "ID de la commande : "
                            )
                        )

                        commande = (
                            self.commande_dao
                            .get_by_id(commande_id)
                        )

                        if commande is None:

                            print(
                                "Commande introuvable."
                            )
                            continue

                        total = (
                            self.commande_dao
                            .calculer_montant_total(
                                commande_id
                            )
                        )

                        print(
                            f"Montant total : {total} FCFA"
                        )

                    except ValueError:
                        print(
                            "L'ID doit être un nombre."
                        )

                # -------------------------------------------------
                # VALIDER
                # -------------------------------------------------

                case "7":

                    try:

                        commande_id = int(
                            input(
                                "ID de la commande : "
                            )
                        )

                        if self.commande_dao.changer_statut(
                            commande_id,
                            "VALIDEE"
                        ):

                            print(
                                "Commande validée avec succès."
                            )

                        else:

                            print(
                                "Impossible de valider "
                                "la commande."
                            )

                    except ValueError:
                        print(
                            "L'ID doit être un nombre."
                        )

                # -------------------------------------------------
                # LIVRER
                # -------------------------------------------------

                case "8":

                    try:

                        commande_id = int(
                            input(
                                "ID de la commande : "
                            )
                        )

                        if self.commande_dao.changer_statut(
                            commande_id,
                            "LIVREE"
                        ):

                            print(
                                "Commande livrée avec succès."
                            )

                        else:

                            print(
                                "Impossible de livrer "
                                "la commande."
                            )

                    except ValueError:
                        print(
                            "L'ID doit être un nombre."
                        )

                # -------------------------------------------------
                # ANNULER
                # -------------------------------------------------

                case "9":

                    try:

                        commande_id = int(
                            input(
                                "ID de la commande : "
                            )
                        )

                        if self.commande_dao.annuler_commande(
                            commande_id
                        ):

                            print(
                                "Commande annulée avec succès."
                            )

                        else:

                            print(
                                "Impossible d'annuler "
                                "la commande."
                            )

                    except ValueError:
                        print(
                            "L'ID doit être un nombre."
                        )

                # -------------------------------------------------
                # SUPPRIMER
                # -------------------------------------------------

                case "10":

                    try:

                        commande_id = int(
                            input(
                                "ID de la commande : "
                            )
                        )

                        if self.commande_dao.delete_by_id(
                            commande_id
                        ):

                            print(
                                "Commande supprimée "
                                "avec succès."
                            )

                        else:

                            print(
                                "Impossible de supprimer "
                                "la commande."
                            )

                    except ValueError:
                        print(
                            "L'ID doit être un nombre."
                        )

                # -------------------------------------------------
                # COMMANDES EN ATTENTE
                # -------------------------------------------------

                case "11":

                    commandes = (
                        self.commande_dao
                        .commande_en_attente()
                    )

                    if not commandes:

                        print(
                            "Aucune commande en attente."
                        )

                    else:

                        print(
                            "\n===== COMMANDES EN ATTENTE ====="
                        )

                        for commande in commandes:

                            commande.afficher()
                            print("--------------------------------")

                # -------------------------------------------------
                # PAR FOURNISSEUR
                # -------------------------------------------------

                case "12":

                    try:

                        fournisseur_id = int(
                            input(
                                "ID du fournisseur : "
                            )
                        )

                        commandes = (
                            self.commande_dao
                            .lister_par_fournisseur(
                                fournisseur_id
                            )
                        )

                        if not commandes:

                            print(
                                "Aucune commande trouvée."
                            )

                        else:

                            print(
                                "\n===== COMMANDES DU FOURNISSEUR ====="
                            )

                            for commande in commandes:

                                commande.afficher()
                                print("--------------------------------")

                    except ValueError:
                        print(
                            "L'ID doit être un nombre."
                        )

                case "0":
                    break

                case _:
                    print("Choix invalide.")

    # =========================================================
    # RAPPORTS ET STATISTIQUES
    # =========================================================

    def menu_rapports(self):

        while True:

            print(
                "\n========== RAPPORTS ET STATISTIQUES =========="
            )

            print("1. Valeur totale du stock")
            print("2. Top 5 des produits les plus commandés")
            print("3. Chiffre d'affaires total")
            print("4. Nombre de commandes")
            print("5. Nombre de produits")
            print("6. Nombre de fournisseurs")
            print("0. Retour")

            print(
                "==============================================="
            )

            choix = input("Votre choix : ")

            match choix:

                case "1":

                    valeur = (
                        self.rapport_dao
                        .valeur_totale_stock()
                    )

                    print(
                        f"\nValeur totale du stock : "
                        f"{valeur} FCFA"
                    )

                case "2":

                    produits = (
                        self.rapport_dao
                        .top5_produits()
                    )

                    if not produits:

                        print(
                            "\nAucun produit commandé."
                        )

                    else:

                        print(
                            "\n===== TOP 5 DES PRODUITS "
                            "LES PLUS COMMANDÉS ====="
                        )

                        for i, produit in enumerate(
                            produits, 1
                        ):

                            reference = produit[0]
                            designation = produit[1]
                            quantite = produit[2]

                            print(
                                f"{i}. {reference} - "
                                f"{designation} : "
                                f"{quantite} unités"
                            )

                case "3":

                    chiffre_affaires = (
                        self.rapport_dao
                        .chiffre_affaires_total()
                    )

                    print(
                        f"\nChiffre d'affaires total : "
                        f"{chiffre_affaires} FCFA"
                    )

                case "4":

                    nombre = (
                        self.rapport_dao
                        .nombre_commandes()
                    )

                    print(
                        f"\nNombre de commandes : {nombre}"
                    )

                case "5":

                    nombre = (
                        self.rapport_dao
                        .nombre_produits()
                    )

                    print(
                        f"\nNombre de produits : {nombre}"
                    )

                case "6":

                    nombre = (
                        self.rapport_dao
                        .nombre_fournisseurs()
                    )

                    print(
                        f"\nNombre de fournisseurs : {nombre}"
                    )

                case "0":
                    break

                case _:
                    print("Choix invalide.")

