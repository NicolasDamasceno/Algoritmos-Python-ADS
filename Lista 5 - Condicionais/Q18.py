from in_onputs import obter_numero_inteiro
# 18. Leia dois valores e uma das seguintes operações a serem executadas (codificadas da seguinte forma: 1 –
# Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão). Calcule e escreva o resultado dessa operação
# sobre os dois valores lidos.

def adicao(num1,num2):
    return num1 + num2

def subtracao(num1,num2):
    return num1 - num2

def multiplicacao(num1,num2):
    return num1 * num2

def divisao(num1,num2):
    return num1 / num2

def main():
    num1 = obter_numero_inteiro('Digite o primeiro número inteiro: ')
    num2 = obter_numero_inteiro('Digite o segundo número inteiro: ')
    escolha = obter_numero_inteiro('Digite 1 - Adição / 2 – Subtração / 3 – Multiplicação / 4 – Divisão\n--> ')
    if escolha == 1:
        print(f'{num1} + {num2} = {adicao(num1,num2)}')
    elif escolha == 2:
        print(f'{num1} - {num2} = {subtracao(num1,num2)}')
    elif escolha == 3:
        print(f'{num1} x {num2} = {multiplicacao(num1,num2)}')
    elif escolha == 4:
        print(f'{num1} / {num2} = {divisao(num1,num2):0.1f}')
    else:
        print('Escolha Inválida')

if __name__ == '__main__':
    main()
