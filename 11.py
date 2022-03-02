"""Defina uma função embaralha que retorne as letras de uma string misturadas
"""

def embaralha(s):
    import random
    lista = list(s)
    random.shuffle(lista)
    return ''.join(lista)
