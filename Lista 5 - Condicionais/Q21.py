from in_onputs import obter_numero_real
# 21. Realize arredondamentos de números utilizando a regra usual da matemática: se a parte fracionaria for
# maior do que ou igual a 0,5, o numero é arredondado para o inteiro imediatamente superior, caso
# contrario, é arredondado para o inteiro imediatamente inferior.
def arrendodamento(num):
    parte_inteira = int(num)
    parte_fracionaria = num - parte_inteira

    if parte_fracionaria >= 0.5:
        return parte_inteira + 1
    return parte_inteira
    
def main():
    num = obter_numero_real('Digite um número decimal: ')
    print(f'O arreedondamento de {num} é {arrendodamento(num)}')

if __name__ == '__main__':
    main()