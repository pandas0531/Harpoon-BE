import uuid
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone, timedelta
from sqlalchemy.dialects.postgresql import UUID

KST = timezone(timedelta(hours=9))

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    userid = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    correct_p = db.relationship('Problem', secondary='correct_problems', backref='correct_users')
    miss_p = db.relationship('Problem', secondary='miss_problems', backref='miss_users')
    my_score = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.now(KST))
    updated_at = db.Column(db.DateTime, default=datetime.now(KST), onupdate=datetime.now(KST))
    isadmin = db.Column(db.Boolean, default=False)

class ProblemCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(2), unique=True)
    problems = db.relationship('Problem', backref='category')

class ProblemDifficulty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    problems = db.relationship('Problem', backref='difficulty')

class Problem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    description = db.Column(db.Text)
    file = db.Column(db.String(100))
    category_id = db.Column(db.Integer, db.ForeignKey('problem_category.id'))
    difficulty_id = db.Column(db.Integer, db.ForeignKey('problem_difficulty.id'))

# 중간 테이블 정의
correct_problems = db.Table('correct_problems',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('problem_id', db.Integer, db.ForeignKey('problem.id'), primary_key=True)
)

miss_problems = db.Table('miss_problems',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('problem_id', db.Integer, db.ForeignKey('problem.id'), primary_key=True)
)