#arquivo que serve para fazer todos os casos de testes de cada função
from clients import *
from orders import *
from file_handler import *
from user_interface import *

################ testes do clients.py ################
teste_clients = read_clients()
print("LISTA DE CLIENTES:")
print(teste_clients)
print("\n")

#testando quando o cliente existe
print("CLIENTE EXISTE:")
find_client('12548796760', teste_clients)
print("\n")

#testando quando o cliente não existe
print("CLIENTE NÃO EXISTE:")
find_client('00000000000', teste_clients)
print("\n")

#printando um único cliente
print_client(teste_clients[0])

#printando a lista de clientes
list_clients(teste_clients)

delete_clients('12548796760', teste_clients)
print("NOVA LISTA DE CLIENTES:")
print(teste_clients)

#registrando um novo cliente
teste_clients = register_clients('12548796760', 'LUIZA CAMERINI', '987969219', teste_clients)
print("NOVA LISTA DE CLIENTES:")
print(teste_clients)

#registrando um cliente ja cadastrado
teste_clients = register_clients('12548796760', 'LUIZA CAMERINI', '987969219', teste_clients)


################ testes do orders.py ################
games = read_games()

list_games(games)

check_game_input('hjk')
check_game_input('123')
check_game_input('1l')

get_game()



################ testes do file_handler.py ################

################ testes do user_interface.py ################