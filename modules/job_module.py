from models.job_seeker import JobSeeker
from models.job_ads import JobAds
from models.job_master import JobMaster
from models.progress_info import ProgressInfo
from models.progress_master import ProgressMaster
from models.progress_result import ProgressResult
from models.memo import Memo
from modules.base_module import BaseModule
from sqlalchemy import desc


class JobModule(BaseModule):
    """
    求人全般用のモジュールクラス
    """

    const = BaseModule.Constant

    @classmethod
    def get_job_seeker(cls, **conditions):
        try:
            with cls.session_scope() as db_session:
                job_seekers = db_session.query(
                    JobSeeker
                ).filter_by(
                    **conditions,
                    delete_flag=cls.const.DELETE_FLAG_OFF
                ).all()

                res_list = []
                for job_seeker in job_seekers:
                    job_id = job_seeker.job_id
                    job_ads_id = job_seeker.ads_id

                    job = db_session.query(
                        JobMaster,
                        JobAds
                    ).join(
                        JobAds,
                        JobMaster.job_master_id == JobAds.job_master_id
                    ).filter(
                        JobAds.delete_flag == cls.const.DELETE_FLAG_OFF,
                        JobMaster.delete_flag == cls.const.DELETE_FLAG_OFF,
                        JobAds.ads_id == job_ads_id
                    ).first()

                    progress = db_session.query(
                        ProgressInfo,
                        ProgressResult,
                        ProgressMaster
                    ).join(
                        ProgressMaster,
                        (ProgressInfo.progress_id
                            == ProgressMaster.progress_id)
                    ).join(
                        ProgressResult,
                        (ProgressInfo.result
                            == ProgressResult.progress_result_id)
                    ).filter(
                        ProgressInfo.delete_flag == cls.const.DELETE_FLAG_OFF,
                        ProgressInfo.job_id == job_id,
                        (ProgressMaster.delete_flag
                            == cls.const.DELETE_FLAG_OFF),
                        (ProgressResult.delete_flag
                            == cls.const.DELETE_FLAG_OFF),
                    )

                    progress_all = progress.all()
                    progress_new = progress.order_by(
                        desc(ProgressInfo.progress_id)
                    ).first()

                    jm = job.JobMaster
                    ja = job.JobAds
                    pi = progress_new.ProgressInfo
                    pr = progress_new.ProgressResult
                    pm = progress_new.ProgressMaster

                    user = cls.get_user(
                        **{"user_id": pi.user_id}
                    ) or {}

                    res_dict = {
                        "job_id": job_id,
                        "name": job_seeker.name,
                        "gender": cls.const.GENDER_DICT[job_seeker.gender],
                        "job_ads": jm.job_offer_name,
                        "title": ja.title,
                        "status": pr.title,
                        "phase": pm.title,
                        "corr_person": user.get("name"),
                        "progress": [],
                        "memo": [],
                        "create_time": cls.date_to_string(
                            job_seeker.create_time
                            )
                    }

                    for prg in progress_all:
                        pi_all = prg.ProgressInfo
                        pr_all = prg.ProgressResult
                        pm_all = prg.ProgressMaster

                        user = cls.get_user(
                            **{"user_id": pi_all.user_id}
                        ) or {}

                        progress_dict = {
                            "phase": pm_all.title,
                            "result": pr_all.title,
                            "corr_person": user.get("name", ""),
                            "info": pi_all.progress_info,
                            "schedule": pi_all.schedule
                        }
                        res_dict["progress"].append(progress_dict)

                    memos = db_session.query(
                        Memo
                    ).filter_by(
                        job_id=job_id,
                        delete_flag=cls.const.DELETE_FLAG_OFF
                    ).all()

                    for memo in memos:
                        create_time = cls.date_to_string(memo.create_time)
                        user = cls.get_user(
                            **{"user_id": memo.changer}
                        ) or {}
                        memo_dict = {
                            "create_time": create_time,
                            "memo": memo.memo,
                            "creater": user.get("name", "")
                        }
                        res_dict["memo"].append(memo_dict)

                    res_list.append(res_dict)
            return {"result": "success", "data": res_list}

        except Exception as e:
            return {"result": "Exception", "data": str(e)}
