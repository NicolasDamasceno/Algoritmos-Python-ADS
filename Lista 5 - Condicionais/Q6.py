from in_onputs import obter_numero_inteiro
# 6. Leia 3 (três) números (cada número corresponde a um ângulo interno do triângulo), verifique e escreva
# se os 3 (três) números formam um triângulo (a soma dos ângulos internos é igual a 180o). Se formam,
# verifique se formam um triângulo acutângulo (3 ângulos < 90o), retângulo (1 ângulo = 90o) ou
# obtusângulo (1 ângulo > 90o). Não existe ângulo com tamanho 0o (zero grau).

def eh_triangulo(ang1,ang2,ang3):
    if ang1 == 0 or ang2 == 0 or ang3 == 0:
        return 'Não existe ângulo 0 em triângulo'
    return ang1 + ang2 + ang3 == 180

def tipo_de_triangulo(ang1,ang2,ang3):
    if ang1 < 90 and ang2 < 90 and ang3 < 90:
        return 'Acutângulo'
    elif ang1 == 90 or ang2 == 90 or ang3 == 90:
        return 'Retângulo'
    elif ang1 > 90 or ang2 > 90 or ang3 > 90:
        return 'Obtusângulo'
    
def main():
    ang1 = obter_numero_inteiro('Digite o primeiro Ângulo: ')
    ang2 = obter_numero_inteiro('Digite o segundo Ângulo: ')
    ang3 = obter_numero_inteiro('Digite o terceiro Ângulo: ')

    triangulo = eh_triangulo(ang1,ang2,ang3)
    if triangulo == True:
        print('É um triângulo')
        print(f'Esse triângulo é um {tipo_de_triangulo(ang1,ang2,ang3)}')
    elif triangulo == False:
        print('Não é um triângulo')
    else:
        print(triangulo)

if __name__ == '__main__':
    main()