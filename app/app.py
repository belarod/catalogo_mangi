from multiprocessing.resource_tracker import register
from database.db import DB
from utils import clear_screen
from models.restaurant import Restaurant


class App:
    def __init__(self, db):
        self.db = db
        self.current_user = None

    def start_app(self):
        # email = input('Digite seu email')
        #
        # comissao = -1
        # while not Restaurante.valida_comissao(comissao):
        #     comissao = int(input('Digite a comissao'))

        #nome_restaurante = 'Baratiê'
        # while not Restaurante.valida_nome_restaurante(nome_restaurante):
        #     nome_restaurante = int(input('Digite o nome do restaurante'))

        # senha = 'Senh4!'
        # restaurante = Restaurante(None, email, senha, nome_restaurante, comissao)
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
        self.show_register_menu()

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
                #clear_screen()


    def show_register_menu(self):
        print('-- Registre seu restaurante --')

        name_restaurant = ''
        while not Restaurant.verify_name_restaurant(name_restaurant): #verificando nome do restaurante
            print('*Nome deve conter pelo menos 10 caracteres.')
            name_restaurant = input('Nome do restaurante: ')

        commission = ''
        while not Restaurant.verify_commission(commission):
            print('*Valor deve ser maior ou igual a zero.')
            commission = input('Comissão (em porcentagem): ')

        email = ''
        while not Restaurant.verify_email(email):
            print('*Deve ser um email válido.')
            email = input('Email: ')

        password = ''
        while not Restaurant.verify_password(password):
            print('*Deve conter ao menos uma letra maiúscila, uma minúscula e um número.')
            password = input('Password: ')


        register_restaurant = Restaurant(None, name_restaurant, commission, email, password)

    def show_login_menu(self):
        print('login')