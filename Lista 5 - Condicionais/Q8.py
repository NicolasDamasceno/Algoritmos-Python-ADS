from in_onputs import obter_numero_inteiro
# 8. Leia data atual (dia, mês e ano) e data de nascimento (dia, mês e ano) de uma pessoa, calcule e escreva
# sua idade exata (em anos).
def calcular_idade_anos(dia_atual, mes_atual, ano_atual, dia_nasc, mes_nas, ano_nasc):
    anos  = ano_atual - ano_nasc
    if mes_atual < mes_nas:
        anos -= 1
        return anos
    elif mes_atual == mes_nas and dia_atual < dia_nasc:
        anos -= 1
        return anos
    
    return anos

def main():
    dia_atual = obter_numero_inteiro('Digite o dia atual: ')
    mes_atual = obter_numero_inteiro('Digite o mês atual: ')
    ano_atual = obter_numero_inteiro('Digite o ano atual: ')

    dia_nasc = obter_numero_inteiro('Digite o dia de nascimento: ')
    mes_nasc = obter_numero_inteiro('Digite o mês do nascimento: ')
    ano_nasc = obter_numero_inteiro('Digite o ano do nascimento: ')

    print(f'A sua idade é {calcular_idade_anos(dia_atual, mes_atual, ano_atual, dia_nasc, mes_nasc, ano_nasc)} anos')

if __name__ == '__main__':
    main()
    