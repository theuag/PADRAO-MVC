from flask import Flask
from controllers.controller import app_controller

app = Flask(__name__)

app.register_blueprint(app_controller)

if __name__ == "__main__" :
    app.run()