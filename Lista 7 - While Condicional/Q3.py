# 3. Leia uma letra e verifique se a letra digitada é vogal ou consoante.

def vogal_consoante(letra):
    if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
        return 'vogal'
    return 'consoante'

def main():
    letra = input('Digite uma letra qualquer: ').upper()
    print(f'A {letra} é uma {vogal_consoante(letra)}')

if __name__ == '__main__':
    main()