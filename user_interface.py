
def get_user_action():
    print("\nQual ação você deseja realizar?")
    print('1 - Cadastrar ')
    print('2 - Fazer pedido - não implementado')
    print('3 - Listar clientes ')
    print('4 - Buscar cliente - não implementado')
    print('5 - Remover cliente - não implementado')
    print('6 - Sair \n')
    return int(input('Digite o número correpondente à ação: '))

def get_user_cpf():
    return str(input('\nDigite o CPF do cliente: '))

def get_user_name():
    return str(input('Digite o nome do cliente: '))

def get_user_phone():
    return str(input('Digite o telefone do cliente: '))

#teste