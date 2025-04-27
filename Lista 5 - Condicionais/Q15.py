from in_onputs import obter_numero_inteiro, obter_numero_real
# 15. Leia a quantidade de horas aula dadas por dois professores e o valor por hora recebido por cada um.
# Escreva na tela qual dos professores tem salário total maior.

def calcular_salario(horas,valor_horas):
    return (valor_horas * horas)

def main():
    horas_prof1 = obter_numero_inteiro('Digite a quantidade de horas do Professor 1: ')
    valor_hora_prof1 = obter_numero_real('Digite o valor do Professor 1: ')

    horas_prof2 = obter_numero_inteiro('Digite a quantidade de horas do Professor 2: ')
    valor_hora_prof2 = obter_numero_real('Digite o valor do Professor 2: ')

    salario_prof1 = calcular_salario(horas_prof1, valor_hora_prof1)
    salario_prof2 = calcular_salario(horas_prof2, valor_hora_prof2)
    print(f'Salário do Professor 1: {salario_prof1:0.2f}')
    print(f'Salário do Professor 2: {salario_prof2:0.2f}')

    if salario_prof1 > salario_prof2:
        print('O salário do Professor 1 é o maior')
    else:
        print('O salário do Professor 2 é o maior')
        
if __name__ == '__main__':
    main()