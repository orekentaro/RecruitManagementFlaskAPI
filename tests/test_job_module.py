from flask import json
import pytest
from tests.base_test import BaseTest
from app import app


class TestJobModule(BaseTest):
    @pytest.fixture
    def app_test(self):
        app.config.update({'TESTING': True})
        # 必要なら前処理を
        # yield app
        return app

    @pytest.fixture
    def client(self, app_test):
        return app_test.test_client()

    def test_job_seeker_list(self, client):
        self.login(client)
        with client:
            res = client.get('/job_seeker_list')
            check_json = json.loads(res.get_data())
            assert "success" == check_json['result']
