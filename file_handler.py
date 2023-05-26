import xml.etree.ElementTree as ET

#fazendo umas brincadeiras com arquivos xml
# tree_orders=ET.parse('orders.xml')
# root_orders=tree_orders.getroot()

# for client in root_orders.iter('client'):
#     client_name = client.find('name')
#     print(client_name.text)
#     client_cpf = client.find('cpf')
#     print(client_cpf.text)
#     if client_name.text == 'LUIZA' and client_cpf.text == '12548796760':
#         client_name.text = 'ARTHUR LEITE'

# tree_orders.write('orders.xml')

#funcao que escreve os clientes no arquvio xml
clients = [{'cpf': '12548796760', 'name': 'LUIZ FELLIPE', 'phone': '965412365'}, 
           {'cpf': '16579545632', 'name': 'LUIZA CAMERINI', 'phone': '987969219'}, 
           {'cpf': '18118614743', 'name': 'ARTHUR LEITE', 'phone': '987654321'}]

def write_clients(clients):
    tree_clients = ET.parse('clients.xml')  # Carrega o arquivo XML existente
    root_clients = tree_clients.getroot()

    for client in clients:
        client_cpf = client['cpf']
        client_name = client['name']
        client_phone = client['phone']
        client_exists = False

        for client_xml in root_clients.iter('client'):
            if client_xml.find('cpf').text == client_cpf:
                client_xml.find('name').text = client_name
                client_xml.find('phone').text = client_phone
                client_exists = True

        if not client_exists:
            new_client = ET.SubElement(root_clients, 'client')
            new_client_cpf = ET.SubElement(new_client, 'cpf')
            new_client_cpf.text = client_cpf
            new_client_name = ET.SubElement(new_client, 'name')
            new_client_name.text = client_name
            new_client_phone = ET.SubElement(new_client, 'phone')
            new_client_phone.text = client_phone


    # PROBLEMA: toda chamada de função, deixa as linhas mais espaçadas
    # xml_string = ET.tostring(root_clients, encoding='utf-8')
    # dom = minidom.parseString(xml_string)
    # formatted_xml = dom.toprettyxml(indent='    ')
    # tree_clients.write(formatted_xml, encoding='utf-8', xml_declaration=True)

    # PROBLEMA: escreve o arquivo em uma linha só
    tree_clients.write('clients.xml', encoding='utf-8', xml_declaration=True)


write_clients(clients)