import pyodbc
import yaml


def configfilereading():
    # Connect to SQL Server
    with open("C:/Users/Niyati.Wawre/.dbt/profiles.yml", "r") as ymlfile:
        cfg = yaml.safe_load(ymlfile)
    # return cfg["mssql"]
    return cfg["demo_dbt"]["outputs"]["dev"]


def sqlserverconnection():
    dbinformation = configfilereading()
    conn = pyodbc.connect(
        'Driver=' + dbinformation["driver"] + ';Server=' + dbinformation["server"] + ';Database=' + dbinformation[
            "database"] + ';UID=' + dbinformation["user"] + ';PWD=' + dbinformation["password"])
    return conn


def schemacreation():
    dbinformation = configfilereading()
    conn = sqlserverconnection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sys.schemas WHERE name = " + "'" + dbinformation["schema"] + "'")
    schemanamequery = cursor.fetchone()
    if schemanamequery:
        print("Schema is present")
    else:
        print("Schema is not present creating one")
        cursor.execute('CREATE SCHEMA nw')
    return dbinformation["schema"]
