def main():
    horas_analisadas = int(input('Horas para análise: '))
    limite_temperatura = float(input('Limite da temperatura(Celsius): '))

    maior_temperatura = 0
    menor_umidade = 100
    contagem = 0

    for hora in range(1, horas_analisadas + 1, 1):
        print(f'>>> Dados da Hora {hora}')
        temperatura = float(input('Temperatura(Celsius): '))
        umidade = float(input('Umidade do ar(%): '))

        if temperatura > maior_temperatura:
            maior_temperatura = temperatura
        if umidade < menor_umidade:
            menor_umidade = umidade
        if temperatura > limite_temperatura:
            contagem += 1

    resultado = f'''
    --> Resultado da Análise das Temperaturas e Umidade em {horas_analisadas}h
    Maior Temperatura Registrada: {maior_temperatura:0.1f}C
    Menor Umidade Registrada: {menor_umidade:0.1f}%
    Contagem de quantas vezes o limite {limite_temperatura:0.1f} foi excedido: {contagem}
    '''
    print(resultado)

if __name__ == '__main__':
    main()