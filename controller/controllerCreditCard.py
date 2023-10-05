import SecretConfig
import psycopg2
import sys
from model import creditCard

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


def create_table():
    """
        Creates  table if it does not exist
    """
    sql = ""
    with open("../sql/createcreditcard.sql", "r") as f:
        sql = f.read()

    cursor = get_cursor()

    try:
        cursor.execute(sql)
        cursor.connection.commit()
        print("Table created succesfully")
    except Exception as err:
        """
        This may execute just if table already exist
        """
        print(err)
        cursor.connection.rollback()


def delete_table():
    """
    Deletes the table completely and all its data

    Drop the table, literally
    """
    sql = "DROP TABLE creditcard;"
    cursor = get_cursor()
    cursor.execute(sql)
    cursor.connection.commit()


def delete_all_rows():
    """
    Deletes all the rows of the table

    If you execute this on Prod, already lost your job
    """
    sql = "DELETE FROM creditcard"
    cursor = get_cursor()
    cursor.execute(sql)
    cursor.connection.commit()


def delete_a_creditcard(creditcard: creditCard):
    """
    Deletes a credit card from the table
    """
    sql = f"DELETE FROM credit_cards WHERE card_number = '{creditcard.card_number}'"
    cursor = get_cursor()
    cursor.execute(sql)
    cursor.connection.commit()

