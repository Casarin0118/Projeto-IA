from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Página inicial (tabela)
@app.route("/")
def index():
    return render_template("index.html")

# Página de cadastro (da Eloa)
@app.route("/cadastrar")
def cadastrar():
    return render_template("cadastrar.html")

if __name__ == "__main__":
    app.run(debug=True)
