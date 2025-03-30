# 1. Defina se Pac-Man come um fantasma
# Defina a função eat_ghost() que recebe dois parâmetros (se Pac-Man tem uma pílula de poder ativa e se Pac-Man está tocando um fantasma) e retorna um valor booleano se Pac-Man é capaz de comer um fantasma. A função deve retornar True somente se Pac-Man tem uma pílula de poder ativa e está tocando um fantasma.

def eat_ghost(has_power_pellet, touching_ghost):
    if has_power_pellet and touching_ghost:
        return True
    else:
        return False
    
#2. Defina se Pac-Man pontua
# Defina a função score() que recebe dois parâmetros (se Pac-Man está tocando uma bolinha de energia e se Pac-Man está tocando um ponto) e retorna um valor booleano se Pac-Man pontuou. A função deve retornar True se Pac-Man estiver tocando uma bolinha de energia ou um ponto.

def score(touching_power_pellet, touching_dot):
    if touching_power_pellet or touching_dot:
        return True
    else:
        return False
    
# 3. Defina se Pac-Man perde
# Defina a função lose() que recebe dois parâmetros (se Pac-Man tem uma pílula de poder ativa e se Pac-Man está tocando um fantasma) e retorna um valor booleano se Pac-Man perde. A função deve retornar True se Pac-Man está tocando um fantasma e não tem uma pílula de poder ativa.

def lose(has_power_pellet, touching_ghost):
    if not has_power_pellet and touching_ghost:
        return True
    else:
        return False
    
# 4. Defina se Pac-Man vence
# Defina a função win() que pega três parâmetros (se Pac-Man comeu todos os pontos, se Pac-Man tem uma pílula de poder ativa e se Pac-Man está tocando um fantasma) e retorna um valor booleano se Pac-Man vence. A função deve retornar True se Pac-Man comeu todos os pontos e não perdeu com base nos parâmetros definidos na parte 3.

def win(ate_all_dots, has_power_pellet, touching_ghost):
    if ate_all_dots and not lose(has_power_pellet, touching_ghost):
        return True
    else:
        return False
    
