import re

class Product:
    def __init__(self,
                 pk: int,
                 name_product: str,
                 price: int,
                 fk_id_restaurant: int):
        self.pk = pk
        self.name_product = name_product
        self.price = price
        self.fk_id_restaurant = fk_id_restaurant
        
    @staticmethod
    def verify_name_product(name_product):
        if len(name_product) >= 5:
            return True
        return False
    
    @staticmethod
    def verify_price(price):
        if price > 0:
            return True
        return False
    
"""@staticmethod
    def verify_delete_input(pk_product):
        pk_product = re.sub(r'[^0-9]', '', pk_product)
        if pk_product:
            return pk_product
        else:
            return None  """