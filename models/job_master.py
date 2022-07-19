import sys
from sqlalchemy import TIMESTAMP, BigInteger, Column, String
from models.db import Base, ENGINE


class JobMaster(Base):
    """求人マスタ"""
    __tablename__ = 'job_master'
    job_master_id = Column('job_master_id', String(
        200), nullable=False, primary_key=True)
    job_offer_name = Column('job_offer_name', String(200), nullable=False)
    subscription_cost = Column('subscription_cost', BigInteger)
    delete_flag = Column('delete_flag', String(1), default="0", nullable=False)
    create_time = Column('cleate_time', TIMESTAMP, nullable=False)
    update_time = Column('update_time', TIMESTAMP, nullable=False)
    changer = Column('changer', String(200), nullable=False)


def create_job_master(args):
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    create_job_master(sys.argv)
