def get_user_action():
    '''Funcao que gerencia e mostra as acoes do usuario.'''
    print("\nQual ação você deseja realizar?")
    print('1 - Cadastrar')
    print('2 - Fazer pedido')
    print('3 - Devolver pedido')
    print('4 - Procurar pedido')
    print('5 - Listar clientes')
    print('6 - Buscar cliente')
    print('7 - Remover cliente')
    print('8 - Listar jogos')
    print('9 - Mostrar saldo')
    print('10 - Sair\n')
    return int(input('Digite o número correpondente à ação: '))


def get_user_cpf():
    '''Funcao que pega o CPF do usuario.'''
    user_cpf = str(input('\nDigite o CPF do cliente: '))
    while not check_cpf(user_cpf):
        user_cpf = str(input('Digite o CPF do cliente: '))
    return user_cpf


def get_user_name():
    '''Funcao que pega o nome do usuario.'''
    user_name = str(input('Digite o nome do cliente: '))
    while not check_client_name(user_name):
        user_name = str(input('Digite o nome do cliente: '))
    return user_name


def get_user_phone():
    '''Funcao que pega o telefone do usuario.'''
    user_phone = str(input('Digite o telefone do cliente (lembre-se do 9 na frente): '))
    while not check_client_phone(user_phone):
        user_phone = str(input('Digite o telefone do cliente (lembre-se do 9 na frente): '))
    return user_phone


def check_cpf(cpf):
    '''Funcao que verifica se o CPF do usuario está no formato correto.'''
    if (len(cpf) == 11):
        for caractere in cpf:
            if not caractere.isdigit():
                print("CPF possui caracteres inválidos.")
                return False
        return True
    else:
        print("CPF possui tamanho inválido.")
        return False


def check_client_name(name):
    '''Funcao que verifica se o nome do cliente está no formato correto ord(c) retorna o valor do caractere na tabela ASCII'''

    isValid = all(ord(c) < 91 and ord(c) > 64 or ord(c)== 32 for c in name)
    if isValid:
        return True

    hasLower = any(ord(c) >= 97 and ord(c) <= 122 for c in name)
    if hasLower:
        print("O nome do cliente deve ser escrito apenas em caracteres maiúsculos.")
        return False
    
    hasNumeric = any(ord(c) >= 48 and ord(c) <= 57 for c in name)
    if hasNumeric:
        print("O nome do cliente não deve possuir caracteres numéricos.")
        return False
    
    print("O nome do cliente não deve possuir acentos e/ou caracteres especiais.")
    return False


def check_client_phone(phone):
    '''Funcao que checa se o telefone do usuario esta no formato correto (contando que todos os telefones tenham tamanho 9)'''
    for c in phone:
        if not c.isdigit():
            print("O telefone do cliente possui caracteres não-numéricos.")
            return False
    if len(phone) != 9:
        print("O tamanho do telefone do cliente está incompatível.")
        return False
    return True


def get_rent_type():
    '''Funcao que pega o tipo de aluguel do usuario.'''
    rent_type = input('Digite o tipo de aluguel (diário (1) ou semanal (2)): ')
    while not check_rent_type(rent_type):
        rent_type = input('Digite o tipo de aluguel (diário (1) ou semanal (2)): ')
    return int(rent_type)


def check_rent_type(rent_type):
    '''Funcao que verifica se o tipo de aluguel do usuario esta no formato correto.'''
    if (rent_type == '1' or rent_type == '2'):
        return True
    else:
        print("Tipo de aluguel inválido.")
        return False

def get_order_id():
    '''Funcao que pega o id dado pelo usuario'''
    order_id = int(input('\nDigite o id do seu pedido: '))
    return order_id