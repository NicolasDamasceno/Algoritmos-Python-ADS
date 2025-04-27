from in_onputs import obter_numero_inteiro
# 9. Leia 1 (um) número entre 0 e 100, verifique e escreva se o número é ou não primo.
def verificar_num(num):
    if 0 <= num <= 100:
        return True
    else:
        return False

def divisivel(num, divisor):
    return num % divisor == 0

def eh_primo(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif divisivel(num,2):
        return False
    elif num == 3:
        return True
    elif divisivel(num,3):
        return False
    elif num == 5:
        return True
    elif divisivel(num,5):
        return False
    elif num == 7:
        return True
    elif divisivel(num,7):
        return False
    
    return True

def main():
    num = obter_numero_inteiro('Digite um número inteiro de 0 a 100: ')
    if verificar_num(num):
        if eh_primo(num):
            print(f'{num} é primo')
        else: 
            print(f'{num} não é primo')
    else: 
        print(f'{num} não está entre 0 e 100')

if __name__ == '__main__':
    main()