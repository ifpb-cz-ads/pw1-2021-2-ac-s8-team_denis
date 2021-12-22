#8) Escreva uma função que receba uma string e uma lista. A função deve comparar a string passada com os elementos da lista, também passada como parâmetro. Retorne verdadeiro se a string for encontrada dentro da lista, e falso em caso contrário.

def procura_string(s, lista):
    return s in lista


L = ["AB",  "CD", "EF", "FG"]

print(procura_string("AB", L))
print(procura_string("CD", L))
print(procura_string("EF", L))
print(procura_string("FG", L))
print(procura_string("XYZ", L))