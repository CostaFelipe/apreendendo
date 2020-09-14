lista = []
contador = 0
total = 0
while True:
    add = int(input('Add numeros:'))
    if add == 0:
        break
    lista.append(add)
    total = total + add
    contador = contador + 1
print("a lista é:",lista, "|qtd:", contador," |total:", total)
