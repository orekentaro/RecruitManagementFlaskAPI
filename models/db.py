from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base


DATABASE = 'postgresql+psycopg2://{user}:{password}@{host}/{name}'.format(**{
    'user': 'nagatokentarou',
    'password': 'nagato8',
    'host': '127.0.0.1',
    'name': 'management_recruit'
})

ENGINE = create_engine(
    DATABASE,
    echo=True
)
db_session = scoped_session(
    sessionmaker(
        autoflush=True,
        bind=ENGINE,
        autocommit=False)
)

Base = declarative_base()
Base.query = db_session.query_property()
