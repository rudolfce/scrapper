#-*- encoding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from scrapper.config.server import DIALECT, USER, PASSWORD, SERVER, DATABASE


db_url = "{}://{}:{}@{}/{}".format(DIALECT, USER, PASSWORD, SERVER, DATABASE)

engine = create_engine(db_url)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
