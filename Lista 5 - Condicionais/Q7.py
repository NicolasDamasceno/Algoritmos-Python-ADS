from in_onputs import obter_numero_inteiro
# 7. Leia 3 (três) números (cada número corresponde a um lado do triângulo), verifique e escreva se os 3
# (três) números formam um triângulo (a soma de dois lados não pode ser menor que o terceiro lado). Se
# formam, verifique se formam um triângulo equilátero (3 lados iguais), isósceles (2 lados iguais) ou
# escaleno (3 lados diferentes). Não existe lado com tamanho 0 (zero).

def eh_triangulo(lado1,lado2,lado3):
    if lado1 == 0 or lado2 == 0 or lado3 == 0:
        return 'Não existe lad 0 em triângulo'
    elif (lado1 + lado2 > lado3) and (lado2 + lado3 > lado1) and (lado1 + lado3 > lado2):
        return True
    
    return False

def tipo_de_triangulo(lado1,lado2,lado3):
    if lado1 == lado2 and lado2 == lado3:
        return 'Equilátero'
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        return 'Isósceles'
    
    return 'Escaleno'
    
def main():
    lado1 = obter_numero_inteiro('Digite o primeiro Lado: ')
    lado2 = obter_numero_inteiro('Digite o segundo Lado: ')
    lado3 = obter_numero_inteiro('Digite o terceiro Lado: ')

    triangulo = eh_triangulo(lado1,lado2,lado3)
    if triangulo == True:
        print('É um triângulo')
        print(f'Esse triângulo é um {tipo_de_triangulo(lado1,lado2,lado3)}')
    elif triangulo == False:
        print('Não é um triângulo')
    else:
        print(triangulo)

if __name__ == '__main__':
    main()