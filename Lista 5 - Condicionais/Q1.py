from in_onputs import obter_numero_inteiro
# 1. Leia 3 (três) números, verifique e escreva quantos números iguais existem entre os números.
def contar_numeros_iguais(num1,num2,num3):
    if num1 == num2 and num2 == num3:
        return 3
    elif num1 == num2:
        return 2
    elif num1 == num3:
        return 2
    elif num2 == num3:
        return 2
    
    return 0
def main():
    num1 = obter_numero_inteiro('1 - Digite um número aleatório inteiro: ')
    num2 = obter_numero_inteiro('2 - Digite um número aleatório inteiro: ')
    num3 = obter_numero_inteiro('3 - Digite um número aleatório inteiro: ')

    print(f'Entre os números digitados há {contar_numeros_iguais(num1,num2,num3)} iguais')
if __name__ == '__main__':
    main()