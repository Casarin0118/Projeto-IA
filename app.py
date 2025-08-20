from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("cadastrar.html")

@app.route("/salvar", methods=["POST"])
def salvar():
    titulo = request.form["titulo"]
    descricao = request.form["descricao"]
    print("Título:", titulo)
    print("Descrição:", descricao)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
