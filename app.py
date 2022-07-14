from flask import Flask
from flask_cors import CORS
from models.create_tabele import create_table
from routes.route import lr, ln

app = Flask(__name__)
CORS(
    app,
    supports_credentials=True
)
app.register_blueprint(lr)
app.register_blueprint(ln)
app.secret_key = "内緒"


if __name__ == '__main__':
    create_table()
    app.run(debug=True)
