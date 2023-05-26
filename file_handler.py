import xml.etree.ElementTree as ET

#fazendo umas brincadeiras com arquivos
tree_orders=ET.parse('orders.xml')
root_orders=tree_orders.getroot()

for client in root_orders.iter('client'):
    name_tag = client.find('name')
    name_tag.text = 'ARTHUR LEITE'

tree_orders.write('orders.xml')