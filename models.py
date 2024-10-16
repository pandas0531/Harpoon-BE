# models.py
import uuid
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from datetime import date, datetime, timezone, timedelta

KST = timezone(timedelta(hours=9))

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    userid = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    correct_p = db.Column(db.Integer, default=0)
    miss_p = db.Column(db.Integer, default=0)
    my_score = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.now(KST).strftime('%Y-%m-%d %H:%M:%S')) 
    updated_at = db.Column(db.DateTime, default=datetime.now(KST).strftime('%Y-%m-%d %H:%M:%S'), onupdate=datetime.now(KST).strftime('%Y-%m-%d %H:%M:%S'))
    isadmin = db.Column(db.Boolean, default=False)
