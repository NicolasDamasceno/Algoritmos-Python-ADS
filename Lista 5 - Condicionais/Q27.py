from in_onputs import obter_numero_inteiro
# 27. Determine a idade de uma pessoa, em anos, meses e dias, dadas a data (dia, mês e ano) do seu
# nascimento e a data (dia, mês e ano) atual.
def data_nascimento(dia_nasc,mes_nasc,ano_nasc,dia_at,mes_at,ano_at):
    ano = ano_at - ano_nasc
    mes = mes_at - mes_nasc
    dia = dia_at
    if mes_at < mes_nasc:
        ano -= 1
        mes = mes_nasc - mes_at
        return ano,mes,dia
    
    elif mes_at == mes_nasc and dia_at < dia_nasc:
        ano -= 1
        mes = mes_nasc
        return ano,mes,dia
    
    return ano,mes,dia

def main():
    dia_nasc = obter_numero_inteiro('Digite o seu dia de nascimento: ')
    mes_nasc = obter_numero_inteiro('Digite o seu mes de nascimento: ')
    ano_nasc = obter_numero_inteiro('Digite o seu ano de nascimento: ')

    dia_atual = obter_numero_inteiro('Digite o dia atual: ')
    mes_atual = obter_numero_inteiro('Digite o mes atual: ')
    ano_atual = obter_numero_inteiro('Digite o ano atual: ')

    ano, mes, dia = data_nascimento(dia_nasc,mes_nasc,ano_nasc,dia_atual,mes_atual,ano_atual)
    print(f'Você tem {ano} anos, {mes} meses, {dia} dias')

if __name__ == '__main__':
    main()