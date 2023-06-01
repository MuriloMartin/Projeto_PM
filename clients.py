import xml.etree.ElementTree as ET

def register_clients(cpf, name, phone, clients):
    '''Funcao que registra os clientes no dicionario.'''
    client = {
        'cpf': cpf,
        'name': name,
        'phone': phone
    }
    if find_client(client['cpf'],clients) == -1:
        clients.append(client)
        print('Cliente cadastrado com sucesso!')
    else:
        print("Cliente com CPF já cadastrado.")
    return clients


def list_clients(clients):
    '''Funcao que lista os clientes do dicionario.'''
    print('\nNúmero de clientes cadastrados:', len(clients))
    print('Listando clientes:\n')
    for client in clients:
        print_client(client)


def print_client(client):
    '''Funcao que imprime apenas um cliente.'''
    print('CPF:', client['cpf'])
    print('Nome:', client['name'])
    print('Telefone:', client['phone'])
    print('------------------------------------')


def find_client(cpf, clients):
    '''Funcao que procura um cliente no dicionario.'''
    for client_index in range(len(clients)):
        if clients[client_index]['cpf'] == cpf:
            print("Cliente encontrado.")
            return client_index
    print("Cliente não encontrado.")
    return -1


def delete_clients(cpf,clients):
    '''Funcao que exclui clientes do dicionario.'''
    client_index = find_client(cpf,clients)
    if(client_index == -1):
        return -1
    clients.pop(client_index)
    print("Cliente removido com sucesso.")
    return 0


def read_clients():
    '''Funcao que pega os dados do XML de clientes e coloca no dicionario.'''
    tree = ET.parse('clients.xml')
    root = tree.getroot()
    clients = []
    for client in root.iter('client'):
        client_cpf = client.find('cpf').text
        client_name = client.find('name').text
        client_phone = client.find('phone').text
        clients.append({'cpf': client_cpf, 'name': client_name, 'phone': client_phone})
    return clients