# Instruções
# Neste exercício, desenvolveremos um sistema de controle simples para um reator nuclear.

# Para um reator produzir energia, ele deve estar em um estado de criticidade. Se o reator estiver em um estado menor que a criticidade, ele pode ser danificado. Se o estado do reator ultrapassar a criticidade, ele pode sobrecarregar e resultar em um colapso. Queremos mitigar as chances de colapso e gerenciar corretamente o estado do reator.

# As três tarefas a seguir estão todas relacionadas à escrita de código para manter o estado ideal do reator.

# 1. Verifique a criticidade
# A primeira coisa que um sistema de controle precisa fazer é verificar se o reator está equilibrado em criticidade. Um reator é considerado crítico se ele satisfaz as seguintes condições:

# A temperatura é menor que 800 K.
# O número de nêutrons emitidos por segundo é maior que 500.
# O produto da temperatura e nêutrons emitidos por segundo é menor que 500000.
# Implemente a função is_criticality_balanced() que toma a temperature medida em kelvin e neutrons_emitted como parâmetros, e retorna True se as condições de criticidade forem atendidas, False se não forem.

def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature < 800 and neutrons_emitted > 500 and (temperature * neutrons_emitted) < 500000:
        return True
    else:
        return False
    

# 2. Determine a faixa de saída de energia
# Assim que o reator começar a produzir energia, sua eficiência precisa ser determinada. A eficiência pode ser agrupada em 4 faixas:

# green -> eficiência de 80% ou mais,
# orange -> eficiência de menos de 80%, mas pelo menos 60%,
# red -> eficiência abaixo de 60%, mas ainda 30% ou mais,
# black -> menos de 30% de eficiência.
# O valor percentual pode ser calculado como (generated_power/theoretical_max_power)*100 onde generated_power = voltage * current. Observe que o valor percentual geralmente não é um número inteiro, portanto, certifique-se de considerar o uso adequado das comparações < e <=.

# Implemente a função reactor_efficiency(<voltage>, <current>, <theoretical_max_power>), com três parâmetros: voltage, current e theoretical_max_power. Esta função deve retornar a faixa de eficiência do reator: 'green', 'orange', 'red' ou 'black'.

def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100
    
    if efficiency >= 80:
        return "green"
    elif efficiency < 80 and efficiency >= 60:
        return "orange"
    elif efficiency < 60 and efficiency >= 30:
        return "red"
    else:
        return "black"


# 3. Mecanismo de segurança contra falhas
# Sua tarefa final envolve criar um mecanismo de segurança contra falhas para evitar sobrecarga e derretimento. Este mecanismo determinará se o reator está abaixo, no limite ou acima do limite de criticidade ideal. A criticidade pode então ser aumentada, diminuída ou interrompida inserindo (ou removendo) barras de controle no reator.

# Implemente a função chamada fail_safe(), que recebe 3 parâmetros: temperature medida em kelvin, neutrons_produced_per_second e threshold, e gera um código de status para o reator.

# Se temperatura * neutrons_produced_per_second < 90% do limite, gera um código de status 'LOW' indicando que as barras de controle devem ser removidas para produzir energia.

# Se o valor temperature * neutrons_produced_per_second estiver dentro de 10% do limite (então 0-10% menor que o limite, no limite ou 0-10% maior que o limite), o reator está em criticidade e o código de status 'NORMAL' deve ser emitido, indicando que o reator está em condições ótimas e as barras de controle estão em uma posição ideal.

# Se temperature * neutrons_produced_per_second não estiver nas faixas acima, o reator está entrando em fusão e um código de status 'DANGER' deve ser passado para desligar o reator imediatamente.

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    temperature_per_second = temperature * neutrons_produced_per_second

    if temperature_per_second < (threshold / 100) * 90:
        return "LOW"
    elif temperature_per_second >= (threshold / 100) * 90 and temperature_per_second <= (threshold / 100) * 110:
        return "NORMAL"
    else:
        return "DANGER"
    
print(fail_safe(1000, 30, 5000))