numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
soma = numero1 + numero2

if soma > 300:
    maior_que = input("A soma deu maior que 300? ")
    if maior_que == "Sim":
        print(True)
    else:
        print(False)