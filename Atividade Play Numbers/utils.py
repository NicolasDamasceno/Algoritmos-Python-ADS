import os
import random
def limpar_console():
    return os.system('clear')

def obter_num_real(label):
    try:
        num = int(input(label))
        return num
    except ValueError:
        print('Caractere inválido')
        return obter_num_real(label)

def obter_num_positivo(label):
    num = obter_num_real(label)
    if num >= 0:
        return num
    else:
        print('Apenas positivos...')
        return obter_num_positivo(label)

def obter_num_em_faixa(num_min, num_max):
    return random.randint(num_min, num_max)

    