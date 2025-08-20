from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    print(f"Tentativa de Login: Email: {email}, Palavra-passe: {password}")
    return jsonify({'message': f'Login com o email {email} recebido!'})

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    print(f"Tentativa de Registo: Utilizador: {username}, Email: {email}, Palavra-passe: {password}")
    return jsonify({'message': f'Utilizador {username} registado com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)