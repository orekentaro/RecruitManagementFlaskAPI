from sqlalchemy import true
from models.job_seeker import JobSeeker
from models.job_ads import JobAds
from models.job_master import JobMaster
from models.progress_info import ProgressInfo
from models.progress_master import ProgressMaster
from models.memo import Memo
from modules.base_module import BaseModule


class JobModule(BaseModule):
    """
    求人全般用のモジュールクラス
    """

    const = BaseModule.Constant

    @classmethod
    def job_seeker_list(cls):
        with cls.session_scope() as db_session:
            job_seekers = db_session.query(
                JobSeeker,
                JobAds,
                JobMaster,
                ProgressInfo,
                ProgressMaster
            ).join(
                JobAds,
                JobSeeker.ads_id == JobAds.ads_id
            ).join(
                JobMaster,
                JobAds.job_master_id == JobMaster.job_master_id
            ).join(
                ProgressInfo,
                JobSeeker.job_id == ProgressInfo.job_id
            ).join(
                ProgressMaster,
                ProgressInfo.progress_id == ProgressMaster.progress_id
            ).filter(
                JobSeeker.delete_flag == cls.const.DELETE_FLAG_OFF,
                JobAds.delete_flag == cls.const.DELETE_FLAG_OFF,
                JobMaster.delete_flag == cls.const.DELETE_FLAG_OFF,
                ProgressInfo.delete_flag == cls.const.DELETE_FLAG_OFF,
                ProgressMaster.delete_flag == cls.const.DELETE_FLAG_OFF
            ).all()
            res_list = []
            for job_seeker in job_seekers:
                js = job_seeker.JobSeeker
                jm = job_seeker.JobMaster
                pi = job_seeker.ProgressInfo
                pm = job_seeker.ProgressMaster
                res_dict = {
                    "job_id": js.job_id,
                    "name": js.name,
                    "gender": js.gender,
                    "job_ads": jm.job_offer_name,
                    "progress": pm.title,
                    "progress_user": pi.user_id
                }
                res_list.append(res_dict)
        return {"result": "success", "data": res_list}
