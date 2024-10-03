import sqlite3
#from database.db import check_email
from models.restaurant import Restaurant


class DB:

    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.__setup_tables()

    def __setup_tables(self):
        cur = self.connection.cursor()  # Create a cursor object to interact with the database

        # Create table if it doesn't exist
        cur.execute('''
            CREATE TABLE IF NOT EXISTS restaurant (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name_restaurant TEXT NOT NULL,
                commission INT NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL
            )
            ''')

        cur.execute('''
            CREATE TABLE IF NOT EXISTS product (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name_product TEXT NOT NULL,
                price FLOAT NOT NULL,
                id_restaurant INT NOT NULL,
                FOREIGN KEY (id_restaurant) REFERENCES restaurant(id) 
            )
            ''')

        self.connection.commit()  # Commit the transaction

    def create_restaurant(self, restaurante: Restaurant):
        # Create a cursor object to interact with the database
        cur = self.connection.cursor()

        # Insert a record into the table
        cur.execute('''
        INSERT INTO restaurante (name_restaurant, commission, email, password) VALUES (?, ?, ?, ?)
        ''', (restaurant.name_restaurant, restaurant.commission, restaurant.email, restaurant.password)
                    )

        # Commit the transaction
        self.connection.commit()

    def login(self, email: str, password: str):
        cur = self.connection.cursor()

        # Search for the record
        cur.execute('''
                SELECT id, name_restaurant, commission, email, password 
                FROM restaurant 
                WHERE email = ? and password = ?
                ''', (email, password))
        record = cur.fetchone()
        if record is None:
            return None
        restaurant = Restaurant(pk=record[0],
                           nome_restaurante=record[1],
                           comissao=record[2],
                           email=record[3],
                           password=record[4])
        return restaurant

    # def check_email(self, email: str, password: None): #parei aq!!
    #     cur = self.connection.cursor()
    #
    #     # procura email
    #     cur.execute('''
    #                     SELECT email
    #                     FROM restaurante
    #                     WHERE email = ? and password = ?
    #                     ''', (email, password))
    #     record = cur.fetchone()
    #     if record is None:
    #         return None
    #     registered_email = Restaurant(email=record)
    #     return registered_email

    def get_user(self, email: str):
        cur = self.connection.cursor()

        # Search for the record
        cur.execute('''
        SELECT * FROM users WHERE email = ?
        ''', (email,))
        record = cur.fetchone()
        # record = cur.fetchall()
        if record is None:
            return None
        user = Restaurant(pk=record[0], email=record[1], password=record[2])
        return user

    def delete_user(self, email: str):
        cur = self.connection.cursor()

        # Delete the record
        cur.execute('''
        DELETE FROM users WHERE name = ?
        ''', (email,))

        self.connection.commit()