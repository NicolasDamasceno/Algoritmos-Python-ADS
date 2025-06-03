from in_onputs import obter_numero_inteiro
# 1. Leia um número e mostre na tela se o número é positivo ou negativo.
def positivo_negativo(num):
    if num > 0:
        return True
    elif num < 0: 
        return False
    return 'neutro'

def main():
    numero = obter_numero_inteiro('Digite um número: ')
    sinal = positivo_negativo(numero)
    
    if sinal == True:
        print(f'O {numero} é positivo')
    elif sinal == False:
        print(f'O {numero} é negativo')
    else:
        print(f'O {numero} é neutro')

if __name__ == '__main__':
    main()
