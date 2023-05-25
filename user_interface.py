
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
    user_name = str(input('Digite o nome do cliente: '))
    while not check_client_name_2(user_name):
        user_name = str(input('Digite o nome do cliente: '))
    return user_name

def get_user_phone():
    return str(input('Digite o telefone do cliente: '))

def check_cpf(cpf):
    '''Funcao que verifica se o CPF do cliente está no formato correto.'''
    if (len(cpf) == 11):
        for caractere in cpf:
            if not caractere.isdigit():
                print("CPF possui caracteres inválidos.")
                return False
        return True
    else:
        print("CPF possui tamanho inválido.")
        return False



def check_client_name_2(name):
    #Funcao que verifica se o nome do cliente está no formato correto
    #ord(c) retorna o valor do caractere na tabela ASCII

    isValid = all(ord(c) < 91 and ord(c) > 64 or ord(c)== 32 for c in name)
    if isValid:
        return True

    hasLower = any(ord(c) >= 97 and ord(c) <= 122 for c in name)
    if hasLower:
        print("O nome do cliente possui letras minúsculas.")
        return False
    
    hasNumeric = any(ord(c) >= 48 and ord(c) <= 57 for c in name)
    if hasNumeric:
        print("O nome do cliente possui caracteres numéricos.")
        return False
    
    print("O nome do cliente possui acentos e/ou caracteres especiais.")
    return False


#from unidecode import unidecode
# def check_client_name(name):
#     '''Funcao que verifica se o nome do cliente está no formato correto.'''
#     sem_acentos = unidecode(name) #converte em um nome sem acentos
#     for c in name:
#         if c.isdigit():
#             print("O nome do cliente possui caracteres numéricos.")
#             return False
#         elif c.islower():
#             print("O nome do cliente possui letras minúsculas.")
#             return False
#         elif sem_acentos != name or not name.isalpha(): #se o caractere tiver acento ou caracter especial
#             print("O nome do cliente possui acentos e/ou caracteres especiais.")
#             return False
#     return True


def check_client_tel(tel):
    '''Funcao que checa se o telefone do cliente esta no formato correto (contando que todos os telefones tenham tamanho 9)'''
    for c in tel:
        if not c.isdigit():
            print("O telefone do cliente possui caracteres não-numéricos.")
            return False
    if len(tel) != 9:
        print("O tamanho do telefone do cliente está incompatível.")
        return False
    return True

########### TESTES ############
#check_client_name_2("LUIZA 10 FERREIRA CAMERINI")
#check_client_name_2("LUiza FERREIRA CAMERINI")
#check_client_name_2("LUIZ@@ FERREIRA CAMERINI")
check_client_name_2("LUIZA FERREIRA CAMERINI")
check_cpf('1254!796760')
check_client_tel("98796921t")