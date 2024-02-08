from random import *

print("Gerador de Cumprimentos")
print("---------------------")

ajetivos = ["maravilhoso", "acima da média",
            "excelente", "magnífico", "excepcional",
            "fantástico", "incrível", "notável"]

hobbies = ["andar de bicicleta", "programar", "fazer chá",
           "pintar", "cozinhar", "jogar videogame", "dançar",
           "fotografar"]

nome = input("Qual é o seu nome?: ")
print("Aqui está o seu cumprimento", nome, ":")

# Obtém um item aleatório de ambas as listas e adiciona-os ao cumprimento
print(nome, "você é", choice(ajetivos), "em", choice(hobbies))

cumprimentos = ["Excelente trabalho. Realmente muito bem feito.",
                "Suas habilidades de programação são muito, muito boas.",
                "Você é um humano excelente.",
                "Seu talento é verdadeiramente inspirador.",
                "Sua criatividade é impressionante.",
                "Parabéns pelo seu excelente desempenho.",
                "Você demonstra uma dedicação notável em tudo o que faz."]

# Imprime um item aleatório da lista 'cumprimentos'
print(choice(cumprimentos))
print("De nada!")
