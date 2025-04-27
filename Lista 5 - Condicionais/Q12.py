from in_onputs import obter_numero_inteiro
# 12. Leia 1 (um) número inteiro e escreva se este número é par ou impar.

def eh_par_impar(num):
    if num == 0: 
        return 'par'
    elif num == 1:
        return 'ímpar'
    elif num % 2 == 0:
        return 'par'
    return 'ímpar'

def main():
    num = obter_numero_inteiro('Digite um número inteiro: ')
    print(f'O número {num} é {eh_par_impar(num)}')

if __name__ == '__main__':
    main()