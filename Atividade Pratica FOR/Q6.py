def calcular_volume_medio(volume_total, sessoes):
    volume_metade1 = volume_total // (sessoes//2)

    volume_metada2 = volume_total - volume_metade1
    if volume_metade1 > volume_metada2:
        return "Não houve melhora significativa"
    return "Tendência de melhora observada"

def main():
    sessoes = int(input('Sessões: '))
    resultado_sessoes = {}
    maior_volume = {"sessao" : 0, "volume" : 0}
    volume_medio = 0
    for sessao in range(1, sessoes + 1, 1):
        print(f'---> Sessão {sessao}')
        repeticoes = int(input('Número de Repetição: '))
        peso = int(input('Peso(KG): '))
        volume_total = repeticoes * peso
        volume_medio += volume_total
        if volume_total > maior_volume.get("volume"):
            maior_volume.update({"sessao": sessao, "volume": volume_total})

        resultado_sessoes.update({sessao : volume_total})
    
    for sessao, volume in resultado_sessoes.items():
        print("---- Resultado das Sessões de Treino ----")
        print(f'Sessão {sessao}')
        print(f'Volume Total: {resultado_sessoes[sessao]}\n')
    
    print(f'A sessão {maior_volume.get("sessao")} teve o maior volume de {maior_volume.get("volume")}')
    print(f'Tendência de Melhora: {calcular_volume_medio(volume_medio,sessoes)}')




if __name__ == '__main__':
    main()