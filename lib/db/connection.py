import sqlite3
from contextlib import contextmanager

# Database connection settings
DATABASE_PATH = '/home/user/development/phase3/Articles/lib/db/articles.db'

@contextmanager
def get_db_connection():
    """Context manager for database connection."""
    connection = None
    try:
        connection = sqlite3.connect(DATABASE_PATH)
        yield connection
    finally:
        if connection:
            connection.close()

def get_connection():
    conn = sqlite3.connect('articles.db')
    conn.row_factory = sqlite3.Row
    return conn

def initialize_database():
    """Initialize the database with required tables."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        # Example table creation
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS articles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

# Initialize the database when the module is run directly
if __name__ == "__main__":
    initialize_database()
    print("Database initialized successfully.")
