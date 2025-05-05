from in_onputs import obter_numero_real
import math
# 24. Leia os coeficientes (A, B e C) de uma equações de 2° grau e escreva suas raízes. Vale lembrar que o
# coeficiente A deve ser diferente de 0 (zero).
def equacao_raizes(numA, numB, numC):
    b = (numB**2) - (4 * numA * numC)
    x1 = (-b + math.sqrt(b)) / (2 * numA)
    x2 = (-b - math.sqrt(b)) / (2 * numA)

    return x1, x2

def main():
    numA = obter_numero_real('Digite o coeficiente de Ax2: ')
    numB = obter_numero_real('Digite o coeficiente de Bx: ')
    numC = obter_numero_real('Digite o coeficiente de C: ')
    if numA == 0:
        print('Essa equação não é do segundo grau')

    else: 
        x1, x2 = equacao_raizes(numA, numB, numC)

        print(f'Equação: ({numA}x2) + ({numB}x) + ({numC})')
        print(f'Raízes: X1 = {x1} e X2 = {x2}')

if __name__ == '__main__':
    main()