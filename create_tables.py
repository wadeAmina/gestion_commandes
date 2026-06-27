from database.connexion import DatabaseConnection


db = DatabaseConnection()

if db.connect():

    # Table fournisseur
    db.execute("""
    CREATE TABLE IF NOT EXISTS fournisseur (
        id INT AUTO_INCREMENT PRIMARY KEY,
        code VARCHAR(20) UNIQUE NOT NULL,
        raison_sociale VARCHAR(100) NOT NULL,
        email VARCHAR(100),
        telephone VARCHAR(20),
        adresse TEXT,
        date_creation DATE DEFAULT (CURRENT_DATE)
    )
    """)

    # Table produit
    db.execute("""
    CREATE TABLE IF NOT EXISTS produit (
        id INT AUTO_INCREMENT PRIMARY KEY,
        reference VARCHAR(20) UNIQUE NOT NULL,
        designation VARCHAR(100) NOT NULL,
        prix_unitaire DECIMAL(10,2) NOT NULL,
        stock INT NOT NULL,
        date_creation DATE DEFAULT (CURRENT_DATE)
    )
    """)

    # Table commande
    db.execute("""
    CREATE TABLE IF NOT EXISTS commande (
        id INT AUTO_INCREMENT PRIMARY KEY,
        numero VARCHAR(20) UNIQUE NOT NULL,
        date_commande DATE DEFAULT (CURRENT_DATE),
        fournisseur_id INT NOT NULL,
        montant_total DECIMAL(10,2),
        statut ENUM('EN_ATTENTE','VALIDEE','LIVREE','ANNULEE'),
        date_creation DATE DEFAULT (CURRENT_DATE),

        CONSTRAINT fk_fournisseur
        FOREIGN KEY (fournisseur_id)
        REFERENCES fournisseur(id)
    )
    """)

    # Table ligne_commande
    db.execute("""
    CREATE TABLE IF NOT EXISTS ligne_commande (
        id INT AUTO_INCREMENT PRIMARY KEY,
        commande_id INT NOT NULL,
        produit_id INT NOT NULL,
        quantite INT NOT NULL,
        prix_unitaire DECIMAL(10,2) NOT NULL,

        CONSTRAINT fk_commande
        FOREIGN KEY (commande_id)
        REFERENCES commande(id),

        CONSTRAINT fk_produit
        FOREIGN KEY (produit_id)
        REFERENCES produit(id)
    )
    """)

    db.commit()
    print("Toutes les tables ont été créées avec succès.")

    db.disconnect()

else:
    print("Impossible de se connecter à la base de données.")