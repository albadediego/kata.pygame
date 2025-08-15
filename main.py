import pygame as pg
from figura_class import Figura

#inicializar todos los modulos de pygame, pantallas, objetos, eventos, sonidos, etc.
pg.init()

xDisplay = 800
yDisplay = 600

#crear pantalla o sourface
pantalla = pg.display.set_mode((xDisplay, yDisplay)) #definicion de tamaño de pantalla
pg.display.set_caption("Intro Pygame") #agregar un titulo a mi ventana

game_over = True


rectangulo1 = Figura(0,300,(223, 40, 220))
rectangulo2 = Figura(0,350, vx=2, vy=2)
rectangulo3 = Figura(0,400,(53,185,36), vx=2, vy=2)

circulo1 = Figura(0,300, radio=30)
circulo2 = Figura(0,360, color=(245, 39, 108), radio=15, vx=2, vy=2)
circulo3 = Figura(0,400, color=(73, 39, 245), radio=20, vx=1, vy=2)

while game_over:
    for eventos in pg.event.get(): #capturar todos los eventos mientras se ejecuta el bucle
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = False
    pantalla.fill((50, 189, 172)) #asignar un color a la pantalla
    
    circulo1.mover(xDisplay,yDisplay)
    circulo2.mover(xDisplay,yDisplay)
    circulo3.mover(xDisplay,yDisplay)
    
    rectangulo1.mover(xDisplay, yDisplay)
    rectangulo2.mover(xDisplay, yDisplay)
    rectangulo3.mover(xDisplay, yDisplay)
    
    #agregamos objeto a la pantalla
    #draw.rect(sourface, color en (rgb), posiciones(posicionX, posicionY, tamañoX, tamañoY))
    circulo1.dibujarCirculo(pantalla)
    circulo2.dibujarCirculo(pantalla)
    circulo3.dibujarCirculo(pantalla)
    
    rectangulo1.dibujarRectangulo(pantalla)
    rectangulo2.dibujarRectangulo(pantalla)
    rectangulo3.dibujarRectangulo(pantalla)
    
    pg.display.flip() #funcion para cargar toda la configuracion que va dentro de la pantalla


pg.quit()