from db_connection import get_connection
from validators import validate_table

def delete_data(table_name, condition):
    validate_table(table_name)

    conn = get_connection()
    cur = conn.cursor()

    where_clause = " AND ".join([f"{k}=%s" for k in condition.keys()])
    values = tuple(condition.values())

    sql = f"DELETE FROM {table_name} WHERE {where_clause}"

    cur.execute(sql, values)
    conn.commit()

    cur.close()
    conn.close()
