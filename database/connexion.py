import psycopg2
import mysql.connector
from database.config import TYPE_BD, MYSQL

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = None
            cls._instance.cursor = None
        return cls._instance

    def connect(self):
        # Etablir la connexion BD
        try:
            if TYPE_BD == "mysql":
                self.connection = mysql.connector.connect(
                    host=MYSQL["host"],
                    port=MYSQL["port"],
                    database=MYSQL["database"],
                    user=MYSQL["user"],
                    password=MYSQL["password"]
                )
                print("Connexion réussie à MySQL")
            else:
                print("Erreur de connexion à la base")
                return False

            self.cursor = self.connection.cursor()
            return True

        except Exception as e:
            print(f"Erreur de connexion : {e}")
            return False

    def disconnect(self):
        # Fermer la connexion BD
        if self.cursor:
            self.cursor.close()

        if self.connection:
            self.connection.close()
            print("Connexion fermée")

    def commit(self):
        # Validation des modifications
        self.connection.commit()

    def rollback(self):
        # Annulation des modifications
        self.connection.rollback()

    def execute(self, query, params=None):
        try:
            self.cursor.execute(query, params or ())
            return True
        except Exception as e:
            print(f"Erreur SQL : {e}")
            return False

    def fetchall(self):
        # Retourner tous les résultats
        return self.cursor.fetchall()

    def fetchone(self):
        # Retourner un seul résultat
        return self.cursor.fetchone()