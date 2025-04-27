from in_onputs import obter_numero_inteiro
# 3. Leia 3 (três) números, verifique e escreva o maior entre os números lidos.
def numero_eh_maior(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    elif num3 >= num1 and num3 >= num2:
        return num3
    
    return 'todos são iguais'

def main():
    num1 = obter_numero_inteiro('Digite o primeiro número inteiro: ')
    num2 = obter_numero_inteiro('Digite o segundo número inteiro: ')
    num3 = obter_numero_inteiro('Digite o terceiro número inteiro: ')

    print(f'Comparando os números, o maior é o {numero_eh_maior(num1,num2, num3)}')

if __name__ == '__main__':
    main()