def aquecimento(temperatura_soma, anos):
    primeira_metade = (temperatura_soma // (anos // 2))
    segunda_metade = temperatura_soma - primeira_metade
    
    if segunda_metade > primeira_metade:
        return 'Tendência de Aquecimento DETECTADA'
    if segunda_metade < primeira_metade:
        return 'Resfriamento DETECTADO'
    
    return 'Não houve uma Tendência de Aquecimento ou Resfriamento EQUILIBRADO'

def media_temperaturas(soma_temperaturas, anos):
    return soma_temperaturas / anos

def main():
    anos = int(input('Tempo de Análise(anos): '))
    maior_temperatura_anual = {"ano" : 0, "temperatura" : 0}
    menor_temperatura_anual = {"ano" : 0, "temperatura" : 100}
    soma_temperaturas = 0

    for ano in range(1, anos + 1, 1):
        temperatura_media_anual = float(input(f'Temperatura Média do ano {ano}: '))
        soma_temperaturas += soma_temperaturas
        if temperatura_media_anual > maior_temperatura_anual.get('temperatura'):
            maior_temperatura_anual.update({"ano" : ano, "temperatura" : temperatura_media_anual})
        if temperatura_media_anual < menor_temperatura_anual.get("temperatura"):
            menor_temperatura_anual.update({"ano" : ano, "temperatura": temperatura_media_anual})

    tendencia_aquecimento = aquecimento(soma_temperaturas, anos)
    media = media_temperaturas(soma_temperaturas, anos)

    resultados = f'''
    ----- Análise de Temperaturas Anuais -----
    Ano da Maior Média: {maior_temperatura_anual.get("ano")}
    Temperatura do Ano com Maior Média: {maior_temperatura_anual.get("temperatura")}
    -------------------------------------------------------
    Ano da Menor Média: {menor_temperatura_anual.get("ano")}
    Temperatura do Ano com Menor Média: {menor_temperatura_anual.get("temperatura")}
    --------------------------------------------------------
    Média das Temperaturas em {anos}: {media:0.2f}C
    Resultado: {tendencia_aquecimento}
    '''
    print(resultados)

if __name__ == '__main__':
    main()
