from in_onputs import obter_numero_inteiro
# 26. Leia os 3 (três) lados de um triângulo e identifique sua hipotenusa e seus catetos.
def triangulo(lado1, lado2, lado3):
    hipotenusa = lado1
    if lado1 > lado2 and lado1 > lado3:
        return hipotenusa, lado2, lado3
    elif lado2 > lado1 and lado2 > lado3:
        hipotenusa = lado2
        return hipotenusa, lado1, lado3
    elif lado3 > lado1 and lado3 > lado2:
        hipotenusa = lado3
        return hipotenusa, lado1, lado2
    
def main():
    l1 = obter_numero_inteiro('Digite o primeiro lado do triângulo: ')
    l2 = obter_numero_inteiro('Digite o segundo lado do triângulo: ')
    l3 = obter_numero_inteiro('Digite o terceiro lado do triângulo: ')

    hipotenusa, cateto1, cateto2 = triangulo(l1,l2,l3)
    print(f'Triângulo {l1}, {l2}, {l3}\nHipotenusa: {hipotenusa}\nCateto 1: {cateto1}\nCateto 2: {cateto2}')
if __name__ == '__main__':
    main()