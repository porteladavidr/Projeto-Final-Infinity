from controller.database import get_connection
from bcrypt import hashpw, gensalt

def gerar_hash_senha(senha):
    salt = gensalt()
    return hashpw(senha.encode('utf-8'), salt)

def add_user(username, senha, nome_completo, email, role):

    senha_hash = gerar_hash_senha(senha)

    connection = get_connection()
    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO Usuarios (username, senha_hash, nome_completo, email, role)
        VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(query, (username, senha_hash, nome_completo, email, role))
        connection.commit()
        print("Usuário adicionado com sucesso!")
    except Exception as e:
        print("Erro ao adicionar usuário:", e)
    finally:
        connection.close()

# Dados para adicionar
username = "funcionario"
senha = "funcionario"
nome_completo = "funcionario"
email = "funcionario@exemplo.com"
role = "funcionario"

add_user(username, senha, nome_completo, email, role)
