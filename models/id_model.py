import sys
from sqlalchemy import BigInteger, Column, String
from models.db import Base, ENGINE


class Id(Base):
    """IDテーブル"""
    __tablename__ = 'id_table'
    id_name = Column('id_name', String(200), nullable=False, primary_key=True)
    id_count = Column('id_count', BigInteger, nullable=False)


def create_id(args):
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    create_id(sys.argv)
