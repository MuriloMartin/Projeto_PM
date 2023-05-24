
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