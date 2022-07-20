from ast import Constant
import hashlib
from contextlib import contextmanager
from models.db import session
from models.id_model import Id


class BaseModule:
    @contextmanager
    def session_scope() -> object:
        db_session = session()
        try:
            yield db_session
            db_session.commit()
        except Exception:
            db_session.rollback()
            raise
        finally:
            db_session.close()

    @classmethod
    def get_id(cls, target_id: str) -> int:
        return_id = 1
        with cls.session_scope() as db_session:
            this_id = db_session.query(Id).filter_by(
                id_name=target_id).with_for_update().first()
            if this_id:
                return_id = this_id.id_count + 1
                this_id.id_count = return_id
                db_session.add(this_id)

            else:
                create_id = Id()
                create_id.id_count = return_id
                create_id.id_name = target_id
                db_session.add(create_id)

        return return_id

    @classmethod
    def pasword_hash(cls, password: str) -> str:
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    class Constant:
        DELETE_FLAG_OFF = "0"
        DELETE_FLAG_ON = "1"
        GENDER_DICT = {"m": "男性", "f": "女性"}
