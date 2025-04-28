from in_onputs import obter_numero_inteiro
# 17. Leia valores inteiros em duas variáveis distintas e se o resto da divisão da primeira pela segunda for 1
# escreva a soma dessas variáveis mais o resto da divisão; se for 2 escreva se o primeiro e o segundo valor
# são pares ou ímpares; se for igual a 3 multiplique a soma dos valores lidos pelo primeiro; se for igual a 4
# divida a soma dos números lidos pelo segundo, se este for diferente de zero. Em qualquer outra situação
# escreva o quadrado dos números lidos.

def soma(num1,num2,resto):
    return num1 + num2 + resto 

def par_ou_impar(num):
    if num % 2 == 0:
        return 'par'
    return 'impar'

def soma_multiplicacao(num1,num2):
    return (num1 + num2) * num1

def soma_divisao(num1,num2):
    return (num1 + num2) / num2

def num_ao_quadrado(num):
    return num**2

def main():
    num1 = obter_numero_inteiro('Digite um número inteiro: ')
    num2 = obter_numero_inteiro('Digite um número inteiro: ')
    resto = num1 % num2

    if resto == 1:
        print(f'{num1} + {num2} + {resto} = {soma(num1,num2,resto)}')
    elif resto == 2:
        print(f'{num1} é {par_ou_impar(num1)}\n{num2} é {par_ou_impar(num2)}')
    elif resto == 3:
        print(f'({num1} + {num2}) * {num1} = {soma_multiplicacao(num1,num2)}')
    elif resto == 4:
        print(f'({num1} + {num2}) / {num2} = {soma_divisao(num1,num2):0.1f}')
    else:
        print(f'{num1}**2 = {num_ao_quadrado(num1)}\n{num2}**2 = {num_ao_quadrado(num2)}')

if __name__ == '__main__':
    main()