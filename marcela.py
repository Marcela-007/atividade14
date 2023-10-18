# Exercício Python 14: Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um
# aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input("Insira o valor do salário: "))
if salario > 1250.0:
   superior = salario + (salario * 10 / 100)
   print(f"Você recebeu um aumento de 10%. Novo salario R$ {superior:.2f}")

elif salario <= 1250:
   inferior = salario + (salario * 15 / 100)
   print(f"Você recebeu um aumento de 15%. Novo salário R$ {inferior:.2f}")