from user_interface import *
from clients import *
from orders import *
from file_handler import *
from balance import *

#####################################################
clients = read_clients()
stock = read_stock()
orders_list = read_orders()
balance = read_balance()
response = read_response()
balance = handle_response(balance, response, stock)

#####################################################

clear_request()
clear_response()
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
                last_order_value = orders_list[-1]['value']
                balance = increase_cash(balance, last_order_value)
                print(orders_list)

        case 3 :
            # Devolver pedido
            id = get_order_id()
            orders_list = return_order(id, orders_list, stock)
        
        case 4:
            #Procurar pedido
            order_id = get_order_id()
            find_order(order_id, orders_list)
            
        case 5 :
            # Listar clientes
            list_clients(clients)

        case 6 :
            # Buscar cliente
            cpf = get_user_cpf()
            index = find_client(cpf, clients)
            if index > -1:
                print_client(clients[index])
        
        case 7 :
            # Remover cliente
            cpf = get_user_cpf()
            delete_clients(cpf,clients)

        case 8 :
            # Listar jogos
            list_games(stock)

        case 9 :
            # Listar jogos
            show_balance(balance)

        case 10 :
           # Sair
           userEnderApplication = True

        case _  :
            print('Ação inválida. Tente novamente.')
    
    input('Press enter to continue...')

#escrever tudo em xml

save_clients(clients)
save_orders(orders_list)
save_stock(stock)
save_balance(balance)