from in_onputs import obter_numero_inteiro
# 30. Existem números de 4 dígitos (entre 1000 e 9999) que obedecem à seguinte característica: se dividirmos
# o número em dois números de dois dígitos, um composto pela dezena e pela unidade, e outro pelo
# milhar e pela centena, se somarmos estes dois novos números gerando um terceiro, o quadrado deste
# terceiro número é exatamente o número original de quatro dígitos. Por exemplo:
# 2025 -> dividindo: 20 e 25 -> somando temos 45 -> 452 = 2025.

def quadrado_gerado(num):
    parte1 = num // 100
    parte2 = num % 100

    soma = parte1 + parte2
    quadrado = soma * soma
    
    if quadrado == num:
        return f'O número {num} é sua divisão {parte1} e {parte2} onde sua soma {soma} ao quadrado é o própio número {quadrado}'
    
    return f'O número {num} não é um quadrado especial'

def main():
    num = obter_numero_inteiro('Digite um número inteiro de 4 dígitos: ')

    if 1000 <= num <= 9999:
        print(quadrado_gerado(num))
    else:
        print('Número é inválido!')

if __name__ == '__main__':
    main()