from random import *

bigPlanets = ["júpiter", "saturno", "urano", "netuno"]
print(bigPlanets)
print(bigPlanets[0])
print(bigPlanets[1])
print(bigPlanets[2])
print(bigPlanets[3])

print("Gerador de Cumprimentos")
print("---------------------")

ajetivos = ["maravilhoso", "acima da média",
            "excelente"]

hobbies = ["andar de bicicleta", "programar", "fazer chá"]

nome = input("Qual é o seu nome?: ")
print("Aqui está o seu cumprimento", nome, ":")

# Obtém um item aleatório de ambas as listas e adiciona-os ao cumprimento
print(nome, "você é", choice(ajetivos), "em", choice(hobbies))

cumprimentos = ["Excelente trabalho. Realmente muito bem feito.",
                "Suas habilidades de programação são muito, muito boas.",
                "Você é um humano excelente."
                ]

# Imprime um item aleatório da lista 'cumprimentos'
print(choice(cumprimentos))
print("De nada!")
