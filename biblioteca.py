def imprime_nome(nome):
    print(f"Nome: {nome}")

def solicitarnome():
    nome=input("Digite seu nome: ")
    return

def piramede (num):
    for i in range(1, num + 1, 1):
        for l in range(0, i):
            print(i, end=" ")
        print()

def contar_vogais(frase):
    contador = 0
    for i in range(len(frase)):
        if frase[i] == "a" or frase[i] == "e" or frase[i] == "i" or frase[i] == "o" or frase[i] == "u":
            contador += 1
    print(contador)

def estoque(produto, qtd, valorunitario):
    valortotal=qtd*valorunitario
    return valortotal

def positivonegativo (num):
    if num >0:
        return 'P'
    elif num <0:
        return "N"
    else :
        return "Z"

def soma (num1, num2):
    soma=num1+num2
    print(soma)

def somaturma (*a):
    soma=0
    for x in range (len(a)):
        soma=soma+a[x]
    print()




















