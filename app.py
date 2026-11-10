from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", titulo="Minha primeira aplicação Flask")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/idade/<int:idade>")
def idade(idade):
    return render_template("idade.html", idade=idade)

    
if __name__ == "__main__":
    # host=0.0.0.0 permite o encaminhamento da porta no Codespaces.
    app.run(host="0.0.0.0", port=5000, debug=True)
