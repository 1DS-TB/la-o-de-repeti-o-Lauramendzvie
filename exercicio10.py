inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))



for k in range(inicio, fim + 1):
    n = len(str(k))
    quadrado = str(k ** 2)
    direita = quadrado[-n:]
    esquerda = quadrado[:-n] if quadrado[:-n] != '' else '0'


    if direita != '0' * len(direita):
        if int(esquerda) + int(direita) == k:
            print(k)
    elif k == 1:
        print(1)

