def computarNotas(nota):
    try:
        if nota <= 1.0 :
            if nota >= 0.9 :
                print('A')
            elif nota >= 0.8 :
                print('B')
            elif nota >= 0.7 :
                print('C')
            elif nota >= 0.6 :
                print('D')
            elif nota < 0.6 :
                print('F')
        else :
            print('Pontuação Inválida.')
    except Exception as e:
        print('Pontuação Inválida.')

computarNotas(2.0)
