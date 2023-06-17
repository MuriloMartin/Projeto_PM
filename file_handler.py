import xml.etree.ElementTree as ET
from xml.dom import minidom
from dicttoxml import dicttoxml
import os.path

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
        order_cpf = order.find('cpf').text
        order_client_name = order.find('client_name').text
        order_game_name = order.find('game_name').text
        order_rent_type = order.find('rent_type').text
        order_rent_date = order.find('rent_date').text
        order_return_date = order.find('return_date').text
        orders_list.append({'cpf': order_cpf, 'client_name': order_client_name, 'game_name': order_game_name, 'rent_type': order_rent_type, 'rent_date': order_rent_date, 'return_date': order_return_date})
    return orders_list


def save_clientes(clients):
    xml_string = dicttoxml(clients, return_bytes=False, item_func=lambda x: 'client')
    tree = ET.ElementTree(ET.fromstring(xml_string))
    tree.write('clients.xml', encoding='utf-8', xml_declaration=True)
    return

def save_orders(clients):
    xml_string = dicttoxml(clients, return_bytes=False, item_func=lambda x: 'client')
    tree = ET.ElementTree(ET.fromstring(xml_string))
    tree.write('clients.xml', encoding='utf-8', xml_declaration=True)
    return

