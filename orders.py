import xml.etree.ElementTree as ET

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