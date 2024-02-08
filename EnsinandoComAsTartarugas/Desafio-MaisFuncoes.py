from turtle import *

bgcolor("Black")


def desenhar_triangulo(lado):
    color("Orange")
    begin_fill()
    for i in range(3):
        forward(lado)
        left(120)
    end_fill()


def desenhar_quadrado(lado):
    color("cyan")
    begin_fill()
    for i in range(4):
        forward(lado)
        left(90)
    end_fill()


def main():
    comprimento_lado_triangulo = 120
    comprimento_lado_quadrado = 150

    speed(1)

    desenhar_triangulo(comprimento_lado_triangulo)
    right(90)
    penup()
    forward(100)
    pendown()
    desenhar_quadrado(comprimento_lado_quadrado)
    hideturtle()

    done()


if __name__ == '__main__':
    main()
