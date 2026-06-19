import sqlite3
conn = sqlite3.connect("company.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER)
""")

employees = [
    (1, "John", "IT", 50000),
    (2, "Alice", "HR", 45000),
    (3, "Bob", "IT", 60000),
    (4, "Emma", "Sales", 40000),
    (5, "David", "HR", 55000)]

cursor.executemany(
    "INSERT OR REPLACE INTO employees VALUES (?, ?, ?, ?)",
    employees
)

conn.commit()
print("Database created successfully!")
conn.close()