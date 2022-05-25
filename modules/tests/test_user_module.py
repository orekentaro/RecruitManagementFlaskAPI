import pytest
from app import app
from flask import json


@pytest.fixture
def app_test():
    app.config.update({'TESTING': True})
    # 必要なら前処理を
    # yield app
    return app


@pytest.fixture
def client(app_test):
    return app_test.test_client()


def test_login_succese(client):
    with client:
        res = client.post(
            '/user/login',
            data={
                "email": 'kntru0218gj@gmail.com',
                "password": "1234"})
        check_json = json.loads(res.get_data())
        assert "success" == check_json['result']


def test_login_failed(client):
    with client:
        res = client.post(
            '/user/login',
            data={
                "email": 'aaa@aaa.aaa',
                "password": "12345"},
            follow_redirects=True)
        check_json = json.loads(res.get_data())
        assert "failed" == check_json['result']


def test_login_failed2(client):
    with client:
        res = client.post(
            '/user/login',
            data={
                "email": 'kntru0218gj@gmail.com',
                "password": "12345"},
            follow_redirects=True)
        check_json = json.loads(res.get_data())
        assert "failed" == check_json['result']


def test_login_failed3(client):
    with client:
        res = client.post(
            '/user/login',
            data={
                "email": 'kntru0218gj@gmai.com',
                "password": "1234"},
            follow_redirects=True)
        check_json = json.loads(res.get_data())
        assert "failed" == check_json['result']
