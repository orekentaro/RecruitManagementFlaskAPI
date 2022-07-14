import sys
from sqlalchemy import BigInteger, Column, String
from models.db import Base, ENGINE


class AuthMaster(Base):
    """権限マスタ"""
    __tablename__ = 'auth_master'
    auth_id = Column('auth_id', BigInteger, nullable=False, primary_key=True)
    auth = Column('auth', String(200), nullable=False)


def create_auth(args):
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    create_auth(sys.argv)
