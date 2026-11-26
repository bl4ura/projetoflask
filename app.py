from flask import Flask, render_template, request, redirect
import aluno_service
import curso_service
import professor_service



app = Flask(__name__)
alunos = aluno_service.listar()

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", titulo="Minha primeira aplicação Flask")


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/idade/<int:idade>")
def idade(idade):
    return render_template("idade.html", idade=idade)


@app.route("/ola/<nome>")
def ola(nome):
    return render_template("ola.html", nome=nome)

@app.route("/disciplinas")
def disciplinas():
  lista = ["Programação Web", "Banco de Dados", "Redes", "Inglês Técnico"]
  return render_template("disciplinas.html", disciplinas=lista)

@app.route("/tabuada/<int:numero>")
def tabuada(numero):
    return render_template("tabuada.html", numero=numero)

@app.route("/tabuadas")
def tabuadas():
    return render_template("tabuadas.html")

@app.route("/aluno/")
def listar_alunos():
    alunos = aluno_service.listar()
    return render_template("aluno/listar.html", alunos=alunos)


@app.route("/aluno/novo")
def novo_aluno():
    return render_template("aluno/form.html", alunos=None)

@app.route("/aluno/salvar", methods=["POST"])
def salvar_aluno():
    id_aluno = request.form["id"]
    nome = request.form["nome"]
    telefone = request.form["telefone"]
    cidade = request.form["cidade"]

    if id_aluno == "":
        aluno_service.cadastrar(nome, telefone, cidade)

    return redirect("/aluno/")



@app.route("/curso/")
def listar_cursos():
    cursos = curso_service.listar()
    return render_template("curso/cursolistar.html", cursos=cursos)

@app.route("/curso/novo")
def novo_curso():
    return render_template("curso/cursoform.html", curso=None)

@app.route("/curso/salvar", methods=["POST"])
def salvar_curso():
    id_curso = request.form["id"]
    nome = request.form["nome"]
    area = request.form["area"]

    if id_curso == "":
        curso_service.cadastrar(nome, area)

    return redirect("/curso/")

@app.route("/professor/")
def listar_professores():
    professores = professor_service.listar()
    return render_template("professor/professorlistar.html", professores=professores)

@app.route("/professor/novo")
def novo_professor():
    return render_template("professor/professorform.html", professores=None)

@app.route("/professor/salvar", methods=["POST"])
def salvar_professor():
    id_professor = request.form["id"]
    nome = request.form["nome"]
    email = request.form["email"]
    titulacao = request.form["titulacao"]


    if id_professor == "":
        professor_service.cadastrar(nome, email,titulacao)

    return redirect("/professor/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)