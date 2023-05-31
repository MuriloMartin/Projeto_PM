import xml.etree.ElementTree as ET
from datetime import date, timedelta
from clients import *

def register_order(num_game, cpf, orders_list, stock, clients, rent_type):
    '''Funcao que registra os pedidos no dicionario.'''
    #order_list tem que ter cpf, nome do cliente, nome do jogo, tipo do aluguel, data de devolucao e data de aluguel
    today = date.today()
    today = today.strftime("%d/%m/%Y")
    order = {
        'cpf': cpf,
        'client_name': clients[find_client(cpf,clients)]['name'],
        'game_name': stock[num_game]['name'],
        'rent_type': 'Diário' if rent_type == 1 else 'Semanal',
        'rent_date': today,
        'return_date':(date.today() + timedelta(days=1)).strftime("%d/%m/%Y") if rent_type == 1 else (date.today() + timedelta(days=7)).strftime("%d/%m/%Y")
    }
    if find_order(order['cpf'],orders_list) == -1:
        orders_list.append(order)
        print('Pedido cadastrado com sucesso!')
        stock[num_game]['stock'] = int(stock[num_game]['stock']) - 1
        print(order)
    else:
        print("Cliente já possui pedido!")
    return orders_list


def find_order(cpf, orders_list):
    '''Funcao que procura um pedido no dicionario.'''
    for order_index in range(len(orders_list)):
        if orders_list[order_index]['cpf'] == cpf:
            return order_index
    print("Nenhum pedido encontrado.")
    return -1


def read_games(games):
    '''Funcao que pega os dados do XML de jogos e coloca no dicionario.'''
    tree = ET.parse('games.xml')
    root = tree.getroot()
    # games = []
    for game in root.iter('game'):
        game_name = game.find('name').text
        # game_price = game.find('price').text
        game_stock = game.find('stock').text
        games.append({'name': game_name, 'stock': game_stock})
    return games


def list_games(games):
    '''Funcao que lista os jogos do dicionario.'''
    print('Listando jogos:\n')
    for i, game in enumerate(games):
        print('(%d)' %(i))
        print('Nome:', game['name'])
        print('Estoque:', game['stock'])
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