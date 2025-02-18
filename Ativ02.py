print("Matheus Golanowski")
nome = input("Digite seu nome: ")
peso = int(input("Qual seu peso "))

if peso >= 52 and peso <65:
    print("{} sua categoria é Pena".format(nome))
elif peso >= 65 and peso <72:
    print("{} sua categoria é Leve".format(nome))  
elif peso >= 72 and peso <79:
    print("{} sua categoria é Ligeiro".format(nome))
elif peso >= 79 and peso <86:
    print("{} sua categoria é Meio-Medio".format(nome))
elif peso >= 86 and peso <90:
    print("{} sua categoria é Medio".format(nome))
elif peso >= 86 and peso <100:
    print("{} sua categoria é Meio-Pesado".format(nome))
elif peso >= 100:
    print("{} sua categoria é Pesado".format(nome))
else:
    print("categoria invalida")