import sqlite3
#from database.db import check_email
from models.restaurant import Restaurant
from models.product import Product


class DB:

    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.__setup_tables()

    def __setup_tables(self): #cria as tabelas, caso não existam
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
                price INT NOT NULL,
                fk_id_restaurant INT NOT NULL,
                FOREIGN KEY (fk_id_restaurant) REFERENCES restaurant(id) 
            )
            ''')

        self.connection.commit()  # Commit the transaction
        cur.close()

    def create_restaurant(self, restaurant: Restaurant): #parametro espera um objeto do tipo Restaurant
        # Create a cursor object to interact with the database
        cur = self.connection.cursor()

        # Insert a record into the table
        cur.execute('''
        INSERT INTO restaurant (name_restaurant, commission, email, password) VALUES (?, ?, ?, ?)
        ''', (restaurant.name_restaurant, restaurant.commission, restaurant.email, restaurant.password)
                    )

        # Commit the transaction
        self.connection.commit()
        cur.close()

    def login(self, email: str, password: str):
        cur = self.connection.cursor()

        # Search for the record
        cur.execute('''
                SELECT id, name_restaurant, commission, email, password
                FROM restaurant
                WHERE email = ? and password = ?
                ''', (email, password))
        record = cur.fetchone()
        cur.close()
        if record is None:
            return None
        restaurant = Restaurant(pk=record[0],
                           name_restaurant=record[1],
                           commission=record[2],
                           email=record[3],
                           password=record[4])
        return restaurant
    
    
    def show_products(self, fk_id_restaurant):
        cur = self.connection.cursor()

        # Search for the record
        cur.execute('''
                SELECT id, name_product, price
                FROM product
                WHERE fk_id_restaurant = ?
                ''', (fk_id_restaurant,))
        
        record = cur.fetchall()
        cur.close()
        product_list = []
        
        
        if not record:
            return None
        else:
            for product in record:
                product_inst = Product(pk=product[0], name_product=product[1], price=product[2], fk_id_restaurant=fk_id_restaurant)
                product_list.append(product_inst)
        return product_list
    
    def insert_product(self, product: Product):
        cur = self.connection.cursor()
        
        cur.execute('''
                INSERT INTO product (name_product, price, fk_id_restaurant)
                VALUES (?, ?, ?)
                ''', (product.name_product, product.price, product.fk_id_restaurant))
        
        self.connection.commit()
        cur.close()
        
        
        
    def delete_product(self, pk):
        cur = self.connection.cursor()
        
        cur.execute('''
                DELETE FROM product
                WHERE id = ?
                ''', (pk,))
        
        self.connection.commit()
        cur.close()
        
    def alter_commission(self, pk, new_commission):
        cur = self.connection.cursor()
        
        cur.execute('''
                UPDATE restaurant
                SET commission = ?
                WHERE id = ?
                ''', (new_commission, pk))
        
        self.connection.commit()
        cur.close()



    def show_highest_commission(self):
        cur = self.connection.cursor()
        
        cur.execute('''
                SELECT commission
                FROM restaurant
                ORDER BY commission DESC
                LIMIT 1
                ''')
        
        highest_commission = cur.fetchone()
        
        if highest_commission:
            print(f"The highest commission is: {highest_commission[0]}")
            return highest_commission
        
        cur.close()
        
        
        
    def show_current_commission(self, pk):
        cur = self.connection.cursor()
        
        cur.execute('''
                SELECT commission
                FROM restaurant
                WHERE id = ?
                ''', (pk,))
        
        current_commission = cur.fetchone()
        
        if current_commission:
            return current_commission[0]
        
        cur.close()

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

    # def get_restaurant(self, email: str):
    #     cur = self.connection.cursor()
    #
    #     # Search for the record
    #     cur.execute('''
    #     SELECT * FROM users WHERE email = ?
    #     ''', (email,))
    #     record = cur.fetchone()
    #     # record = cur.fetchall()
    #     if record is None:
    #         return None
    #     user = Restaurant(pk=record[0], email=record[1], password=record[2])
    #     return user
    #
    # def delete_restaurant(self, email: str):
    #     cur = self.connection.cursor()
    #
    #     # Delete the record
    #     cur.execute('''
    #     DELETE FROM users WHERE name = ?
    #     ''', (email,))
    #
    #     self.connection.commit()