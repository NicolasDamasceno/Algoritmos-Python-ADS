from in_onputs import obter_numero_inteiro
# 13. Leia 5 (cinco) números inteiros e escreva o maior e o menor deles. Considere que todos os valores são
# diferentes.

def maior_menor_num(n1,n2,n3,n4,n5):
    maior = n1
    menor = n1
    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3
    if n4 > maior:
        maior = n4
    if n5 > maior:
        maior = n5
    
    if n2 < menor:
        n2 = menor
    if n3 < menor:
        n3 = menor
    if n4 < menor:
        n4 = menor
    if n5 < menor:
        n5 = menor
    
    return f'Maior: {maior}\nMenor: {menor}'

def main():
    num1 = obter_numero_inteiro('Digite o primeiro número: ')
    num2 = obter_numero_inteiro('Digite o segundo número: ')
    num3 = obter_numero_inteiro('Digite o terceiro número: ')
    num4 = obter_numero_inteiro('Digite o quarto número: ')
    num5 = obter_numero_inteiro('Digite o quinto número: ')

    print(maior_menor_num(num1,num2,num3,num4,num5))
if __name__ == '__main__':
    main()