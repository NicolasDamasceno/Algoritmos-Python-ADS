from in_onputs import obter_numero_real, obter_numero_inteiro
# 19. Leia a altura (em metros) e peso (em Kg) de uma pessoa, em seguida calcule o índice de massa corpórea
# (IMC = peso / altura2). Ao final, escreva se a pessoa está com peso normal (IMC abaixo de 25), obeso
# (IMC entre 25 e 30) ou obesidade mórbida (IMC acima de 30).

def calcular_imc(peso,altura):
    return peso / (altura ** altura)

def main():
    peso = obter_numero_inteiro('Digite o peso em KG: ')
    altura = obter_numero_real('Digite a altura em M: ')
    imc = calcular_imc(peso,altura)

    if imc < 25:
        print(f'IMC: {imc:0.1f}\nSituação: Peso Normal')
    elif 25 <= imc <= 30:
        print(f'IMC: {imc:0.1f}\nSituação: Obeso')
    elif imc > 30:
        print(f'IMC: {imc:0.1f}\nSituação: Obesidade Mórbida')

if __name__ == '__main__':
    main()
