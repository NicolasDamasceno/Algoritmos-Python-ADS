from in_onputs import obter_numero_inteiro
# 10. Leia uma data (dia, mês e ano), verifique e escreva se a data é ou não válida.

def validar_data(dia, mes, ano):
    if  1 <= mes <= 12 and 1 <= dia <= 30 and 0 < ano:
        return True

    return False 

def main():
    dia = obter_numero_inteiro('Digite um dia: ')
    mes = obter_numero_inteiro('Digite um mes, número: ')
    ano = obter_numero_inteiro('Digite um ano: ')

    if validar_data(dia, mes, ano):
        print(f'A data {dia}/{mes}/{ano} é válida')
    else: 
        print(f'A data {dia}/{mes}/{ano} não é válida...')
        
if __name__ == '__main__':
    main()