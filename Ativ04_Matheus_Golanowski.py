nome = input("Qual seu nome ")
idade = int(input("Qual sua idade "))
sexo = input("Qual seu sexo ")

if sexo == "f".lower() and idade >= 21 and idade <= 34:
    print("Voce pode servir ")
    print("Matheus Golanowski")
elif sexo == "F".lower() and idade >= 21 and idade <= 34:
    print("Voce pode servir ")
    print("Matheus Golanowski")
elif sexo == "m".lower() and idade >= 18 and idade <= 39:
    print("Voce pode servir ")
    print("Matheus Golanowski")
elif sexo == "M".lower() and idade >= 18 and idade <= 39:
    print("Voce pode servir ")
    print("Matheus Golanowski") 
else:
    print("Voce não pode servir")
    print("Matheus Golanowski")   
