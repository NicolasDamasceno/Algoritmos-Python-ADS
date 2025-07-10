import random 
from utils import obter_num_real, obter_num_em_faixa, limpar_console


def criar_vetor_auto(max,min):
    vetores = []
    quantidade = random.randint(0,50)

    for i in range(quantidade):
        vetores.append(random.randint(min,max))

    return vetores


def criar_vetor_manual(max,min,qtd):
    vetores = []

    for i in range(qtd):
        vetores.append(random.randint(min,max))

    return vetores


def resetar_vetores(vetores):
    padrao = obter_num_real('Digite o número padrão: ')

    for index in range(len(vetores)):
        vetores[index] = padrao

    return vetores


def quantidade_itens_no_vetor(vetores):
    return len(vetores)


def maior_menor_valor_vetor(vetores):
    maior_valor = 0
    menor_valor = vetores[0]

    for num in range(len(vetores)):
        if vetores[num] > maior_valor:
            maior_valor = vetores[num]

        if vetores[num] < menor_valor:
            menor_valor = vetores[num]

    return maior_valor, menor_valor


def somatorio_vetor(vetores):
    soma = 0
    for i in range(len(vetores)):
        soma += vetores[i]
    return soma


def media_vetor(vetores):
    return (somatorio_vetor(vetores)/len(vetores)) 

def qtd_itens_negativos(vetores):
    lista_negativos = []
    qtd = 0
    
    for index in range(len(vetores)):
        if vetores[index] < 0:
            lista_negativos.append(vetores[index])
            qtd += 1

    return lista_negativos, qtd


def qtd_itens_positivos(vetores):
    lista_positivos = []
    qtd = 0
    for index in range(len(vetores)):
        if vetores[index] > 0:
            lista_positivos.append(vetores[index])
            qtd += 1

    return lista_positivos, qtd

def multiplicar_itens_vetor(vetores):
    mutiplicador = obter_num_real('Digite o multiplicador: ')
    vetores_multiplicados = []

    for index in range(len(vetores)):
        vetores_multiplicados.append((vetores[index]*mutiplicador))
        
    return vetores_multiplicados, mutiplicador

def elevar_itens_vetor(vetores):
    lista_elevados = []
    expoente = obter_num_real('Digite o expoente: ')

    for index in range(len(vetores)):
        lista_elevados.append((vetores[index]**expoente))

    return lista_elevados, expoente

def reduzir_vetor_por_fracao(vetores):
    numerador = obter_num_real('Numerador da Fração: ')
    denominador = obter_num_real('Denominador da Fração: ')
    lista_fracao = []
    for index in range(len(vetores)):
        lista_fracao.append(((vetores[index]*numerador)//denominador))

    return lista_fracao, numerador, denominador


def substituir_valores_negativos(vetores):
    max = obter_num_real('Número Máximo: ')
    min = obter_num_real('Número Minímo: ')
    lista_substituta = []
    for index in range(len(vetores)):
        if vetores[index] < 0:
            lista_substituta.append(obter_num_em_faixa(min,max))
        
        else: 
            lista_substituta.append(vetores[index])
    
    return lista_substituta

def ordenar_vetor(vetores):
    ordem = obter_num_real('Digite 1 - Crescente ou 2 - Decrescente\n-> ')
    if ordem == 1:
        vetores.sort()
        return vetores
    elif ordem == 2:
        vetores.sort(reverse=True)
        return vetores
    else:
        print('Alternativa inválida...')
        limpar_console()
        return ordenar_vetor(vetores)
    
def embaralhar_vetores(vetores):
    qtd = len(vetores)

    for i in range(qtd - 1, 0, -1):
        posicao_aleatoria = random.randint(0,i)

        vetores[i], vetores[posicao_aleatoria] = vetores[posicao_aleatoria], vetores[i]

    return vetores

def adicionar_novo_valor(vetores):
    novo_valor = obter_num_real('Novo valor: ')
    vetores.append(novo_valor)
    
    return vetores


def remover_iten_por_valor(vetores):
    valor = obter_num_real('Digite o valor do vetor: ')
    vetores.remove(valor)
    
    return vetores

def remover_item_por_posicao(vetores):
    posicao = obter_num_real('Digite a posição do vetor: ')
    vetores.pop(posicao)

    return vetores

def editar_valor_por_posicao(vetores):
    posicao = obter_num_real('Digite a posição do vetor: ')
    novo_valor = obter_num_real('Digite o novo Valor: ')
    vetores[posicao] = novo_valor
    return vetores