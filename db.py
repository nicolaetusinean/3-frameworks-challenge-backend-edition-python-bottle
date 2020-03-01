from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from bottle.ext.sqlalchemy import SQLAlchemyPlugin
from models import Base


def setup_db(app):
    engine = create_engine('sqlite:///:memory:', echo=True)
    create_session = sessionmaker(bind=engine)

    app.install(SQLAlchemyPlugin(engine, Base.metadata, create=True, create_session=create_session))

    Base.metadata.create_all(engine)
