from app import app
from flask import render_template
from flask import request
import json
import requests

link = "https://flaskti18n-fe743-default-rtdb.firebaseio.com/" #Conecta o banco


# As rotas são para poder definir os caminhos
@app.route('/')#Configurando uma rota web '/' == vazio, ao entrar no site vazio(sem a /) vai para o index.html
@app.route('/index')#Tanto '/' quanto '/index', levam para index.html
def index():
    return render_template('index.html', titulo="Página Inicial", nome="Fabio")#Direciona para uma página

@app.route('/contato')
def contato():
    return render_template('contato.html', titulo="Contato", nome="Fabio")

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', titulo="Cadastro", nome="Fabio", fundoId="fundoLoginCadastro")

@app.route('/cadastrarUsuario', methods=['POST']) #POST = método de envio de dados pela rede(mais lento, mais seguro)  GET = (mais rapido, fica a mostra)
def cadastrarUsuario():
    try:
        requisicao2 = requests.get(f'{link}/cadastrar/.json')
        dicionario = requisicao2.json()

        nome = request.form.get("nome")
        sobrenome = request.form.get("sobrenome")
        email = request.form.get("email")
        for codigo in dicionario:
            emailUsuario = dicionario[codigo]['email']
            if(email == emailUsuario):
                return "O e-mail informado já se encontra em uso"
        senha = request.form.get("senha")
        cpf = request.form.get("cpf")
        for codigo in dicionario:
            cpfUsuario = dicionario[codigo]['cpf']
            if(cpf == cpfUsuario):
                return "O CPF informado já se encontra em uso"
        endereco = request.form.get("endereco")
        dados = {"nome":nome, "sobrenome":sobrenome, "email":email, "senha":senha, "cpf":cpf, "endereco":endereco, "tipo":"CLIENTE"} #monta o vetor
        requisicao = requests.post(f'{link}/cadastrar/.json', data=json.dumps(dados)) #json = coleção de dados / json.dumps = inserção conjuntos de dados
        return 'Cadastrado com sucesso!!!'
    except Exception as e:
        return f'Ocorreu um erro\n\n + {e}'

@app.route('/listar')
def listarTudo():
    try:
        requisicao = requests.get(f'{link}/cadastrar/.json') #Solicitar o dado
        dicionario = requisicao.json() #Retorna a estrutura de dados
        return dicionario
    except Exception as e:
        return f'Ocorreu um erro\n\n + {e}'

@app.route('/listarIndividual')
def listarIndividual():
    try:
        requisicao = requests.get(f'{link}/cadastrar/.json')
        dicionario = requisicao.json()
        idCadastro = "" #Recebe o ID
        for codigo in dicionario:
            usuario = dicionario[codigo]['cpf'] #dado/campo. Filtro pelo CPF, conforme verificado, cada cpf é substituido pelo proximo que a variavel recebe
            if(usuario == "123"):
                idCadastro = codigo
        return idCadastro
    except Exception as e:
        return f'Ocorreu um erro\n\n + {e}'


@app.route('/realizarLogin', methods=['POST'])
def logado():
    try:
        email = request.form.get("emailLogin")
        senha = request.form.get("senhaLogin")

        requisicao = requests.get(f'{link}/cadastrar/.json')
        dicionario = requisicao.json()
        for codigo in dicionario:
            emailUsuario = dicionario[codigo]['email']
            senhaUsuario = dicionario[codigo]['senha']
            if (email == emailUsuario and senha == senhaUsuario):
                tipo = dicionario[codigo]['tipo']
                nome = dicionario[codigo]['nome']
                sobrenome = dicionario[codigo]['sobrenome']
                email = dicionario[codigo]['email']
                senha = dicionario[codigo]['senha']
                cpf = dicionario[codigo]['cpf']
                endereco = dicionario[codigo]['endereco']
                if (tipo == "CLIENTE"):
                    return render_template('cliente.html', titulo="Cliente", nome="Fabio", nomeUsuario=nome, sobrenomeUsuario=sobrenome, emailUsuario=email, senhaUsuario=senha, cpfUsuario=cpf, enderecoUsuario=endereco)
                else:
                    return render_template('admin.html', titulo="Admin", nome="Fabio", nomeUsuario=nome)
            else:
                continue
        return "Login inválido ou inexistente"
    except Exception as e:
        return f'Ocorreu um erro\n\n + e'


@app.route('/atualizar', methods=['POST'])
def atualizar():
    try:
        id = ""
        nome = request.form.get("nomeCliente")
        sobrenome = request.form.get("sobrenomeCliente")
        email = request.form.get("emailCliente")
        senha = request.form.get("senhaCliente")
        cpf = request.form.get("cpfCliente")
        endereco = request.form.get("enderecoCliente")
        requisicao2 = requests.get(f'{link}/cadastrar/.json')
        dicionario = requisicao2.json()
        for codigo in dicionario:
            cpfUsuario = dicionario[codigo]['cpf']
            if(cpf == cpfUsuario):
                id = codigo
        dados = {"nome":nome, "sobrenome":sobrenome, "email":email, "senha":senha, "cpf":cpf, "endereco":endereco} #Parametro para atualização
        requisicao = requests.patch(f'{link}/cadastrar/{id}/.json', data=json.dumps(dados))
        return "Atualizado com sucesso"
    except Exception as e:
        return f'Ocorreu um erro + {e}'

# -Nz0KaF14VExmbi7I5Gf
@app.route('/excluir', methods=["POST"])
def excluir():
    try:
        cpf = request.form.get("exclusaoCpf")
        requisicao = requests.get(f'{link}/cadastrar/.json')
        dicionario = requisicao.json()
        for codigo in dicionario:
            cpfUsuario = dicionario[codigo]['cpf']
            if(cpf == cpfUsuario):
                requisicao2 = requests.delete(f'{link}/cadastrar/{codigo}/.json')
                return "Excluido com sucesso!"
            else:
                continue
        return "CPF inválido!"
    except Exception as e:
        return f'Ocorreu um erro + {e}'

@app.route('/login')
def login():
    return render_template('login.html', titulo="Login", nome="Fabio", fundoId="fundoLoginCadastro")

@app.route('/relogios')
def relogios():
    return render_template('relogios.html', titulo="Relogios", nome="Fabio")

@app.route('/historia')
def historia():
    return render_template('historia.html', titulo="História", nome="Fabio")
