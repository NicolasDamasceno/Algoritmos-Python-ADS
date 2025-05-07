from in_onputs import obter_numero_inteiro
# 28. Leia as coordenadas cartesianas (x e y) de 2 (dois) pontos no plano, que corresponderão a dois cantos de
# um retângulo. Baseado nisto, calcule e escreva a área deste retângulo. Lembre-se de que o valor da área
# não pode ser negativo.

def area_retangulo(x1, y1, x2, y2):
    base = abs(x2 - x1)
    altura = abs(y2 - y1)
    return base * altura

def main():
    x1 = obter_numero_inteiro('Digite o x1: ')
    y1 = obter_numero_inteiro('Digite o y1: ')
    x2 = obter_numero_inteiro('Digite o x2: ')
    y2 = obter_numero_inteiro('Digite o y2: ')

    print(f'A área do retângulo é {area_retangulo(x1,y1,x2,y2)}')
    
if __name__ == '__main__':
    main()