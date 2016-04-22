SQLALCHEMY_DATABASE_URI = "postgresql://rudolf:some_password@127.0.0.1/scrapper_temp"
SQLALCHEMY_TRACK_MODIFICATIONS = True
#DEBUG = True # Generates some problems with nosetests
CELERY_BROKER_URL='redis://localhost:6379',
CELERY_RESULT_BACKEND='redis://localhost:6379'
CELERY_ALWAYS_EAGER=True
TESTING=True
