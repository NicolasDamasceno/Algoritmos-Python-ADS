from in_onputs import obter_numero_inteiro
# 5. Leia 3 (três) números e escreva-os em ordem crescente.
def ordem_crescente(num1, num2, num3):
    if num1 > num2 and num1 > num3 and num2 > num3:
        return f'{num1}>{num2}>{num3}'
    elif num1 > num2 and num1 > num3 and num3 > num2:
        return f'{num1}>{num3}>{num2}'
    elif num2 > num1 and num2 > num3 and num1 > num3:
        return f'{num2}>{num1}>{num3}'
    elif num2 > num1 and num2 > num3 and num3 > num1:
        return f'{num2}>{num3}>{num1}'
    elif num3 > num1 and num3 > num2 and num2 > num1:
        return f'{num3}>{num2}>{num1}'
    elif num3 > num1 and num3 > num2 and num1 > num2:
        return f'{num3}>{num1}>{num2}'
    
def main():
    num1 = obter_numero_inteiro('Digite o primeiro número inteiro: ')
    num2 = obter_numero_inteiro('Digite o segundo número inteiro: ')
    num3 = obter_numero_inteiro('Digite o terceiro número inteiro: ')

    print(f'Ordem crescente: {ordem_crescente(num1,num2,num3)}')

if __name__ == '__main__':
    main()