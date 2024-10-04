from multiprocessing.resource_tracker import register
from database.db import DB

from models.restaurant import Restaurant
from utils.utils import Utils

#inicia app
class App:
    def __init__(self, db):
        self.db = db
        self.current_user = None

    def start_app(self):
        self.show_main_menu()

    #mostra menu principal
    def show_main_menu(self):
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
            self.show_restaurant_pannel()

    #mostra painel do restaurante
    def show_restaurant_pannel(self):
        Utils.clear_screen()
        print('painel do restaurante')
        #mostrar produtos cadastrados
        #1 cadastrar prod (insert
        #2 apagar prod (delete
        #3 alterar commission (update
        #4 logout (user = none e retornar ao menu principal
        pass