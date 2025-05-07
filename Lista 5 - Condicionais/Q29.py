from in_onputs import obter_numero_inteiro
import math
# 29. Um número é um quadrado perfeito quando a raiz quadrada do número é igual à soma das dezenas
# formadas pelos seus dois primeiros e dois últimos dígitos.
# Exemplo: √9801 = 99 = 98 + 01. O número 9801 é um quadrado perfeito.
# Escreva um algoritmo que leia um número de 4 dígitos e verifique se ele é um quadrado perfeito.

def quadrado_perfeito(num): 
    parte1 = num // 100
    parte2 = num % 100
    soma = parte1 + parte2
    raiz = math.isqrt(num)

    if raiz == soma and raiz * raiz == num:
        return f'{num} é um quadrado perfeito'
    
    return f'{num} não é um quadrado perfeito'

def main():
    num = obter_numero_inteiro('Digite um número de 4 dígitos inteiro: ')
    if 1000 <= num <= 9999:
        print(quadrado_perfeito(num))
    else:
        print('Número inválido')

if __name__ == '__main__':
    main()