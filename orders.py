import xml.etree.ElementTree as ET
from datetime import timedelta, datetime
from clients import *
from user_interface import *
from file_handler import *
from random import randint

def register_order(num_game, orders_list, stock, clients):
    '''Funcao que registra os pedidos no dicionario.'''
    cpf = get_user_cpf()
    if find_client(cpf,clients) == -1:
        print("Cliente ainda não cadastrado. Cadatre o cliente antes de fazer o pedido.")
        register_clients(cpf, get_user_name(), get_user_phone(), clients)
    rent_type = get_rent_type()
    order = {
        'order_id' : get_valid_id(orders_list),
        'cpf': cpf,
        'client_name': clients[find_client(cpf,clients)]['name'],
        'game_name': stock[num_game]['name'],
        'rent_type': 'DIARIO' if rent_type == 1 else 'SEMANAL',
        'rent_date': datetime.now().strftime("%d/%m/%Y %H:%M"),
        'return_date':(datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y %H:%M") if rent_type == 1 
        else (datetime.now() + timedelta(days=7)).strftime("%d/%m/%Y %H:%M") ,
        'value': 50 if rent_type == 1 else 50,
        'status': 'PENDENTE'
    }
    if find_order(order['cpf'],orders_list) == -1: #se o cliente ainda nao tem pedidos feitos
        if check_game_stock(num_game, stock) == 1: #se o jogo estiver em estoque
            orders_list.append(order)
            stock[num_game]['stock'] = int(stock[num_game]['stock']) - 1
            print("Pedido feito com sucesso! O id do seu pedido e: ",order['order_id'])
    else:
        print("Cliente já possui pedido!")
    return orders_list

def return_order(order_id, orders_list, stock):
    '''Funcao que registra a devolucao de pedidos no dicionario.'''
    print('order_id',order_id)
    print('orders_list',orders_list)
    order_index = find_order(order_id,orders_list)
    if(order_index == -1):
        print("Pedido não encontrado.")
        return orders_list
    order = orders_list[order_index]
    print('order',order)
    if order['status'] == 'PENDENTE':
        orders_list[order_index]['status'] = 'DEVOLVIDO'
        print("Pedido devolvido com sucesso!")
        for i in range(len(stock)):
                    if stock[i]['name'] == order['game_name']:
                        stock[i]['stock'] = int(stock[i]['stock']) + 1
                        print("Devolução do jogo ", order['game_name'], " realizada com sucesso!")
                        break
        return orders_list
    else:
        print("Pedido já devolvido.")
        return orders_list

def get_valid_id(orders_list):
    '''Funcao que gera um id valido para um pedido'''
    while(1):
        id_try = randint(0,99)
        if find_order(id_try,orders_list) == -1:
            break
    return id_try

#funcao que le o xml de orders e guarda no dicionario orders_list

def check_game_stock(num_game, stock):
    '''Funcao que verifica se o jogo esta em estoque e diminui a quantidade em estoque.'''
    if int(stock[num_game]['stock']) == 0: #se o jogo nao estiver em estoque
        print("O jogo nao está disponível em estoque.")
        stock[num_game]['count'] = count_order(int(stock[num_game]['count']),num_game,stock)
        return 0
    else: #se o jogo estiver em estoque
        return 1


def count_order(count, num_game, stock):
    '''Funcao que controla quantas vezes o jogo indisponivel foi pedido.'''
    if count == 2:
        #Gerar json com o formato {nome: 'nome do jogo'}
        create_request(num_game, stock)
        print("Pedido para o fornecedor será enviado!")
        count = 0
    else:

        count = count+1

    return count


def find_order(order_id, orders_list):
    '''Funcao que procura um pedido no dicionario.'''
    for order_index in range(len(orders_list)):
        if orders_list[order_index]['order_id'] == str(order_id):
            return order_index
    #print("Nenhum pedido registrado encontrado.")
    return -1


def list_games(games):
    '''Funcao que lista os jogos do dicionario.'''
    print('Listando jogos:\n')
    for i, game in enumerate(games):
        print('JOGO (%d)' %(i))
        print('Nome:', game['name'])
        print('Quantidade em estoque:', game['stock'])
        print('Pedidos indisponíveis:',game['count'])
        print('------------------------------------')

def get_game(games):
    '''Funcao que pega o jogo escolhido pelo usuario.'''
    num_game = input('Digite o numero do jogo que deseja alugar: ')
    while check_game_input(num_game) != 0:
        num_game = input('Digite o numero do jogo que deseja alugar: ')
    if (num_game > str(len(games)-1)):
        print("Jogo não encontrado.")
        return -1
    return int(num_game)


def check_game_input(num_game):
    '''Funcao que verifica se o input do jogo escolhido pelo usuario e valido.'''
    if not (num_game.isdigit()):
        print("Input inválido.")
        return -1
    return 0