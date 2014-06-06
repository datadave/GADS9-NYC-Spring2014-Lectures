"""A Flask web application that provides an interface to enter
lyrics and receive an artist prediction.
"""

# Standard imports
import os
import sqlite3

# Flask imports
from flask import Flask, request, g, redirect, url_for, render_template, flash

# Import our classifier class
from lyrics_classifier import LyricsClf

# create the app as a global variable
app = Flask(__name__)

# Specify a basic configuration
# (Remember that this step happens in the application context)
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'lyrics.db'),
    DEBUG=True,
    SECRET_KEY='my super secret string',
    CLF_PICKLE='classifier.p'
))

# Load our pickled classifier before servicing requests
clf = LyricsClf(app.config['CLF_PICKLE'])

def connect_db():
    """Connects to the database defined in the application configuration.
    Returns a sqlite3 object that allows rows to be manipulated as python
    dictionaries.
    """
    rv = sqlite3.connect(app.config['DATABASE'])
    # allows a row to be accessed as a dictionary rather than a tuple.
    rv.row_factory = sqlite3.Row
    return rv
# end of connect_db()

def init_db():
    """Initialize the database from schema.sql.
    This needs to be run once manually, or whenever the database table 
    should be dropped. This is not executed during online operation.
    """
    # establish the application context
    with app.app_context():
        # Open a connection to the database
        db = get_db()
        # Open schema.sql
        with app.open_resource('schema.sql','r') as f:
            # Execute the commands in the schema file
            db.cursor().executescript(f.read())
        # Write changes to the database
        db.commit()
# end of init_db()

def get_db():
    """Opens a new db connection if none exists for the current app context."""
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db
# end of get_db()

@app.teardown_appcontext
def close_db(error):
    """Closes the db at the end of the request.
    The flask app.teardown_appcontext decorator releases and destroys
    the back-end server resources. We just need to close the database.
    """
    # Note that we were using the global application object, g, to store
    # our open sqlite handle.
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()
# end of close_db()

# Views - Note how simple these endpoints are!
# We hardly need to consider the fact that we are operating online!

@app.route('/')
def show_predictions():
    """Main view to display all lyric/artist predictions.
    Returns them in descending order by id.
    """
    # TODO
    # Remember to change predictions=[] to predictions=<your prediction>
    return render_template('show_predictions.html', predictions=[])
# end of show_predictions()

@app.route('/add', methods=['POST'])
def add_prediction():
    """Predicts an artist based on the lyrics posted in the form.
    Finds the lyrics in the request object's form dictionary.
    Calls our classifier's predictArtist routine to return an artist
    name. Connects to the database and inserts the prediction.
    Flashes a message that the prediction was posted. Redirects the
    user from the /add endpoint back to the show_predictions endpoint.
    """
    # TODO
    return redirect(url_for('show_predictions'))
# end of add_prediction()

# This condition is true when we are executed as a python script. 
# It is not true if we are imported. This is how we can run:
# >>> from lyricsapp import init_db
# >>> init_db()
if __name__=="__main__":
    # Tell Flask to run!
    app.run()
