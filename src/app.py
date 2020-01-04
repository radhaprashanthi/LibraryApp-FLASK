import os
from flask import Flask, flash, redirect, render_template, request
from flask_wtf.csrf import CsrfProtect
from .models import db, bcrypt
from .forms import RegisterForm

from .models.UserModel import UserModel
from .models.BookModel import BookModel
from .models.ReaderModel import ReaderModel
from .models.BooksBorrowedModel import BooksBorrowedModel


csrf = CsrfProtect()

def create_app():
    """
    Create app
    """

    # app initiliazation
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = ''
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY

    csrf.init_app(app)
    bcrypt.init_app(app)
    db.init_app(app)

    @app.route('/')
    def application():
        return render_template('application.html')

    @app.route('/readers/login')
    def readers_login():
        return render_template('readers_login.html')

    @app.route('/admin')
    def home():
        """Return login page"""
        return render_template('admin_login.html')

    @app.route('/login', methods = ['POST'])
    def do_admin_login():
        """Return admin functions if user exists if not return login page"""
        data = request.form
        users = UserModel.query.all()
        users_list = [(i.email, i.password) for i in users]
        for email_password in users_list:
            if email_password[0] == data['email'] and bcrypt.check_password_hash(email_password[1], data['password']):
                return render_template('admin_functions.html')
        else:
            return render_template('user_doesnt_exist.html')

    @app.route('/home_add_books')
    def home_add_books():
        """Return add books page"""
        return render_template('add_books.html')

    @app.route('/add_books', methods = ['GET', 'POST'])
    def add_books():
        data = request.form
        BookModel(data).save()
        return render_template('add_books.html')


    @app.route('/home_add_readers')
    def home_add_readers():
        """Return add readers page"""
        return render_template('add_readers.html')

    @app.route('/add_readers', methods = ['POST'])
    def add_readers():
        data = request.form
        try:
            ReaderModel(data).save()
            return render_template('add_readers.html')
        except Exception:
            db.session.rollback()
            flash('ERROR! Reader Email ({}) already exists.'.format(data['email']), 'error')

        return render_template('add_readers.html')

    @app.route('/show_books', methods = ['GET', 'POST'])
    def show_books():
        data = request.form
        print(data)
        if len(data) != 0:
            search_title = data['title_search']
            if search_title != "":
                return render_template('books_list.html',books = BookModel(data).query.filter(BookModel.title.like('%' + search_title + '%')))

        return render_template('books_list.html',books = BookModel(data).get_all_books())

    @app.route('/show_readers', methods = ['GET', 'POST'])
    def show_readers():
        data = request.form
        if len(data) != 0:
            search_reader = data['search_reader']
            if search_reader != "":
                return render_template('readers_list.html', readers = ReaderModel(data).query.filter(ReaderModel.email.like('%' + search_reader + '%')))

        return render_template('readers_list.html', readers=ReaderModel(data).get_all_readers())

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        form = RegisterForm(request.form)
        if request.method == 'POST' and form.validate():
            try:
                new_user = UserModel(request.form)
                new_user.authenticated = True
                new_user.save()
                flash('Thanks for registering!', 'success')
                return render_template('admin_login.html')
            except Exception:
                db.session.rollback()
                flash('ERROR! Email ({}) already exists.'.format(form.email.data), 'error')
        else:
            flash('Enter all details')
        return render_template('register.html', form=form)

    @app.route('/home_checkout_books', methods = ['GET', 'POST'])
    def home_checkout_books():
        """Return add books page"""
        data = request.form
        return render_template('checkout_books.html', books=BookModel(data).get_all_books())


    @app.route('/checkout_books', methods = ['GET', 'POST'])
    def checkout_books():
        data = request.form
        import pdb
        pdb.set_trace()
        print(data)
        BooksBorrowedModel(data).save()
        return render_template('checkout_books.html')
        # add to go back or logout button here

    @app.route('/admin_functions')
    def admin_functions():
        """Return admin functions page"""
        return render_template('admin_functions.html')

    @app.route('/show_borrowed_books', methods = ['GET', 'POST'])
    def show_borrowed_books():
        data = request.form
        print(data)
        if len(data) != 0:
            email = data['email']
            if email != "":
                return render_template('borrowed_books.html',books = BooksBorrowedModel(data).query.filter(BooksBorrowedModel.email.like('%' + email + '%')))

        return render_template('borrowed_books.html', books = BooksBorrowedModel(data).get_books_issued())

    @app.route('/reports')
    def reports():
        """Return admin functions page"""
        return render_template('reports.html')

    @app.route('/reports_department_books')
    def reports_department_books():
        """Return department books page"""
        return render_template('reports_department_books.html')

    @app.route('/reports_most_borrowed_books')
    def reports_most_borrowed_books():
        """Return admin functions page"""
        return render_template('reports.html')

    return app


