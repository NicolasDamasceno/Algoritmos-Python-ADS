def juros_compostos(valor, juros, tempo):
    return valor*((1 + juros/100)**tempo)

def main():
    valor_inicial = float(input('Valor da dívida (R$): '))
    taxa_juros_mensal = float(input('Taxa de Juros Mensal(%): '))
    meses = int(input('Meses para Projeção: '))

    divida = valor_inicial
    for mes in range(1, meses + 1, 1):
        valor_pago = float(input(f'(R$)Valor pago no mês {mes}: '))
        valor_restante = divida - valor_pago
        if valor_restante <= 0:
            resultado = f'''
            >>> Dívida QUITADA <<<
            Valor Inicial da dívida: R${valor_inicial:0.2f}
            Mês da Quitação: {mes}
            '''
            print(resultado)
            break
        divida = juros_compostos(valor_restante, taxa_juros_mensal, meses - mes)
        print(f'Mês Pago, novo valor do saldo devedor: R${divida:0.2f}')

    if divida > 0:
        resultado = f'''
            >>> Dívida Final <<<
            Valor Inicial da dívida: R${valor_inicial:0.2f}
            Valor Restante do Saldo: R${divida:0.2f} 
            '''
        print(resultado)

if __name__ == '__main__':
    main()

