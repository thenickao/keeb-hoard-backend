from flask import Flask, jsonify, g
from resources.users import users
from resources.keyboards import keyboards
from resources.keyboards import keyboard
from resources.switches import switches
from resources.switches import switch
from resources.stabilizers import stabilizers
from resources.stabilizers import stabilizer
from resources.keycaps import keycaps
from resources.keycaps import keycap
import models
from flask_cors import CORS
from flask_login import LoginManager
from flask_login import current_user
# from flask_jwt_extended import create_access_token
# from flask_jwt_extended import get_jwt_identity
# from flask_jwt_extended import jwt_required
# from flask_jwt_extended import JWTManager

login_manager = LoginManager()

DEBUG=True
PORT=8000
app = Flask(__name__)
# app.config["JWT_SECRET_KEY"] = "WE423098RUIYE6548793RWJHKGFDJK354987GFDJKHFGD"
# jwt = JWTManager(app)
app.config['CORS_SUPPORTS_CREDENTIALS'] = True
cors = CORS(app, origins=['http://localhost:3000'], supports_credentials=True)
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

app.secret_key = "LJAKLJLKJJLJKLSDJLKJASD"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    try:
        return models.User.get(models.User.id == id)
    except models.DoesNotExist:
        return None

@login_manager.user_loader
def load_user(user_id):
    return models.User.get(models.User.id == id)

@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()
    g.user = current_user

@app.after_request
def after_request(response):
    g.db.close()
    return response

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response
    
app.register_blueprint(users, url_prefix="/user")
app.register_blueprint(keyboards, url_prefix="/keyboard")
app.register_blueprint(switches, url_prefix="/switch")
app.register_blueprint(stabilizers, url_prefix="/stabilizer")
app.register_blueprint(keycaps, url_prefix="/keycap")



if __name__ == "__main__":
    models.initialize()
    app.run(debug=DEBUG, port=PORT)

# if __name__ == "__main__":
#     models.delete_tables()
#     app.run(debug=DEBUG, port=PORT)


# @app.route("/")
# def home():
#     return jsonify("Hello, this is home.")

# @app.route("/<keyboard>")
# def keyboard(keyboard):
#     return f"This is {keyboard}"

# @app.route("/keyboards")
# def keyboards():
#     return {"This is the keyboards test": ["keyboard1", "keyboard2", "keyboard3"]}

# @app.route("/<keyboard>")
# def keyboard(keyboard):
#     data = {"message": f"This is {keyboard}"}
#     return jsonify(data)