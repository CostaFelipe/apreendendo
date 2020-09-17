fruta = 'banana'
letra = fruta[1]
letra = fruta[0]
print(letra)

carro = 'gol'
print(carro[0])

comprimento = len(fruta)
print(comprimento)


ultima = fruta[comprimento - 1]
print(ultima)

print("\n")

indice = 0
while indice < len(fruta):
    letra = fruta[indice]
    print(letra)
    indice = indice + 1
