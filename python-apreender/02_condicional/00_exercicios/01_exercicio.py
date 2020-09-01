inp1 = input('Digite as horas trabalhadas:')
inp2 = input('Digite a taxa:')

horas = float(inp1)
taxas = float(inp2)

if horas > 40 :
    salario =  horas * taxas * 1.5
    print('salario:', salario)
else :
    salario = horas * taxas
    print('salario:', salario)
