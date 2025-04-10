"""
Instruções

Neste exercício, você está ajudando sua irmã mais nova a editar seu trabalho para a escola. O professor está procurando pontuação correta, gramática e excelente escolha de palavras.

Você tem quatro tarefas para limpar e modificar strings.
"""

"""
1. Coloque o título do artigo em maiúscula
Qualquer bom artigo precisa de um título formatado corretamente. Implemente a função capitalize_title(<title>)que recebe um título str como parâmetro e coloca a primeira letra de cada palavra em maiúscula. Esta função deve retornar um string title case.
"""

def capitalize_title(title):
    return title.title()


"""
2. Verifique se cada frase termina com um ponto final
Você quer ter certeza de que a pontuação no artigo está perfeita. Implemente a função check_sentence_ending()que recebe sentence como parâmetro. Esta função deve retornar um bool.
"""

def check_sentence_ending(sentence):
    return sentence.endswith(".")


"""
3. Limpe o espaçamento
Para fazer o artigo parecer profissional, espaçamentos desnecessários precisam ser removidos. Implemente a função clean_up_spacing()que recebe sentence como parâmetro. A função deve remover espaços em branco extras no início e no fim da frase, retornando uma frase nova e atualizada str.
"""

def clean_up_spacing(sentence):
    return sentence.strip()


"""
4. Substitua as palavras por um sinônimo
Para tornar o artigo ainda melhor , você pode substituir alguns dos adjetivos por seus sinônimos. Escreva a função replace_word_choice()que recebe sentence, old_word, e new_word como parâmetros. Esta função deve substituir todas as instâncias de pelo old_word, new_word e retornar um novo str com a frase atualizada.
"""

def replace_word_choice(sentence, old_word, new_word):
    return sentence.replace(old_word, new_word)