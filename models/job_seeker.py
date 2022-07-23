
import sys
from sqlalchemy import TIMESTAMP, Column, String, Text, ForeignKey
from models.db import Base, ENGINE


class JobSeeker(Base):
    """求職者情報"""
    __tablename__ = 'job_seeker'
    job_id = Column('job_id', String(200), nullable=False, primary_key=True)
    name = Column('name', String(200), nullable=False)
    gender = Column('gender', String(1))
    birthday = Column("birthday", String(10))
    career = Column('career', Text)
    ads_id = Column('ads_id', String(200),
                    ForeignKey('job_ads.ads_id',
                    onupdate='CASCADE', ondelete='CASCADE'))
    active_flag = Column('active_flag', String(1), default="0", nullable=False)
    delete_flag = Column('delete_flag', String(1), default="0", nullable=False)
    create_time = Column('cleate_time', TIMESTAMP, nullable=False)
    update_time = Column('update_time', TIMESTAMP, nullable=False)
    changer = Column('changer', String(200), nullable=False)


def create_job_seeker(args):
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    create_job_seeker(sys.argv)
