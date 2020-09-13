contador = 0
array = [1.00, 1.00, 1.00, 1.00, 1.00, 1.00]
for itervar in array:
    contador = contador + 1

print('contagem:', contador)

total = 0
for itervar in array:
    total = total + itervar

print('Total:', total)

saldo_total = 0
cart = [2.67, 4.78, 7.99]
for itens_cart in cart:
    saldo_total = saldo_total + itens_cart
print('total da compra:', saldo_total)
