# Instruções
# Neste exercício, você implementará algumas regras do Blackjack, como a maneira como o jogo é jogado e pontuado.

# Nota: Neste exercício, A significa ás, J significa valete, Q significa rainha e K significa rei. Os coringas são descartados. Um baralho francês padrão de 52 cartas é assumido, mas na maioria das versões, vários baralhos são embaralhados juntos para jogar.

# 1. Calcule o valor de uma carta
# No Blackjack, cabe a cada jogador individual se um ás vale 1 ou 11 pontos (mais sobre isso depois). Cartas de figuras (J, Q, K) são pontuadas em 10 pontos e qualquer outra carta vale seu valor "pip" (numérico).

# Defina a função value_of_card(<card>) com o parâmetro card. A função deve retornar o valor numérico da sequência de cartas passada. Como um ás pode assumir vários valores (1 ou 11), esta função deve fixar o valor de uma carta ás em 1 por enquanto. Mais tarde, você implementará uma função para determinar o valor de uma carta ás, dada uma mão existente.
DECK = {
    'A': 1,
    'K': 10,
    'Q': 10,
    'J': 10,
    '10': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2
}
def value_of_card(card):
    return DECK[card]


# 2. Determine qual carta tem um valor maior
# Defina a função higher_card(<card_one>, <card_two>) tendo os parâmetros card_one e card_two. Para fins de pontuação, o valor de J, Q ou K é 10. A função deve retornar qual carta tem o valor maior para pontuação. Se ambas as cartas tiverem um valor igual, retorne ambas. Retornar ambas as cartas pode ser feito usando uma vírgula na declaração return:
# Um ás pode assumir vários valores, então fixaremos as cartas A no valor 1 para esta tarefa.

def higher_card(card_one, card_two):
    if DECK[card_one] > DECK[card_two]:
        return card_one
    elif DECK[card_one] < DECK[card_two]:
        return card_two
    else:
        return card_one, card_two
    
# 3. Calcule o valor de um ás
# Como mencionado antes, um ás pode valer 1 ou 11 pontos. Os jogadores tentam chegar o mais perto possível de uma pontuação de 21, sem passar de 21 (estourando).

# Defina a função value_of_ace(<card_one>, <card_two>) com os parâmetros card_one e card_two, que são um par de cartas já na mão antes de obter uma carta ás. Sua função terá que decidir se o ás que vem a seguir obterá um valor de 1 ou um valor de 11 e retornará esse valor. Lembre-se: o valor da mão com o ás precisa ser o mais alto possível sem passar de 21.

# Dica: se já tivermos um ás na mão, o valor para o ás que vem a seguir seria 1.

def value_of_ace(card_one, card_two):
    if card_one != "A" and card_two != "A":
        if (DECK[card_one] + DECK[card_two]) <= 10:
            return 11
        else:
            return 1
    else:
        return 1
    

# 4. Determine uma mão "Natural" ou "Blackjack"
# Se um jogador recebe um ás (A) e uma carta de dez (10, K, Q ou J) como suas duas primeiras cartas, então o jogador tem uma pontuação de 21. Isso é conhecido como uma mão de blackjack.

# Defina a função is_blackjack(<card_one>, <card_two>) com os parâmetros card_one e card_two, que são um par de cartas. Determine se a mão de duas cartas é um blackjack e retorne o booleano True se for, False caso contrário.

# Nota: O cálculo da pontuação pode ser feito de muitas maneiras. Mas, se possível, gostaríamos que você verificasse se há um ás e uma carta de dez na mão (ou em uma determinada posição), em vez de somar os valores da mão.

def is_blackjack(card_one, card_two):
    if card_one == "A" and DECK[card_two] == 10 or card_two == "A" and DECK[card_one] == 10:
        return True
    else:
        return False
    

# 5. Dividindo pares
# Se as duas primeiras cartas do jogador forem do mesmo valor, como dois seis, ou um Q e K, o jogador pode escolher tratá-las como duas mãos separadas. Isso é conhecido como "dividir pares".

# Defina a função can_split_pairs(<card_one>, <card_two>) com os parâmetros card_one e card_two, que são um par de cartas. Determine se essa mão de duas cartas pode ser dividida em dois pares. Se a mão puder ser dividida, retorne o booleano True, caso contrário, retorne False

def can_split_pairs(card_one, card_two):
    if DECK[card_one] == DECK[card_two]:
        return True
    else:
        return False
    

# 6. Dobrar
# Quando as duas cartas originais distribuídas totalizam 9, 10 ou 11 pontos, um jogador pode fazer uma aposta adicional igual à sua aposta original. Isso é conhecido como "dobrar".

# Defina a função can_double_down(<card_one>, <card_two>) com os parâmetros card_one e card_two, que são um par de cartas. Determine se a mão de duas cartas pode ser "dobrada" e retorne o booleano True se puder, False caso contrário.

def can_double_down(card_one, card_two):
    if (DECK[card_one] + DECK[card_two]) >= 9 and (DECK[card_one] + DECK[card_two]) <= 11:
        return True
    else:
        return False