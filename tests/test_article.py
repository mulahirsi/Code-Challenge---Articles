import pytest
import os
import sys
from pathlib import Path

# Add the project root to Python path
sys.path.append(str(Path(__file__).parent.parent))

from lib.models.article import Article
from lib.db.connection import get_connection

@pytest.fixture(autouse=True)
def setup_database():
    # Setup test database
    with get_connection() as conn:
        cursor = conn.cursor()
        with open('lib/db/schema.sql') as f:
            conn.executescript(f.read())
        conn.commit()
    yield
    # Cleanup
    if os.path.exists('articles.db'):
        os.remove('articles.db')

def test_article_creation():
    article_id = Article.create("Test Title", "Test Content", 1)
    assert article_id is not None

    article = Article.find_by_id(article_id)
    assert article.title == "Test Title"
    assert article.content == "Test Content"
    assert article.author_id == 1

    article.title = "Updated Title"
    assert article.update() is True

    assert article.delete() is True