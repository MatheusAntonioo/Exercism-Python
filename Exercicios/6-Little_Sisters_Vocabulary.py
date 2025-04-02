# Instruções
# Você está ajudando sua irmã mais nova com a tarefa de vocabulário de inglês, que ela está achando muito tediosa. A turma dela está aprendendo a criar novas palavras adicionando prefixos e sufixos. Dado um conjunto de palavras, o professor está procurando palavras transformadas corretamente com grafia correta adicionando o prefixo ao início ou o sufixo ao final.

# A tarefa tem quatro atividades, cada uma com um conjunto de texto ou palavras para trabalhar.

# 1. Adicione um prefixo a uma palavra
# Um dos prefixos mais comuns em inglês é un, que significa "não". Nesta atividade, sua irmã precisa formar palavras negativas, ou "não", adicionando un a elas.

# Implemente a função add_prefix_un(<word>) que recebe word como parâmetro e retorna uma nova palavra prefixada un:

def add_prefix_un(word):
    return "un" + word


# 2. Adicione prefixos a grupos de palavras
# Há mais quatro prefixos comuns que a turma da sua irmã está estudando: en (que significa 'colocar em' ou 'cobrir com'), pre (que significa 'antes' ou 'para a frente'), auto (que significa 'próprio' ou 'mesmo') e inter (que significa 'entre' ou 'entre').

# Neste exercício, a turma está criando grupos de palavras de vocabulário usando esses prefixos, para que possam ser estudados juntos. Cada prefixo vem em uma lista com palavras comuns com as quais é usado. Os alunos precisam aplicar o prefixo e produzir uma sequência que mostre o prefixo aplicado a todas as palavras.

# Implemente a função make_word_groups(<vocab_words>) que recebe um vocab_words como parâmetro no seguinte formato: [<prefix>, <word_1>, <word_2> .... <word_n>] e retorna uma string com o prefixo aplicado a cada palavra que se parece com: '<prefix> :: <prefix><word_1> :: <prefix><word_2> :: <prefix><word_n>'.

def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    word_with_prefix = [prefix + word for word in vocab_words[1:]]
    return f"{prefix} :: " + " :: ".join(word_with_prefix)
    
    
# 3. Remova um sufixo de uma palavra
# ness é um sufixo comum que significa 'estado de ser'. Nesta atividade, sua irmã precisa encontrar a palavra raiz original removendo o sufixo ness. Mas é claro que existem regras de ortografia incômodas: se a palavra raiz originalmente terminasse em uma consoante seguida por um 'y', então o 'y' foi alterado para 'i'. Remover 'ness' precisa restaurar o 'y' nessas palavras raiz. por exemplo, happiness --> happi --> happy.

# Implemente a função remove_suffix_ness(<word>) que recebe uma palavra e retorna a palavra raiz sem o sufixo ness.

def remove_suffix_ness(word):
    word_without_ness = word[:-4]
    if word_without_ness[-1] == "i":
        return word_without_ness[:-1] + "y"
    else:
        return word_without_ness



# 4. Extraia e transforme uma palavra
# Sufixos são frequentemente usados ​​para mudar a classe gramatical à qual uma palavra é atribuída. Uma prática comum em inglês é "verbing" ou "verbifying" — onde um adjetivo se torna um verbo ao adicionar um sufixo en.

# Nesta tarefa, sua irmã vai praticar "verbing" palavras extraindo um adjetivo de uma frase e transformando-o em um verbo. Felizmente, todas as palavras que precisam ser transformadas aqui são "regulares" — elas não precisam de mudanças ortográficas para adicionar o sufixo.

# Implemente a função adjective_to_verb(<sentence>, <index>) que recebe dois parâmetros. Uma frase usando a palavra do vocabulário e o índice da palavra, uma vez que a frase é dividida. A função deve retornar o adjetivo extraído como um verbo.

def adjective_to_verb(sentence, index):
    verb = sentence.split()[index]
    if verb[-1] == ".":
        verb = verb[:-1]
    return f"{verb}en"
