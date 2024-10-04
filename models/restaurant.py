import re

class Restaurant:
    def __init__(self,
                 pk: int | None,
                 email: str,
                 password: str,
                 name_restaurant: str,
                 commission: int
                 ):
        self.pk = pk
        self.email = email
        self.password = password
        self.commission = commission
        self.name_restaurant = name_restaurant

    def __str__(self):
        return f'{self.name_restaurant}'

    @staticmethod
    def verify_name_restaurant(name_restaurant):
        if len(name_restaurant) >= 10:
            return True
        return False

    @staticmethod
    def verify_commission(commission):
        if commission >= 0:
            return True
        return False

    @staticmethod
    def verify_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if re.match(pattern, email):
            return True
        return False

    @staticmethod
    def verify_password(password):
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$'
        if len(password) >= 5 and re.match(pattern, password):
            return True
        return False