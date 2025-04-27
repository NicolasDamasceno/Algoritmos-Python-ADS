from in_onputs import obter_numero_inteiro
# Exercício 3: Verificador de Números Primos
# Descrição do Problema:
# Crie um programa que verifica se um número é primo. Um número primo é aquele
# que só é divisível por 1 e por ele mesmo.
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
    
    if eh_primo(num):
        print(f'{num} é primo')
    else: 
        print(f'{num} não é primo')


if __name__ == '__main__':
    main()