from flask import Blueprint, make_response, request, session
from modules.user_module import UserModule


user_route = Blueprint('user_route', __name__, url_prefix='/user')


@user_route.route('/login', methods=['POST'])
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
