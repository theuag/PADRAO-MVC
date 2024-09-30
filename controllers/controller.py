from flask import Blueprint, render_template
from models.nome import*

app_controller = Blueprint("nome", __name__)

@app_controller.route("/")
def index():
    return render_template('index.html')

