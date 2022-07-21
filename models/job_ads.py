
import sys
from sqlalchemy import TIMESTAMP, BigInteger, Column, String, Text, ForeignKey
from models.db import Base, ENGINE


class JobAds(Base):
    """求人広告"""
    __tablename__ = 'job_ads'
    ads_id = Column('ads_id', String(200), nullable=False, primary_key=True)
    job_master_id = Column('job_master_id', String(200),
                           ForeignKey('job_master.job_master_id',
                                      onupdate='CASCADE', ondelete='CASCADE'))
    publication_start = Column('publication_start', String(10))
    publication_end = Column('publication_end', String(10))
    title = Column('title', Text)
    contents = Column('contents', Text)
    views = Column('views', BigInteger)
    cost = Column('cost', BigInteger)
    delete_flag = Column('delete_flag', String(1), default="0", nullable=False)
    create_time = Column('cleate_time', TIMESTAMP, nullable=False)
    update_time = Column('update_time', TIMESTAMP, nullable=False)
    changer = Column('changer', String(200), nullable=False)


def create_job_ads(args):
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    create_job_ads(sys.argv)
