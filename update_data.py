from db_connection import get_connection
from validators import validate_table

def update_data(table_name, update_dict, condition):
    validate_table(table_name)

    conn = get_connection()
    cur = conn.cursor()

    set_clause = ", ".join([f"{k}=%s" for k in update_dict.keys()])
    values = list(update_dict.values()) + list(condition.values())

    where_clause = " AND ".join([f"{k}=%s" for k in condition.keys()])

    sql = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"

    cur.execute(sql, values)
    conn.commit()

    cur.close()
    conn.close()
