from user_interface import *
from clients import *
from orders import *
from file_handler import *
global path
path = r'C:\Users\Murilo\Desktop\Projetos\Projeto_PM\comunicacao'
#####################################################
clients = read_clients()
stock = read_stock()
orders_list = read_orders()
order_fornecedor = []
balance = 0
#####################################################
print('clientes', clients)
print('\nestoque', stock)
print('\npedidos', orders_list)

userEnderApplication = False



while userEnderApplication == False:
    user_action = get_user_action()

    match user_action:
        case 1:
            # Cadastrar
            cpf = get_user_cpf()
            name = get_user_name()
            phone = get_user_phone()
            clients = register_clients(cpf, name, phone, clients)
        
        case 2 :
            # Fazer pedido
            list_games(stock)
            num_game = get_game(stock)
            check = check_game_stock(num_game, stock)
            if check == 1:
                orders_list = register_order(num_game, orders_list, stock, clients)
                print(orders_list)
        
        case 3:
            #Procurar pedido
            order_id = get_order_id()
            find_order(order_id, orders_list)
            
        case 4 :
            # Listar clientes
            list_clients(clients)

        case 5 :
            # Buscar cliente
            cpf = get_user_cpf()
            index = find_client(cpf, clients)
            if index > -1:
                print_client(clients[index])
        
        case 6 :
            # Remover cliente
            cpf = get_user_cpf()
            delete_clients(cpf,clients)

        case 7 :
            # Listar jogos
            list_games(stock)

        case 8 :
           # Sair
           userEnderApplication = True

        case _  :
            print('Ação inválida. Tente novamente.')
    
    input('Press enter to continue...')

#escrever tudo em xml

save_clients(clients)
save_orders(orders_list)
save_stock(stock)