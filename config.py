# config.py
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'your_secret_key'  # 세션 및 보안을 위한 키
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')  # SQLite 데이터베이스 경로