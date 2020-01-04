# Description
Design Library Database application to manage the library using a computerized system where we can record various transactions like issue of books, return of books, addition of new books, addition of new students, etc. Books and student maintenance modules are also included in this system which would keep track of the students using the library and also a detailed description about the books a library contains.

# Data source:
A sample dataset containing user login details, books, readers, books issued and returned dates will be created.

# Tools:
Python, Flask, SQLAlchemy and Postgres.

# Core Features:
1. User Login/Sign up - Allows user(librarian) to login/sign up to the application.
2. 2. Add new book - This feature allows to add new books to the library. 
3. 3. Register new reader - This feature allows to add a new reader to the readers list in order to borrow books.
4. 4. Search for book availability - Gives information about available number of copies when searched by book id, name or author.

# Steps of Execution

1. Create flask application ( `app.py` )
2. Create run to run the application ( `run.py` )
3. Create sqlalchemy models to interact with database ( `models` )
4. Using flask migrate create data models on DB ( `manage.py` )
5. `python manage.py db init` - initialize the DB
6. `python manage.py db migrate` - create tables
7. `python manage.py db upgrade` - apply changes to DB, when we do any changes 
8. Create HTML pages (`templates`) to get user input and access them using GET and POST methods in flask application.
9. Create CSS to style each HTML pages of flask application (`static/styles`)
