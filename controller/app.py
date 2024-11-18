import os
import bcrypt
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_cors import CORS
from werkzeug.utils import secure_filename
from auth import get_user_by_username
from database import get_connection

# Configuração do app
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app = Flask(
    __name__,
    template_folder=os.path.join(base_dir, 'views'),
    static_folder=os.path.join(base_dir, 'static')
)
app.config['UPLOAD_FOLDER'] = os.path.join(app.static_folder, 'img', 'items')
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])
# Definindo configurações de CORS para full
CORS(app)

# Função para verificar senha
def verificar_senha(senha, senha_hash):
    if isinstance(senha_hash, str):
        senha_hash = senha_hash.encode('utf-8')
    return bcrypt.checkpw(senha.encode('utf-8'), senha_hash)

## Páginas
# Rota de login
@app.route('/')
def login():
    return render_template('login.html')

# Rota principal (Dashboard)
@app.route('/main')
def main():
    return render_template('main.html')

# Rota monitoramento
@app.route('/monitoramento')
def monitoramento():
    return render_template('monitoramento.html')

# Rota para a Batcaverna (Área Restrita)
@app.route('/batcaverna')
def batcaverna():
    role = request.args.get('role')
    if role != 'admin':
        return redirect(url_for('main'))
    return render_template('batcaverna.html')

# Rota de Gestão
@app.route('/gestao')
def gestao():
    role = request.args.get('role')
    if role not in ['admin', 'gerente']:
        return redirect(url_for('main'))
    return render_template('gestao.html')

## Rotas de funções
# Rota de login
@app.route('/login', methods=['POST'])
def login_route():
    data = request.json
    username = data.get('username')
    senha = data.get('senha')

    user = get_user_by_username(username)
    if not user:
        return jsonify({"message": "Credenciais inválidas."}), 401

    senha_hash = user['senha_hash']
    if verificar_senha(senha, senha_hash):
        return jsonify({
            "message": "Login bem-sucedido!",
            "username": user['nome_completo'],
            "role": user['role']
        }), 200
    else:
        return jsonify({"message": "Credenciais inválidas."}), 401

# CRUD da Batcaverna
@app.route('/batcaverna/items', methods=['GET', 'POST', 'PUT', 'DELETE'])
def manage_batcaverna_items():
    if request.method == 'GET':
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM items_batcaverna')
            items = cursor.fetchall()
            connection.close()

            return jsonify([
                {
                    "id": row[0],
                    "nome": row[1],
                    "tipo": row[2],
                    "quantidade": row[3],
                    "descricao": row[4],
                    "imagem": url_for('static', filename=row[5].replace("\\", "/"))
                }
                for row in items
            ])
        except Exception as e:
            print(f"Erro ao carregar itens: {e}")
            return jsonify({"error": "Erro ao carregar itens."}), 500

    elif request.method == 'POST':
        try:
            data = request.form
            file = request.files.get('imagem')

            if not file:
                return jsonify({"error": "Nenhuma imagem enviada."}), 400

            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            path_no_static = os.path.relpath(filepath, app.static_folder).replace("\\", "/")

            connection = get_connection()
            cursor = connection.cursor()
            sql = '''
            INSERT INTO items_batcaverna (nome, tipo, quantidade, descricao, imagem)
            VALUES (?, ?, ?, ?, ?)
            '''
            cursor.execute(sql, (data['nome'], data['tipo'], data['quantidade'], data['descricao'], path_no_static))
            connection.commit()
            connection.close()
            return jsonify({"message": "Item adicionado com sucesso!"}), 200
        except Exception as e:
            print(f"Erro ao adicionar item: {e}")
            return jsonify({"error": "Erro ao adicionar item."}), 500

    elif request.method == 'PUT':
        try:
            data = request.json
            connection = get_connection()
            cursor = connection.cursor()
            sql = '''
            UPDATE items_batcaverna
            SET nome = ?, tipo = ?, quantidade = ?, descricao = ?
            WHERE id = ?
            '''
            cursor.execute(sql, (data['nome'], data['tipo'], data['quantidade'], data['descricao'], data['id']))
            connection.commit()
            connection.close()
            return jsonify({"message": "Item atualizado com sucesso!"}), 200
        except Exception as e:
            print(f"Erro ao atualizar item: {e}")
            return jsonify({"error": "Erro ao atualizar item."}), 500

    elif request.method == 'DELETE':
        try:
            item_id = request.args.get('id')
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute('DELETE FROM items_batcaverna WHERE id = ?', (item_id,))
            connection.commit()
            connection.close()
            return jsonify({"message": "Item removido com sucesso!"}), 200
        except Exception as e:
            print(f"Erro ao remover item: {e}")
            return jsonify({"error": "Erro ao remover item."}), 500
        
        # Endpoint GET para obter o estado das câmeras
@app.route('/gestao/cameras', methods=['GET'])
def get_cameras():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, ativa FROM cameras")
        cameras = [{"id": row[0], "nome": row[1], "ativa": bool(row[2])} for row in cursor.fetchall()]
        conn.close()
        return jsonify(cameras), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint POST para atualizar o estado das câmeras
@app.route('/gestao/cameras', methods=['POST'])
def update_cameras():
    try:
        data = request.json 
        conn = get_connection()
        cursor = conn.cursor()

        for camera in data:
            cursor.execute(
                "UPDATE cameras SET ativa = ? WHERE id = ?",
                (1 if camera['ativa'] else 0, camera['id'])
            )

        conn.commit()
        conn.close()
        return jsonify({"message": "Câmeras atualizadas com sucesso."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)