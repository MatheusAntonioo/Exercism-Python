# Constante que determina o tempo de cozimento esperado para a lasanha (em minutos).
EXPECTED_BAKE_TIME = 40

# Função que calcula o tempo de cozimento restante da lasanha.
# O tempo total é a soma do tempo de preparação e do tempo de cozimento já decorrido.
# O tempo de cozimento já decorrido é passado como argumento para a função.
def bake_time_remaining(actual_mitunes):
    """Calculate the bake time remaining.
 
    :param actual_mitunes: int - actual time cooking.
    :return: int - minutes remaining (in minutes)to cooking.
 
    This function takes the actual minutes the lasagna has been in the oven as an argument and returns how many minutes the lasagna still needs to bake based on the EXPECTED_BAKE_TIME constant.
    """
    
    minutes_remaining = EXPECTED_BAKE_TIME - actual_mitunes
    return minutes_remaining

# Função que calcula o tempo de preparação da lasanha.
# O tempo de preparação é calculado multiplicando o número de camadas (layers) por 2 minutos.
# O número de camadas é passado como argumento para a função.
# O tempo de preparação é retornado em minutos.
def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time in minutes.
 
    :param number_of_layers: int - number of layers.
    :return: int - minutes remaining (in minutes)to prepare the lasagna.
 
    This function takes the number_of_layers you want to add to the lasagna as an argument and returns how many minutes you would spend making them. Assume each layer takes 2 minutes to prepare.
    """
    
    time_to_prepare_each_layer = 2
    preparation_time = number_of_layers * time_to_prepare_each_layer
    return preparation_time

# Função que calcula o tempo total decorrido (em minutos) para preparar e cozinhar a lasanha.
# O tempo total é a soma do tempo de preparação e do tempo de cozimento já decorrido.
# O tempo de cozimento já decorrido é passado como argumento para a função.
# O tempo de preparação é calculado chamando a função preparation_time_in_minutes com o número de camadas (layers) como argumento.
def elapsed_time_in_minutes(number_of_layers, elapse_bake_time):
    """Calculate the elapsed cooking time.
 
    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.
 
    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    preparation_time = preparation_time_in_minutes(number_of_layers)
    total_time = preparation_time + elapse_bake_time
    return total_time