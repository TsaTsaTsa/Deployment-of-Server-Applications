import os
import psycopg2
from flask import Flask, jsonify, request

app = Flask(__name__)

# Получаем параметры подключения из переменных окружения
DB_HOST = os.getenv('DB_HOST', 'pg-postgres-service')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', '1234')
DB_NAME = os.getenv('DB_NAME', 'postgres')
TABLE_NAME = os.getenv('TABLE_NAME', 'your_table_name')  # Укажите вашу таблицу по умолчанию

# Создаем подключение к базе данных
def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        dbname=DB_NAME
    )
    return conn

# Роут для получения данных из таблицы
@app.route('/data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Выполняем SQL-запрос для получения данных из указанной таблицы
    try:
        cursor.execute(f"SELECT * FROM {TABLE_NAME};")
        rows = cursor.fetchall()

        # Преобразуем результат в список словарей для удобства
        columns = [desc[0] for desc in cursor.description]  # Список названий колонок
        result = [dict(zip(columns, row)) for row in rows]

        # Закрываем соединение
        cursor.close()
        conn.close()

        return jsonify(result)

    except Exception as e:
        cursor.close()
        conn.close()
        return jsonify({'error': str(e)}), 500


@app.route('/')
def index():
    return "Welcome to the PostgreSQL API!\nDescription: This API connects to a PostgreSQL database and retrieves data from the specified table.\nGet data: /data - Get data from the table."
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
