#6) Reescreva o programa da abaixo de forma a utilizar for em vez de while.

def soma(L):
    total = 0
    for k in L:
        total = total + k 
    return total


L = [1, 7, 2, 9, 15]
print(soma(L))
print(soma([7, 9, 12, 3, 100, 20, 4]))