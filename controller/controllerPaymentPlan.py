import SecretConfig
import psycopg2


def get_cursor():
    """
    Create the connection to the database and return a cursor to execute instructions
    """
    DATABASE = SecretConfig.DATABASE
    USER = SecretConfig.USER
    PASSWORD = SecretConfig.PASSWORD
    HOST = SecretConfig.HOST
    PORT = SecretConfig.PORT
    connection = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
    return connection.cursor()


def delete_table():
    """
    Deletes the table completely and all its data

    Drop the table, literally
    """
    sql = "DROP TABLE paymentplan;"
    cursor = get_cursor()
    cursor.execute(sql)
    cursor.connection.commit()


def delete_all_rows():
    """
    Deletes all the rows of the table, don´t call it in Production
    """
    sql = "DELETE FROM paymentplan"
    cursor = get_cursor()
    cursor.execute(sql)
    cursor.connection.commit()


def create_table():
    """
    Creates table if it does not exist
    """
    sql = ""
    with open("../sql/createpaymentplan.sql", "r") as f:
        sql = f.read()

    cursor = get_cursor()
    try:
        cursor.execute(sql)
        cursor.connection.commit()
    except Exception as err:
        """
        This may execute just if table already exist
        """
        print(err)
        cursor.connection.rollback()

