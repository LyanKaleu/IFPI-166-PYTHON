print("SUA IDADE EM DIAS!")
print("Informe sua idade expressa em anos, meses e dias")
anos = int(input("-> ANOS: "))
meses = int(input("-> MESES: "))
dias = int(input("-> DIAS: "))

anos_em_dias = anos * 365
meses_em_dias = meses * 30

idade_em_dias = anos_em_dias + meses_em_dias + dias
print(f"\n\nEstá é a sua idade convertida: {idade_em_dias} DIAS!!")
