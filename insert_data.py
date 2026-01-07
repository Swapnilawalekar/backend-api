from db_connection import get_connection
from validators import validate_table, validate_columns

def insert_data(table_name, data_dict):
    validate_table(table_name)
    validate_columns(table_name, data_dict)

    conn = get_connection()
    cur = conn.cursor()

    columns = ", ".join(data_dict.keys())
    placeholders = ", ".join(["%s"] * len(data_dict))
    values = tuple(data_dict.values())

    sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

    cur.execute(sql, values)
    conn.commit()

    cur.close()
    conn.close()


