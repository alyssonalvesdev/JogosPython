import random
import repositorio.padroes

def jogar():

    repositorio.padroes.abertura

    #Declarando Variavel 
    numero_secreto = random.randrange(0,101)
    tentativas = 0
    pontos = 1000

    #Cadastro de nível
    print("Qual o nível de dificuldades?")
    print("(1) Fácil (2) Médio (3) Dificíl")

    nivel = int(input("Defina seu nível: "))

    #Condição de nível
    if(nivel == 1):
        tentativas = 10
    elif(nivel == 2):
        tentativas = 5
    elif(nivel == 3):
        tentativas = 3
    else:
        print("Nenhuma errada")


    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada , tentativas))
        #Capturando informação
        chute_str = input("Digite o seu número entre 1 e 100: ")

        print("Você digitou " , chute_str)

        #Convertendo String em Inteiro
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deveria ter digitado um número entre 1 e 100")
            continue

        #Condições
        acertou = numero_secreto == chute
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Você Acertou e fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("Você Errou! o seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Você errou! o seu chute foi menor do que o número secreto.")  
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do Jogo")
    print("A Chave secreta era: {}! e fez {} pontos.".format(numero_secreto, pontos))

repositorio.padroes.liberar_leitura()
