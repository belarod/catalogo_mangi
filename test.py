import re

def validar_senha(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$'
    return bool(re.match(pattern, password))
senha = 'trUta123'
print(validar_senha(senha))