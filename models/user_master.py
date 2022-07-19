import sys
from sqlalchemy import Column, String, BigInteger, TIMESTAMP
from models.db import Base, ENGINE


class UserMaster(Base):
    """ユーザーテーブル"""
    __tablename__ = 'user_master'
    user_id = Column('user_id', String(200), nullable=False, primary_key=True)
    name = Column('name', String(200), nullable=False)
    email = Column('email', String(256), nullable=False)
    password = Column('password', String(100), nullable=False)
    lock_fag = Column('lock_flag', String(
        1), server_default="0", nullable=False)
    miss_count = Column('miss_count', BigInteger,
                        server_default="0", nullable=False)
    init_fag = Column('init_flag', String(
        1), server_default="0", nullable=False)
    auth_id = Column('auth_id', String(200), nullable=False)
    delete_flag = Column('delete_flag', String(1), server_default="0")
    changer = Column('changer', String(200), nullable=False)
    create_time = Column('create_time', TIMESTAMP, nullable=False)
    update_time = Column('update_time', TIMESTAMP, nullable=False)


def create_user(args):
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    create_user(sys.argv)
