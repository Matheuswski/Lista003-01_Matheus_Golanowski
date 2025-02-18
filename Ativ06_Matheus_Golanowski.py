nome_cidade = input("Qual a cidade ")
votos_canndidato = int(input("quantidade de votos do candidato: "))
qtde_votos = int(input("Qual a quantidade de votos: "))
porcetagem = votos_canndidato/qtde_votos
if porcetagem <= 0.50 :
    print("Avera segundo turno na cidade: ",nome_cidade)
    print("Matheus Golanowski")
else:
    print("Não avera segundo turno ")
    print("Matheus Golanowski")