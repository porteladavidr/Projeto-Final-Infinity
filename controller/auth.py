from database import get_connection

def login(username, senha_hash):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM Usuarios WHERE username = ? AND senha_hash = ? AND ativo = 1"
        cursor.execute(query, (username, senha_hash))
        user = cursor.fetchone()
        return user is not None
    except Exception as e:
        print("Erro ao logar usuário:", e)
        return False
    finally:
        connection.close()
