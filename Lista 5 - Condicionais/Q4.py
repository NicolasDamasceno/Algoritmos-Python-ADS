from in_onputs import obter_numero_inteiro
# 4. Leia 1 (um) número de 2 (dois) dígitos, verifique e escreva se o algarismo da dezena é igual ou diferente
# do algarismo da unidade.
def comparando_dezena_unidade(num):
    dezena = num // 10
    unidade = num % 10
    if dezena == unidade: 
        return 'são iguais'
    
    return 'são diferentes' 

def main():
    num = obter_numero_inteiro('Digite um número de dois dígitos: ')

    print(f'Os dígitos de {num} {comparando_dezena_unidade(num)}')

if __name__ == '__main__':
    main()