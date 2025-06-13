def avoids(palavra, letras_proibidas):
    for letra in palavra:
        if contem_caractere(letras_proibidas, letra):
            return False
    
    return True

def contem_caractere(palavra, caractere):
    for letra in palavra:
        if letra == caractere:
            return True
        
    return False

def uses_only(palavra, letras_permitidas):
    for letra in palavra:
        if not contem_caractere(letras_permitidas, letra):
            return False
    
    return True

def uses_all(palavra, letras_obrigatorias):
    for letra in letras_obrigatorias:
        if not contem_caractere(palavra, letra):
            return False
        
    return True

def is_upper_letter(char):
  return ord(char) >= 65 and ord(char) <= 90

def to_lower(texto):
    novo_texto = ''
    for char in texto:
        if is_upper_letter(char):
            novo_texto += chr(ord(char) + 32)
        else:
            novo_texto += char

    return novo_texto

def is_abecedarian(palavra):
    anterior = palavra[0]

    for i in range(1, len(palavra)):
        atual = palavra[i]
        if anterior> atual:
            return False
        
        anterior = atual

    return True