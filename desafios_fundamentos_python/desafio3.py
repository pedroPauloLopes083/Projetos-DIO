import re

def validar_numero_telefone(numero):
    # Expressão regular para verificar o formato do número de telefone
    padrao = r"\(\d{2}\) 9\d{4}-\d{4}"

    # Verifica se o número corresponde ao padrão
    if re.match(padrao, numero):
        return "O número de telefone é válido."
    else:
        return "O número de telefone é inválido."

numero_telefone = input("") 

print(validar_numero_telefone(numero_telefone))
