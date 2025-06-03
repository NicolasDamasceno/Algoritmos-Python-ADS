from in_onputs import obter_numero_real
# 4. Leia 2 (duas) notas parciais de um aluno, calcule a média e escreva a mensagem:
# o "Aprovado", se a média alcançada for maior ou igual a sete;
# o "Reprovado", se a média for menor do que sete;
# o "Aprovado com Distinção", se a média for igual a dez

def calcular_media(nota1,nota2,nota3):
    return (nota1 + nota2 + nota3) / 3

def classificacao_media(media):
    if media == 10:
        return 'Aprovado com Distinção'
    elif media >= 7:
        return 'Aprovado'
    return 'Reprovado'
    
def main():
    nota1 = obter_numero_real('Digite a primeira nota: ')
    nota2 = obter_numero_real('Digite a segunda nota: ')
    nota3 = obter_numero_real('Digite a terceira nota: ')

    media = calcular_media(nota1,nota2,nota3)
    
    print(f'Média: {media:0.1f}\nClassificação: {classificacao_media(media)}')

if __name__  == '__main__':
    main()