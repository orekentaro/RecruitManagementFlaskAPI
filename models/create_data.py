from modules.base_module import BaseModule as bm
from models.job_ads import JobAds
from models.job_master import JobMaster
from models.job_seeker import JobSeeker
from models.user_master import UserMaster
from models.progress_master import ProgressMaster
from models.auth_master import AuthMaster
from datetime import datetime as dt


def create_data():
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
            name="test_user",
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
