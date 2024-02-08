# Dicionário de nomes e senhas
passwordDictionary = {
    "alice": "12345",
    "leo": "password123",
    "arthur": "qwerty"
}

print("Programa super secreto")
print("=====================")

# Contador de tentativas de login
loginAttempts = 0

# Loop para solicitar nome de usuário e senha
while loginAttempts < 3:
    name = input("Nome: ")
    password = input("Senha: ")

    if name in passwordDictionary and password == passwordDictionary[name]:
        print("Login bem-sucedido!")
        print("BEM-VINDO PROGRAMADOR")
        break
    else:
        print("Nome de usuário ou senha incorretos. Tente novamente.")
        loginAttempts += 1

if loginAttempts == 3:
    print("Número máximo de tentativas de login excedido. Conta bloqueada.")
