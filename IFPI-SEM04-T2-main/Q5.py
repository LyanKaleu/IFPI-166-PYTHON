print("CALCULADORA DE MÉDIA ESCOLAR")
print("\t-Informe as suas 3 notas:")
nota1 = float(input("-> Nota 1: "))
nota2 = float(input("-> Nota 2: "))
nota3 = float(input("-> Nota 3: "))

media_ponderada = ((nota1*2) + (nota2*3) + (nota3*5)) / 10
print(f"\n\nSua média é: {media_ponderada}")
