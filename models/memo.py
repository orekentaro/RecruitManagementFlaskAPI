import sys
from sqlalchemy import TIMESTAMP, Column, String, Text, ForeignKey
from models.db import Base, ENGINE


class Memo(Base):
    """求職者情報"""
    __tablename__ = 'memo'
    memo_id = Column('memo_id', String(200), nullable=False, primary_key=True)
    job_id = Column('job_id', String(200),
                    ForeignKey('job_seeker.job_id', onupdate='CASCADE',
                    ondelete='CASCADE'))
    delete_flag = Column('delete_flag', String(1), default="0", nullable=False)
    memo = Column('memo', Text, nullable=False)
    create_time = Column('cleate_time', TIMESTAMP, nullable=False)
    update_time = Column('update_time', TIMESTAMP, nullable=False)
    changer = Column('changer', String(200), nullable=False)


def create_memo(args):
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    create_memo(sys.argv)
