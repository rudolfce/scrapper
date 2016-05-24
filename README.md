#Scrapper for Twitter data about users#

This is a simple python webservice designed to scrap
information about a requested user from Twitter. It is designed to run on Python3
and is an exercise for learning [flask][flask]; it has little to no
ambitions.

This study project features:

  * App factory behavior (eventhough there is only one app);
  * Celery workers;
  * SQL database interface with SQLAlchemy's ORM;
  * MVC architecture;
  * Unit Testing.

##Details##

This service reads the value sent along with the GET request
and searches for a user with that identificator on Twitter.
It then returns a json output with data from the user. It uses
requests for sending HTTP requests for Twitter and BeautifulSoup
to parse the received HTML.

Because of the assyncronous behaviour of the Celery workers,
the first time a user is requested it will return a 202 HTTP status,
and the string "Processing..." is sent. The scrapping function
searches for the user on twitter and then stores into a local
SQL database.

If the requested user is found in the database, it is returned with a
200 instead. If the user is found, but wasn't found in Twitter,
a 404 is returned with no data.

##Configuration##

Every necessary library is in the requirements.txt file. Since I had no time
to look for versions, I'll keep them fixed. I suggest you run the server on a
Virtual Environment if any of the versions is wrong.

```sh
$ virtualenv -p python3 env
(env) $ pip install -r requirements.txt
```

Depending on your system, SQL server or specific libraries, you might
need to install some packages from your package manager.

It is important to set the database before launching. To initialize the database,
first the config/db\_data.json must be set to match your preferences and the
server you have running. Once the settings are to your taste, you can run
the init\_db command from manage.py:

```sh
(env) $ ./manage.py init_db
```

Since I use SQLAlchemy interface and only simple queries, it's quite
likely that any database server supported by SQLAlchemy is
going to work out of the box.

###If you want to set the table manualy###

It is required that a table with name 'users' and the following columns:

* name - string compatible type;
* username - string compatible type;
* bio - string compatible type;
* location - string compatible type;
* query\_date - string compatible type;
* exists - boolean compatible type.

##Usage##

The scrapping function is a Celery task, and relies on Celery workers to run.
To spawn a worker, its module must be passed to the celery script like so:

```sh
(env) $ celery -A scrapper.controllers.miner worker
```

This will spawn a worker in the current shell. The stderr output will be sent
to this shell if necessary.

To get the server to work, the manage.py has everything it needs to start. The runserver
command starts a server on port 5000 by default. The default settings
set Flask to run in debug mode, but this behaviour can be changed.

```sh
(env) $ ./manage.py runserver
```

Once it is working, you can test it by
opening the page in your browser by requesting http://127.0.0.1:5000.
It should send you to /twitter/ and return a 400 (BAD REQUEST). This
behavior must be changed if another app is added to the factory.

You can then add to the URL the user you want to look for after the
last slash. To look for flubbercwb, you can try:

http://127.0.0.1:5000/twitter/flubbercwb

[flask]: http://flask.pocoo.org/
