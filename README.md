# 📦 Gestion des Commandes

## 📌 Présentation du projet

**Gestion des Commandes** est une application développée en **Python** permettant de gérer les fournisseurs, les produits et les commandes d'une entreprise.

L'application fonctionne en mode **console (CLI)** et utilise une base de données **MySQL**.

Le projet a été réalisé dans le cadre de notre formation en **Informatique Appliquée à la Gestion des Entreprises (IAGE)**.

---
[connexion.py](database/connexion.py)
## 🎯 Objectifs

L'application permet de :

* Gérer les fournisseurs
* Gérer les produits
* Gérer les commandes
* Gérer les lignes de commande
* Contrôler les stocks
* Calculer les montants des commandes
* Gérer les différents statuts des commandes
* Consulter des rapports et statistiques
* Utiliser une architecture organisée avec les modèles, DAO, base de données et interface

---

## ⚙️ Fonctionnalités principales

### 👥 Gestion des fournisseurs

* Ajouter un fournisseur
* Afficher les fournisseurs
* Rechercher un fournisseur
* Modifier un fournisseur
* Supprimer un fournisseur

### 📦 Gestion des produits

* Ajouter un produit
* Afficher les produits
* Rechercher un produit
* Modifier un produit
* Supprimer un produit
* Gérer les alertes de stock

### 🛒 Gestion des commandes

* Créer une commande
* Afficher les commandes
* Rechercher une commande
* Ajouter une ligne de commande
* Afficher le détail d'une commande
* Calculer le montant total
* Vérifier le stock
* Valider une commande
* Livrer une commande
* Annuler une commande
* Supprimer une commande
* Afficher les commandes en attente
* Rechercher les commandes par fournisseur

### 📊 Rapports et statistiques

* Valeur totale du stock
* Top 5 des produits les plus commandés
* Chiffre d'affaires total
* Nombre de commandes
* Nombre de produits
* Nombre de fournisseurs

---

## 🗄️ Base de données

La base de données **MySQL** est composée de quatre tables :

```text
fournisseur
     │
     ▼
commande ───────► ligne_commande ◄────── produit
```

### Tables utilisées

* `fournisseur`
* `produit`
* `commande`
* `ligne_commande`

Les relations entre les tables sont assurées par des **clés primaires et des clés étrangères**.

---

## 🛠️ Technologies utilisées

* Python
* MySQL
* MySQL Connector
* Programmation Orientée Objet (POO)
* DAO (Data Access Object)
* Git
* GitHub

---

## 📁 Structure du projet

```text
gestion_commandes/
│
├── dao/
│   ├── base_dao.py
│   ├── fournisseur_dao.py
│   ├── produit_dao.py
│   ├── commande_dao.py
│   ├── ligne_commande.py
│   └── rapport_dao.py
│
├── database/
│   ├── connexion.py
│   └── create_tables.py
│
├── menu/
│   └── interface.py
│
├── models/
│   ├── fournisseur.py
│   ├── produit.py
│   ├── commande.py
│   └── ligne_commande.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 👨‍💻 Répartition du travail

Le projet a été réalisé par quatre membres. Chaque membre est responsable d'une partie précise du projet.

| Membre               | Partie gérée                                                      |
| -------------------- | ----------------------------------------------------------------- |
| **Aminata Wade**     | Interface utilisateur, base de données et gestion du dépôt GitHub |
| **Khoudia**          | Gestion des commandes, `commande_dao.py` et `ligne_commande.py`   |
| **Mouhamed Mbaye**   | Gestion des produits, `produit_dao.py` et `rapport_dao.py`        |
| **Soukeynaa Ndiaye** | Gestion des fournisseurs et `fournisseur_dao.py`                  |

### 👩‍💻 Aminata Wade

Responsable de :

* La conception et la gestion de la base de données
* La création des tables
* La connexion à MySQL
* L'interface utilisateur dans `menu/interface.py`
* L'intégration des différents modules
* La gestion du projet sur GitHub
* Les commits et la mise à jour du dépôt

### 👩‍💻 Khoudia

Responsable de la partie **commandes** :

* `models/commande.py`
* `models/ligne_commande.py`
* `dao/commande_dao.py`
* `dao/ligne_commande.py`

Fonctionnalités principales :

* Création des commandes
* Gestion des lignes de commande
* Calcul du montant total
* Vérification du stock
* Validation
* Livraison
* Annulation
* Suppression des commandes

### 👨‍💻 Mouhamed Mbaye

Responsable de la partie **produits et rapports** :

* `models/produit.py`
* `dao/produit_dao.py`
* `dao/rapport_dao.py`

Fonctionnalités principales :

* Ajout des produits
* Affichage des produits
* Recherche
* Modification
* Suppression
* Alertes de stock
* Rapports et statistiques
* Calcul de la valeur du stock
* Top 5 des produits les plus commandés
* Chiffre d'affaires
* Statistiques générales

### 👩‍💻 Soukeyna Ndiaye

Responsable de la partie **fournisseurs** :

* `models/fournisseur.py`
* `dao/fournisseur_dao.py`

Fonctionnalités principales :

* Ajout des fournisseurs
* Affichage
* Recherche par ID
* Recherche par code
* Recherche par raison sociale
* Modification
* Suppression

---

## 🏗️ Architecture du projet

Le projet est organisé selon plusieurs couches :

### `models/`

Contient les classes représentant les différentes entités du système :

* Fournisseur
* Produit
* Commande
* Ligne de commande

### `dao/`

Contient les classes permettant d'effectuer les opérations avec la base de données.

### `database/`

Contient les éléments liés à la base de données et à la connexion MySQL.

### `menu/`

Contient l'interface console permettant à l'utilisateur d'interagir avec l'application.

### `main.py`

Point d'entrée principal de l'application.

---

## 🚀 Installation

### 1. Cloner le projet

```bash
git clone https://github.com/wadeAmina/gestion_commandes.git
```

### 2. Accéder au projet

```bash
cd gestion_commandes
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configurer MySQL

Créer la base de données `gestion_commandes` et vérifier les paramètres de connexion dans :

```text
database/connexion.py
```

### 5. Créer les tables

Exécuter le fichier :

```text
database/create_tables.py
```

### 6. Lancer l'application

```bash
python main.py
```

---

## 🔗 Gestion du projet

Le développement du projet a été réalisé avec **Git et GitHub** afin de :

* Suivre les modifications du code
* Effectuer des commits
* Collaborer entre les membres
* Centraliser le projet
* Conserver l'historique des modifications

---

## 📄 Licence

Projet réalisé dans un cadre académique.
