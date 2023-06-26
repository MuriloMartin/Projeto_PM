# Simulação de Locadora de Jogos de Tabuleiro
### Por: Murilo Martin, Luíza Camerini & Miguel Batista

Nossa aplicação foi feita para a disciplina Programação Modular, 2023.1, PUC-Rio. Nela, há a nossa proposta de solução para uma simulação de uma locadora de jogos de tabuleiro. A simulação deverá abordar diversos atributos específicos, como registro de clientes, dados de jogos, dados de pedidos e, especialmente, um meio de comunicação com outra aplicação, a qual seria o fornecedor de jogos de tabuleiro.

Nossa proposta possui diversos módulos consistentes e separados por tipo tema. Por exemplo, temos um módulo apenas para tratar a interface e tratamento de inputs entre sistema e usuário.

As funcionalidades da nossa aplicação abordam as seguintes opções:

1) Registro, exclusão e busca de clientes;
2) Registro, exclusão e busca de pedidos;
3) Listagem de jogos em estoque;
4) Mostrar saldo da locadora;
5) Envio de pedido de um ou mais jogos para o fornecedor;
6) Envio de uma preferência de um ou mais jogos para o fornecedor;

O nosso "banco de dados" é totalmente baseado em arquivos XML. Estes arquivos incluem dados dos clientes, dados dos pedidos, dados do estoque e dados do caixa da loja.

 Os arquivos de comunicação com o fornecedor são em formatos JSON.