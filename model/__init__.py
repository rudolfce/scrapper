import json
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_data = open('config/db_data.json').read()
db_data = json.loads(db_data)

db_url = "%s://%s:%s@%s/%s" % (db_data['dialect'], db_data['user'], db_data['password'],
                               db_data['server'], db_data['database'])

engine = create_engine(db_url)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
