from flask import Blueprint, make_response, jsonify, session, request
from modules.user_module import UserModule
from modules.job_module import JobModule

# ログイン不要ルート
ln = Blueprint('ln', __name__)
# ログイン必要ルート
lr = Blueprint('lr', __name__)


@lr.before_request
def befor_request():
    if 'user_id' not in session:
        return {'result': "not_login"}
    else:
        result = request.cookies.get('login', None)
        print(result)


@lr.route('/', methods=['get'])
def test():
    """befor_requestのテスト"""
    response = jsonify({'result': 'ok'})
    return make_response(response)


@ln.route('/login', methods=['POST'])
def login():
    """ログインルート"""
    email = request.form['email']
    password = request.form["password"]
    res = UserModule.login(email, password)
    result = res['result']
    response = make_response(res)
    if result == 'success':
        response.set_cookie('login', value=email, secure=None, httponly=False)
        response.set_cookie(
            'user_id', value=res['user'], secure=None, httponly=False)
        session['user_id'] = res['user']
    return response


@lr.route('/job_seeker_list', methods=['GET'])
def job_seeker_list():
    conditions = dict(request.args)
    res = JobModule.job_seeker_list(**conditions)
    response = make_response(res)
    return response
