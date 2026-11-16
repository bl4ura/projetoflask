from flask import Flask, render_template

app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)