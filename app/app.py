from multiprocessing.resource_tracker import register
from database.db import DB

from models.product import Product
from models.restaurant import Restaurant
from utils.utils import Utils

#inicia app
class App:
    def __init__(self, db):
        self.db = db
        self.current_restaurant = None

    def start_app(self):
        self.show_main_menu()

    #mostra menu principal
    def show_main_menu(self):
        Utils.clear_screen()
        while True:
            print('-- Tela Inicial --')
            print('1. Cadastrar restaurante')
            print('2. Login')

            res = input('Escolha uma opção: ')

            if res == '1':
                Utils.clear_screen()
                self.show_register_menu()
                break
            elif res == '2':
                Utils.clear_screen()
                self.show_login_menu()
                break
            else:
                Utils.clear_screen()
                print('Esta opção não é valida, digite um dos números acima.')



    #abre menu para registro
    def show_register_menu(self):
        Utils.clear_screen()
        print('-- Registre seu restaurante --')

        name_restaurant = ''
        while not Restaurant.verify_name_restaurant(name_restaurant): #verificando nome do restaurante
            print('*Nome deve conter pelo menos 10 caracteres.')
            name_restaurant = input('Nome do restaurante: ')

        commission = 0
        while not Restaurant.verify_commission(commission):
            print('*Valor deve ser maior ou igual a zero.')
            commission = int(input('Comissão (em porcentagem): '))

        email = ''
        while not Restaurant.verify_email(email):
            print('*Deve ser um email válido.')
            email = input('Email: ')

        password = ''
        while not Restaurant.verify_password(password):
            print('*Deve conter ao menos uma letra maiúscila, uma minúscula e um número.')
            password = input('Senha: ')

        register_restaurant = Restaurant(pk=None, name_restaurant=name_restaurant, commission=commission, email=email, password=password)
        app = DB("example.db")
        DB.create_restaurant(app, register_restaurant) #insere
        Utils.clear_screen()
        print('Seu restaurante foi registrado!')
        self.show_main_menu()



    #abre menu para login
    def show_login_menu(self):
        Utils.clear_screen()

        print('-- Login --')
        email = input('Email: ')
        password = input('Senha: ')
        restaurant = self.db.login(email=email, password=password)
        
        if restaurant is None: #se login estiver incorreto ou nao existir
            Utils.clear_screen()
            print('Credenciais inválidas. Não possui cadastro? Registre-se agora mesmo!')
            self.show_main_menu()
        else:
            self.current_restaurant = restaurant
            print(f'Bem vindo, {restaurant.name_restaurant} seu ID é {restaurant.pk} e a comissão {restaurant.commission}.')
            self.show_restaurant_pannel(restaurant)

    def show_product_list(self, restaurant):
        self.current_restaurant = restaurant
        app = DB("example.db")
        product_list = DB.show_products(app, restaurant.pk)
        
        if product_list is None:
            print("Ainda não possui cardápio.")
        else:
            for product in product_list:
                print(f'{product.name_product:<20} --- ID: {product.pk:<5}')



    #mostra painel do restaurante
    def show_restaurant_pannel(self, restaurant):
        Utils.clear_screen()
        print(f'-- Produtos do {restaurant.name_restaurant} --')
        self.show_product_list(restaurant)
        
        while True:
            print('1. Cadastrar produto')
            print('2. Apagar produto')
            print('3. Alterar comissão')
            print('4. Logout')

            res = input('Escolha uma opção: ')
            
            self.current_restaurant = restaurant
            app = DB("example.db")
            
            if res == '1':
                Utils.clear_screen()
                self.show_insert_product(restaurant)
                break
            elif res == '2':
                Utils.clear_screen()
                self.show_delete_product(restaurant)
                break
            elif res == '3':
                Utils.clear_screen()
                self.show_alter_commission()
                break
            elif res == '4':
                #logout
                self.current_restaurant = None
                self.show_main_menu()

            else:
                Utils.clear_screen()
                print('Esta opção não é valida, digite um dos números acima.')
                
                
                
    #insere produto            
    def show_insert_product(self, restaurant):
        print('-- Cadastrar produto --')
        
        name_product = ''
        while not Product.verify_name_product(name_product):
            print('*Nome deve conter pelo menos 5 caracteres.')
            name_product = input('Produto: ')

        price = 0
        while not Product.verify_price(price):
            print('*Valor deve ser maior que zero.')
            price = int(input('Preço: '))
        
        self.current_restaurant = restaurant
        insert_product = Product(pk=None, name_product=name_product, price=price, fk_id_restaurant=restaurant.pk)
        app = DB("example.db")
        DB.insert_product(app, insert_product)
        Utils.clear_screen()
        print(f'O produto {name_product} foi registrado!')
        Utils.sleep(5)
        self.show_restaurant_pannel(restaurant)
        
        
        
    def show_delete_product(self, restaurant):
        print('-- Deletar produto --')
        self.show_product_list(restaurant)
        
        pk_product = 0
        while not int(pk_product):
            print('*Somente números.')
            pk_product = input('ID do produto: ')
            
        app = DB("example.db")
        DB.delete_product(app, pk_product)
        Utils.clear_screen()
        print(f'O produto de ID {pk_product} foi deletado.')
        Utils.sleep(5)
        self.show_restaurant_pannel(restaurant)
        
            
            
    def show_alter_commission(self, restaurant): #parei aqui
        new_commission = 0
        while not int(new_commission) and Restaurant.verify_commission(new_commission):
            print('Em porcentagem, de 0 a 100.')
            new_commission = input('Nova comissão: ')
            
        app = DB("example.db")
        DB.alter_product(app, new_commission)