fruta = "laranja"

indice = 0
while indice < len(fruta):
    letra = fruta[indice]
    indice = indice + 1
    print(letra)

contar = 0
for letra in fruta:
    if letra == 'a':
        contar = contar + 1

print(contar)
