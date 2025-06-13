from str_utils import avoids, uses_only, uses_all, to_lower, is_abecedarian

def tamanho_palavras():
    tamanho = int(input('Tamanhos das Palavras: '))
    arquivo = open("Atividades Strigns/br-sem-acentos.txt")
    qtd_palavras_tamanho = 0
    palavras_total = 0

    for linha in arquivo:
        palavra = linha.strip()
        if len(palavra) >= tamanho:
            qtd_palavras_tamanho += 1
            print(palavra)
        palavras_total += 1
    
    print('------------------------------------------------')
    percentual = (qtd_palavras_tamanho / palavras_total) * 100
    print(f'Filtro {tamanho}: {qtd_palavras_tamanho}\nPercentual: {percentual:0.2f}%')


def palavra_proibida(caractere,palavra):
    for letra in palavra:
        if letra == caractere:
            return False
        
    return True


def palavra_sem_letra():
    letra = input('Letra: ')
    arquivo = open("Atividades Strigns/br-sem-acentos.txt")
    qtd_palavras_sem_letra = 0
    palavras_total = 0
    for linha in arquivo:
        palavra = linha.strip()
        if palavra_proibida(letra,palavra):
            qtd_palavras_sem_letra += 1
            print(palavra)
        palavras_total += 1
    
    print('------------------------------------------------')
    percentual = (qtd_palavras_sem_letra/palavras_total) * 100
    print(f'Filtro {letra}: {qtd_palavras_sem_letra}\nPercentual: {percentual:0.2f}%')


def conjuto_letras_proibidas(): 
    qtd_palavras_sem_letra = 0
    palavras_total = 0
    letras = input('Letras proibidas: ')
    arquivo = open("Atividades Strigns/br-sem-acentos.txt") 
    for linha in arquivo:
        palavra = linha.strip()
        if avoids(palavra, letras):
            print(palavra)
            qtd_palavras_sem_letra += 1       
        palavras_total += 1

    percentual = (qtd_palavras_sem_letra/palavras_total) * 100
    print(f'Filtro {letras}: {qtd_palavras_sem_letra}\nPercentual: {percentual:0.2f}%')


def palavras_letras_permitidas():
    palavras_filtradas = 0
    palavras_total = 0
    letras_permitidas = input('Letras permitidas: ')
    arquivo = open("Atividades Strigns/br-sem-acentos.txt")

    for linha in arquivo:
        palavra = linha.strip()
        if uses_only(palavra, letras_permitidas):
            print(palavra)
            palavras_filtradas += 1
        palavras_total += 1
    
    percentual = (palavras_filtradas/palavras_total) * 100
    print(f'Filtro {letras_permitidas}: {palavras_total}\nPercentual: {percentual:0.2f}%')

def palavras_letras_obrigatorias():
    palavras_filtradas = 0
    palavras_total = 0
    letras_obrigatorias = input('Letras obrigatórias: ')
    arquivo = open("Atividades Strigns/br-sem-acentos.txt")

    for linha in arquivo:
        palavra = linha.strip()
        if uses_all(palavra, letras_obrigatorias):
            print(palavra)
            palavras_filtradas += 1
        palavras_total += 1
    
    percentual = (palavras_filtradas/palavras_total) * 100
    print(f'Filtro {letras_obrigatorias}: {palavras_total}\nPercentual: {percentual:0.2f}%')

def palavras_ordem_alfabetica():
    palavras_filtradas = 0
    palavras_total = 0
    arquivo = open("Atividades Strigns/br-sem-acentos.txt")

    for linha in arquivo:
        palavra = to_lower(linha.strip())
        if is_abecedarian(palavra):
            print(palavra)
            palavras_filtradas += 1
        palavras_total += 1
    
    percentual = (palavras_filtradas/palavras_total) * 100
    print(f'Filtro: {palavras_total}\nPercentual: {percentual:0.2f}%')

        


def main():
    menu = '''
    ---- Word Play ----
    1 - Palavras com tamanhos N
    2 - Palavras sem Letra Proibida
    3 - Letras Proibidas
    4 - Palavras com Letras Permitidas
    5 - Palavras com Letras Obrigátorias
    6 - Palavras em ordem alfabética

    0 - Sair do Sistema
    ---> '''
    opcao = int(input(menu))
    while opcao != 0:
        if opcao == 1:
            tamanho_palavras()
            
        elif opcao == 2:
            palavra_sem_letra()

        elif opcao == 3:
            conjuto_letras_proibidas()
    
        elif opcao == 4:
            palavras_letras_permitidas()
        
        elif opcao == 5:
            palavras_letras_obrigatorias()

        elif opcao == 6:
            palavras_ordem_alfabetica()
        
        opcao = int(input('--> '))
        
    print('fim...')
    

if __name__ == '__main__':
    main()