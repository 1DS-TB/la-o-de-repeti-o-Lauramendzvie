soma = 0
contador = 1

informacao = int(input("digie o que voce quer"))

if informacao <= 0:
    print("INVALIDO")
else:
    while contador <= informacao:
        soma += contador # soma = soma + contador 1+2-3/ 2+3-5 / 3+6-9 /4+10-14
        contador += 1 # contador = contador + 1 2+1-3/5+1-6/ 9+1-10/ 14+1-15
    print(f"A soma do número {informacao} é {soma}")

