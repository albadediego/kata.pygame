import pygame as pg
from figura_class import Figura
import random as ra

#inicializar todos los modulos de pygame, pantallas, objetos, eventos, sonidos, etc.
pg.init()

xDisplay = 800
yDisplay = 600

#crear pantalla o sourface
pantalla = pg.display.set_mode((xDisplay, yDisplay)) #definicion de tamaño de pantalla
pg.display.set_caption("Intro Pygame") #agregar un titulo a mi ventana

game_over = True

lista_circulos=[]
lista_rectangulos=[]

for i in range(1,101):
    lista_circulos.append(Figura(ra.randint(0,xDisplay), ra.randint(0,yDisplay),(ra.randint(0,255),ra.randint(0,255),ra.randint(0,255)), radio=ra.randint(10,100)))
    lista_rectangulos.append(Figura(ra.randint(0,xDisplay), ra.randint(0,yDisplay),(ra.randint(0,255),ra.randint(0,255),ra.randint(0,255)), w=ra.randint(10,100), h=ra.randint(10,100)))

while game_over:
    for eventos in pg.event.get(): #capturar todos los eventos mientras se ejecuta el bucle
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = False
    pantalla.fill((50, 189, 172)) #asignar un color a la pantalla

    for circulo in lista_circulos:
        circulo.mover(xDisplay-circulo.radio ,yDisplay-circulo.radio)
        circulo.dibujarCirculo(pantalla)
    
    for rectangulo in lista_rectangulos:
        rectangulo.mover(xDisplay-rectangulo.w,yDisplay-rectangulo.h)
        rectangulo.dibujarRectangulo(pantalla)

    pg.display.flip() #funcion para cargar toda la configuracion que va dentro de la pantalla


pg.quit()