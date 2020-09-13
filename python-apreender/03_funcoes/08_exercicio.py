def calcularSoma(a, b):
    try:
        added = a + b
        print(added)
    except Exception as e:
        print('Não é um inteiro, por favor digite um inteiro')


while True:
    primeiro_numero = int(input("Digite o primeiro numero:"))
    if primeiro_numero == 0:
        break
    segundo_numero  = int(input("Digite o segundo numero:"))    
    calcularSoma(primeiro_numero, segundo_numero)
print('sistema encerrado')
