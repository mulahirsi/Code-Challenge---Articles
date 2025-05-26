from ..db.connection import get_connection

class Article:
    def __init__(self, id=None, title=None, content=None, author_id=None):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id

    @classmethod
    def create(cls, title, content, author_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO articles (title, content, author_id)
                VALUES (?, ?, ?)
            """, (title, content, author_id))
            conn.commit()
            return cursor.lastrowid

    @classmethod
    def find_by_id(cls, id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM articles WHERE id = ?", (id,))
            row = cursor.fetchone()
            if row:
                return cls(row['id'], row['title'], row['content'], row['author_id'])
            return None

    def update(self):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE articles 
                SET title = ?, content = ?, author_id = ?
                WHERE id = ?
            """, (self.title, self.content, self.author_id, self.id))
            conn.commit()
            return cursor.rowcount > 0

    def delete(self):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM articles WHERE id = ?", (self.id,))
            conn.commit()
            return cursor.rowcount > 0