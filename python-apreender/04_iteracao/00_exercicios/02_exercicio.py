lista = []
contador = 0
total = 0
maximo = None

while True:
    add = int(input('Add numeros:'))
    if add == 0:
        break
    lista.append(add)
    if maximo is None or add > maximo:
        maximo = add
    #print('Laço:', add, maximo)

    total = total + add
    contador = contador + 1

print("|lista:",lista, "|qtd:", contador,"\n|total:", total, "|Maior:", maximo)
