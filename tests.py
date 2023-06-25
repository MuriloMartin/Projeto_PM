#arquivo que serve para fazer todos os casos de testes de cada função
from clients import *
from orders import *
from file_handler import *
from user_interface import *

################################ testes do clients.py ################################
teste_clients = read_clients()
save_clients(teste_clients)
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
print("JOGO APENAS COM LETRAS:")
check_game_input('hjk')
print("\n")

#teste de input com letra e numero
print("JOGO COM LETRA E NUMERO:")
check_game_input('1l')
print("\n")

#teste de input vazio
print("JOGO VAZIO:")
check_game_input('')
print("\n")

#teste de input apenas com numeros
print("JOGO VÁLIDO (APENAS COM NUMERO):")
check_game_input('123')
print("\n")

################################ testes do file_handler.py ################################
lista_clientes = read_clients()
print("LISTA LIDA DE CLIENTES:")
print(lista_clientes)

lista_jogos = read_stock()
print("LISTA LIDA DE JOGOS:")
print(lista_jogos)

lista_pedidos = read_orders()
print("LISTA LIDA DE PEDIDOS:")
print(lista_pedidos)

save_clients(lista_clientes)
save_stock(lista_jogos)
save_orders(lista_pedidos)

create_request(0,lista_jogos)

################################ testes do user_interface.py ################################

#pegando a ação do usuario
get_user_action()
print('\n')

#pegando o cpf do usuario
get_user_cpf()
print('\n')

#pegando o nome do usuario
get_user_name()
print('\n')

#pegando o telefone do usuario
get_user_phone()
print('\n')

#checando o cpf do usuario
print("CPF VÁLIDO: (APENAS COM NUMEROS)")
check_cpf('12548796760')
print('\n')

print("CPF VAZIO:")
check_cpf('')
print('\n')

print("CPF COM LETRAS E NUMEROS:")
check_cpf('125487A676a')
print('\n')

print("CPF APENAS COM LETRAS:")
check_cpf('aaaaaaaaaaa')
print('\n')

print("CPF MENOR:")
check_cpf('1a3456710')
print('\n')

print("CPF MAIOR:")
check_cpf('123456789A011')
print('\n')

#checando o nome do usuario
print("NOME VAZIO:")
check_client_name('')
print('\n')

print("NOME APENAS COM NUMEROS:")
check_client_name('1234567890')
print('\n')

print("NOME COM NUMEROS:")
check_client_name('LUIZA123')
print('\n')

print("NOME COM CARACTERES ESPECIAIS:")
check_client_name('LUIZA!!')
print('\n')

print("NOME COM LETRAS MINUSCULAS:")
check_client_name('luiza')
print('\n')

print("NOME VÁLIDO:")
check_client_name('LUIZA')
print('\n')

#checando o telefone do usuario
print("TELEFONE VAZIO:")
check_client_phone('')
print('\n')

print("TELEFONE APENAS COM LETRAS:")
check_client_phone('bhjiujhgf')
print('\n')

print("TELEFONE COM CARACTERES ESPECIAIS:")
check_client_phone('98796921!')
print('\n')

print("TELEFONE COM LETRAS E NUMEROS:")
check_client_phone('98796921j0')
print('\n')

print("TELEFONE MAIOR:")
check_client_phone('987969219000')
print('\n')

print("TELEFONE MENOR:")
check_client_phone('98796921')
print('\n')

print("TELEFONE VÁLIDO:")
check_client_phone('987969219')
print('\n')

#checando o tipo de aluguel
print("TIPO DE ALUGUEL VAZIO:")
check_rent_type('')
print('\n')

print("TIPO DE ALUGUEL APENAS COM LETRAS:")
check_rent_type('bhjiujhgf')
print('\n')

print("TIPO DE ALUGUEL COM CARACTERES ESPECIAIS:")
check_rent_type('98796921!')
print('\n')

print("TIPO DE ALUGUEL COM LETRAS E NUMEROS:")
check_rent_type('98796921j0')
print('\n')

print("TIPO DE ALUGUEL VÁLIDO: (1)")
check_rent_type('1')
print('\n')

print("TIPO DE ALUGUEL VÁLIDO: (2)")
check_rent_type('2')