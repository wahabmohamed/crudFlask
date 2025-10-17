# Initialise Flask et les extensions (DB, login…)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialiser les extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    # Importer les modèles après l'initialisation de db pour éviter l'importation circulaire
    from app.models.user import User

    # Importer et enregistrer les Blueprints
    from .controllers.auth_controller import auth_bp
    from .controllers.user_controller import user_bp
    from .controllers.product_controller import product_bp
    from .controllers.cart_controller import cart_bp
    from .controllers.home_controller import home_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(home_bp)

    # Loader pour Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    # Configurer la clé secrète pour les sessions
    app.secret_key = app.config['SECRET_KEY']

    return app