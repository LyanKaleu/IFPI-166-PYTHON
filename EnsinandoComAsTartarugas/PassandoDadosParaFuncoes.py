from turtle import *


# Uma função para desenhar uma estrela de um tamanho específico e de uma cor específica
def drawStar(starSize, starColour):
    color(starColour)
    pendown()
    begin_fill()
    for side in range(5):
        left(144)
        forward(starSize)
    end_fill()
    penup()


# Isso vai desenhar um fundo azul escuro
bgcolor("MidnightBlue")

# Use a função para desenhar estrelas de tamanhos diferentes e de cores diferentes!
drawStar(50, "Red")
forward(100)
drawStar(30, "White")
left(120)
forward(150)
drawStar(70, "Green")

hideturtle()
done()
