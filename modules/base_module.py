from contextlib import contextmanager
from models.db import session


class BaseModule:
    @contextmanager
    def session_scope():
        db_session = session()
        try:
            yield db_session
            db_session.commit()
        except Exception:
            db_session.rollback()
            raise
        finally:
            db_session.close()
