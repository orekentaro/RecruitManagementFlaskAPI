import hashlib
from models.user_master import UserMaster
from models.db import db_session


class UserModule:
    """
    ユーザー認証やログイン、権限、ユーザー管理用のモジュールクラス
    """

    @staticmethod
    def login(email, password):
        '''
        ログイン認証API
        '''

        try:
            password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            user = db_session.query(UserMaster).filter_by(
                email=email, password=password).first()

            if not user:
                return {"result": "failed"}

            return {"result": "success", 'user': user.user_id}

        except Exception as e:
            print(e)
            return {"result": 'Exceptinon'}

        finally:
            db_session.close()
