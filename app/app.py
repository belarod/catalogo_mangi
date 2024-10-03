from multiprocessing.resource_tracker import register
#from database.db import DB

from models.restaurant import Restaurant
from utils.utils import Utils


class App:
    def __init__(self, db):
        self.db = db
        self.current_user = None

    def start_app(self):

        # self.db.create_restaurant(restaurante)
        #
        # user = self.db.login(email, senha)
        # if user is None:
        #     print('Erro no login')
        # else:
        #     print(f'Bem vindo, {user.nome_restaurante} seu ID é {user.pk} e a comissao {user.comissao}')
        #     self.current_user = user
        #
        # self.current_user.pk

        # print(user)
        # # Código acima pode ser descartado
        self.show_main_menu()

    def show_main_menu(self):
        while True:
            print('-- Tela Inicial --')
            print('1. Cadastrar restaurante')
            print('2. Login')

            res = input('Escolha uma opção: ')

            if res == '1':
                self.show_register_menu()
                break
            elif res == '2':
                self.show_login_menu()
                break
            else:
                print('Esta opção não é valida, digite um dos números acima.')
                Utils.clear_screen()

    @staticmethod
    def show_register_menu():
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

        password = 0
        while not Restaurant.verify_password(password):
            print('*Deve conter ao menos uma letra maiúscila, uma minúscula e um número.')
            password = input('Password: ')


        register_restaurant = Restaurant(pk=None, name_restaurant=name_restaurant, commission=commission, email=email, password=password)

    def show_login_menu(self):
        Utils.clear_screen()
        # user = self.db.login(email, senha)
        # if user is None:
        #     print('Erro no login')
        # else:
        #     print(f'Bem vindo, {user.nome_restaurante} seu ID é {user.pk} e a comissao {user.comissao}')
        #     self.current_user = user