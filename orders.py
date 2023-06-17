import xml.etree.ElementTree as ET
from datetime import timedelta, datetime
from clients import *
from user_interface import *

def register_order(num_game, orders_list, stock, clients):
    '''Funcao que registra os pedidos no dicionario.'''
    cpf = get_user_cpf()
    rent_type = get_rent_type()
    order = {
        'cpf': cpf,
        'client_name': clients[find_client(cpf,clients)]['name'],
        'game_name': stock[num_game]['name'],
        'rent_type': 'DIARIO' if rent_type == 1 else 'SEMANAL',
        'rent_date': datetime.now().strftime("%d/%m/%Y %H:%M"),
        'return_date':(datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y %H:%M") if rent_type == 1 
        else (datetime.now() + timedelta(days=7)).strftime("%d/%m/%Y %H:%M")
    }
    if find_order(order['cpf'],orders_list) == -1: #se o cliente ainda nao tem pedidos feitos
        if check_game_stock(num_game, stock) == 1: #se o jogo estiver em estoque
            orders_list.append(order)
            stock[num_game]['stock'] = int(stock[num_game]['stock']) - 1
            print("Pedido feito com sucesso!")
    else:
        print("Cliente já possui pedido!")
    return orders_list


#funcao que le o xml de orders e guarda no dicionario orders_list


def check_game_stock(num_game, stock):
    '''Funcao que verifica se o jogo esta em estoque e diminui a quantidade em estoque.'''
    if int(stock[num_game]['stock']) == 0: #se o jogo nao estiver em estoque
        print("O jogo nao está disponível em estoque.")
        stock[num_game]['count'] = count_order(int(stock[num_game]['count']))
        return 0
    else: #se o jogo estiver em estoque
        return 1


def count_order(count):
    '''Funcao que controla quantas vezes o jogo indisponivel foi pedido.'''
    if count == 2:
        print("Pedido para o fornecedor precisa ser enviado!")
        count = 0
    else:
        count = count+1
    return count


def find_order(cpf, orders_list):
    '''Funcao que procura um pedido no dicionario.'''
    for order_index in range(len(orders_list)):
        if orders_list[order_index]['cpf'] == cpf:
            return order_index
    print("Nenhum pedido registrado encontrado.")
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


def get_game():
    '''Funcao que pega o jogo escolhido pelo usuario.'''
    num_game = input('Digite o numero do jogo que deseja alugar: ')
    while check_game_input(num_game) != 0:
        num_game = input('Digite o numero do jogo que deseja alugar: ')
    return int(num_game)


def check_game_input(num_game):
    '''Funcao que verifica se o input do jogo escolhido pelo usuario e valido.'''
    if not (num_game.isdigit()):
        print("Input inválido.")
        return -1
    return 0