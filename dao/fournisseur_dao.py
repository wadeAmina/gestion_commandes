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
        pass

    def get_by_id(self, id):
        pass

    def delete_by_id(self, id):
        pass