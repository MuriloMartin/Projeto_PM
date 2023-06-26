import xml.etree.ElementTree as ET
from xml.dom import minidom
from dicttoxml import dicttoxml
import os.path
import json

global requerimentos_path, resposta_path
requerimentos_path = r'comunicacao\requerimento.json'
resposta_path = r'comunicacao\resposta.json'
preference_path = r'comunicacao\preferencia.json'

def read_clients():
    '''Funcao que pega os dados do XML de clientes e coloca no dicionario.'''
    file_exists = os.path.isfile('clients.xml')
    if file_exists == False:
        return []
    tree = ET.parse('clients.xml')
    root = tree.getroot()
    clients = []
    for client in root.iter('client'):
        client_cpf = client.find('cpf').text
        client_name = client.find('name').text
        client_phone = client.find('phone').text
        clients.append({'cpf': client_cpf, 'name': client_name, 'phone': client_phone})
    return clients

def read_stock():
    '''Funcao que pega os dados do XML de jogos e coloca no dicionario.'''
    file_exists = os.path.isfile('games.xml')
    if file_exists == False:
        return []
    tree = ET.parse('games.xml')
    root = tree.getroot()
    games = []
    for game in root.iter('game'):
        game_name = game.find('name').text
        game_count = game.find('count').text
        game_stock = game.find('stock').text
        games.append({'name': game_name, 'stock': game_stock, 'count': game_count})
    return games

def read_orders():
    '''Funcao que pega os dados do XML de pedidos e coloca no dicionario.'''
    file_exists = os.path.isfile('orders.xml')
    if file_exists == False:
        return []
    tree = ET.parse('orders.xml')
    root = tree.getroot()
    orders_list = []
    for order in root.iter('order'):
        order_id = order.find('order_id').text
        order_cpf = order.find('cpf').text
        order_client_name = order.find('client_name').text
        order_game_name = order.find('game_name').text
        order_rent_type = order.find('rent_type').text
        order_rent_date = order.find('rent_date').text
        order_return_date = order.find('return_date').text
        order_status = order.find('status').text
        orders_list.append({'order_id': order_id,'cpf': order_cpf, 'client_name': order_client_name, 'game_name': order_game_name, 'rent_type': order_rent_type, 'rent_date': order_rent_date, 'return_date': order_return_date, 'status': order_status})
    return orders_list


def save_clients(clients):
    '''Funcao que salva os dados do dicionario de clientes no XML.'''
    try:
        xml_string = dicttoxml(clients, return_bytes=False, item_func=lambda x: 'client')
        tree = ET.ElementTree(ET.fromstring(xml_string))
        tree.write('clients.xml', encoding='utf-8', xml_declaration=True)
        return 0
    except:
        return -1

def save_orders(orders):
    '''Funcao que salva os dados do dicionario de pedidos no XML.'''
    try:
        xml_string = dicttoxml(orders, return_bytes=False, item_func=lambda x: 'order')
        tree = ET.ElementTree(ET.fromstring(xml_string))
        tree.write('orders.xml', encoding='utf-8', xml_declaration=True)
        return 0
    except:
        return -1

def save_stock(stock):
    '''Funcao que salva os dados do dicionario de jogos no XML.'''
    try:
        xml_string = dicttoxml(stock, return_bytes=False, item_func=lambda x: 'game')
        tree = ET.ElementTree(ET.fromstring(xml_string))
        tree.write('games.xml', encoding='utf-8', xml_declaration=True)
        return 0
    except:
        return -1

def save_balance(balance):
    '''Funcao que salva os dados do dicionario de jogos no XML.'''
    print('balance', balance)
    try:
        xml_string = dicttoxml({'caixa': balance}, return_bytes=False, item_func=lambda x: 'game')
        tree = ET.ElementTree(ET.fromstring(xml_string))
        tree.write('balance.xml', encoding='utf-8', xml_declaration=True)
        return 0
    except:
        return -1
    
def read_balance():
    '''Função que lê um arquivo xml contendo o caixa da loja'''
    try:
        file_exists = os.path.isfile('balance.xml')
        if file_exists == False:
            return 0
        tree = ET.parse('balance.xml')
        root = tree.getroot()
        balance = root.find('caixa').text
        return float(balance)
    except:
        return -1

def create_request(num_game, stock):
    '''Funcao que cria um pedido de compra para o fornecedor.'''
    file_exists = os.path.isfile(resposta_path)
    if file_exists == False:
        currentUnavailableGames = []
    else:
        f = open(requerimentos_path, "r")
        emptyFile = os.stat(requerimentos_path).st_size == 0
        currentUnavailableGames = json.load(f) if not emptyFile else []
    gameName = stock[num_game]['name']
    if gameName in currentUnavailableGames:
        print("Jogo já está na lista de pedidos para o fornecedor. Ele estará disponível na proxima execução da aplicação")
        return 0 
    currentUnavailableGames.append(gameName)
    jsnStr = json.dumps(currentUnavailableGames)
    with open(requerimentos_path, "w") as outfile:
        outfile.write(jsnStr)
    return 0 

clear_request = lambda: open(requerimentos_path, "w").close()

def create_preference(gamesArray):
    '''Funcao que cria um arquivo de preferencias para o fornecedor.'''
    jsnStr = json.dumps(gamesArray)
    with open(preference_path, "w") as outfile:
        outfile.write(jsnStr)
    return

def read_response():
    file_exists = os.path.isfile(resposta_path)
    if file_exists == False:
        return {}
    f = open(resposta_path, "r")
    emptyFile = os.stat(resposta_path).st_size == 0
    response = json.load(f) if not emptyFile else {}
    return response

clear_response = lambda: open(resposta_path, "w").close()

