from in_onputs import obter_numero_inteiro
# 14. Leia 5 (cinco) números inteiros, calcule a sua média e escreva os que são maiores que a média.

def calcular_media(n1,n2,n3,n4,n5):
    return ((n1 + n2 + n3 + n4 + n5)/5)

def maior_numero_media(n1,n2,n3,n4,n5,media):
    maior = n1
    if n2 > media:
        maior = n2
    if n3 > media:
        maior = n2
    if n4 > media:
        maior = n4
    if n5 > media:
        maior = n5
    
    return maior

def main():
    num1 = obter_numero_inteiro('Digite o primeiro número: ')
    num2 = obter_numero_inteiro('Digite o segundo número: ')
    num3 = obter_numero_inteiro('Digite o terceiro número: ')
    num4 = obter_numero_inteiro('Digite o quarto número: ')
    num5 = obter_numero_inteiro('Digite o quinto número: ')

    media = calcular_media(num1,num2,num3,num4,num5)
    print(f'A média dos números é {media:0.1f}')
    print(f'O número maior que a média é {maior_numero_media(num1,num2,num3,num4,num5,media)}')

if __name__ == '__main__':
    main()