from user_interface import *
from clients import *
from orders import *

#####################################################
clients = read_clients([])
balance = 0
#stock eh onde ficam os dados dos jogos (nome e quantidade em estoque)
stock = read_games([])
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
            # print("Fazer pedido")
            list_games(stock)
            num_game = get_game()
            #identificar qual o cliente que está fazendo o pedido
            cpf = get_user_cpf()
            #monta o pedido em um dicionario
            #order_list tem que ter cpf, nome do cliente, nome do jogo, tipo do aluguel, data de devolucao e data de aluguel
            rent = get_rent_type()
            orders_list = register_order(num_game, cpf, orders_list, stock, clients, rent)
            
        case 3 :
            # Listar clientes
            list_clients(clients)

        case 4 :
            # Buscar cliente
            # print("Buscar cliente")
            cpf = get_user_cpf()
            index = find_client(cpf, clients)
            if index > -1:
                print_client(clients[index])
        
        case 5 :
            # Remover cliente
            # print("Remover cliente")
            cpf = get_user_cpf()
            delete_clients(cpf,clients)

        case 6 :
            # Sair
           userEnderApplication = True

        case _  :
            print('Ação inválida. Tente novamente.')
    
    input('Press enter to continue...')

#escrever tudo em xml