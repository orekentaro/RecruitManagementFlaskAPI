from flask import json
import pytest
from tests.base_test import BaseTest
from app import app

SUCCESS_DATA = [
        {
            "corr_person": "テストくん",
            "create_time": "2022/07/22",
            "gender": "男性",
            "job_ads": "テスト求人",
            "job_id": "1",
            "memo": [
                {
                    "create_time": "2022/07/22",
                    "creater": "テストくん",
                    "memo": "ちゃんと勉強してそう"
                }
            ],
            "name": "テスト太郎",
            "phase": "一次面接",
            "progress": [
                {
                    "corr_person": "テストくん",
                    "info": "応募がありました",
                    "phase": "応募",
                    "result": "選考中",
                    "schedule": "20220801"
                },
                {
                    "corr_person": "テストくん",
                    "info": "",
                    "phase": "一次面接",
                    "result": "日程調整中",
                    "schedule": ""
                }
            ],
            "status": "日程調整中",
            "title": "未経験可"
        }
    ]


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
            res = client.get('/job_seeker')
            check_json = json.loads(res.get_data())
            print(check_json)
            assert check_json['result'] == "success"
            assert check_json["data"] == SUCCESS_DATA

    def test_job_seeker_active(self, client):
        self.login(client)
        with client:
            res = client.get('/job_seeker?active_flag=0')
            check_json = json.loads(res.get_data())
            print(check_json)
            assert check_json['result'] == "success"
            assert check_json["data"] == SUCCESS_DATA

    def test_job_seeker_deactive(self, client):
        self.login(client)
        with client:
            res = client.get('/job_seeker?active_flag=1')
            check_json = json.loads(res.get_data())
            print(check_json)
            assert check_json['result'] == "success"
            assert check_json["data"] == []
