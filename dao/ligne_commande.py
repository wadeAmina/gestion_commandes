from database.connexion import DatabaseConnection
from models.ligne_commande import LigneCommande


class LigneCommandeDAO:

    def ajouter(self, ligne):
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
                ligne.commande_id,
                ligne.produit_id,
                ligne.quantite,
                ligne.prix_unitaire
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

    def get_by_id(self, ligne_id):
        db = DatabaseConnection()

        if not db.connect():
            return None

        try:
            sql = """
                SELECT id, commande_id, produit_id,
                       quantite, prix_unitaire
                FROM ligne_commande
                WHERE id = %s
            """

            db.execute(sql, (ligne_id,))
            ligne = db.fetchone()

            if ligne:
                return LigneCommande(
                    id=ligne[0],
                    commande_id=ligne[1],
                    produit_id=ligne[2],
                    quantite=ligne[3],
                    prix_unitaire=ligne[4]
                )

            return None

        except Exception as e:
            print(f"Erreur : {e}")
            return None

        finally:
            db.disconnect()

    def get_by_commande(self, commande_id):
        db = DatabaseConnection()

        if not db.connect():
            return []

        try:
            sql = """
                SELECT id, commande_id, produit_id,
                       quantite, prix_unitaire
                FROM ligne_commande
                WHERE commande_id = %s
            """

            db.execute(sql, (commande_id,))
            resultats = db.fetchall()

            lignes = []

            for ligne in resultats:
                lignes.append(
                    LigneCommande(
                        id=ligne[0],
                        commande_id=ligne[1],
                        produit_id=ligne[2],
                        quantite=ligne[3],
                        prix_unitaire=ligne[4]
                    )
                )

            return lignes

        except Exception as e:
            print(f"Erreur : {e}")
            return []

        finally:
            db.disconnect()

    def modifier(self, ligne):
        db = DatabaseConnection()

        if not db.connect():
            return False

        try:
            sql = """
                UPDATE ligne_commande
                SET produit_id = %s,
                    quantite = %s,
                    prix_unitaire = %s
                WHERE id = %s
            """

            params = (
                ligne.produit_id,
                ligne.quantite,
                ligne.prix_unitaire,
                ligne.id
            )

            if not db.execute(sql, params):
                db.rollback()
                return False

            db.commit()
            return True

        except Exception as e:
            print(f"Erreur lors de la modification : {e}")
            db.rollback()
            return False

        finally:
            db.disconnect()

    def supprimer_par_commande(self, commande_id):
        db = DatabaseConnection()

        if not db.connect():
            return False

        try:
            sql = """
                DELETE FROM ligne_commande
                WHERE commande_id = %s
            """

            if not db.execute(sql, (commande_id,)):
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