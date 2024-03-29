from datetime import timedelta
import os

databaseUrl = os.environ["DATABASE_URL"]

class Config:
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://root:root@{databaseUrl}/auth"
    JWT_SECRET_KEY = "Mala_tajna"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
