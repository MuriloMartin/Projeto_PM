#arquivo que serve para fazer todos os casos de testes de cada função
from clients import *
from orders import *
from file_handler import *
from user_interface import *
########################## testes do clients.py ################################
clients = [
    {'cpf': '12548796760', 'name': 'LUIZA CAMERINI', 'phone': '987969219'},
    {'cpf': '23069677843', 'name': 'MURILO', 'phone': '987654321'},
    {'cpf': '14644014702', 'name': 'MIGUEL', 'phone': '123456789'},
]


#file_hanlde
print('Teste read_clients')
print('Retorno esperado: ', clients)
print('Retorno obtido:', read_clients())