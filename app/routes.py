from app import app
from flask import render_template
from flask import request

@app.route('/')#Configurando uma rota web '/' == vazio, ao entrar no site vazio(sem a /) vai para o index.html
@app.route('/index')#Tanto '/' quanto '/index', levam para index.html
def index():
    return render_template('index.html', titulo="Página Inicial", nome="Fabio")#Direciona para uma página

@app.route('/contato')
def contato():
    return render_template('contato.html', titulo="Contato", nome="Fabio")