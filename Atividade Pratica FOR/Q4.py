def aluguel_anual_recebido(aluguel, anos):
    return aluguel*(anos*12)


def roi(valor_recebido,investimento_inicial):
    return (valor_recebido - investimento_inicial) / investimento_inicial


def main():
    qtd_imoveis = int(input('Quantidade de imóveis: '))

    imoveis = {}
    imovel_maior_roi = {"imovel" : 0, "roi" : 0}
    imovel_maior_retorno = {"imovel" : 0, "retorno": 0}

    for imovel in range(1, qtd_imoveis + 1, 1):
        valor_compra = float(input(f'(R$)Valor de compra do Imóvel {imovel}: '))
        aluguel_mensal = float(input('(R$)Valor do aluguel: '))
        anos_aluguel = int(input('Anos de Aluguel do Imóvel: '))

        aluguel_total = aluguel_anual_recebido(aluguel_mensal,anos_aluguel)
        roi_imovel = roi(aluguel_total, valor_compra) * 100

        if roi_imovel > imovel_maior_roi.get("roi"):
            imovel_maior_roi.update({"imovel" : imovel, "roi" : roi_imovel})
        if aluguel_total > imovel_maior_retorno.get("retorno"):
            imovel_maior_retorno.update({"imovel" : imovel, "retorno" : aluguel_total})
    
        imoveis.update({imovel : {"pago": valor_compra, "recebido" : aluguel_total, "roi" : roi_imovel}})
        
    for imovel, valor in imoveis.items():
        print(f'---> Imóvel {imovel}')
        print(f'Valor Pago: R${imoveis[imovel].get("pago"):0.2f}')
        print(f'Valor Recebido do imóvel: R${imoveis[imovel].get("recebido"):0.2f}')
        print(f'ROI do Imóvel: {imoveis[imovel].get("roi"):0.2f}%\n')

    print(f'---- Imóvel com Maior ROI ----')
    print(f'Imóvel: {imovel_maior_roi.get("imovel")}')
    print(f'ROI: {imovel_maior_roi.get("roi")}%')
    print('-------------------------------------')
    print(f'$$$$ Imóvel com Maior Retorno $$$$')
    print(f'Imóvel: {imovel_maior_retorno.get("imovel")}')
    print(f'Maior Retorno: R${(imovel_maior_retorno.get("retorno")):0.2f}')


if __name__ == '__main__':
    main()