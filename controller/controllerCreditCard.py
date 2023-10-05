import SecretConfig
import psycopg2
from model.creditCard import CreditCard
import Exceptions


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
        Creates table if it does not exist
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


def search_by_id(card_number):
    cursor = get_cursor()
    cursor.execute(f"""SELECT card_number, owner_id, owner_name, bank_name, due_date, franchise, payment_day,
     monthly_fee, interest_rate FROM credit_cards where card_number = '{card_number}'""")

    row = cursor.fetchone()
    if row is None:
        raise Exceptions.NoCard

    result = CreditCard(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
    return result


def insert(creditcard: CreditCard):
    """Insert a credit card in the database"""

    cursor = get_cursor()

    try:

        card_number_search = search_by_id(creditcard.card_number)

        if card_number_search is None:
            pass
        elif card_number_search.card_number == creditcard.card_number:
            raise Exceptions.CreditCardAlreadyInDatabase
    except Exceptions.NoCard:
        pass
    except Exceptions.CreditCardAlreadyInDatabase:
        raise Exceptions.CreditCardAlreadyInDatabase

    try:

        cursor.execute(f"""
        INSERT INTO credit_cards (
            card_number, owner_id, owner_name, bank_name, due_date, franchise, payment_day, monthly_fee, interest_rate
        )
        VALUES
        (
            '{creditcard.card_number}', 
            '{creditcard.owner_id}', 
            '{creditcard.owner_name}', 
            '{creditcard.bank_name}', 
            '{creditcard.due_date}', 
            '{creditcard.franchise}', 
            '{creditcard.payment_day}',
            '{creditcard.monthly_fee}', 
            '{creditcard.interest_rate}'
        );
                        """)

        cursor.connection.commit()
        print("Credit card saved succesfully")
    except Exception as err:
        print(err)
        cursor.connection.rollback()


def delete_a_creditcard(creditcard: CreditCard):
    """
    Deletes a credit card from the table
    """
    sql = f"DELETE FROM credit_cards WHERE card_number = '{creditcard.card_number}'"
    cursor = get_cursor()
    cursor.execute(sql)
    cursor.connection.commit()

