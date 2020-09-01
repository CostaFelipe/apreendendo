inp = input('Digite as Horas:')
inp2 = input('Digite a taxa:')

try:
    horas = float(inp)
    taxa  = float(inp2)
    salario = horas * taxa
    print('O salario é:', salario)
except Exception as e:
        print('Erro, por favor utilize uma entrada numerica.')
