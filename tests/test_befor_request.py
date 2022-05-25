from flask import json
import pytest
from tests.base_test import BaseTest
from app import app


class TestBeforRequest(BaseTest):
    @pytest.fixture
    def app_test(self):
        app.config.update({'TESTING': True})
        # 必要なら前処理を
        # yield app
        return app

    @pytest.fixture
    def client(self, app_test):
        return app_test.test_client()

    def test_login(self, client):
        self.login(client)
        with client:
            res = client.get('/')
            check_json = json.loads(res.get_data())
            assert "ok" == check_json['result']

    def test_not_login(self, client):
        with client:
            res = client.get('/')
            check_json = json.loads(res.get_data())
            assert "not_login" == check_json['result']
