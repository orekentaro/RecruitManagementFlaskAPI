from flask import Flask, make_response, jsonify, session, request
from flask_cors import CORS
from models.create_tabele import create_table
from routes.user_route import user_route
from datetime import timedelta


app = Flask(__name__)
CORS(
    app,
    supports_credentials=True
)
app.register_blueprint(user_route)
app.secret_key = "内緒"

# ログイン不要ルート
NOT_REQUIRED_LOGIN = [
    "/user/login?"
]


@app.before_request
def befor_request():
    if (request.full_path not in NOT_REQUIRED_LOGIN
            and 'user_id' not in session):
        return {'result': "not_login"}

    else:
        print(session)
        session.permanent = True
        app.permanent_session_lifetime = timedelta(minutes=15)
        session.modified = True


@app.route('/', methods=['get'])
def test():
    """befor_requestのテスト"""
    response = jsonify({'result': 'ok'})
    return make_response(response)


if __name__ == '__main__':
    create_table()
    app.run(debug=True)
