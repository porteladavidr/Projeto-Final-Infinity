from database import get_connection

def get_user_by_username(username):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM Usuarios WHERE username = ? AND ativo = 1"
        cursor.execute(query, (username,))
        user = cursor.fetchone()
        if user:
            return {
                "id": user[0],
                "username": user[1],
                "senha_hash": user[2],
                "nome_completo": user[3],
                "email": user[4],
                "role": user[5]
            }
        return None
    except Exception as e:
        print("Erro ao buscar usuário:", e)
        return None
    finally:
        connection.close()
