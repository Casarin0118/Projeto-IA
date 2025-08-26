import os
from uuid import uuid4
from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "dev"

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf"}
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16MB

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

# começa com 1 linha vazia
linhas = [{"perfil": "", "descricao": "", "arquivo": None}]

@app.route("/", methods=["GET", "POST"])
def index():
    global linhas
    if request.method == "POST":
        file = request.files.get("pdf_file")

        if not file or file.filename == "":
            flash("Nenhum arquivo selecionado.")
            return redirect(url_for("index"))

        if not allowed_file(file.filename):
            flash("Envie apenas arquivos .pdf")
            return redirect(url_for("index"))

        safe_name = secure_filename(file.filename)
        final_name = f"{uuid4().hex}_{safe_name}"
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], final_name))

        # marca o arquivo na última linha e cria uma nova
        linhas[-1]["arquivo"] = final_name
        linhas.append({"perfil": "", "descricao": "", "arquivo": None})

        return redirect(url_for("index"))

    return render_template("index.html", linhas=linhas)

@app.route("/uploads/<path:filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

@app.route("/cadastrar")
def cadastrar():
    return render_template("cadastrar.html")

# 🔥 NOVAS ROTAS
@app.route("/empresa")
def empresa():
    return render_template("empresa.html")

@app.route("/como-funciona")
def como_funciona():
    return render_template("como_funciona.html")

if __name__ == "__main__":
    app.run(debug=True)
