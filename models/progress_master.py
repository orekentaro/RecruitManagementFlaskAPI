import sys
from sqlalchemy import TIMESTAMP, Column, String, Text
from models.db import Base, ENGINE


class ProgressMaster(Base):
    """進捗マスタ"""
    __tablename__ = 'progress_master'
    progress_id = Column('progress_id', String(
        200), nullable=False, primary_key=True)
    title = Column('title', Text, nullable=False)
    delete_flag = Column('delete_flag', String(1), default="0", nullable=False)
    create_time = Column('cleate_time', TIMESTAMP, nullable=False)
    update_time = Column('update_time', TIMESTAMP, nullable=False)
    changer = Column('changer', String(200), nullable=False)


def create_progress_master(args):
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    create_progress_master(sys.argv)
