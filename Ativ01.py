quantidade = input("insira o grau de aceitação do investimento que deseja receber ")
investimento = float (input("Agora, insira o valor do ivestimento "))
if quantidade == "Bx":
    if investimento < 1000.00:
        print("invist na poupaça")
        print("Matheus Golanowski")
    else:
        print("Invest na renda fixa")
        print("Matheus Golanowski")
if quantidade == "Al":
    if investimento < 1000.00:
        print("invist nos bitcoins")
        print("Matheus Golanowski")
    else:
        print("Invest na ações")
        print("Matheus Golanowski")        