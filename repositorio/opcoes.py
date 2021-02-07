import random

def fruta():
    
    arquivo = open("../opcoes/frutas.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    linhas = len(palavras) + 1
    item = random.randrange(linhas)


    palavra_secreta = palavras[item].upper()
    return palavra_secreta

def animais():
    
    arquivo = open("../opcoes/animais.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    linhas = len(palavras) + 1
    item = random.randrange(linhas)


    palavra_secreta = palavras[item].upper()
    return palavra_secreta

def pessoas():
    
    arquivo = open("../opcoes/pessoas.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    linhas = len(palavras) + 1
    item = random.randrange(linhas)


    palavra_secreta = palavras[item].upper()
    return palavra_secreta

def paises():
    
    arquivo = open("../opcoes/paises.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    linhas = len(palavras) + 1
    item = random.randrange(linhas)


    palavra_secreta = palavras[item].upper()
    return palavra_secreta

def times():
    
    arquivo = open("../opcoes/times.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    linhas = len(palavras) + 1
    item = random.randrange(linhas)


    palavra_secreta = palavras[item].upper()
    return palavra_secreta