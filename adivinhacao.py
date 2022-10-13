import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************\n")

    numero_secreto = random.randrange(1,101)   #random.randrange() gera um numero inteiro aleatorio entre 1 e 100
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1)Fácil (2)Médio (3)Dificil ")

    nivel = int(input())

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {0} de {1}".format(rodada, total_de_tentativas))
        chute = int(input("Digite um numero entre 1 e 100: "))

        print("Voce digitou ", chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100\n")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto


        if(acertou):
            print("Você acertou e fez {0} pontos".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior que o número secreto\n")
                pontos = pontos - abs((numero_secreto - chute))                    #Abs() devolve o valor em módulo(numero positivo)
            elif(menor):
                print("Você errou! O seu chute foi menor que o número secreto\n")
                pontos = pontos - abs((numero_secreto - chute))

    print("Fim de jogo")

if(__name__ == "__main__"):     #Verifica de o arquivo advinhação é chamado individualmente
    jogar()
