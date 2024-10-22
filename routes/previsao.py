from flask import Blueprint, render_template

previsao_route = Blueprint('previsao', __name__)

@previsao_route.route('/')
def previsao():
    return render_template('previsao.html')