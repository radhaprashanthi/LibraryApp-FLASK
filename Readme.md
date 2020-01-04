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
