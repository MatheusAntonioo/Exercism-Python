"""
Instruções
Elyse está realmente ansiosa para jogar pôquer (e outros jogos de cartas) durante sua próxima viagem a Vegas. Sendo uma grande fã de "self-tracking", ela quer juntar algumas pequenas funções que a ajudarão com tarefas de rastreamento e pediu sua ajuda para pensar nelas.

"""

"""
1. Acompanhamento de rodadas de pôquer
Elyse gosta especialmente de pôquer e quer acompanhar quantas rodadas ela joga - e quais são essas rodadas . Cada rodada tem seu próprio número, e cada mesa mostra o número da rodada que está sendo jogada no momento. Elyse escolhe uma mesa e se senta para jogar sua primeira rodada. Ela planeja jogar três rodadas.

Implemente uma função get_rounds(<round_number>)que pega o número da rodada atual e retorna um único list com essa rodada e as duas próximas que estão por vir:
"""
def get_rounds(round_number):
    return [round_number, round_number +1, round_number +2]


"""
2. Mantendo todas as rodadas no mesmo lugar
Elyse jogou algumas rodadas na primeira mesa, então fez uma pausa e jogou mais algumas rodadas em uma segunda mesa... mas acabou com uma lista diferente para cada mesa! Ela quer juntar as duas listas, para poder acompanhar todas as rodadas de pôquer no mesmo lugar.

Implemente uma função concatenate_rounds(<rounds_1>, <rounds_2>)que recebe duas listas e retorna uma única list contendo todas as rodadas da primeira list, seguidas de todas as rodadas da segunda list:
"""

def concatenate_rounds(round_1, round_2):
    return round_1 + round_2



"""
3. Encontrando rodadas anteriores
Falando sobre algumas das rodadas anteriores de Poker, outro jogador observa como duas delas foram jogadas de forma similar. Elyse não tem certeza se jogou essas rodadas ou não.

Implemente uma função list_contains_round(<rounds>, <round_number>)que recebe dois argumentos, uma lista de rounds jogados e um número de round. A função retornará True se o round estiver na lista de rounds jogados, False se não:
"""

def list_contains_round(rounds, round_number):
    return round_number in rounds


"""
4. Média dos valores das cartas
Elyse quer experimentar um novo jogo chamado Black Joe. É parecido com Black Jack - onde seu objetivo é fazer com que as cartas na sua mão somem um valor alvo - mas no Black Joe o objetivo é fazer com que a média dos valores das cartas seja 7. A média pode ser encontrada somando todos os valores das cartas e então dividindo essa soma pelo número de cartas na mão.

Implemente uma função card_average(<hand>)que retornará o valor médio de uma mão de Black Joe.
"""

def card_average(hand):
    return sum(hand) / len(hand)

"""
5. Médias alternativas
Em Black Joe, a velocidade é importante. Elyse vai tentar encontrar uma maneira mais rápida de encontrar a média.

Ela pensou em duas maneiras de obter um número próximo à média :

Faça a média do primeiro e do último número da mão.
Usando a mediana (carta do meio) da mão.
Implemente a função approx_average_is_average(<hand>), dada hand, uma lista contendo os valores das cartas na sua mão.

Retorne True se qualquer uma das or duas estratégias acima resultar em um número igual à média real .

Observação: o comprimento de todos os ponteiros é ímpar para facilitar a localização da mediana.
"""

def approx_average_is_average(hand):
    actual_average = card_average(hand)
    first_last_average = (hand[0] + hand[-1]) / 2
    middle_card = hand[len(hand) // 2]
    
    return first_last_average == actual_average or middle_card == actual_average


"""
6. Mais técnicas de média
Intrigada pelos resultados de seu experimento de média, Elyse está se perguntando se tomar a média das cartas nas posições pares versus a média das cartas nas posições ímpares daria os mesmos resultados. Hora de outra função de teste!

Implemente uma função average_even_is_average_odd(<hand>) que retorna um booleano indicando se a média das cartas em índices pares é a mesma que a média das cartas em índices ímpares.
"""

def average_even_is_average_odd(hand):
    return card_average(hand[0::2]) == card_average(hand[1::2])


"""
7. Regras da rodada de bônus
Cada 11ª mão no Black Joe é uma mão bônus com uma regra de bônus: se a última carta que você comprar for um Valete, você dobra seu valor.

Implemente uma função maybe_double_last(<hand>) que pega uma mão e verifica se a última carta é um Valete (11). Se a última carta for um Valete (11), dobre seu valor antes de retornar a mão.
"""

def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] = hand[-1] * 2
        return hand
    else:
        return hand


print(maybe_double_last([11,2,1]))