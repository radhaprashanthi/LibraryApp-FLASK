from marshmallow import fields, Schema
import datetime
from . import db
from ..app import bcrypt

class ReaderModel(db.Model):
    """
    Reader Model
    """

    # table name
    __tablename__ = 'readers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    department = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.name = data.get('name')
        self.email = data.get('email')
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()
        self.department = data.get('department')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            if key == 'password':
                self.password = self.__generate_hash(value)
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def __generate_hash(self, password):
        return bcrypt.generate_password_hash(password, rounds=10).decode("utf-8")

    def check_hash(self, password):
        return bcrypt.check_password_hash(self.password, password)

    @staticmethod
    def get_all_readers():
        return ReaderModel.query.all()

    @staticmethod
    def get_one_reader(id):
        return ReaderModel.query.get(id)
