import forca
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************\n")

    print("Escolha qual jogo deseja jogar!")
    print("(1) Forca       (2)Adivinhação!")

    jogo = int(input())

    if(jogo == 1):
        print("\nJogo da forca")
        forca.jogar()
    elif(jogo == 2):
        print("\nJogo da advinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()