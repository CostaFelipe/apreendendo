def calculoPagamento(horas, TaxaHora):
    if horas > 40 :
        salario =  horas * TaxaHora * 1.5
        print('salario:', salario)
    else :
        salario = horas * TaxaHora
        print('salario:', salario)

calculoPagamento(45, 10)
