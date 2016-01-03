#Scrapper for Twitter data about users#

This is a simple python webservice designed to scrap
informations about a requested user. For now it runs on both Python2
and Python3, provided all libraries are present.

It is an exercise for learning [flask][flask] and has little to no
ambitions for now.

##Requirements##
- flask
- BeautifulSoup4
- requests

##Details##

This service reads the value sent along with the GET request
and searches for a user with that identificator on Twitter.
It then returns an HTML page with the data from that user.

If no user is found, it will return a warning.

##Usage##

If you execute scrapper.py, it will open by default a HTTP server
listening to port 5000. Once it is working, you can test it by
opening the page in your browser by requesting http://127.0.0.1:5000.
It should return a warning saying that you should type in some username.

Another way to run the server is through the manage.py. It has little use
for now, but as the project grows it might be needed to deal with stored
data.

If all works, you can try requesting a particular user by requesting
http://127.0.0.1:5000/some-user, where "some-user" is the username.

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
