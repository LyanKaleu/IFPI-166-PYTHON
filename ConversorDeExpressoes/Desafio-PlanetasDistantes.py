distancias_planetas = {
    "Mercúrio": 77300000,
    "Vênus": 38000000,
    "Marte": 54600000,
    "Júpiter": 628000000,
    "Saturno": 1200000000,
    "Urano": 2600000000,
    "Netuno": 4300000000
}

planeta = input("Digite um planeta: ")

if planeta in distancias_planetas:
    print(f"{planeta} está a {distancias_planetas[planeta]}km da Terra")
else:
    print("Planeta inválido!")
