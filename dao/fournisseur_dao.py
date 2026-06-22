from database.connexion import DatabaseConnection
from models.fournisseur import Fournisseur
from dao.base_dao import BaseDAO


class FournisseurDAO(BaseDAO):

    def ajouter(self, fournisseur):
        db = DatabaseConnection()

        if not db.connect():
            return False

        sql = """
        INSERT INTO fournisseur
        (code, raison_sociale, email, telephone, adresse)
        VALUES (%s,%s,%s,%s,%s)
        """

        ok = db.execute(sql, (
            fournisseur.code,
            fournisseur.raison_sociale,
            fournisseur.email,
            fournisseur.telephone,
            fournisseur.adresse
        ))

        if ok:
            db.commit()

        db.disconnect()
        return ok

    def get_all(self):
        db = DatabaseConnection()

        if not db.connect():
            return []

        sql = """SELECT * FROM fournisseur"""

        db.execute(sql)
        resultats = db.fetchall()

        db.disconnect()

        fournisseurs = []

        for ligne in resultats:
            fournisseur = Fournisseur(
                id=ligne[0],
                code=ligne[1],
                raison_sociale=ligne[2],
                email=ligne[3],
                telephone=ligne[4],
                adresse=ligne[5],
                date_creation=ligne[6]
            )

            fournisseurs.append(fournisseur)

        return fournisseurs

    def get_by_id(self, id):
        db = DatabaseConnection()

        if not db.connect():
            return None

        sql = """SELECT * FROM fournisseur WHERE id=%s"""

        db.execute(sql, (id,))
        ligne = db.fetchone()

        db.disconnect()

        if ligne:
            return Fournisseur(
                id=ligne[0],
                code=ligne[1],
                raison_sociale=ligne[2],
                email=ligne[3],
                telephone=ligne[4],
                adresse=ligne[5],
                date_creation=ligne[6]
            )

        return None

    def delete_by_id(self, id):
        db = DatabaseConnection()

        if not db.connect():
            return False

        sql_check = """
        SELECT COUNT(*) FROM commande
        WHERE fournisseur_id=%s
        """

        db.execute(sql_check, (id,))
        nb_commandes = db.fetchone()[0]

        if nb_commandes > 0:
            db.disconnect()
            print("Impossible de supprimer ce fournisseur : des commandes sont associées.")
            return False

        sql = """DELETE FROM fournisseur WHERE id=%s"""

        ok = db.execute(sql, (id,))

        if ok:
            db.commit()

        db.disconnect()
        return ok

    def update(self, fournisseur):
        db = DatabaseConnection()

        if not db.connect():
            return False

        sql = """
        UPDATE fournisseur
        SET code=%s,
            raison_sociale=%s,
            email=%s,
            telephone=%s,
            adresse=%s
        WHERE id=%s
        """

        ok = db.execute(sql, (
            fournisseur.code,
            fournisseur.raison_sociale,
            fournisseur.email,
            fournisseur.telephone,
            fournisseur.adresse,
            fournisseur.id
        ))

        if ok:
            db.commit()

        db.disconnect()
        return ok

    def rechercher_par_code(self, code):
        db = DatabaseConnection()

        if not db.connect():
            return None

        sql = """SELECT * FROM fournisseur WHERE code=%s"""

        db.execute(sql, (code,))
        ligne = db.fetchone()

        db.disconnect()

        if ligne:
            return Fournisseur(
                id=ligne[0],
                code=ligne[1],
                raison_sociale=ligne[2],
                email=ligne[3],
                telephone=ligne[4],
                adresse=ligne[5],
                date_creation=ligne[6]
            )

        return None

    def rechercher_par_raison_sociale(self, raison_sociale):
        db = DatabaseConnection()

        if not db.connect():
            return []

        sql = """
        SELECT * FROM fournisseur
        WHERE raison_sociale LIKE %s
        """

        db.execute(sql, (f"%{raison_sociale}%",))
        resultats = db.fetchall()

        db.disconnect()

        fournisseurs = []

        for ligne in resultats:
            fournisseur = Fournisseur(
                id=ligne[0],
                code=ligne[1],
                raison_sociale=ligne[2],
                email=ligne[3],
                telephone=ligne[4],
                adresse=ligne[5],
                date_creation=ligne[6]
            )

            fournisseurs.append(fournisseur)

        return fournisseurs