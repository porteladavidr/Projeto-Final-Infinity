import pyodbc

# Configurações de conexão
server = 'DAVID\\SQLEXPRESS'  # Substitua pelo nome do seu servidor
database = 'INDUSTRIA_WAYNE'  # Substitua pelo nome do seu banco de dados
username = 'wayne'            # Substitua pelo nome do usuário
password = 'batman'           # Substitua pela senha do usuário

# Configuração da string de conexão
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

try:
    # Conectar ao banco de dados
    connection = pyodbc.connect(connection_string)
    print("Conexão com o banco de dados SQL Server foi bem-sucedida!")

    # Teste uma consulta simples
    cursor = connection.cursor()
    cursor.execute("SELECT TOP 1 * FROM Usuarios")
    row = cursor.fetchone()
    print("Dados da tabela Usuarios:", row)

except Exception as e:
    print("Erro ao conectar ao banco de dados:", e)

finally:
    # Fechar a conexão
    if 'connection' in locals():
        connection.close()
