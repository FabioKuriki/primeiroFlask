from app import app
from flask import render_template
from flask import request

# As rotas são para poder definir os caminhos
@app.route('/')#Configurando uma rota web '/' == vazio, ao entrar no site vazio(sem a /) vai para o index.html
@app.route('/index')#Tanto '/' quanto '/index', levam para index.html
def index():
    return render_template('index.html', titulo="Página Inicial", nome="Fabio")#Direciona para uma página

@app.route('/contato')
def contato():
    return render_template('contato.html', titulo="Contato", nome="Fabio", fundo="fundoContato")

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', titulo="Cadastro", nome="Fabio", fundo="cadastro")

@app.route('/login')
def login():
    return render_template('login.html', titulo="Login", nome="Fabio", fundo="fundoLogin")
