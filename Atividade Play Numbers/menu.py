from utils import limpar_console, obter_num_real
from funcionalidades import criar_vetor_auto, criar_vetor_manual, resetar_vetores, quantidade_itens_no_vetor, maior_menor_valor_vetor, somatorio_vetor, media_vetor, qtd_itens_negativos, qtd_itens_positivos, multiplicar_itens_vetor, elevar_itens_vetor, reduzir_vetor_por_fracao, substituir_valores_negativos, ordenar_vetor, embaralhar_vetores, adicionar_novo_valor, remover_iten_por_valor, remover_item_por_posicao, editar_valor_por_posicao
from utils_arquivo import gravar_dados, carregar_dados


def main():
    limpar_console()
    vetores = []
    menu = '''
    ------ Sys Vetores Inicio------

    1 - Inicializar um Vetor(Sem Arquivo)
    2 - Carregar um Arquivo
    3 - Mostrar Valores
    4 - Resetar Vetores
    5 - Quantidades de itens no Vetor
    6 - Maior e Menor valor no Vetor
    7 - Somátorio do Vetor
    8 - Média do Vetor
    9 - Mostra itens negativo e quantidade
    10 - Mostra itens positivos e quantidade
    11 - Atualizar valores por Regra
    12 - Adicionar Valor
    13 - Remover item por Valor
    14 - Remover item por Posição
    15 - Editar Valor por Posição

    0 - Finalizar o Programa e Salvar
    '''
    print(menu)
    opcao = obter_num_real('--> ')

    while opcao != 0:
        if opcao == 1:
            vetores = main_tela_2()
            print(f'Vetores Criados!\n{vetores}')
            
        elif opcao == 2:
            vetores = carregar_dados('vetores.txt')

        elif opcao == 3:
            limpar_console()
            print(f'Lista dos Vetores\n{vetores}')

        elif opcao == 4:
            limpar_console()
            vetores = resetar_vetores(vetores)
            print(f'Vetores Resetados!\n{vetores}')

        elif opcao == 5:
            limpar_console()
            qtd_vetor = quantidade_itens_no_vetor(vetores)
            print(f'Quantidade de itens no Vetor: {qtd_vetor}')
        
        elif opcao == 6:
            limpar_console()
            maior, menor = maior_menor_valor_vetor(vetores)
            print(f'Maior valor do vetor: {maior}\nMenor valor do vetor: {menor}')

        elif opcao == 7:
            limpar_console()
            somatorio = somatorio_vetor(vetores)
            print(f'Somatório do Vetor: {somatorio}')

        elif opcao == 8:
            limpar_console()
            media = media_vetor(vetores)
            print(f'Média do Vetor: {media}')

        elif opcao == 9:
            limpar_console()
            vetores_negativos, qtd_negativos = qtd_itens_negativos(vetores)
            print(f'Vetor Negativo: {vetores_negativos}\nQuantidade de itens Negativos: {qtd_negativos}')

        elif opcao == 10:
            limpar_console()
            vetores_positivos, qtd_positivos = qtd_itens_positivos(vetores)
            print(f'Vetor Positivo: {vetores_positivos}\nQuantidade de itens Positivos: {qtd_positivos}')
        
        elif opcao == 11:
            limpar_console()
            vetores = main_tela_3(vetores)

        elif opcao == 12:
            limpar_console()
            vetores = adicionar_novo_valor(vetores)
            print(f'Valor Adicionado: {vetores}')
        
        elif opcao == 13:
            limpar_console()
            vetores = remover_iten_por_valor(vetores)
            print(f'Valor Removido: {vetores}')

        elif opcao == 14:
            limpar_console()
            vetores = remover_item_por_posicao(vetores)
            print(f'Valor Removido por posição: {vetores}')
        
        elif opcao == 15:
            limpar_console()
            vetores = editar_valor_por_posicao(vetores)
            print(f'Vetores com Valor editado: {vetores}')

        input('Continue...')
        limpar_console()
        print(menu)
        opcao = obter_num_real('--> ')

    gravar_dados(vetores, 'vetores.txt')

    print('Fim')
      
def main_tela_2():
    limpar_console()
    tela_1 = '''
    ----- Iniciando Vetores
    1 - Iniciar vetor Automático
    2 - Iniciar Vetor Manual

    0 - Sair
    '''
    print(tela_1)
    escolha = obter_num_real('---> ')
    if escolha == 1:
        max = obter_num_real('Digite o número máximo: ')
        min = obter_num_real('Digite o número minímo: ')
        return criar_vetor_auto(max,min)

    elif escolha == 2:
        max = obter_num_real('Digite o número máximo: ')
        min = obter_num_real('Digite o número minímo: ')
        quantidade = obter_num_real('Digite a quantidade: ')
        return criar_vetor_manual(max,min,quantidade)
    elif escolha == 0:
        return []


def main_tela_3(vetores):
    limpar_console()
    menu = '''
    ------ Atualizar Valores por Regra ------
    1 - Multiplica os itens por um Valor
    2 - Eleva os itens a um Valor 
    3 - Reduzi os itens por Fração
    4 - Substituir negativos por números em uma Faixa
    5 - Ordenar Vetores
    6 - Embaralhar Vetores

    0 - Sair da tela
    '''
    print(menu)
    opcao = obter_num_real('--> ')
    while opcao != 0:
        if opcao == 1:
            limpar_console()
            vetores, multiplicador = multiplicar_itens_vetor(vetores)
            print(f'Vetores Multiplicados x{multiplicador}: {vetores}')
        
        elif opcao == 2:
            limpar_console()
            vetores, expoente = elevar_itens_vetor(vetores)
            print(f'Vetores Elevados a {expoente}: {vetores}')
        
        elif opcao == 3:
            limpar_console()
            vetores, numerador, denominador = reduzir_vetor_por_fracao(vetores)
            print(f'Vetores Reduzidos pela fração {numerador}/{denominador}: {vetores}')

        elif opcao == 4:
            limpar_console()
            vetores = substituir_valores_negativos(vetores)
            print(f'Vetores com valores negativos substituido: {vetores}')

        elif opcao == 5:
            limpar_console()
            vetores = ordenar_vetor(vetores)
            print(f'Vetor Ordenado: {vetores}')

        elif opcao == 6:
            limpar_console()
            vetores = embaralhar_vetores(vetores)
            print(f'Vetores Embaralhados: {vetores}')

        input('Continue...')
        limpar_console()
        print(menu)
        opcao = obter_num_real('--> ')

    limpar_console()
    return vetores

if __name__ == '__main__':
    main()

