import random
import repositorio.padroes
import repositorio.opcoes


def jogar():

    repositorio.padroes.abertura()

    enforcou = False
    acertou = False
    erros = 1
    

    print("Escolha o tipo de palavra que você quer jogar!")
    print("(1) Frutas \n(2) Pessoas Famosas \n(3) Paises \n(4) Animais \n(5) Times ")
    print(" ")
    opcao = input("Qual opção você escolhe? ")

    if(opcao == 1):
        palavra_secreta = repositorio.opcoes.fruta()
        #return palavra_secreta
    elif(opcao == 2):
        palavra_secreta = repositorio.opcoes.pessoas_famosas()
        #return palavra_secreta
    elif(opcao == 3):
        palavra_secreta = repositorio.opcoes.paises()
        #return palavra_secreta
    elif(opcao == 4):
        palavra_secreta = repositorio.opcoes.animais()
        return
    elif(opcao == 5):
        palavra_secreta = repositorio.opcoes.times()
        return palavra_secreta
    else:
        print("Escolha a opção correta!")


    letras_acertadas = ["_" for letra in palavra_secreta]

    print(letras_acertadas)
    
    while(not enforcou and not acertou):
        chute = input("Qual Letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            i = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[i] = letra 
                i += 1
        
        else:
            erros += 1
            repositorio.padroes.desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print("##############################")
        print(letras_acertadas)
        print("\n")
        print("Jogando ...")

    if(acertou):
        repositorio.padroes.voce_ganhou()
    else:
        repositorio.padroes.voce_perdeu()

if(__name__ == "__main__"):
    jogar()