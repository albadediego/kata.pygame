import pygame as pg


#inicializar todos los modulos de pygame, pantallas, objetos, eventos, sonidos, etc.
pg.init()

#crear pantalla o sourface
pantalla = pg.display.set_mode((800,600)) #definicion de tamaño de pantalla
pg.display.set_caption("Intro Pygame") #agregar un titulo a mi ventana

game_over = True
x = 0
vx = 1
y = 0
vy = 1

x2 = 100
vx2 = 1
y2 = 500
vy2 = 1
while game_over:
    for eventos in pg.event.get(): #capturar todos los eventos mientras se ejecuta el bucle
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = False
    pantalla.fill((171, 43, 98)) #asignar un color a la pantalla
    x += vx
    y += vy

    x2 += vx2
    y2 += vy2

    if x == 800 or x == 0:
        vx = vx * -1
    if y == 600 or y == 0:
        vy = vy * -1

    if x2 == 800 or x2 == 0:
        vx2 = vx2 * -1
    if y2 == 600 or y2 == 0:
        vy2 = vy2 * -1
    #agregamos objeto a la pantalla
    #draw.rect(sourface, color en (rgb), posiciones(posicionX, posicionY, tamañoX, tamañoY))
    pg.draw.rect(pantalla, (43, 171, 116), (x, y, 20, 20))
    pg.draw.rect(pantalla, (154, 201, 13), (x2, y2, 20, 20))
    
    pg.display.flip() #funcion para cargar toda la configuracion que va dentro de la pantalla


pg.quit()