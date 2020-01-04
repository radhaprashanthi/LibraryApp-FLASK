from marshmallow import fields, Schema
import datetime
from . import db

from .BookModel import BookModel

class BooksBorrowedModel(db.Model):
    """
    Book Borrowed Model
    """

    # table name
    __tablename__ = 'books_borrowed'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), nullable=False)
    title = db.Column(db.String(128), nullable=False)
    author = db.Column(db.String(128), nullable=False)
    department = db.Column(db.String(128), nullable=False)
    issued_on = db.Column(db.DateTime, nullable=False)
    return_by = db.Column(db.DateTime)


    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.book_id = data.get('book_id')
        self.email = None
        self.title = None
        self.author = None
        self.department = None
        self.issued_on = datetime.datetime.utcnow()

    def save(self):
        for i in BookModel.query.all():
            if i.book_id == self.book_id:
                existing = BookdBorrowedModel.query.filter_by(
                    email=self.email,
                    title=self.title,
                    author=self.author,
                    department=self.department,
                    issued_on=self.issued_on)
                date_1 = datetime.datetime.strptime(self.issued_on, "%Y-%m-%d")
            if existing:
                existing.update({'return_by': date_1 + datetime.timedelta(days=15)})
                update_books = BookModel.query.filter_by(title=self.title).first()
                if update_books:
                    update_books.update({'copies': BookModel.copies - 1})


    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
            db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_books_borrowed():
        return BooksBorrowedModel.query.all()

    @staticmethod
    def get_books_borrowed(book_id):
        return BooksBorrowedModel.query.get(book_id)

    def __repr(self):
        return '<id {}>'.format(self.id)
