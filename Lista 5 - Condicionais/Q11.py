from in_onputs import obter_numero_inteiro
# 11. Leia quatro números (opção, num 1, num2, num3) e que escreva o valor de num1 se opção igual a 1; o
# valor de num2 se opção for igual a 2; e o valor de num3 se opção for igual a 3. Os únicos valores
# possíveis para a variável opção são 1, 2 e 3.

def verificar_opcao(opcao):
    if opcao == 1 or opcao == 2 or opcao == 3:
        return True
    
    return False

def main():
    opcao = obter_numero_inteiro('Escolha uma opção (1, 2, 3): ')
    num1 = obter_numero_inteiro('Digite um número inteiro: ')
    num2 = obter_numero_inteiro('Digite um número inteiro: ')
    num3 = obter_numero_inteiro('Digite um número inteiro: ')
    if opcao:
        if opcao == 1:
            print(f'Opção {opcao}, primeiro número digitado {num1}')
        elif opcao == 2:
            print(f'Opção {opcao}, primeiro número digitado {num2}')
        elif opcao == 3:
            print(f'Opção {opcao}, primeiro número digitado {num3}')
    else:
        print(f'{opcao} não é uma escolha válida')
if __name__ == '__main__':
    main()