from user_interface import *
from clients import *
from orders import *

#####################################################
#Pega os dados do XML e traz par o dicionario:
clients = read_clients([])
balance = 0
stock = read_games([])
# print(stock)
orders_list = []
#####################################################

userEnderApplication = False

while userEnderApplication == False:
    user_action = get_user_action()

    match user_action:
        case 1:
            # Cadastro de clientes
            cpf = get_user_cpf()
            name = get_user_name()
            phone = get_user_phone()
            clients = register_clients(cpf, name, phone, clients)
        
        case 2 :
            # Fazer pedido
            print("Fazer pedido")
            
        case 3 :
            # Listar clientes
            list_clients(clients)

        case 4 :
            # Buscar cliente
            print("Buscar cliente")
        
        case 5 :
            # Remover cliente
            print("Remover cliente")
            cpf = get_user_cpf()
            delete_clients(cpf,clients)

        case 6 :
            # Sair
           userEnderApplication = True

        case _  :
            print('ação inválida')
    
    input('Press enter to continue...')

# print(clients)