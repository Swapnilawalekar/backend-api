from db_config import ALLOWED_TABLES

TABLE_SCHEMAS = {
    "empl2": {"Eid", "Name", "Salary"},
    "student": {"roll", "name", "branch", "marks"}
}

def validate_table(table_name):
    if table_name not in ALLOWED_TABLES:
        raise ValueError("Invalid table name")

def validate_columns(table_name, data):
    expected = TABLE_SCHEMAS.get(table_name)
    if not expected:
        raise ValueError("Schema not found")

    if set(data.keys()) != expected:
        raise ValueError("Invalid columns for table")
