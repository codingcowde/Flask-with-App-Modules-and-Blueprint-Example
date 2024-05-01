from flask import Flask
from auth.routes import auth

app = Flask(__name__)
app.register_blueprint(auth, url_prefix='/auth')