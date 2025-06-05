def media(soma,n):
    return soma/n


def main():

    dias = int(input('Digite a quantidade de dias para análise: '))
    limite_calorias = int(input('Digite o limite de calorias: '))

    menor_calorias_diaria = limite_calorias
    dia_menor_calorias = 0
    maior_calorias_diaria = 0
    dia_maior_calorias = 0
    soma_calorias = 0
    # Recebendo os dados
    for dia in range(1, dias + 1, 1):
        print(f'---> Calorias do dia {dia} <---')
        cafe_manha = int(input('Digite as calorias do café da manhã: '))
        almoco = int(input('Digite as calorias do almoço: '))
        jantar = int(input('Digite as calorias do jantar: '))
        ceia = int(input('Digite as calorias da ceia: '))
        
        calorias_diarias = cafe_manha + almoco + jantar + ceia
        # Selecinando dias de maior e menor consumo
        if calorias_diarias >= maior_calorias_diaria:
            maior_calorias_diaria = calorias_diarias
            dia_maior_calorias = dia
        elif calorias_diarias <= menor_calorias_diaria:
            menor_calorias_diaria = calorias_diarias
            dia_menor_calorias = dia

        soma_calorias += calorias_diarias

    media_calorias = media(soma_calorias, dias)
    # Varificando média e limites
    if media_calorias > limite_calorias:
        resultado = f'''
            ---- Calorias ----\n
            Limete Calórico: {limite_calorias}
            Média de Calórias: {media_calorias}
            Dia {dia_maior_calorias} teve o maior consumo calórico de {maior_calorias_diaria}
            Dia {dia_menor_calorias} teve o menor consumo calórico de {menor_calorias_diaria}

            Resutado final = O limite de calorias foi ULTRAPRASSADO
            ''' 
        print(resultado)

    elif media_calorias < limite_calorias:
        resultado = f'''
            ---- Calorias ----\n
            Limete Calórico: {limite_calorias}
            Média de Calórias: {media_calorias}
            Dia {dia_maior_calorias} teve o maior consumo calórico de {maior_calorias_diaria}
            Dia {dia_menor_calorias} teve o menor consumo calórico de {menor_calorias_diaria}

            Resutado final = O limite de calorias foi CUMPRIDO
            ''' 
        print(resultado)

    elif media_calorias == limite_calorias:
        resultado = f'''
            ---- Calorias ----\n
            Limete Calórico: {limite_calorias}
            Média de Calórias: {media_calorias}
            Dia {dia_maior_calorias} teve o maior consumo calórico de {maior_calorias_diaria}
            Dia {dia_menor_calorias} teve o menor consumo calórico de {menor_calorias_diaria}

            Resutado final = O limite de calorias foi IGUAL
            ''' 
        print(resultado)

if __name__ == '__main__':
    main()

