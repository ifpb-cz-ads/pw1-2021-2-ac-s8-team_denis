#1) Escreva uma função que retorne o maior de dois números. Valores esperados:

def retorna_maior(n1,n2):
    maior = n1
    if n2>n1:
        return n2
    else:
        return n1
    
n1 = int(input("Informe um numero:"))
n2 = int(input("Informe o segundo numero:"))
print("O maior numero é:",retorna_maior(n1,n2))