# Lecture #17 - Flask

![Flask icon](http://flask.pocoo.org/docs/_static/flask.png)

## External Resources
This Flask application was cribbed heavily from the [Flaskr Tutorial](http://flask.pocoo.org/docs/tutorial/introduction/). The [Flask Mega-Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) is also fantastic, and much more in-depth if you are looking for greater challenges and experience.

## The Goal
We will be developing a classifier to predict an artist based on song lyrics. The training data comes from the [Million Song Dataset](http://labrosa.ee.columbia.edu/millionsong/) and has been limited to knowledge of The Beatles, The Rolling Stones, and Lady Gaga.

After this lesson, you will have created a web application that lets users input lyrics and get back one of those three artists. In the process, you will have created a reusable classifier.


## New Terminology
General Web Terms:

* [Cookies](http://en.wikipedia.org/wiki/HTTP_cookie)
* [Sessions](http://stackoverflow.com/questions/3804209/what-are-sessions-how-do-they-work)
* [Cascading Style Sheets](http://www.w3schools.com/css/css_intro.asp)

Flask Terms:

* Templates
	* [Jinja2](http://jinja.pocoo.org/)
* Contexts
	* [Application](http://flask.pocoo.org/docs/appcontext/)
	* [Request](http://flask.pocoo.org/docs/reqcontext/)
* [Message Flashing](http://flask.pocoo.org/docs/patterns/flashing/)
	* Not the same as Adobe Flash!

New SQL Terms:

* Schema

New Python Terms:

* [Pickle](https://wiki.python.org/moin/UsingPickle)
* [Decorators](http://www.artima.com/weblogs/viewpost.jsp?thread=240808)

## Explore the Project Folder Structure

	$ unzip lyricsapp_skeleton.zip
	$ cd lyricsapp
	$ ls
	lyrics.csv		lyrics_classifier.py		lyricsapp.py         msd                  	schema.sql      static               		templates
	
The ``templates`` and ``static`` directories for Flask. The ``msd`` directory contains helper Python routines to ensure input lyrics are stemmed the same way as in the Million Song Dataset.

	
## Create a Reusable Classifier
Open lyrics_classifier.py. The skeleton has all of the definitions but most need to be populated.

	"""Lyrics classifier for Flask application"""
	
	# Our familiar imports	
	import pandas as pd
	from sklearn.feature_extraction.text import CountVectorizer
	from sklearn.naive_bayes import MultinomialNB

	# A new import
	import pickle
	
	# Local imports for the Million Song Dataset stemming algorithm
	from msd.stem import transformLyrics

	class LyricsClf():
		"""A MultinomialNB classifier for predicting artists from lyrics.
		Offers train, save, and load routines for offline and startup
		purposes. Offers predictArtist for online use.
		"""
		def __init__(self,picklefile=None):
			"""Constructor that creates an empty artistLabels dictionary,
			a CountVectorizer placeholder, and a classifier placeholder.
			If a picklefile is specified, the returned object is instantiated
	        from a pickled version on disk.
			"""
		...
		

## Test LyricsClf
We will use our new class right from the Python interpreter. After showing that it works, we will pickle it for use with the web app.

	$ python
	>>> from lyrics_classifier import LyricsClf
	>>> lclf = LyricsClf()
	>>> lclf.train('lyrics.csv')
	>>> lclf.predictArtist("i want to hold your hand")
	'The Beatles'
	>>> lclf.save('classifier.p')
	>>> quit()
	
## Review the Basic Web App Database Routines 
Some database code is already written for you. Take a look at ``connect_db``, ``get_db`` and ``init_db`` within ``lyricsapp.py``.

## Prepare the Database from the Schema (5 mins)
Here is where we create a sqlite3 database file from our schema.

	$ python
	>>> from lyricsapp import init_db
	>>> init_db()
	
You may wish to try this if you have the sqlite3 utility installed:

	$ sqlite3 lyrics.db
	SQLite version 3.7.13 2012-07-17 17:46:21
	Enter ".help" for instructions
	Enter SQL statements terminated with a ";"
	sqlite> .tables
	predictions
	sqlite> PRAGMA table_info(predictions);
	0|id|integer|0||1
	1|lyrics|text|1||0
	2|artist|text|1||0
	sqlite> .quit
	
## First test of the App
The application should load and present the interface, but the prediction form shouldn't do anything because the ``/add`` endpoint is incomplete.

	$ python lyricsapp.py
	 * Running on http://127.0.0.1:5000/
	 * Restarting with reloader

## Build the Views
Finish ``show_predictions()`` and ``add_prediction()`` inside ``lyricsapp.py``.

## Run the App!
Run the application now and it should work:

	$ python lyricsapp.py
	 * Running on http://127.0.0.1:5000/
	 * Restarting with reloader

## Lyric Cribsheet
Use any of these to test predictions if you're short on ideas:

	i want your love and i want your revenge you and me could have a bad romance

	yellow submarine octopus penny lane hold your hand woke up got out of bed

	sweet virginia tumbling dice crossfire hurricane

	once upon a time you dressed so fine threw the bums a dime in your prime didn't you
 
	once upon a time you dressed so fine how does it feel to be on your own like a

	yo vip let's kick it ice ice baby stop collaborate and listen
	
## Next Steps
Consider these questions:

* How would you add a login and logout feature to the application?
* How would you normalize the database to avoid redundancy in the artists column?
	* Consider how this may conflict with the way we mapped artists to labels in the ``LyricsClf`` class 