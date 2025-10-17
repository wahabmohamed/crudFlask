import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev_secret_key_please_change")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "mysql+pymysql://root:@localhost/ecommerce_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False