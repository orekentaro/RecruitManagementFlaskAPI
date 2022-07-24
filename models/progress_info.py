import sys
from sqlalchemy import TIMESTAMP, Column, String, Text, ForeignKey
from models.db import Base, ENGINE


class ProgressInfo(Base):
    """進捗マスタ"""
    __tablename__ = 'progress_info'
    progress_info_id = Column('progress_info_id', String(
        200), nullable=False, primary_key=True)
    progress_id = Column('progress_id', String(200),
                         ForeignKey('progress_master.progress_id',
                                    onupdate='CASCADE', ondelete='CASCADE'))
    user_id = Column('user_id', String(200),
                     ForeignKey('user_master.user_id', onupdate='CASCADE',
                     ondelete='CASCADE'))
    job_id = Column('job_id', String(200),
                    ForeignKey('job_seeker.job_id', onupdate='CASCADE',
                    ondelete='CASCADE'))
    progress_info = Column('progress_info', Text, nullable=False)
    # TODO: ここタイムスタンプにした方がいい
    schedule = Column('schedule', String(8))
    result = Column('result', String(200),
                    ForeignKey('progress_result.progress_result_id',
                               onupdate='CASCADE', ondelete='CASCADE'))
    delete_flag = Column('delete_flag', String(1), default="0", nullable=False)
    create_time = Column('cleate_time', TIMESTAMP, nullable=False)
    update_time = Column('update_time', TIMESTAMP, nullable=False)
    changer = Column('changer', String(200), nullable=False)


def create_progress_info(args):
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    create_progress_info(sys.argv)
