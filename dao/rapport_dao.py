from database.connexion import DatabaseConnection


class RapportDAO:

    # Valeur totale du stock
    def valeur_totale_stock(self):
        db = DatabaseConnection()

        if not db.connect():
            return 0

        try:
            sql = """
                SELECT COALESCE(
                    SUM(prix_unitaire * stock), 0
                )
                FROM produit
            """

            db.execute(sql)
            resultat = db.fetchone()

            return resultat[0] or 0

        except Exception as e:
            print(f"Erreur : {e}")
            return 0

        finally:
            db.disconnect()

    # Top 5 des produits les plus commandés
    def top5_produits(self):
        db = DatabaseConnection()

        if not db.connect():
            return []

        try:
            sql = """
                SELECT
                    p.reference,
                    p.designation,
                    SUM(lc.quantite) AS total
                FROM produit p
                INNER JOIN ligne_commande lc
                    ON p.id = lc.produit_id
                GROUP BY
                    p.id,
                    p.reference,
                    p.designation
                ORDER BY total DESC
                LIMIT 5
            """

            db.execute(sql)
            return db.fetchall()

        except Exception as e:
            print(f"Erreur : {e}")
            return []

        finally:
            db.disconnect()

    # Chiffre d'affaires total
    def chiffre_affaires_total(self):
        db = DatabaseConnection()

        if not db.connect():
            return 0

        try:
            sql = """
                SELECT COALESCE(
                    SUM(montant_total), 0
                )
                FROM commande
                WHERE statut IN ('VALIDEE', 'LIVREE')
            """

            db.execute(sql)
            resultat = db.fetchone()

            return resultat[0] or 0

        except Exception as e:
            print(f"Erreur : {e}")
            return 0

        finally:
            db.disconnect()

    # Nombre de commandes
    def nombre_commandes(self):
        db = DatabaseConnection()

        if not db.connect():
            return 0

        try:
            sql = """
                SELECT COUNT(*)
                FROM commande
            """

            db.execute(sql)
            resultat = db.fetchone()

            return resultat[0]

        except Exception as e:
            print(f"Erreur : {e}")
            return 0

        finally:
            db.disconnect()

    # Nombre de produits
    def nombre_produits(self):
        db = DatabaseConnection()

        if not db.connect():
            return 0

        try:
            sql = """
                SELECT COUNT(*)
                FROM produit
            """

            db.execute(sql)
            resultat = db.fetchone()

            return resultat[0]

        except Exception as e:
            print(f"Erreur : {e}")
            return 0

        finally:
            db.disconnect()

    # Nombre de fournisseurs
    def nombre_fournisseurs(self):
        db = DatabaseConnection()

        if not db.connect():
            return 0

        try:
            sql = """
                SELECT COUNT(*)
                FROM fournisseur
            """

            db.execute(sql)
            resultat = db.fetchone()

            return resultat[0]

        except Exception as e:
            print(f"Erreur : {e}")
            return 0

        finally:
            db.disconnect()