from database.connexion import DatabaseConnection
from models.commande import Commande
from dao.base_dao import BaseDAO


class CommandeDAO(BaseDAO):

    # Ajouter une commande


    # Ajouter une commande
    def ajouter(self, commande):

        db = DatabaseConnection()

        if not db.connect():
            return False

        try:

            # On ne renseigne pas les dates.
            # MySQL utilisera automatiquement CURRENT_DATE.

            sql = """
                INSERT INTO commande
                (numero, fournisseur_id, montant_total, statut)
                VALUES (%s, %s, %s, %s)
            """

            params = (
                commande.numero,
                commande.fournisseur_id,
                commande.montant_total,
                commande.statut
            )

            if not db.execute(sql, params):
                db.rollback()
                return False

            db.commit()
            return True

        except Exception as e:

            print(f"Erreur lors de la création : {e}")
            db.rollback()
            return False

        finally:

            db.disconnect()



    # Alias pour garder le nom utilisé par l'ancien code
    def creer_commande(self, commande):
        return self.ajouter(commande)

    # Afficher toutes les commandes
    def get_all(self):
        db = DatabaseConnection()

        if not db.connect():
            return []

        try:
            sql = """
                SELECT id, numero, date_commande,
                       fournisseur_id, montant_total,
                       statut, date_creation
                FROM commande
                ORDER BY id
            """

            db.execute(sql)
            resultats = db.fetchall()

            commandes = []

            for ligne in resultats:
                commandes.append(
                    Commande(
                        id=ligne[0],
                        numero=ligne[1],
                        date_commande=ligne[2],
                        fournisseur_id=ligne[3],
                        montant_total=ligne[4],
                        statut=ligne[5],
                        date_creation=ligne[6]
                    )
                )

            return commandes

        except Exception as e:
            print(f"Erreur lors de l'affichage : {e}")
            return []

        finally:
            db.disconnect()

    def lister_commandes(self):
        return self.get_all()

    # Rechercher par ID
    def get_by_id(self, commande_id):
        db = DatabaseConnection()

        if not db.connect():
            return None

        try:
            sql = """
                SELECT id, numero, date_commande,
                       fournisseur_id, montant_total,
                       statut, date_creation
                FROM commande
                WHERE id = %s
            """

            db.execute(sql, (commande_id,))
            ligne = db.fetchone()

            if ligne:
                return Commande(
                    id=ligne[0],
                    numero=ligne[1],
                    date_commande=ligne[2],
                    fournisseur_id=ligne[3],
                    montant_total=ligne[4],
                    statut=ligne[5],
                    date_creation=ligne[6]
                )

            return None

        except Exception as e:
            print(f"Erreur : {e}")
            return None

        finally:
            db.disconnect()

    # Vérifier le stock
    def verifier_stock(self, produit_id, quantite):
        db = DatabaseConnection()

        if not db.connect():
            return False

        try:
            sql = """
                SELECT stock
                FROM produit
                WHERE id = %s
            """

            db.execute(sql, (produit_id,))
            ligne = db.fetchone()

            if ligne is None:
                return False

            return ligne[0] >= quantite

        except Exception as e:
            print(f"Erreur de vérification du stock : {e}")
            return False

        finally:
            db.disconnect()

    # Ajouter une ligne de commande
    def ajouter_ligne_commande(
        self,
        commande_id,
        produit_id,
        quantite,
        prix_unitaire
    ):
        if quantite <= 0:
            print("La quantité doit être supérieure à 0.")
            return False

        if not self.verifier_stock(produit_id, quantite):
            print("Stock insuffisant.")
            return False

        db = DatabaseConnection()

        if not db.connect():
            return False

        try:
            sql = """
                INSERT INTO ligne_commande
                (commande_id, produit_id, quantite, prix_unitaire)
                VALUES (%s, %s, %s, %s)
            """

            params = (
                commande_id,
                produit_id,
                quantite,
                prix_unitaire
            )

            if not db.execute(sql, params):
                db.rollback()
                return False

            db.commit()
            return True

        except Exception as e:
            print(f"Erreur lors de l'ajout de la ligne : {e}")
            db.rollback()
            return False

        finally:
            db.disconnect()

    # Calculer automatiquement le montant total
    def calculer_montant_total(self, commande_id):
        db = DatabaseConnection()

        if not db.connect():
            return 0

        try:
            sql = """
                SELECT COALESCE(
                    SUM(quantite * prix_unitaire), 0
                )
                FROM ligne_commande
                WHERE commande_id = %s
            """

            db.execute(sql, (commande_id,))
            resultat = db.fetchone()

            total = resultat[0] or 0

            sql_update = """
                UPDATE commande
                SET montant_total = %s
                WHERE id = %s
            """

            db.execute(sql_update, (total, commande_id))
            db.commit()

            return total

        except Exception as e:
            print(f"Erreur de calcul du montant : {e}")
            db.rollback()
            return 0

        finally:
            db.disconnect()

    # Mettre à jour le stock après validation
    def mettre_a_jour_stock(self, commande_id):
        db = DatabaseConnection()

        if not db.connect():
            return False

        try:
            sql = """
                SELECT produit_id, quantite
                FROM ligne_commande
                WHERE commande_id = %s
            """

            db.execute(sql, (commande_id,))
            lignes = db.fetchall()

            for produit_id, quantite in lignes:

                sql_stock = """
                    SELECT stock
                    FROM produit
                    WHERE id = %s
                """

                db.execute(sql_stock, (produit_id,))
                stock = db.fetchone()

                if stock is None or stock[0] < quantite:
                    raise Exception("Stock insuffisant.")

                sql_update = """
                    UPDATE produit
                    SET stock = stock - %s
                    WHERE id = %s
                """

                db.execute(
                    sql_update,
                    (quantite, produit_id)
                )

            db.commit()
            return True

        except Exception as e:
            print(f"Erreur lors de la mise à jour du stock : {e}")
            db.rollback()
            return False

        finally:
            db.disconnect()

    # Détail d'une commande
    def detail_commande(self, commande_id):
        db = DatabaseConnection()

        if not db.connect():
            return []

        try:
            sql = """
                SELECT p.reference,
                       p.designation,
                       lc.quantite,
                       lc.prix_unitaire,
                       (lc.quantite * lc.prix_unitaire) AS sous_total
                FROM ligne_commande lc
                INNER JOIN produit p
                    ON lc.produit_id = p.id
                WHERE lc.commande_id = %s
            """

            db.execute(sql, (commande_id,))
            return db.fetchall()

        except Exception as e:
            print(f"Erreur : {e}")
            return []

        finally:
            db.disconnect()

    # Changer le statut
    def changer_statut(self, commande_id, nouveau_statut):
        statuts = {
            "EN_ATTENTE": 1,
            "VALIDEE": 2,
            "LIVREE": 3
        }

        if nouveau_statut not in statuts:
            print("Statut invalide.")
            return False

        commande = self.get_by_id(commande_id)

        if commande is None:
            print("Commande introuvable.")
            return False

        ancien_statut = commande.statut

        if ancien_statut == "ANNULEE":
            print("Une commande annulée ne peut plus être modifiée.")
            return False

        if nouveau_statut == "VALIDEE":

            if ancien_statut != "EN_ATTENTE":
                print("La commande doit être EN_ATTENTE.")
                return False

            total = self.calculer_montant_total(commande_id)

            if not self.mettre_a_jour_stock(commande_id):
                return False

            return self._modifier_statut(
                commande_id,
                "VALIDEE"
            )

        if nouveau_statut == "LIVREE":

            if ancien_statut != "VALIDEE":
                print("Une commande doit être VALIDEE avant LIVREE.")
                return False

            return self._modifier_statut(
                commande_id,
                "LIVREE"
            )

        return False

    def _modifier_statut(self, commande_id, statut):
        db = DatabaseConnection()

        if not db.connect():
            return False

        try:
            sql = """
                UPDATE commande
                SET statut = %s
                WHERE id = %s
            """

            if not db.execute(sql, (statut, commande_id)):
                db.rollback()
                return False

            db.commit()
            return True

        except Exception as e:
            print(f"Erreur de changement de statut : {e}")
            db.rollback()
            return False

        finally:
            db.disconnect()

    # Annuler une commande
    def annuler_commande(self, commande_id):
        commande = self.get_by_id(commande_id)

        if commande is None:
            print("Commande introuvable.")
            return False

        if commande.statut in ("LIVREE", "ANNULEE"):
            print("Cette commande ne peut pas être annulée.")
            return False

        db = DatabaseConnection()

        if not db.connect():
            return False

        try:
            # Si la commande était validée,
            # son stock avait déjà été retiré.
            if commande.statut == "VALIDEE":

                sql = """
                    SELECT produit_id, quantite
                    FROM ligne_commande
                    WHERE commande_id = %s
                """

                db.execute(sql, (commande_id,))
                lignes = db.fetchall()

                for produit_id, quantite in lignes:

                    sql_stock = """
                        UPDATE produit
                        SET stock = stock + %s
                        WHERE id = %s
                    """

                    db.execute(
                        sql_stock,
                        (quantite, produit_id)
                    )

            sql = """
                UPDATE commande
                SET statut = 'ANNULEE'
                WHERE id = %s
            """

            if not db.execute(sql, (commande_id,)):
                db.rollback()
                return False

            db.commit()
            return True

        except Exception as e:
            print(f"Erreur lors de l'annulation : {e}")
            db.rollback()
            return False

        finally:
            db.disconnect()

    # Supprimer une commande
    def delete_by_id(self, commande_id):
        commande = self.get_by_id(commande_id)

        if commande is None:
            return False

        db = DatabaseConnection()

        if not db.connect():
            return False

        try:
            # Si la commande était validée/livrée,
            # remettre le stock avant suppression.
            if commande.statut in ("VALIDEE", "LIVREE"):

                sql = """
                    SELECT produit_id, quantite
                    FROM ligne_commande
                    WHERE commande_id = %s
                """

                db.execute(sql, (commande_id,))
                lignes = db.fetchall()

                for produit_id, quantite in lignes:
                    sql_stock = """
                        UPDATE produit
                        SET stock = stock + %s
                        WHERE id = %s
                    """

                    db.execute(
                        sql_stock,
                        (quantite, produit_id)
                    )

            # Supprimer d'abord les lignes
            sql_lignes = """
                DELETE FROM ligne_commande
                WHERE commande_id = %s
            """

            if not db.execute(sql_lignes, (commande_id,)):
                db.rollback()
                return False

            # Puis supprimer la commande
            sql_commande = """
                DELETE FROM commande
                WHERE id = %s
            """

            if not db.execute(sql_commande, (commande_id,)):
                db.rollback()
                return False

            db.commit()
            return True

        except Exception as e:
            print(f"Erreur lors de la suppression : {e}")
            db.rollback()
            return False

        finally:
            db.disconnect()

    def supprimer_commande(self, commande_id):
        return self.delete_by_id(commande_id)

    # Commandes en attente
    def commande_en_attente(self):
        db = DatabaseConnection()

        if not db.connect():
            return []

        try:
            sql = """
                SELECT id, numero, date_commande,
                       fournisseur_id, montant_total,
                       statut, date_creation
                FROM commande
                WHERE statut = 'EN_ATTENTE'
                ORDER BY date_commande DESC
            """

            db.execute(sql)
            resultats = db.fetchall()

            commandes = []

            for ligne in resultats:
                commandes.append(
                    Commande(
                        id=ligne[0],
                        numero=ligne[1],
                        date_commande=ligne[2],
                        fournisseur_id=ligne[3],
                        montant_total=ligne[4],
                        statut=ligne[5],
                        date_creation=ligne[6]
                    )
                )

            return commandes

        except Exception as e:
            print(f"Erreur : {e}")
            return []

        finally:
            db.disconnect()

    # Commandes par fournisseur
    def lister_par_fournisseur(self, fournisseur_id):
        db = DatabaseConnection()

        if not db.connect():
            return []

        try:
            sql = """
                SELECT id, numero, date_commande,
                       fournisseur_id, montant_total,
                       statut, date_creation
                FROM commande
                WHERE fournisseur_id = %s
                ORDER BY date_commande DESC
            """

            db.execute(sql, (fournisseur_id,))
            resultats = db.fetchall()

            commandes = []

            for ligne in resultats:
                commandes.append(
                    Commande(
                        id=ligne[0],
                        numero=ligne[1],
                        date_commande=ligne[2],
                        fournisseur_id=ligne[3],
                        montant_total=ligne[4],
                        statut=ligne[5],
                        date_creation=ligne[6]
                    )
                )

            return commandes

        except Exception as e:
            print(f"Erreur : {e}")
            return []

        finally:
            db.disconnect()