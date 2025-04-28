from in_onputs import obter_numero_real
# 16. Leia duas notas de um aluno e escreva na tela a palavra “Aprovado” se a média das duas notas for maior
# ou igual a 7,0. Caso a média seja inferior a 7,0, o programa deve ler a nota do exame e calcule a média
# final. Se esta média for maior ou igual a 5,0, o programa deve escreva “Aprovado”, caso contrário deve
# escreva “Reprovado”.

def calcular_media(nota1,nota2):
    return (nota1 + nota2) / 2

def classificar_media(media):
    if media >= 7:
        return 'Aprovado', media
    elif media < 7:
        nota_final = obter_numero_real('Digite a nota do exame final: ')
        media_final = calcular_media(media, nota_final)
        if media_final >= 5: 
            return 'Aprovado', media_final
        return 'Reprovado', media_final
    
def main():
    nota1 = obter_numero_real('Digite a nota 1: ')
    nota2 = obter_numero_real('Digite a nota 2: ')
    media = calcular_media(nota1,nota2)
    classificacao, media_final = classificar_media(media)

    print(f'\nMédia: {media_final:0.1f}\nSituação: {classificacao}')

if __name__ == '__main__':
    main()