 

### Structure Guidelines:
1. **Models**: Python classes that interact with the database via SQL
- `author.py`: Author class with methods using SQL queries
- `article.py`: Article class with relationships to Author and Magazine
- `magazine.py`: Magazine class with relationships
 

2. **Database Layer**:
- `connection.py`: Database connection handling
- `schema.sql`: Table definitions and constraints
- `seed.py`: Populate database with test data
 

3. **Package Organization**:
- Use `__init__.py` files to make directories into packages
- Each model file should handle its own SQL queries
 

4. **Testing**:
- Create separate test files for each model
- Tests should verify SQL queries and data integrity
- Run tests with `pytest` from the main directory
 

## Testing Your Code
- Run `pytest` to verify your implementation
- For debugging, use `python lib/debug.py` to start an interactive session
- Set up test database with: `python scripts/setup_db.py`
 

## Deliverables
 1. Database Schema
Create SQL tables for Authors, Articles, and Magazines with appropriate relationships:
 

```sql
-- Example schema (implement in lib/db/schema.sql)
CREATE TABLE IF NOT EXISTS authors (
id INTEGER PRIMARY KEY,
name VARCHAR(255) NOT NULL
);
 

CREATE TABLE IF NOT EXISTS magazines (
id INTEGER PRIMARY KEY,
name VARCHAR(255) NOT NULL,
category VARCHAR(255) NOT NULL
);
 

CREATE TABLE IF NOT EXISTS articles (
id INTEGER PRIMARY KEY,
title VARCHAR(255) NOT NULL,
author_id INTEGER,
magazine_id INTEGER,
FOREIGN KEY (author_id) REFERENCES authors(id),
FOREIGN KEY (magazine_id) REFERENCES magazines(id)
);