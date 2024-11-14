import bcrypt
from flask import Flask, request, jsonify
from flask_cors import CORS
from auth import get_user_by_username

app = Flask(__name__)
CORS(app)

def verificar_senha(senha, senha_hash):
    return bcrypt.checkpw(senha.encode('utf-8'), senha_hash)

@app.route('/login', methods=['POST'])
def login_route():
    data = request.json
    username = data.get('username')
    senha = data.get('senha')

    user = get_user_by_username(username)
    if not user:
        return jsonify({"message": "Usuário não encontrado."}), 401

    senha_hash = user['senha_hash'] 

    if verificar_senha(senha, senha_hash):
        return jsonify({"message": "Login bem-sucedido!"}), 200
    else:
        return jsonify({"message": "Usuário ou senha incorretos."}), 401

if __name__ == '__main__':
    app.run(debug=True)
