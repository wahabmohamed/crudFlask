# app/models/user.py
from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    first_name = db.Column(db.String(150), nullable=True)
    last_name = db.Column(db.String(150), nullable=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), default="user")

    def set_password(self, password_plain: str):
        self.password = generate_password_hash(password_plain)

    def check_password(self, password_plain: str) -> bool:
        return check_password_hash(self.password, password_plain)

    def __repr__(self):
        return f"<User {self.username}>"

    @property
    def is_admin(self):
        return self.role == "admin"