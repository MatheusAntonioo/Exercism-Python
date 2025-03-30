# 1. Estimar valor após a troca
# Crie a função exchange_money(), pegando 2 parâmetros:

# budget: A quantia de dinheiro que você está planejando trocar.
# exchange_rate: A quantia de moeda nacional igual a uma unidade de moeda estrangeira.
# Esta função deve retornar o valor da moeda trocada.

def exchange_money(budget, exchange_rate):
    exchange_value = budget / exchange_rate
    return exchange_value


# 2. Calcular moeda restante após uma troca
# Crie a função get_change(), pegando 2 parâmetros:

# budget : Quantidade de dinheiro antes da troca.
# exchanging_value : Quantidade de dinheiro que é retirada do orçamento para ser trocada.
# Esta função deve retornar a quantidade de dinheiro que resta do orçamento.

def get_change(budget, exchanging_value):
    remaining_money = budget - exchanging_value
    return remaining_money


# 3. Calcular valor das notas
# Crie a função get_value_of_bills(), pegando 2 parâmetros:

# denomination: O valor de uma única nota.
# number_of_bills: O número total de notas.
# Esta cabine de câmbio só lida com dinheiro de certos incrementos. O total que você recebe deve ser divisível pelo valor de uma "nota" ou unidade, o que pode deixar para trás uma fração ou resto. Sua função deve retornar apenas o valor total das notas (excluindo quantias fracionárias) que a cabine devolveria. Infelizmente, a cabine fica com o resto/troco como um bônus adicional.

def get_value_of_bills(denomination, number_of_bills):
    total_bills = denomination * number_of_bills
    return int(total_bills)


# 4. Calcular o número de notas
# Crie a função get_number_of_bills(), pegando amount e denomination.

# Esta função deve retornar o número de notas de moeda que você pode receber dentro do valor fornecido. Em outras palavras: Quantas notas inteiras de moeda cabem no valor inicial? Lembre-se — você só pode receber notas inteiras, não frações de notas, então lembre-se de dividir adequadamente. Efetivamente, você está arredondando para baixo para a nota/denominação inteira mais próxima.

def get_number_of_bills(amount, denomination):
    total_bills = amount / denomination
    return int(total_bills)


# 5. Calcule o restante após a troca por notas
# Crie a função get_leftover_of_bills(), pegando o valor e a denominação.

# Esta função deve retornar o valor restante que não pode ser retornado do seu valor inicial, dada a denominação das notas. É muito importante saber exatamente quanto o estande pode ficar.

def get_leftover_of_bills(amount, denomination):
    leftover_amount = amount % denomination
    return leftover_amount

#6. Calcular valor após a troca
# Crie a função exchangeable_value(), pegando budget, exchange_rate, spread e denomination.

# O parâmetro spread é a porcentagem tomada como taxa de câmbio, escrita como um inteiro. Ele precisa ser convertido para decimal dividindo-o por 100. Se 1,00 EUR == 1,20 USD e o spread for 10, a taxa de câmbio real será: 1,00 EUR == 1,32 USD porque 10% de 1,20 é 0,12, e essa taxa adicional é adicionada à troca.

# Esta função deve retornar o valor máximo da nova moeda após calcular a taxa de câmbio mais o spread. Lembre-se de que a denominação da moeda é um número inteiro e não pode ser subdividida.

# Observação: o valor retornado deve ser do tipo int.

def exchangeable_value(budget, exchange_rate, spread, denomination):
    actual_exchange = exchange_rate + (exchange_rate * (spread / 100))
    exchange_value = budget / actual_exchange
    leftover_amount = denomination * (exchange_value // denomination)
    return int(leftover_amount)

print(exchangeable_value(127.25, 1.20, 10, 20))
print(exchangeable_value(127.25, 1.20, 10, 5))