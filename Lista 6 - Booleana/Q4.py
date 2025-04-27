from in_onputs import obter_numero_real
# Exercício 4: Sistema de Notas Escolares
# Descrição do Problema:
# Desenvolva um programa que receba três notas de um aluno, calcule a média e
# determine sua situação com base nos critérios:
# ● Média >= 7.0: Aprovado
# ● Média entre 5.0 e 6.9: Recuperação
# ● Média < 5.0: Reprovado
# Adicionalmente, se o aluno tiver alguma nota igual a 0.0, ele estará
# automaticamente reprovado.
def validar_nota_0_10(nota1, nota2, nota3):
    if 0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10:
        return True
    return False

def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

def classificar_nota(media):
    if media < 5:
        return 'Reprovado'
    elif 5 <= media < 7:
        return 'Recuperação'
    return 'Aprovado'

def main():
    nota1 = obter_numero_real('Digite a nota 1 do aluno: ')
    nota2 = obter_numero_real('Digite a nota 2 do aluno: ')
    nota3 = obter_numero_real('Digite a nota 3 do aluno: ')
    
    notas_validadas = validar_nota_0_10(nota1,nota2,nota3)
    if notas_validadas:
        if nota1 == 0 or nota2 == 0 or nota3 == 0:
            print(f'Nota 1: {nota1}\nNota 2: {nota2}\nNota3: {nota3}\nSituação: Recuperação')
        else: 
            media = calcular_media(nota1,nota2,nota3)
            classificacao = classificar_nota(media)
            print(f'Nota 1: {nota1}\nNota 2: {nota2}\nNota3: {nota3}\nMédia: {media:0.1f}\nSituação: {classificacao}')
    else:
        print('As notas digitas não estão entre 0 e 10...')
if __name__ == '__main__':
    main()