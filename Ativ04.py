nome = input("Qual seu nome ")
idade = int(input("Qual sua idade "))
sexo = input("Qual seu sexo ")

if sexo == "f".lower() and idade >= 21 and idade <= 34:
    print("Voce pode servir ")
elif sexo == "F".lower() and idade >= 21 and idade <= 34:
    print("Voce pode servir ")
elif sexo == "m".lower() and idade >= 18 and idade <= 39:
    print("Voce pode servir ")
elif sexo == "M".lower() and idade >= 18 and idade <= 39:
    print("Voce pode servir ") 
else:
    print("Voce não pode servir")   