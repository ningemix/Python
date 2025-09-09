from random import randint


def sortnum ():
    nums = {}
    cont = 1
    while True:
        n = int (input ("Digite um número [-1 para parar]: "))
        if n == -1:
            break
        nums [cont] = n
        cont += 1
    while True:
        sorteio = randint(1, len(nums))
        sort = str (input ("Sortear? [s/n]: ")).strip().lower()
        if sort == "n":
            break
        print (nums[sorteio])


def sortnome ():
    nomes = {}
    cont = 1
    while True:
        n = str (input("Digite um nome [x para parar]: ")).lower().title()
        if n == "X":
            break
        nomes [cont] = n
        cont += 1
    while True:
        sorteio = randint(1, len(nomes))
        sort = str(input("Sortear? [s/n]: ")).strip().lower()
        if sort == "n":
            break
        print(nomes[sorteio])