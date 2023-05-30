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