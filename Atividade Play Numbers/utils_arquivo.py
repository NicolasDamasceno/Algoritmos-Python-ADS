def gravar_dados(vetores, nome_arquivo):

    arquivo = open(nome_arquivo, 'w')

    linha = ''
    for index in range(len(vetores)):
        linha += f'{vetores[index]}\n'
        arquivo.write(linha)
    
    print('Dados Salvos!')


def carregar_dados(nome_arquivo):
    vetores = []
    arquivo = open(nome_arquivo)

    for linha in arquivo:
        vetores.append(linha)
    return vetores