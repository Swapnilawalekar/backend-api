from db_connection import get_connection
from validators import validate_table

def fetch_all(table_name):
    validate_table(table_name)

    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows
