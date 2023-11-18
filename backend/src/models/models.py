from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False) 
    email = db.Column(db.String(200), unique=True, nullable=False)
    created = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())
    comments = db.relationship('Comment', backref='user', lazy=True)

    def __init__(self, username, email) -> None:
        self.username = username
        self.email = email

class Query(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    qy_name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    description = db.Column(db.String(255))
    parameters = db.Column(db.String(255), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    comments = db.relationship('Comment', backref='query', lazy=True)

    def __init__(self, qy_name, user_id, description, parameters) -> None:
        self.qy_name = qy_name
        self.user_id = user_id
        self.description = description
        self.parameters = parameters

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    query_id = db.Column(db.Integer, db.ForeignKey('query.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, query_id, user_id, description) -> None:
        self.query_id = query_id
        self.user_id = user_id
        self.description = description
    
