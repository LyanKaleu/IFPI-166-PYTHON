# Passo 3: Variáveis
print("Em que ano você nasceu?")
nascimento = input()
nascimento = int(nascimento)
idadeEm2025 = 2025 - nascimento
print("Em 2025 você terá", idadeEm2025, "anos!\n\n")


# Desafio 1
print("Desafio: O ano 3000!")
ano_nascimento = int(input("Em que ano você nasceu?"))
ano_futuro = int(input("Para qual ano você quer saber sua idade?"))
print(f"No ano {ano_futuro} você terá {ano_futuro-ano_nascimento} anos!\n\n")


# Desafio 2
print("Desafio: Sua idade em anos de cachorro")
idade = int(input("Quantos anos você tem?"))
print(f"Se você fosse um cachorro, você teria {idade * 7} anos!!")
print("  '0'______'")
print("      || ||")
