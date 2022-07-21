from models.job_seeker import JobSeeker
from models.job_ads import JobAds
from models.job_master import JobMaster
from models.progress_info import ProgressInfo
from models.progress_master import ProgressMaster
from models.progress_result import ProgressResult
from modules.base_module import BaseModule
from sqlalchemy import desc


class JobModule(BaseModule):
    """
    求人全般用のモジュールクラス
    """

    const = BaseModule.Constant

    @classmethod
    def job_seeker_list(cls, **conditions):
        with cls.session_scope() as db_session:
            job_seekers = db_session.query(
                JobSeeker
            ).filter_by(
                **conditions
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
                    ProgressInfo.progress_id == ProgressMaster.progress_id
                ).join(
                    ProgressResult,
                    ProgressInfo.result == ProgressResult.progress_result_id
                ).filter(
                    ProgressInfo.delete_flag == cls.const.DELETE_FLAG_OFF,
                    ProgressInfo.job_id == job_id,
                    ProgressMaster.delete_flag == cls.const.DELETE_FLAG_OFF,
                    ProgressResult.delete_flag == cls.const.DELETE_FLAG_OFF,
                ).order_by(
                    desc(ProgressInfo.progress_id)
                    ).first()

                jm = job.JobMaster
                ja = job.JobAds
                pr = progress.ProgressResult
                pm = progress.ProgressMaster
                res_dict = {
                    "job_id": job_id,
                    "name": job_seeker.name,
                    "gender": job_seeker.gender,
                    "job_ads": jm.job_offer_name,
                    "title": ja.title,
                    "result": pr.title,
                    "phase": pm.title
                }
                res_list.append(res_dict)
        return {"result": "success", "data": res_list}
