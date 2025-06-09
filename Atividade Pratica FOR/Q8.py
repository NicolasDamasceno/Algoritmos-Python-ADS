def main():
    receitas = {}
    maior_receita = {"descricao" : '', "valor" : 0}
    valor_total_receitas = 0
    qtd_receitas = int(input('Quantidades de Receitas: '))

    for receita in (1,qtd_receitas+1,1):
        descricao = input(f'Descrição da Receita {receita}: ')
        valor = float(input(f'(R$)Valor da Receita {receita}: '))
        if valor > maior_receita.get("valor"):
            maior_receita.update({"descricao": descricao, "valor" : valor})
        valor_total_receitas += valor
        receitas.update({descricao : valor})

    despesas = {}
    maior_despesas = {"descricao" : '', "valor" : 0}
    valor_total_despesas = 0
    qtd_despesas = int(input('Quantidades de Despesas: '))

    for despesa in (1, qtd_despesas + 1, 1):
        descricao = input(f'Descrição da Despesa {despesa}: ')
        valor = float(input(f'(R$)Valor da Despesa {despesa}: '))
        if valor > maior_despesas.get("valor"):
            maior_despesas.update({"descricao" : descricao, "valor" : valor})
        valor_total_despesas += valor
        despesas.update({descricao : valor})

    saldo = valor_total_receitas - valor_total_despesas

    resultados = f'''
    --- Caixa do Mês ---
    Total de Receitas: R${valor_total_receitas:0.2f}
    Total de Despesas: R${valor_total_despesas:0.2f}
    Saldo: R${saldo:0.2f}
    ----------------------------------------------------------
    Maior Receita do Mês: {maior_receita.get("descricao")}
    Valor da Receita: {maior_receita.get("valor"):0.2f}
    ----------------------------------------------------------
    Maior Despesa do Mês: {maior_despesas.get("descricao")}
    Valor da Despesa: {maior_despesas.get("valor"):0.2f}
    '''
    print(resultados)

if __name__ == '__main__':
    main()

