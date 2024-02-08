from turtle import *
from random import randint

Screen().bgcolor("lightblue")
Screen().screensize(500, 500)
Screen().setworldcoordinates(-300, 300, 300, 900)
Screen().tracer(0, 0)


def moveToRandomLocation():
    penup()
    setpos(randint(-500, 500), randint(-500, 500))
    pendown()


def circulo_preenchido(raio, cor):
    color(cor, cor)
    begin_fill()
    circle(raio)
    end_fill()


def nuvem(raio, cor_nuvem="white"):
    circulo_preenchido(raio, cor_nuvem)
    forward(raio)
    circulo_preenchido(raio, cor_nuvem)
    right(90)
    circulo_preenchido(raio, cor_nuvem)
    right(90)
    circulo_preenchido(raio, cor_nuvem)
    right(90)
    circulo_preenchido(raio, cor_nuvem)
    right(90)


def arco_iris(raio=200, intervalo=10):
    cores_arco_iris = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'lightblue']

    for cor in cores_arco_iris:
        circulo_preenchido(raio, cor)
        raio -= intervalo

        left(90)
        forward(intervalo)
        right(90)


penup()

moveToRandomLocation()
nuvem(20)
moveToRandomLocation()
nuvem(30)
moveToRandomLocation()
nuvem(50)
moveToRandomLocation()
nuvem(5)

goto(0, 0)
arco_iris(300, 10)

moveToRandomLocation()
nuvem(15)
moveToRandomLocation()
nuvem(10)
moveToRandomLocation()
nuvem(10)


done()
