import psycopg2
from faker import Faker

def seed_database():
    # Підключення до PostgreSQL
    conn = psycopg2.connect(
        dbname="postgres_db", 
        user="postgres_user", 
        password="postgres_password", 
        host="localhost"
    )
    cur = conn.cursor()

    # Ініціалізація Faker
    fake = Faker()

    # Додавання статусів
    statuses = ['new', 'in progress', 'completed']
    for status in statuses:
        cur.execute("INSERT INTO status (name) VALUES (%s) ON CONFLICT (name) DO NOTHING;", (status,))

    # Додавання користувачів
    for _ in range(10):  # додати 10 випадкових користувачів
        fullname = fake.name()
        email = fake.email()
        cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s) ON CONFLICT (email) DO NOTHING;", (fullname, email))

    # Додавання завдань
    for _ in range(30):  # додати 30 випадкових завдань
        title = fake.sentence(nb_words=6)
        description = fake.text()
        status_id = fake.random_int(min=1, max=3)
        user_id = fake.random_int(min=1, max=10)
        cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s);", 
                    (title, description, status_id, user_id))

    # Збереження змін та закриття з'єднання
    conn.commit()
    cur.close()
    conn.close()
    print("Дані додано")

if __name__ == "__main__":
    seed_database()
