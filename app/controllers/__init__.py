# Ce fichier centralise tous les Blueprints pour simplifier l'import dans l'application.

# centralisation des blueprints
from .auth_controller import auth_bp
from .user_controller import user_bp
from .product_controller import product_bp
from .cart_controller import cart_bp
from .home_controller import home_bp

# On pourra les enregistrer dans app/__init__.py via:
# app.register_blueprint(auth_bp)
# app.register_blueprint(user_bp)
# app.register_blueprint(product_bp)
# app.register_blueprint(cart_bp)