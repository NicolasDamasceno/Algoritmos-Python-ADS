# 2. Leia uma letra, verifique se letra é "F" ou "M" e escreva F - Feminino, M - Masculino, Sexo Inválido.

def verificacao_letra(letra):
    if letra == 'F':
        return 'F - Feminino'
    elif letra == 'M':
        return 'M - Masculino'
    return 'Sexo inválido'

def main():
    letra = input('Digite F ou M: ').upper()
    print(verificacao_letra(letra))

if __name__ == '__main__':
    main()