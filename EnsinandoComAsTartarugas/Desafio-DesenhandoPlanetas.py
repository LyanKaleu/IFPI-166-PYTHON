from turtle import *

bgcolor("Black")


def drawPlanet(raio, cor):
    begin_fill()
    color(cor)
    circle(raio)
    end_fill()


def drawMercurio():
    drawPlanet(20, "gray")


def drawVenus():
    drawPlanet(40, "yellow")


def drawTerra():
    drawPlanet(45, "blue")


def drawMarte():
    drawPlanet(35, "red")


def drawJupiter():
    drawPlanet(100, "orange")


def drawSaturno():
    color("goldenrod")
    begin_fill()
    circle(80)
    end_fill()

    color("brown")
    begin_fill()
    circle(80, 180)
    end_fill()


def drawUrano():
    drawPlanet(60, "lightblue")


def drawNetuno():
    drawPlanet(55, "blue")


def main():
    speed(5)

    penup()
    goto(-150, 100)
    pendown()
    drawMercurio()

    penup()
    goto(-70, 200)
    pendown()
    drawVenus()

    penup()
    goto(100, 250)
    pendown()
    drawTerra()

    penup()
    goto(300, 150)
    pendown()
    drawMarte()

    penup()
    goto(-350, -100)
    pendown()
    drawJupiter()

    penup()
    goto(-100, -300)
    pendown()
    drawSaturno()

    penup()
    goto(250, -300)
    pendown()
    drawUrano()

    penup()
    goto(-400, 200)
    pendown()
    drawNetuno()

    done()


if __name__ == '__main__':
    main()
