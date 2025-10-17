# Point d’entrée de l’app

from app import create_app

app = create_app()

if __name__ == "__main__":
    # debug True pour développement local (désactiver en production)
    app.run(debug=True)