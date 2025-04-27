from in_onputs import obter_numero_inteiro, obter_numero_real
# Exercício 2: Calculadora de IMC com Classificação
# Descrição do Problema:
# Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma
# pessoa e forneça sua classificação de acordo com a tabela:
# ● Abaixo de 18.5: Abaixo do peso
# ● Entre 18.5 e 24.9: Peso normal
# ● Entre 25.0 e 29.9: Sobrepeso
# ● Entre 30.0 e 34.9: Obesidade grau 1
# ● Entre 35.0 e 39.9: Obesidade grau 2
# ● Acima de 40.0: Obesidade grau 3
# IMC = peso / (altura x altura)

def calcular_imc(peso, altura):
    return (peso / (altura * altura))

def classificar_imc(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif 18.5 <= imc < 25:
        return 'Peso normal'
    elif 25 <= imc < 30:
        return 'Sobrepeso'
    elif 30 <= imc < 35:
        return 'Obesidade grau 1'
    elif 35 <= imc < 40:
        return 'Obesidade grau 2'
    
    return 'Obesidade grau 3'

def main():
    peso = obter_numero_inteiro('Digite o peso em Kg: ')
    altura = obter_numero_real('Digite a altura em m: ')

    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)

    print(f'IMC: {imc:0.1f}\nClassificação do IMC: {classificacao}')

if __name__ == '__main__':
    main()