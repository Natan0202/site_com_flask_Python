from flask import Flask
from flask.templating import render_template

#criando o site - iniciando ele - padrão
app = Flask(__name__)

#criando a primeira página do site
#toda página tem um route (link) -> google.com/ + nome do local do arquivo
@app.route("/") # / - pois é a página home

#@ - decoretor - linha de código que atribui uma nova funcionalidade a função que vem a baixo dela
#sempre colocar antes da função no qual você quer mudar a função do DEF


#@ - app - por causa da váriavel "app" e route é o link/caminho

#e uma função - o que você quer exibir na página

def home():
    #o que eu quero que apareça
    return render_template("index.html")

@app.route("/contatos")
def contatos():
    return render_template("contact.html")

#criando uma página para cada usuário 
#isso faz que com que depois do link seja o nome do usuário
@app.route("/usuarios/<nome_usuario>")
#exemplo site/usuarios/natan
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

@app.route("/php")
def php():
    return render_template("teste.php")
#colocando o site no ar
#if - verifica se ele está rodando no próprio arquivo
if __name__ == "__main__":
    app.run(debug = True) #debug - na hora da criação - ele ativa o debug - isso serve para editar o código e atualizar sozinho


############
#obs: para colocar os códigos HTML - é preciso criar uma pasta chamada templates

#colocamos o site no servidor do heroku

#para hospedar é preciso colocar as tecnologias usadas
#dois arquivos
#Procfile e requirements.txt