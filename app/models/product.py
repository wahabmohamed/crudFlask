# Modèle Product (table produit)

from app import db
from datetime import datetime

class Product(db.Model):
    """
    Modèle Product correspondant à la table MySQL 'produit'.
    Champs:
      - id_p: clé primaire
      - type_p: type/catégorie du produit
      - designation_p: nom / désignation
      - prix_ht: prix hors taxe (DECIMAL)
      - date_in: date d'entrée
      - timeS_in: timestamp d'insertion automatique
      - stock_p: quantité en stock
    """
    __tablename__ = "produit"

    id_p = db.Column(db.Integer, primary_key=True)
    type_p = db.Column(db.String(100), nullable=False)
    designation_p = db.Column(db.String(255), nullable=False)
    prix_ht = db.Column(db.Numeric(10, 2), nullable=False)
    date_in = db.Column(db.Date, nullable=False)
    timeS_in = db.Column(db.DateTime, server_default=db.func.now())
    stock_p = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<Product {self.designation_p}>"

    def to_dict(self):
        """Retourne une représentation JSON-serializable du produit"""
        return {
            "id_p": self.id_p,
            "type_p": self.type_p,
            "designation_p": self.designation_p,
            "prix_ht": float(self.prix_ht),
            "date_in": self.date_in.isoformat() if self.date_in else None,
            "timeS_in": self.timeS_in.isoformat() if self.timeS_in else None,
            "stock_p": self.stock_p
        }