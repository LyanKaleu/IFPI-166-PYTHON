n1 = float(input("Digite para o primeiro número: "))
n2 = int(input("Digite para o segundo número: "))

soma = n1 + n2
concatenacao = str(n1) + str(n2)
multiplicacao_numeros = n1 * n2
multiplicacao_strings = str(n1) * int(n2)
divisao_normal = n1 / n2
divisao_inteira = n1 // n2
exponenciacao = n1 ** n2
resto = n1 % n2

print(f"\n\n-> SOMA: {soma}")
print(f"-> CONCATENAÇÃO DAS STRINGS: {concatenacao}")
print(f"-> MULTIPLICAÇÃO: {multiplicacao_numeros}")
print(f"-> MULTIPLICAÇÃO COMO STRINGS: {multiplicacao_strings}")
print(f"-> DIVISÃO COM PONTO FLUTUANTE: {divisao_normal}")
print(f"-> DIVISÃO INTEIRA: {divisao_inteira}")
print(f"-> EXPONENCIAÇÃO: {exponenciacao}")
print(f"-> MÓDULO: {resto}")
