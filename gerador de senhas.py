import random
import string

def gerar_senha(tamanho=7):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

tamanho_da_senha = 10
senha = gerar_senha(tamanho_da_senha)
print("nova senha gerada:",senha)



