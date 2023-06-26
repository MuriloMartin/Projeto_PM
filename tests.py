#arquivo que serve para fazer todos os casos de testes de cada função
from clients import *
from orders import *
from file_handler import *
from user_interface import *
from balance import *

teste_clients = [
    {'cpf': '12548796760', 'name': 'LUIZA CAMERINI', 'phone': '987969219'},
    {'cpf': '23069677843', 'name': 'MURILO', 'phone': '987654321'},
    {'cpf': '14644014702', 'name': 'MIGUEL', 'phone': '123456789'},
]

test_games = [
{
    "name": "COUP",
    "stock": '3',
    "count": '0'
},
{
    "name": "LOVE LETTER",
    "stock": '3',
    "count": '0'
},
{
    "name": "DEAD OF WINTER",
    "stock": '3',
    "count": '0'
},
{
    "name": "STARDEW VALLEY",
    "stock": '3',
    "count": '0'
}
]
empty_games = []

test_orders =[
    {
        'order_id': '264398',
        'cpf': '14644014702', 
        'client_name': 'MIGUEL', 
        'game_name': 'STARDEW VALLEY', 
        'rent_type': 'DIARIO', 
        'rent_date': '22/06/2023 13:27', 
        'return_date': '23/06/2023 13:27', 
        'status': 'DEVOLVIDO'},
    
    {
        'order_id': '186619',
        'cpf': '12345678911',
        'client_name': 'LIVIA',
        'game_name': 'COUP',
        'rent_type': 'SEMANAL',
        'rent_date': '24/06/2023 19:14',
        'return_date': '01/07/2023 19:14',
        'status': 'PENDENTE'
    },
     {
        'order_id': '451709',
        'cpf': '12345678911',
        'client_name': 'LIVIA',
        'game_name': 'COUP',
        'rent_type': 'SEMANAL',
        'rent_date': '24/06/2023 19:15',
        'return_date': '01/07/2023 19:15',
        'status': 'PENDENTE'
    },
        {
        'order_id': '434707',
        'cpf': '12345678911',
        'client_name': 'LIVIA',
        'game_name': 'COUP',
        'rent_type': 'SEMANAL',
        'rent_date': '24/06/2023 19:17',
        'return_date': '01/07/2023 19:17',
        'status': 'PENDENTE'
    }
]
################################ testes do file_handler.py ################################
lista_clientes = read_clients()
print("LISTA LIDA DE CLIENTES:")
print("Lista esperada: ")
print(teste_clients)
print('Lista encontrada: ')
print(lista_clientes)
print("\n")

lista_jogos = read_stock()
print("LISTA LIDA DE JOGOS:")
print("Lista esperada: ")
print(test_games)
print('Lista encontrada: ')
print(lista_jogos)
print("\n")

lista_pedidos = read_orders()
print("LISTA LIDA DE PEDIDOS:")
print("Lista esperada: ")
print(test_orders)
print('Lista encontrada: ')
print(lista_pedidos)
print("\n")


print('TESTES DE PERCISTENCIA DOS DADOS')
if save_clients(lista_clientes) == 0:
    print("Clientes salvos com sucesso")

if save_stock(lista_jogos) == 0:
    print("Jogos salvos com sucesso")
    
if save_orders(lista_pedidos) == 0:
    print("Pedidos salvos com sucesso")

print('\n\n')

################################ testes do clients.py ################################

print("LISTA DE CLIENTES:")
print("Cliente na lista: Luiza, Murilo e Miguel")
print(teste_clients)
print("\n")

#testando achar um cliente que ja existe
print("CLIENTE EXISTE:")
print('Procurando cliente com cpf 12548796760')
print(teste_clients[find_client('12548796760', teste_clients)])
print("\n")

#testando achar um cliente que nao existe
print("CLIENTE NÃO EXISTE:")
print('Procurando cliente com cpf 00000000000')
if (find_client('00000000000', teste_clients) == -1):
    print("Cliente não encontrado, teste ok")
print("\n")

#printando um unico cliente
print("PRINTA UM CLIENTE:")
print('Printando o primeiro cliente no registro')
print_client(teste_clients[0])
print("\n")

#printando a lista de clientes
print("PRINTA VÁRIOS CLIENTES:")
print('Printando a lista inteira de clientes')
list_clients(teste_clients)
print("\n")

#deletando um cliente que existe
print("DELETA CLIENTE QUE EXISTE:")
print('Deletando cliente com cpf 12548796760')
delete_clients('12548796760', teste_clients)
print("NOVA LISTA DE CLIENTES:")
print(teste_clients)
print("\n")

#deletando um cliente que nao existe
print("DELETA CLIENTE QUE NAO EXISTE:")
print('Deletando cliente com cpf 78932145600')
delete_clients('78932145600', teste_clients)
print("NOVA LISTA DE CLIENTES:")
print(teste_clients)
print("\n")

#registrando um novo cliente
print("REGISTRA NOVO CLIENTE:")
print('Registrando cliente com cpf: 12548796760, nome: LUIZA CAMERINI, telefone: 987969219 ')
teste_clients = register_clients('12548796760', 'LUIZA CAMERINI', '987969219', teste_clients)
print("NOVA LISTA DE CLIENTES:")
print(teste_clients)
print("\n")

#registrando um cliente ja cadastrado
print("REGISTRA CLIENTE EXISTENTE:")
print('Registrando cliente com cpf: 12548796760, nome: LUIZA CAMERINI, telefone: 987969219 ')
teste_clients = register_clients('12548796760', 'LUIZA CAMERINI', '987969219', teste_clients)
print("\n")


################################ testes do orders.py ################################
#teste de print de todos os jogos do dicionario
print("PRINTA VÁRIOS JOGOS DO DICIONARIO:")
print("Lista dos jogos: COUP, LOVE LETTER, DEAD OF WINTER, STARDEW VALLEY.")
list_games(test_games)
print("\n")

#teste de print de todos os jogos do dicionario vazio
print("PRINTA VÁRIOS JOGOS DO DICIONARIO VAZIO:")
print("Lista dos jogos: ")
list_games(empty_games)
print("\n")

#testando função find_order
print("TESTA FUNÇÃO FIND_ORDER ID EXISTENTE:")
print("Procurando pedido com id 264398")
print(test_orders[find_order('264398', test_orders)])
print("\n")

print("TESTA FUNÇÃO FIND_ORDER ID INEXISTENTE:")
print("Procurando pedido com id 000000")
find_order('000000', test_orders)
print("\n")




#teste de input apenas com letras
print("JOGO APENAS COM LETRAS:")
print("Checa o jogo: jklm")
check_game_input('kjk')
print("\n")

#teste de input com letra e numero
print("JOGO COM LETRA E NUMERO:")
print("Testa o jogo: 1l")
check_game_input('1l')
print("\n")

#teste de input vazio
print("JOGO VAZIO:")
print("Testa o jogo: '' ")
check_game_input('')
print("\n")

#teste de input apenas com numeros
print("JOGO VÁLIDO (APENAS COM NUMERO):")
print("Testa o jogo: 123")
if check_game_input('123') == 0:
    print('Input valido')
print("\n")

################################ testes do user_interface.py ################################

#checando o cpf do usuario
print("CPF VÁLIDO: (APENAS COM NUMEROS)")
print("Testando o cpf: 12548796760")
if check_cpf('12548796760'):
    print("CPF valido")
print('\n')

print("CPF VAZIO:")
print("Testando o cpf: ''")
check_cpf('')
print('\n')

print("CPF COM LETRAS E NUMEROS:")
print("Testando o cpf: 125487A676a")
check_cpf('125487A676a')
print('\n')

print("CPF APENAS COM LETRAS:")
print("Testando o cpf: aaaaaaaaaaa")
check_cpf('aaaaaaaaaaa')
print('\n')

print("CPF MENOR:")
print("Testando o cpf: 1a3456710")
check_cpf('1a3456710')
print('\n')

print("CPF MAIOR:")
print("Testando o cpf: 123456789A011")
check_cpf('123456789A011')
print('\n\n')

#checando o nome do usuario
print("NOME VAZIO:")
print("Testando o nome: '' ")
check_client_name('')
print('\n')

print("NOME APENAS COM NUMEROS:")
print("Testando o nome: 1234567890")
check_client_name('1234567890')
print('\n')

print("NOME COM NUMEROS:")
print("Testando o nome: LUIZA123")
check_client_name('LUIZA123')
print('\n')

print("NOME COM CARACTERES ESPECIAIS:")
print("Testando o nome: LUIZA!!")
check_client_name('LUIZA!!')
print('\n')

print("NOME COM LETRAS MINUSCULAS:")
print("Testando o nome: luiza")
check_client_name('luiza')
print('\n')

print("NOME VÁLIDO:")
print("Testando o nome: LUIZA")
if check_client_name('LUIZA'):
    print("Nome valido")
print('\n')

#checando o telefone do usuario
print("TELEFONE VAZIO:")
print("Testando o telefone: '' ")
check_client_phone('')
print('\n')

print("TELEFONE APENAS COM LETRAS:")
print("Testando o telefone: bhjiujhgf")
check_client_phone('bhjiujhgf')
print('\n')

print("TELEFONE COM CARACTERES ESPECIAIS:")
print("Testando o telefone: 98796921!")
check_client_phone('98796921!')
print('\n')

print("TELEFONE COM LETRAS E NUMEROS:")
print("Testando o telefone: 98796921j0")
check_client_phone('98796921j0')
print('\n')

print("TELEFONE MAIOR:")
print("Testando o telefone: 987969219000")
check_client_phone('987969219000')
print('\n')

print("TELEFONE MENOR:")
print("Testando o telefone: 98796921")
check_client_phone('98796921')
print('\n')

print("TELEFONE VÁLIDO:")
print("Testando o telefone: 987969219")
if check_client_phone('987969219'):
    print("Telefone valido")
print('\n')

#checando o tipo de aluguel
print("TIPO DE ALUGUEL VAZIO:")
print("Testando o tipo de aluguel: '' ")
check_rent_type('')
print('\n')

print("TIPO DE ALUGUEL APENAS COM LETRAS:")
print("Testando o tipo de aluguel: bhjiujhgf")
check_rent_type('bhjiujhgf')
print('\n')

print("TIPO DE ALUGUEL COM CARACTERES ESPECIAIS:")
print("Testando o tipo de aluguel: 98796921!")
check_rent_type('98796921!')
print('\n')

print("TIPO DE ALUGUEL COM LETRAS E NUMEROS:")
print("Testando o tipo de aluguel: 98796921j0")
check_rent_type('98796921j0')
print('\n')

print("TIPO DE ALUGUEL NUMÉRICO INVALIDO:")
print("Testando o tipo de aluguel: 3")
check_rent_type('3')
print('\n')


print("TIPO DE ALUGUEL VALIDO")
print('Testando o tipo de aluguel: 1')
if check_rent_type('1'):
    print("Tipo de aluguel valido")
print('\n')


print("TIPO DE ALUGUEL VÁLIDO")
print('Testando o tipo de aluguel: 2')
if check_rent_type('2'):
    print("Tipo de aluguel valido")
print('\n')


################################ testes do ballance.py ################################

#testando o aumento do caixa
print("AUMENTO DO CAIXA:")
print("Testando o aumento do com um valor não numérico")
increase_cash(100.0, 'a')
print('\n')

print("Testando o aumento do com um valor negativo")
increase_cash(100.0, -1)
print('\n')

print("Testando o aumento do com um valor válido")
print(increase_cash(100.0, 10))
print('\n')

#testando a diminuição do caixa

print("DIMINUIÇÃO DO CAIXA:")
print("Testando a diminuição do com um valor não numérico")
decrease_cash(100.0, 'a')
print('\n')

print("Testando a diminuição do com um valor negativo")
decrease_cash(100.0, -1)
print('\n')

print("Testando a diminuição do com um valor válido")
print(decrease_cash(100.0, 10))
print('\n')

#testando o print do caixa

print("PRINT DO CAIXA:")
print("Testando o print do caixa com um valor não numérico")
show_balance('a')
print('\n')

print("Testando o print do caixa com um valor válido")
show_balance(100.0)