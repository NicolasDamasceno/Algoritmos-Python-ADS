from in_onputs import obter_numero_real, obter_numero_inteiro
# Exercício 5: Calculadora de Descontos
# Descrição do Problema:
# Crie um programa para uma loja que calcule o preço final de um produto com base
# em regras de desconto:
# ● Compras acima de R$ 500,00: 15% de desconto
# ● Compras entre R$ 200,00 e R$ 500,00: 10% de desconto
# ● Compras entre R$ 100,00 e R$ 199,99: 5% de desconto
# ● Cliente VIP: desconto adicional de 5% (acumulativo)
# ● Cliente Aniversariante: desconto adicional de 3% (acumulativo)

def desconto_base(valor_compra):
    if 100 <= valor_compra < 200:
        return (valor_compra * 0.05), 5
    elif 200 <= valor_compra < 500:
        return (valor_compra * 0.10), 10
    elif valor_compra >= 500:
        return (valor_compra * 0.15), 15
    
    return 0, 0

def desconto_vip(valor_compra):
    return (valor_compra * 0.05)

def desconto_aniversariante(valor_compra):
    return (valor_compra * 0.03)

def main():
    print('------ Loja do Pato ------')
    valor_compra = obter_numero_real('Digite o valor da compra em R$: ')
    desconto_inicial, porcentagem = desconto_base(valor_compra)
    if desconto_inicial == 0:
        print(f'Desconto base não aplicado, valor menor que R$100')
        aniversario = obter_numero_inteiro('Aniversário do Cliente? 1-Y / 2-N: ')
        if aniversario == 1:
            valor_compra -= desconto_aniversariante(valor_compra)
            print(f'Valor com desconto de 3% de aniversario: R${valor_compra}')
            vip = obter_numero_inteiro('Cliente VIP? 1-Y / 2-N: ')
            if vip == 1:
                valor_compra -= desconto_vip(valor_compra)
                print(f'Valor Final com desconto Vip de 5% e Anivesário 3%: R${valor_compra}')
            elif vip == 2:
                 print(f'Valor Final com desconto Anivesário 3%: R${valor_compra}')
        elif aniversario == 2:
            vip = obter_numero_inteiro('Cliente VIP? 1-Y / 2-N: ')
            if vip == 1:
                valor_compra -= desconto_vip(valor_compra)
                print(f'Valor Final com desconto Vip de 5% : R${valor_compra}')
            elif vip == 2:
                 print(f'Valor Final sem desconto: R${valor_compra}')
    
    elif desconto_inicial > 0:
        valor_compra -= desconto_inicial
        print(f'Desconto Base {porcentagem}%, valor R${valor_compra}')
        aniversario = obter_numero_inteiro('Aniversário do Cliente? 1-Y / 2-N: ')
        if aniversario == 1:
            valor_compra -= desconto_aniversariante(valor_compra)
            print(f'Valor com mais 3% de aniversario: R${valor_compra}')
            vip = obter_numero_inteiro('Cliente VIP? 1-Y / 2-N: ')
            if vip == 1:
                valor_compra -= desconto_vip(valor_compra)
                print(f'Valor Final com desconto base {porcentagem}%, Vip de 5% e Anivesário 3%: R${valor_compra}')
            elif vip == 2:
                 print(f'Valor Final com desconto base {porcentagem}% e Anivesário 3%: R${valor_compra}')
        elif aniversario == 2:
            vip = obter_numero_inteiro('Cliente VIP? 1-Y / 2-N: ')
            if vip == 1:
                valor_compra -= desconto_vip(valor_compra)
                print(f'Valor Final com desconto base {porcentagem}% e Vip de 5% : R${valor_compra}')
            elif vip == 2:
                 print(f'Valor Final com desconto base {porcentagem}%: R${valor_compra}')

if __name__ == '__main__':
    main()