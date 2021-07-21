from util import dbUtils as db

table_name = 'pc_actuals_updates'


def create_actuals_table():
    schema_name = db.schema_present()
    if db.table_present(schema_name, table_name):
        return schema_name

    print("creating table " + schema_name + '.' + table_name)
    ocean_db_conn = db.sql_server_connection()
    ocean_cursor = ocean_db_conn.cursor()
    ocean_cursor.execute('''
        create table ''' + schema_name + '.' + table_name + ''' (
            updated_at datetime,
            excel_file nvarchar(max),
            excel_user nvarchar(max),
            comment nvarchar(max),
            amp_name varchar(16),
            OFWAT_Year varchar(7),
            submission_status varchar(18),
            unique_id nvarchar(max),
            company_acronym varchar(50),
            company_name varchar(50),
            pcl nvarchar(18),
            pcl_met nvarchar(max),
            outperformance_or_underperformance_payment nvarchar(max),
            forecast_of_total_2020_25_outperformance_or_underperformance_payment nvarchar(max)
        );
    ''')
    ocean_db_conn.commit()
    ocean_db_conn.close()

    return schema_name


def insert_to_actuals_table(records_for_db):
    schema_name = create_actuals_table()

    ocean_db_conn = db.sql_server_connection()
    ocean_cursor = ocean_db_conn.cursor()

    insert_statement = '''
        insert ''' + schema_name + '.' + table_name + ''' (
            updated_at,
            excel_file,
            excel_user,
            comment,
            amp_name,
            OFWAT_Year,
            submission_status,
            unique_id,
            company_acronym,
            company_name,
            pcl,
            pcl_met,
            outperformance_or_underperformance_payment, 
            forecast_of_total_2020_25_outperformance_or_underperformance_payment
        )
        values (?,?,?,?,?,?,?,?,?,?,?,?,?,?);
    '''
    ocean_cursor.executemany(insert_statement, records_for_db)
    ocean_db_conn.commit()
    ocean_db_conn.close()
