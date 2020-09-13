array = [3, 41, 12, 9, 74, 1]

maximo = None
print('Antes:', maximo)
for itervar in array:
    if maximo is None or itervar > maximo :
        maximo = itervar
    print('Laço:', itervar, maximo)
print('Máximo:', maximo)

print('____________________________________________')

minimo = None
print('Antes', minimo)
for itervar in array:
    if minimo is None or itervar < minimo:
        minimo = itervar
    print('Laço:', itervar, minimo)
print('Mínimo:', minimo)

def min(valores):
    minimo = None
    for valor is None or valor < minimo:
        minimo = valor
    return minimo
