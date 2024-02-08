from turtle import *


# Uma função para desenhar uma estrela
# 'def' significa 'define'
def drawStar():
    pendown()
    begin_fill()
    for side in range(5):
        left(144)
        forward(50)
    end_fill()
    penup()


# Isso vai desenhar uma estrela cinza clara em um fundo azul escuro
color("WhiteSmoke")
bgcolor("MidnightBlue")

# Use a função para desenhar estrelas!
drawStar()
forward(100)
drawStar()
left(120)
forward(150)
drawStar()

hideturtle()
done()
