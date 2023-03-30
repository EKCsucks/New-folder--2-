import sqlite3
import pandas as pd
from sqlite3 import Error


# Establishes a connection to the sql database, prints error if failure to connect.
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(e)

    return connection


# Creates a table from SQL connection, and from a query
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def check_email_exists(conn, email):

    sql = """SELECT 1 from customers where email=?"""
    cur = conn.cursor()
    cur.execute(sql, [email])
    conn.commit()
    try:
        return cur.fetchall()[0][0]
    except IndexError:
        return 0


# Creates a user inserting into the table, based off customer parameter
def check_login(conn, user):
    sql = """SELECT user_id from customers where (email=? and password=?)"""
    cur = conn.cursor()
    cur.execute(sql, [user])
    conn.commit()
    try:
        return cur.fetchall()[0][0]
    except IndexError:
        return 0


def create_user(conn, user):
    sql = """INSERT INTO customers(email, password)
                     VALUES(?,?)"""
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()
    return cur.lastrowid


# make it a list Main function, path of database is database.db and creation table query for a customer ID,
# firstname, lastname and email. SQLite will then attempt to connect and add 2 users to the table.
def main():
    database = r"userdata.db"

    sql_create_projects_table ="""CREATE TABLE IF NOT EXISTS customers(customerID integer PRIMARY KEY,
             email text NOT NULL, password text NOT NULL);"""

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_projects_table)
        user = ("hello@hello.com", "password")
        create_user(conn, user)
        user = ("email@email.com", "notpassword")
        create_user(conn, user)
        df = pd.read_sql_query("SELECT * FROM customers", conn)
        print(df)
    else:
        print("error")

