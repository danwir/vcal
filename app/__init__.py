# Import flask and template operators
from flask import Flask, render_template
from flask_babel import Babel
# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# translations using flask babel
babel = Babel(app)

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('oops.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_draft.controllers import mod_draft as draft_module

# Register blueprint(s)
app.register_blueprint(draft_module)
# app.register_blueprint(xyz_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()