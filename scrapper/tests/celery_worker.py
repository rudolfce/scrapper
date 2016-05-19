from scrapper import create_app, make_celery
import scrapper.controllers.miner

flask_app = create_app('scrapper.config.testing')
celery = make_celery(flask_app)
