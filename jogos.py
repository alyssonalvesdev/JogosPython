import forca
import adivinhacao

def escolha_jogo():
    print("***********************************************")
    print("-------- Bem vindo, Escolha seu jogo! ---------")
    print("***********************************************")

    print("(1) Forca \n(2) Adivinhação")

    jogo = int(input("Qual jogo?"))

    if (jogo == 1):
        print("Boa sorte! Você escolheu o jogo da Forca")
        forca.jogar()
    elif(jogo == 2): 
        print("Boa sorte! Você escolheu o jogo de Adivinhação")
        adivinhacao.jogar()
    else:
        print("Escolha a opção correta!")

if(__name__ == "__main__"):
    escolha_jogo()