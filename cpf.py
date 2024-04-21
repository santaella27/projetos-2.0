def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))  # Remove caracteres não numéricos do CPF
    if len(cpf) != 11:  # Verifica se o CPF tem 11 dígitos
        return False
    
    # Calcula o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    primeiro_digito = (soma * 10) % 11
    if primeiro_digito == 10:
        primeiro_digito = 0
    
    # Verifica se o primeiro dígito verificador está correto
    if primeiro_digito != int(cpf[9]):
        return False
    
    # Calcula o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    segundo_digito = (soma * 10) % 11
    if segundo_digito == 10:
        segundo_digito = 0
    
    # Verifica se o segundo dígito verificador está correto
    if segundo_digito != int(cpf[10]):
        return False
    
    return True

# Exemplo de uso:
cpf_usuario = input("Digite o CPF (apenas números): ")
if validar_cpf(cpf_usuario):
    print("CPF Válido.")
else:
    print("CPF Inválido.")
                

