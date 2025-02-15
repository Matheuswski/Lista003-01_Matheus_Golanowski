salario = int(input("Qual seu salario: "))
parcelas = int(input("Quantas parcelas voce quer: "))
emprestimo = int(input("Quanto de dinheiro voce quer: "))

taxa = salario * 0.08
if taxa >= emprestimo:
    print("O emprestimo sera concedido")
else:
    print("Infelizmente o emprestimo não sera concedido")