import sqlite3
conn = sqlite3.connect("company.db")
cursor = conn.cursor()
print("All Employees")
for row in cursor.execute("SELECT * FROM employees"):
    print(row)

print("\nSalary > 50000")
for row in cursor.execute(
    "SELECT * FROM employees WHERE salary > 50000"
):
    print(row)

print("\nDepartment Wise Count")
for row in cursor.execute(
    "SELECT department, COUNT(*) FROM employees GROUP BY department"
):
    print(row)

print("\nAverage Salary")
for row in cursor.execute(
    "SELECT AVG(salary) FROM employees"
):
    print(row)
conn.close()