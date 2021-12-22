#2) Escreva uma função que receba dois números e retorne True se o primeiro número for múltiplo do segundo
def retorna_multiplo(n1,n2):
    return n1 % n2 == 0
      

n1 = int(input("Informe um numero inteiro:"))
n2 = int(input("Informe um segundo numero:"))
print(retorna_multiplo(n1,n2))
