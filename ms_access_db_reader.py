import pyodbc

def test_table_access() -> None:
    # Replace 'YourDatabasePath' with the path to your Access database file
    database_path = "data_sources/gest_gaz.accdb"

    # Create a connection to the Access database
    # connection_args = 'DRIVER={MDBTools};DBQ=%s;' % database_path
    connection_args = f"DRIVER={{MDBTools}};DBQ={database_path};"
    connection = pyodbc.connect(connection_args)

    # Create a cursor for executing SQL queries
    cursor = connection.cursor()

    # Example: Execute a query to retrieve data from a table
    cursor.execute('SELECT * FROM "T_Indice"')

    # Fetch and process the data
    for row in cursor.fetchall():
        print(row)

    # Close the cursor and the connection
    cursor.close()
    connection.close()
