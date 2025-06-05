alimentos = {
    "arroz" : {"calorias": 130, "proteinas": 2.7},
    "frango" : {"calorias": 165, "proteinas": 31},
    "feijao" : {"calorias": 80, "proteinas": 3.4},
    "peixe" : {"calorias": 130, "proteinas": 28},
    "bife" : {"calorias": 195, "proteinas": 45},
    "alface" : {"calorias": 37, "proteinas": 1.1},
    "milho" : {"calorias": 36, "proteinas": 4.7},
    "pequi" : {"calorias": 38, "proteinas":0.9},
    "batata" : {"calorias": 80, "proteinas": 3.2},
    "cenoura" : {"calorias": 30, "proteinas": 2.4}
}

def main():
    pessoas = int(input('Pessoas: '))
    consumo_pessoas = {}
    menor_calorias_pessoa = 10000
    pessoa_menor = 0
    maior_calorias_pessoa = 0
    pessoa_maior = 0

    for pessoa in range(1, pessoas + 1, 1):
        qtd_alimentos = int(input((f'(Pessoa {pessoa})Digite a quantidade de alimentos: ')))
        calorias = 0
        proteinas = 0
        for alimento in range(1, qtd_alimentos + 1, 1):
            nome_alimento = input(f'(Pessoa {pessoa})Digite o nome do alimento: ')
            while nome_alimento not in alimentos:
                print('Nome inválido...')
                nome_alimento = input('Digite o nome do alimento: ')
            calorias += alimentos[nome_alimento].get("calorias")
            proteinas += alimentos[nome_alimento].get("proteinas")

        if calorias >= maior_calorias_pessoa: 
            maior_calorias_pessoa = calorias
            pessoa_maior = pessoa
        if calorias <= menor_calorias_pessoa:
            menor_calorias_pessoa = calorias
            pessoa_menor = pessoa

        consumo_pessoas.update({pessoa : {"calorias": calorias, "proteinas": proteinas}})

    for consumo in consumo_pessoas:
        print(f'--- Consumo da Pessoa {consumo} ---')
        print(f'Calorias: {consumo_pessoas[consumo].get("calorias")}')
        print(f'Proteínas: {consumo_pessoas[consumo].get("proteinas"):0.1f}\n')
    
    print(f'Pessoa {pessoa_maior} teve maior consumo calórico de {maior_calorias_pessoa}')
    print(f'Pessoa {pessoa_menor} teve menor consumo calórico de {menor_calorias_pessoa}')

if __name__ == '__main__':
    main()
