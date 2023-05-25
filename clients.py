
def register_clients(cpf, name, phone, clients):
    client = {
        'cpf': cpf,
        'name': name,
        'phone': phone
    }
    clients.append(client)
    print('Cliente cadastrado com sucesso!')
    return clients

def list_clients(clients):
    print('\nNúmero de clientes cadastrados:', len(clients))
    print('Listando clientes:\n')
    for client in clients:
        print('CPF:', client['cpf'])
        print('Nome:', client['name'])
        print('Telefone:', client['phone'])
        print('------------------------------------')

def find_clients(cpf, clients):
    for client_index in range(len(clients)):
        if clients[client_index]['cpf'] == cpf:
            return client_index
    print("Cliente nao encontrado")
    return -1

def delete_clients(cpf,clients):
    client_index = find_clients(cpf,clients)
    if(client_index == -1):
        return -1
    clients.pop(client_index)
    print("Cliente removido com sucesso")
    return 0