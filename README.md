# crudFlask — Mini application e-commerce en Flask

Application web e-commerce développée avec **Flask** (Python), organisée selon une architecture
**MVC**. Elle gère l'authentification des utilisateurs, un catalogue de produits, un panier
d'achat et les opérations **CRUD** (Create, Read, Update, Delete) associées.

---

## ✨ Fonctionnalités

- 🔐 **Authentification** — inscription, connexion et déconnexion des utilisateurs
- 📦 **Gestion des produits** — création, consultation, modification et suppression (CRUD)
- 🛒 **Panier d'achat** — ajout et gestion des produits sélectionnés
- 👤 **Gestion des utilisateurs** — comptes et profils
- 🗄️ **Base de données** avec migrations versionnées (SQLAlchemy / Flask-Migrate)
- ✅ **Tests** unitaires

## 🏗️ Architecture (MVC)

```
crudFlask/
├── app/
│   ├── controllers/     # Routes et logique métier (auth, cart, product, user, home)
│   ├── models/          # Modèles de données SQLAlchemy (User, Product)
│   ├── forms/           # Formulaires et validation (WTForms)
│   ├── templates/       # Vues HTML (Jinja2)
│   ├── static/          # CSS, JavaScript, images
│   ├── utils/           # Fonctions utilitaires
│   └── __init__.py      # Initialisation de l'application Flask (factory)
├── migrations/          # Migrations de la base de données
├── tests/               # Tests unitaires
├── config.py            # Configuration (dev / prod)
├── requirements.txt     # Dépendances Python
└── run.py               # Point d'entrée de l'application
```

## 🛠️ Technologies

- **Python** · **Flask**
- **SQLAlchemy** (ORM) · **Flask-Migrate** (migrations)
- **WTForms** (formulaires et validation)
- **Jinja2** (templates) · HTML / CSS

## 🚀 Installation & lancement

```bash
# 1. Cloner le dépôt
git clone https://github.com/wahabmohamed/crudFlask.git
cd crudFlask

# 2. Créer un environnement virtuel
python -m venv venv
source venv/bin/activate        # Windows : venv\Scripts\activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Initialiser la base de données
flask db upgrade

# 5. Lancer l'application
python run.py
```

L'application est ensuite accessible sur http://127.0.0.1:5000/

## 📄 Configuration

Les paramètres (clé secrète, URL de la base de données, etc.) sont définis dans `config.py`.
Il est recommandé d'utiliser des variables d'environnement pour les valeurs sensibles.

---

Projet réalisé par [Mohamed Wahab](https://github.com/wahabmohamed).
