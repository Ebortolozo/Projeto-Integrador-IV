from flask import Flask, url_for
from configuration import configure_all

# Deixar inicialização no Inicio
app = Flask(__name__)

# Função pra configurar tanto as rotas quanto o DB
configure_all(app)

# Deixar a Execução no final!
app.run(debug=True)