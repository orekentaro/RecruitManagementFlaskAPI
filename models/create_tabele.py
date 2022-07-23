from modules.base_module import BaseModule as bm
from models.job_ads import JobAds
from models.job_master import JobMaster
from models.job_seeker import JobSeeker
from models.user_master import UserMaster
from models.progress_master import ProgressMaster
from models.auth_master import AuthMaster
from models.progress_info import ProgressInfo
from models.progress_result import ProgressResult
from models.memo import Memo
from datetime import datetime as dt
from models.db import Base, ENGINE


def create_table():
    Base.metadata.create_all(bind=ENGINE)
    try:
        _create_data()
    except Exception as e:
        print(f'データ作成エラー→{e}')
        pass


def _create_data():
    now = dt.now()
    with bm.session_scope() as db_session:
        auth = AuthMaster(
            auth_id=1,
            auth='admin'
        )
        db_session.add(auth)

        user_id = bm.get_id('user_id')
        user = UserMaster(
            user_id=user_id,
            name="テストくん",
            email="test@test.test",
            password=bm.pasword_hash('password1234'),
            auth_id=1,
            changer="create",
            create_time=now,
            update_time=now
        )
        db_session.add(user)

        progress_id = bm.get_id('progress_id')
        entry = ProgressMaster(
            progress_id=progress_id,
            title="応募",
            changer="create",
            create_time=now,
            update_time=now
        )
        db_session.add(entry)

        progress_id = bm.get_id('progress_id')
        step1 = ProgressMaster(
            progress_id=progress_id,
            title="一次面接",
            changer="create",
            create_time=now,
            update_time=now
        )
        db_session.add(step1)

        progress_id = bm.get_id('progress_id')
        step2 = ProgressMaster(
            progress_id=progress_id,
            title="二次面接",
            changer="create",
            create_time=now,
            update_time=now
        )
        db_session.add(step2)

        progress_id = bm.get_id('progress_id')
        unofficial_decision = ProgressMaster(
            progress_id=progress_id,
            title="内定",
            changer="create",
            create_time=now,
            update_time=now
        )
        db_session.add(unofficial_decision)

        progress_id = bm.get_id('progress_id')
        acceptance = ProgressMaster(
            progress_id=progress_id,
            title="内定承諾",
            changer="create",
            create_time=now,
            update_time=now
        )
        db_session.add(acceptance)

        progress_id = bm.get_id('progress_id')
        joined = ProgressMaster(
            progress_id=progress_id,
            title="入社",
            changer="create",
            create_time=now,
            update_time=now
        )
        db_session.add(joined)

        progress_id = bm.get_id('progress_id')
        decline = ProgressMaster(
            progress_id=progress_id,
            title="辞退",
            changer="create",
            create_time=now,
            update_time=now
        )
        db_session.add(decline)

        progress_result_id = bm.get_id('progress_result_id')
        checking = ProgressResult(
            progress_result_id=progress_result_id,
            title="選考中",
            changer="create",
            create_time=now,
            update_time=now
        )
        db_session.add(checking)

        progress_result_id = bm.get_id('progress_result_id')
        adjustment = ProgressResult(
            progress_result_id=progress_result_id,
            title="日程調整中",
            changer="create",
            create_time=now,
            update_time=now
        )
        db_session.add(adjustment)

        progress_result_id = bm.get_id('progress_result_id')
        schedule = ProgressResult(
            progress_result_id=progress_result_id,
            title="予定",
            changer="create",
            create_time=now,
            update_time=now
        )
        db_session.add(schedule)

        progress_result_id = bm.get_id('progress_result_id')
        done = ProgressResult(
            progress_result_id=progress_result_id,
            title="実施",
            changer="create",
            create_time=now,
            update_time=now
        )
        db_session.add(done)

        progress_result_id = bm.get_id('progress_result_id')
        cancel = ProgressResult(
            progress_result_id=progress_result_id,
            title="キャンセル",
            changer="create",
            create_time=now,
            update_time=now
        )
        db_session.add(cancel)

        progress_result_id = bm.get_id('progress_result_id')
        passing = ProgressResult(
            progress_result_id=progress_result_id,
            title="通過",
            changer="create",
            create_time=now,
            update_time=now
        )
        db_session.add(passing)

        progress_result_id = bm.get_id('progress_result_id')
        failure = ProgressResult(
            progress_result_id=progress_result_id,
            title="不合格",
            changer="create",
            create_time=now,
            update_time=now
        )
        db_session.add(failure)

        job_master_id = bm.get_id('job_master_id')
        job_master = JobMaster(
            job_master_id=job_master_id,
            job_offer_name='テスト求人',
            subscription_cost=100000,
            create_time=dt.now(),
            update_time=dt.now(),
            changer='create'
        )
        db_session.add(job_master)

        ads_id = bm.get_id('ads_id')
        job_ads = JobAds(
            ads_id=ads_id,
            job_master_id=1,
            publication_start='20220401',
            publication_end='20220901',
            title="未経験可",
            contents="エンジニア募集中",
            views=200,
            cost=200,
            create_time=dt.now(),
            update_time=dt.now(),
            changer='create'
        )
        db_session.add(job_ads)

        job_id = bm.get_id('job_id')
        job_seeker = JobSeeker(
            job_id=job_id,
            name='テスト太郎',
            gender="m",
            birthday="19930218",
            career='2021年テスト株式会社入社',
            ads_id=1,
            create_time=dt.now(),
            update_time=dt.now(),
            changer='create'
            )
        db_session.add(job_seeker)

        progress_info_id = bm.get_id('progress_info_id')
        progress_info = ProgressInfo(
            progress_info_id=progress_info_id,
            progress_id=1,
            user_id=1,
            job_id=1,
            progress_info='応募がありました',
            schedule='20220801',
            result='1',
            create_time=dt.now(),
            update_time=dt.now(),
            changer='create'
        )
        db_session.add(progress_info)

        progress_info_id = bm.get_id('progress_info_id')
        progress_info = ProgressInfo(
            progress_info_id=progress_info_id,
            progress_id=2,
            user_id=1,
            job_id=1,
            progress_info='',
            schedule='',
            result=2,
            create_time=dt.now(),
            update_time=dt.now(),
            changer='create'
        )
        db_session.add(progress_info)

        memo_id = bm.get_id('memo_id')
        memo = Memo(
            memo_id=memo_id,
            job_id=1,
            memo='ちゃんと勉強してそう',
            create_time=dt.now(),
            update_time=dt.now(),
            changer='create'
        )
        db_session.add(memo)


if __name__ == "__main__":
    create_table()
