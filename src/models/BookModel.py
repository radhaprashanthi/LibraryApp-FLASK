from marshmallow import fields, Schema
import datetime
from . import db

class BookModel(db.Model):
    """
    Book Model
    """

    # table name
    __tablename__ = 'books'

    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True, nullable=False)
    author = db.Column(db.String(128), nullable=False)
    department = db.Column(db.String(128), nullable=False)
    copies = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.title = data.get('title')
        self.author = data.get('author')
        self.department = data.get('department')
        self.copies = data.get('copies')
        self.created_at = datetime.datetime.utcnow()

    def save(self):
        existing = BookModel.query.filter_by(title=self.title).first()
        if existing:
            existing.update({'copies': BookModel.copies + int(self.copies) })
        else:
            db.session.add(self)
            db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
            db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_books():
        return BookModel.query.all()

    @staticmethod
    def get_books_by_title(title):
        return BookModel.query.filter(BookModel.title.like(title))

    @staticmethod
    def get_one_book(id):
        return BookModel.query.get(id)

    def __repr(self):
        return '<id {}>'.format(self.id)
