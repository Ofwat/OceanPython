import os

import pyodbc
import yaml


def read_config_file():
    with open(os.environ['USERPROFILE'] + '/.dbt/profiles.yml', "r") as ymlfile:
        cfg = yaml.safe_load(ymlfile)
    target = cfg["Ocean"]["target"]
    return cfg["Ocean"]["outputs"][target]


def sql_server_connection():
    dbinformation = read_config_file()
    conn = pyodbc.connect('Driver=' + dbinformation["driver"] + ';'
                            'Server=' + dbinformation["server"] + ';'
                            'Database=' + dbinformation["database"] + ';'
                            'UID=' + dbinformation["user"] + ';'
                            'PWD=' + dbinformation["password"] + ';')
    return conn


def schema_present():
    db_information = read_config_file()
    schema_name = db_information["schema"] + "_generated_sources"
    conn = sql_server_connection()
    cursor = conn.cursor()
    statement = "SELECT * FROM sys.schemas WHERE name = " + "'" + schema_name + "'"
    cursor.execute(statement)
    if cursor.fetchone():
        print("Schema " + schema_name + " is present")
    else:
        print("Schema " + schema_name + " is not present")
        print("CREATE SCHEMA " + schema_name)
        cursor.execute("CREATE SCHEMA " + schema_name)
        conn.commit()
    conn.close()
    return schema_name


def table_present(schema_name, table_name):
    conn = sql_server_connection()
    cursor = conn.cursor()
    statement = "SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '" + schema_name + "' AND TABLE_NAME = '" + table_name + "'"
    cursor.execute(statement)
    if cursor.fetchone():
        print("Table " + schema_name + '.' + table_name + " is present")
        table_present = True
    else:
        print("Table " + schema_name + '.' + table_name + " is not present")
        table_present = False
    conn.close()
    return table_present
