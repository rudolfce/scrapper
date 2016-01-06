#Scrapper for Twitter data about users#

This is a simple python webservice designed to scrap
informations about a requested user. It is designed to run on Python3,
but is still compatible with Python2 (or so I'm being misled to believe). 
It is an exercise for learning [flask][flask] and has little to no
ambitions for now.

##Requirements##
- Flask
- Flask-Script
- BeautifulSoup4
- requests
- psycopg2
- SQLAlchemy

Although psycopg2 is a requirement for SQLAlchemy, it must be installed manually
since pip does not does that automatically. Either way, it's in the requirements.txt.

##Details##

This service reads the value sent along with the GET request
and searches for a user with that identificator on Twitter.
It then returns an HTML page with the data from that user.

If no user is found, it will return a warning.

##Configuration##

Every necessary library is in the requirements.txt file. Since I had no time
to look for versions, I'll keep them fixed. I suggest you run the server on a
Virtual Environment if any of the versions is wrong and you are lazy like me.
Really, I do suggest using a virtual environment.

```sh
pip install -r requirements.txt
```

Since I recently added database functionality, it is important to set the database
before launching. How to set up a database is not the matter for this readme - for that,
reference to your favourite database server's documentation. Future updates might include
automatic configuration, but I'm not certain yet - will work on it, for sure.

It is required that a table with name 'users' and the following columns:
- name - string compatible type;
- username - string compatible type;
- bio - string compatible type;
- location - string compatible type;
- query_date - string compatible type.

Once the database is set, the file db\_data.json must be edited to match the details of
your newly set environment. Since I use SQLAlchemy for database interface and use only
simple queries, it's quite likely that any database server supported by SQLAlchemy is
going to work out of the box.

##Usage##

If you execute scrapper.py, it will open by default a HTTP server
listening to port 5000. Once it is working, you can test it by
opening the page in your browser by requesting http://127.0.0.1:5000.
It should return a warning saying that you should type in some username
and a form. If you submit the form, the user will be scrapped and shown.
If this user is in the database, the local data will be shown instead (with
the option to refresh the entry).

Another way to run the server is through the manage.py. It has little use
for now, but as the project grows it might be needed to deal with stored
data.

##Changing html layout##

All the html used for now on this application is a small page called
index.html, located inside the templates folder. By default, flask
supports [Jinja2][jinja2] templates, and that's exactly what I used. If you are
interested on trying any different page layout, you should look into
that file.

This application will be improved with time to include more features
(and to cover more stuff to study as well).

[flask]: http://flask.pocoo.org/
[jinja2]: http://jinja.pocoo.org/
