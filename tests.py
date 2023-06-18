#arquivo que serve para fazer todos os casos de testes de cada função
from clients import *
from orders import *
from file_handler import *
from user_interface import *

################################ testes do clients.py ################################
teste_clients = read_clients()
print("LISTA DE CLIENTES:")
print(teste_clients)
print("\n")

#testando achar um cliente que ja existe
print("CLIENTE EXISTE:")
find_client('12548796760', teste_clients)
print("\n")

#testando achar um cliente que nao existe
print("CLIENTE NÃO EXISTE:")
find_client('00000000000', teste_clients)
print("\n")

#printando um unico cliente
print("PRINTA UM CLIENTE:")
print_client(teste_clients[0])
print("\n")

#printando a lista de clientes
print("PRINTA VÁRIOS CLIENTES:")
list_clients(teste_clients)
print("\n")

#deletando um cliente que existe
print("DELETA CLIENTE QUE EXISTE:")
delete_clients('12548796760', teste_clients)
print("NOVA LISTA DE CLIENTES:")
print(teste_clients)
print("\n")

#deletando um cliente que nao existe
print("DELETA CLIENTE QUE NAO EXISTE:")
delete_clients('78932145600', teste_clients)
print("NOVA LISTA DE CLIENTES:")
print(teste_clients)
print("\n")

#registrando um novo cliente
print("REGISTRA NOVO CLIENTE:")
teste_clients = register_clients('12548796760', 'LUIZA CAMERINI', '987969219', teste_clients)
print("NOVA LISTA DE CLIENTES:")
print(teste_clients)
print("\n")

#registrando um cliente ja cadastrado
print("REGISTRA CLIENTE EXISTENTE:")
teste_clients = register_clients('12548796760', 'LUIZA CAMERINI', '987969219', teste_clients)
print("\n")

################################ testes do orders.py ################################
games = read_stock()
games2=[]

#teste de print de todos os jogos do dicionario
print("PRINTA VÁRIOS JOGOS DO DICIONARIO:")
list_games(games)
print("\n")

#pega o numero do jogo
print("PEGA O NUMERO DO JOGO:")
get_game(games)
print("\n")

#teste de print de todos os jogos do dicionario vazio
print("PRINTA VÁRIOS JOGOS DO DICIONARIO VAZIO:")
list_games(games2)

#teste de input apenas com letras
print("CHECA INPUT INVÁLIDO (INPUT APENAS LETRA):")
check_game_input('hjk')
print("\n")

#teste de input com letra e numero
print("CHECA INPUT INVÁLIDO (INPUT COM LETRA E NUMERO):")
check_game_input('1l')
print("\n")

#teste de input vazio
print("CHECA INPUT INVÁLIDO (INPUT VAZIO):")
check_game_input('')
print("\n")

#teste de input apenas com numeros
print("CHECA INPUT VÁLIDO (INPUT APENAS NUMEROS):")
check_game_input('123')
print("\n")

################################ testes do file_handler.py ################################

################################ testes do user_interface.py ################################