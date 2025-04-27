from in_onputs import obter_numero_inteiro
# 2. Leia 2 (dois) números, verifique e escreva o menor e o maior entre os números lidos.
def numero_maior_e_menor(num1, num2):
    if num1 > num2:
        return f'{num1} é maior que {num2}'
    elif num2 > num1:
        return f'{num2} é maior que {num1}'
    
    return 'ambos são iguais'

def main():
    num1 = obter_numero_inteiro('Digite o primeiro número inteiro: ')
    num2 = obter_numero_inteiro('Digite o segundo número inteiro: ')

    print(f'Comparando os números, {numero_maior_e_menor(num1,num2)}')

if __name__ == '__main__':
    main()