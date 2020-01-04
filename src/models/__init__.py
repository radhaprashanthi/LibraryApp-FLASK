from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# initialize our db
db = SQLAlchemy()

# encrypting user password
bcrypt = Bcrypt()
