# Exercício 3: Escreva um programa que solicite ao usuário as horas e o
#valor da taxa por horas para calcular o valor a ser pago por horas de
#serviço.

horas = float(input('Digite as horas:'))
taxa = float(input('Digite a taxa:'))

pagamento = horas * taxa

print("Valor a ser pago: R$", pagamento)
