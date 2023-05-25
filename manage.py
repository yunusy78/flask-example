from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app1 = Flask(__name__)
app1.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://b5f74bf9c03a63:3a96461f@us-cdbr-east-06.cleardb.net/heroku_66e39329c433106'
app1.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app1)
migrate = Migrate(app1, db)
# User model
class users(db.Model):
    user_id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    def __init__(self, name, email):
        self.name = name
        self.email = email

# Note model
class notes(db.Model):
    note_id = db.Column(db.String(255), primary_key=True)
    user_id = db.Column(db.String(255), db.ForeignKey('user.user_id'), nullable=False)
    timestamp = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp())
    note = db.Column(db.Text, nullable=False)

    user = db.relationship('User', backref=db.backref('notes', cascade='all, delete'))

    def __init__(self, user_id, note):
        self.user_id = user_id
        self.note = note


# Image model
class images(db.Model):
    image_id = db.Column(db.String(255), primary_key=True)
    user_id = db.Column(db.String(255), db.ForeignKey('user.user_id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp())

    user = db.relationship('User', backref=db.backref('images', cascade='all, delete'))

    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

        if __name__ == '__manage__':
            app1.run()