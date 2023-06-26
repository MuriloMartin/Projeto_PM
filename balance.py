from file_handler import *

def decrease_cash(caixa, valor):
    '''Funcao que decrementa o caixa da loja'''
    
    try:
        caixa = float(caixa)
        valor = float(valor)
        if valor > 0:
            return caixa-valor
        else:
            print("Valor inválido")
            return -1
    except:
        print("Valor inválido")
        return -1

def increase_cash(caixa,valor):
    '''Funcao que incrementa o caixa da loja'''
    try:
        caixa = float(caixa)
        valor = float(valor)
        if valor > 0:
            return caixa+valor
        else:
            print("Valor inválido")
            return -1
    except:
        print("Valor inválido")
        return -1

def handle_response(balance, response, stock):
    '''Funcao que trata a resposta do fornecedor e atualiza o estoque e o caixa da loja'''
    preference_games = []
    for game in response:
        if response[game]['status'] == 'disponivel':
            game_cost = float(response[game]['preco'])
            if balance > game_cost:
                print('')
                balance = decrease_cash(balance, game_cost)
                print("aaaaaaaaaa")
                for i in range(len(stock)):
                    if stock[i]['name'] == game:
                        stock[i]['stock'] = int(stock[i]['stock']) + 1
                        print("Compra do jogo ", game, " realizada com sucesso!")
                        break
            else:
                print("Saldo insuficiente para comprar o jogo", game)
        else:
            preference_games.append(game)
    if len(preference_games) > 0:
        print("Foi feita a preferência para os seguinte jogos: ", preference_games)
    create_preference(preference_games)
    return balance

def show_balance(balance):
    '''Funcao que mostra o caixa da loja'''
    try:
        print("O caixa da loja é: ",float(balance))
        return
    except:
        print("Valor de balance não numérico")
        return