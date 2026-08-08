from database.connexion import DatabaseConnection
from models.produit import Produit
from dao.base_dao import BaseDAO


class ProduitDAO(BaseDAO):

    # Ajouter un produit
    def ajouter(self, produit):
        db = DatabaseConnection()

        if not db.connect():
            return False

        try:
            sql = """
                INSERT INTO produit
                (reference, designation, prix_unitaire, stock)
                VALUES (%s, %s, %s, %s)
            """

            params = (
                produit.reference,
                produit.designation,
                produit.prix_unitaire,
                produit.stock
            )

            if not db.execute(sql, params):
                db.rollback()
                return False

            db.commit()
            return True

        except Exception as e:
            print(f"Erreur lors de l'ajout du produit : {e}")
            db.rollback()
            return False

        finally:
            db.disconnect()

    # Afficher tous les produits
    def get_all(self):
        db = DatabaseConnection()

        if not db.connect():
            return []

        try:
            sql = """
                SELECT id, reference, designation,
                       prix_unitaire, stock, date_creation
                FROM produit
                ORDER BY id
            """

            if not db.execute(sql):
                return []

            resultats = db.fetchall()

            produits = []

            for ligne in resultats:
                produits.append(
                    Produit(
                        id=ligne[0],
                        reference=ligne[1],
                        designation=ligne[2],
                        prix_unitaire=ligne[3],
                        stock=ligne[4],
                        date_creation=ligne[5]
                    )
                )

            return produits

        except Exception as e:
            print(f"Erreur lors de l'affichage des produits : {e}")
            return []

        finally:
            db.disconnect()

    # Rechercher un produit par ID
    def get_by_id(self, produit_id):
        db = DatabaseConnection()

        if not db.connect():
            return None

        try:
            sql = """
                SELECT id, reference, designation,
                       prix_unitaire, stock, date_creation
                FROM produit
                WHERE id = %s
            """

            if not db.execute(sql, (produit_id,)):
                return None

            ligne = db.fetchone()

            if ligne:
                return Produit(
                    id=ligne[0],
                    reference=ligne[1],
                    designation=ligne[2],
                    prix_unitaire=ligne[3],
                    stock=ligne[4],
                    date_creation=ligne[5]
                )

            return None

        except Exception as e:
            print(f"Erreur lors de la recherche : {e}")
            return None

        finally:
            db.disconnect()

    # Rechercher par référence
    def rechercher_par_reference(self, reference):
        db = DatabaseConnection()

        if not db.connect():
            return None

        try:
            sql = """
                SELECT id, reference, designation,
                       prix_unitaire, stock, date_creation
                FROM produit
                WHERE reference = %s
            """

            if not db.execute(sql, (reference,)):
                return None

            ligne = db.fetchone()

            if ligne:
                return Produit(
                    id=ligne[0],
                    reference=ligne[1],
                    designation=ligne[2],
                    prix_unitaire=ligne[3],
                    stock=ligne[4],
                    date_creation=ligne[5]
                )

            return None

        except Exception as e:
            print(f"Erreur lors de la recherche : {e}")
            return None

        finally:
            db.disconnect()

    # Rechercher par désignation
    def rechercher_par_designation(self, designation):
        db = DatabaseConnection()

        if not db.connect():
            return []

        try:
            sql = """
                SELECT id, reference, designation,
                       prix_unitaire, stock, date_creation
                FROM produit
                WHERE designation LIKE %s
            """

            if not db.execute(sql, (f"%{designation}%",)):
                return []

            resultats = db.fetchall()

            produits = []

            for ligne in resultats:
                produits.append(
                    Produit(
                        id=ligne[0],
                        reference=ligne[1],
                        designation=ligne[2],
                        prix_unitaire=ligne[3],
                        stock=ligne[4],
                        date_creation=ligne[5]
                    )
                )

            return produits

        except Exception as e:
            print(f"Erreur lors de la recherche : {e}")
            return []

        finally:
            db.disconnect()

    # Modifier un produit
    def update(self, produit):
        db = DatabaseConnection()

        if not db.connect():
            return False

        try:
            sql = """
                UPDATE produit
                SET reference = %s,
                    designation = %s,
                    prix_unitaire = %s,
                    stock = %s
                WHERE id = %s
            """

            params = (
                produit.reference,
                produit.designation,
                produit.prix_unitaire,
                produit.stock,
                produit.id
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

    # Supprimer un produit
    def delete_by_id(self, produit_id):
        db = DatabaseConnection()

        if not db.connect():
            return False

        try:
            # Vérifier si le produit apparaît dans une commande
            sql_check = """
                SELECT COUNT(*)
                FROM ligne_commande
                WHERE produit_id = %s
            """

            if not db.execute(sql_check, (produit_id,)):
                return False

            resultat = db.fetchone()

            if resultat[0] > 0:
                print(
                    "Impossible de supprimer ce produit : "
                    "il apparaît dans une commande."
                )
                return False

            sql = """
                DELETE FROM produit
                WHERE id = %s
            """

            if not db.execute(sql, (produit_id,)):
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

    # Alerte de stock
    def alerte_stock(self, seuil):
        db = DatabaseConnection()

        if not db.connect():
            return []

        try:
            sql = """
                SELECT id, reference, designation,
                       prix_unitaire, stock, date_creation
                FROM produit
                WHERE stock < %s
                ORDER BY stock
            """

            if not db.execute(sql, (seuil,)):
                return []

            resultats = db.fetchall()

            produits = []

            for ligne in resultats:
                produits.append(
                    Produit(
                        id=ligne[0],
                        reference=ligne[1],
                        designation=ligne[2],
                        prix_unitaire=ligne[3],
                        stock=ligne[4],
                        date_creation=ligne[5]
                    )
                )

            return produits

        except Exception as e:
            print(f"Erreur lors de l'alerte stock : {e}")
            return []

        finally:
            db.disconnect()