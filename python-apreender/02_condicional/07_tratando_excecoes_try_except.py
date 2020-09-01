inp = input('Enter Fahrenheit Temperature:')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except Exception as e:
    print('Please enter a number')

inp = input('Enter Velocidade:')
try:
    velocidade = float(inp)
    calcular = velocidade * 5
    print('velocidade do som:', calcular)
except Exception as e:
    print('Por favor coloque em numeros a velocidade.')
