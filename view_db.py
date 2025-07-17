import sqlite3

# Connect to the database
conn = sqlite3.connect('access_api.db')
cursor = conn.cursor()

# Show all tables
print("=== TABLES IN DATABASE ===")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
for table in tables:
    print(f"- {table[0]}")

print("\n=== STUDENTS DATA ===")
try:
    cursor.execute("SELECT * FROM students;")
    students = cursor.fetchall()
    
    # Get column names
    cursor.execute("PRAGMA table_info(students);")
    columns = [row[1] for row in cursor.fetchall()]
    print(f"Columns: {', '.join(columns)}")
    
    if students:
        for student in students:
            print(student)
    else:
        print("No students found")
except Exception as e:
    print(f"Error: {e}")

print("\n=== FACULTY DATA ===")
try:
    cursor.execute("SELECT * FROM faculty;")
    faculty = cursor.fetchall()
    if faculty:
        for f in faculty:
            print(f)
    else:
        print("No faculty found")
except Exception as e:
    print(f"Error: {e}")

print("\n=== IT STAFF DATA ===")
try:
    cursor.execute("SELECT * FROM it_staff;")
    staff = cursor.fetchall()
    if staff:
        for s in staff:
            print(s)
    else:
        print("No IT staff found")
except Exception as e:
    print(f"Error: {e}")

conn.close()