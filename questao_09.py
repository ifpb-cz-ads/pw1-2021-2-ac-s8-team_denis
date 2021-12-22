#9) Altere o programa abaixo de forma que o usuário tenha três chances de acertar o número. O programa termina se o usuário acertar ou errar três vezes. A função ‘random.randint(x, y)’ recebe como parâmetros dois inteiros, x e y, e retorna um outro inteiro escolhido aleatoriamente entre x e y.

def valida_entrada(mensagem, opções_válidas):
    opções = opções_válidas.lower()
    while True:
        escolha = input(mensagem)
        if escolha.lower() in opções:
            break
        print("Erro: opção inválida. Redigite.\n")
    return escolha