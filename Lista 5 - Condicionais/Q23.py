from in_onputs import obter_numero_inteiro
# 23. Leia 2 datas (cada data é composta por 3 variáveis inteiras: dia, mês e ano) e escreva qual delas é a mais
# recente.

def data_recente(dia1, mes1, ano1, dia2, mes2, ano2):
    if ano1 > ano2:
        return f'{dia1}/{mes1}/{ano1} é a mais recente'
    elif ano1 < ano2:
        return f'{dia2}/{mes2}/{ano2} é a mais recente'
    else:
        if mes1 > mes2:
            return f'{dia1}/{mes1}/{ano1} é a mais recente'
        elif mes1 < mes2:
            return f'{dia2}/{mes2}/{ano2} é a mais recente'
        else: 
            if dia1 > dia2:
                return f'{dia1}/{mes1}/{ano1} é a mais recente'
            elif dia1 < dia2:
                return f'{dia2}/{mes2}/{ano2} é a mais recente'
            else: 
                return 'As datas são iguais'
            
def main():
    dia1 = obter_numero_inteiro('Digite o primeiro dia: ')
    mes1 = obter_numero_inteiro('Digite o primeiro mês: ')
    ano1 = obter_numero_inteiro('Digite o primeiro ano: ')

    dia2 = obter_numero_inteiro('Digite o segundo dia: ')
    mes2 = obter_numero_inteiro('Digite o segundo mês: ')
    ano2 = obter_numero_inteiro('Digite o segundo ano: ')

    print(data_recente(dia1,mes1,ano1,dia2,mes2,ano2))
if __name__ == '__main__':
    main()