from in_onputs import obter_numero_inteiro
# 20. Leia a medida de um ângulo (entre 0 e 360°) e escreva o quadrante (primeiro, segundo, terceiro ou
# quarto) em que o ângulo se localiza.
def quadrantes_angulo(ang):
    if 0 <= ang <= 90:
        return f'O Ângulo {ang} está no Quadrante I'
    elif 90 < ang <= 180:
        return f'O Ângulo {ang} está no Quadrante II'
    elif 180 < ang <= 270:
        return f'O Ângulo {ang} está no Quadrante III'
    elif 270 < ang <= 360:
        return f'O Ângulo {ang} está no Quadrante IV'
    
    return 'Valor de Ângulo Inválido'

def main():
    ang = obter_numero_inteiro('Digite o valor do Ângulo em graus: ')
    print(quadrantes_angulo(ang))
if __name__ == '__main__':
    main()