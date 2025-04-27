from in_onputs import obter_numero_inteiro
# Exercício 1: Verificador de Ano Bissexto
# Descrição do Problema:
# Crie um programa que determine se um ano é bissexto ou não. Um ano é bissexto
# se for divisível por 4, exceto quando é divisível por 100 mas não por 400.
def verificar_ano_bissexto(ano):
    if ano % 4 == 0 and ano % 100 != 0:
        return True
    
    elif ano % 400 == 0:
        return True
    
    return False

def main():
    ano = obter_numero_inteiro('Digite o ano para saber se ele é bissexto: ')

    bissexto = verificar_ano_bissexto(ano)
    if bissexto:
        print(f'O ano {ano} é Bissexto!')
    else:
        print(f'O ano {ano} não é Bissexto...')

if __name__ == '__main__':
    main()