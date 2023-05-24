el = {'cpf': 123456789, 'nome': 'Fulano', 'telefone': 123456789}
el2 = {'cpf': 987654321, 'nome': 'Ciclano', 'telefone': 987654321}
el3 = {'cpf': 123456789, 'nome': 'Beltrano', 'telefone': 123456789}

lista = [el, el2, el3]

for client in lista:
    if client['nome'] == 'Fulano':
        print(client)


userEnderApplication = False

