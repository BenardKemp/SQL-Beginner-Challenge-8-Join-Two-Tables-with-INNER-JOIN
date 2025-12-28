import sqlite3

def join_two_tables_with_inner_join():
    # Connect to a local SQLite database (example.db)
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    # SQL query for Challenge #8
    query = "SELECT p.name, s.supplier_name FROM products p INNER JOIN suppliers s ON p.supplier_id = s.supplier_id"

    cursor.execute(query)
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    conn.close()


if __name__ == "__main__":
    join_two_tables_with_inner_join()