import psycopg2

def create_tables():
    # Підключення до PostgreSQL
    conn = psycopg2.connect(
        dbname="your_dbname", 
        user="your_user", 
        password="your_password", 
        host="localhost"
    )
    cur = conn.cursor()

    # Створення таблиці користувачів
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        fullname VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL
    );
    """)

    # Створення таблиці статусів
    cur.execute("""
    CREATE TABLE IF NOT EXISTS status (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) UNIQUE NOT NULL
    );
    """)

    # Створення таблиці завдань
    cur.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id SERIAL PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        description TEXT,
        status_id INTEGER REFERENCES status(id) ON DELETE CASCADE,
        user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
    );
    """)

    # Збереження змін та закриття з'єднання
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    create_tables()
