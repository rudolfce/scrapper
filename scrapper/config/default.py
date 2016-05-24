SQLALCHEMY_DATABASE_URI = "postgresql://rudolf:some_password@localhost/scrapper_test"
SQLALCHEMY_TRACK_MODIFICATIONS = True
DEBUG = True
CELERY_BROKER_URL='redis://localhost:6379',
CELERY_RESULT_BACKEND='redis://localhost:6379'
