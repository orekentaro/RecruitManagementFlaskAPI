import hashlib
from models.user_master import UserMaster
from modules.base_module import BaseModule


class UserModule(BaseModule):
    """
    ユーザー認証やログイン、権限、ユーザー管理用のモジュールクラス
    """

    @classmethod
    def login(cls, email, password):
        '''
        ログイン認証API
        '''

        try:
            password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            with cls.session_scope() as db_session:
                user = db_session.query(UserMaster).filter_by(
                    email=email, password=password).first()

                if not user:
                    return {"result": "failed"}

            return {"result": "success", 'user': user.user_id}

        except Exception as e:
            print(e)
            return {"result": 'Exceptinon'}
