from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base


DATABASE = 'postgresql+psycopg2://{user}:{password}@{host}/{name}'.format(**{
    # set youer db config
    'user': '',
    'password': '',
    'host': '',
    'name': ''
})

ENGINE = create_engine(
    DATABASE,
    echo=True
)

session = scoped_session(
    sessionmaker(
        autoflush=True,
        bind=ENGINE,
        autocommit=False,
        expire_on_commit=False
        )
)

Base = declarative_base()
