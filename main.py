import pygame as pg


#inicializar todos los modulos de pygame, pantallas, objetos, eventos, sonidos, etc.
pg.init()

#crear pantalla o sourface
pantalla = pg.display.set_mode((800,600)) #definicion de tamaño de pantalla
pg.display.set_caption("Intro Pygame") #agregar un titulo a mi ventana

game_over = True
x = 1
vx = 1
while game_over:
    for eventos in pg.event.get(): #capturar todos los eventos mientras se ejecuta el bucle
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = False
    pantalla.fill((171, 43, 98)) #asignar un color a la pantalla
    x += vx
    if x == 800 or x == 0:
        vx = vx * -1
        
    #agregamos objeto a la pantalla
    #draw.rect(sourface, color en (rgb), posiciones(posicionX, posicionY, tamañoX, tamañoY))
    pg.draw.rect(pantalla, (43, 171, 116), (x, 300-20, 20, 20))
    
    pg.display.flip() #funcion para cargar toda la configuracion que va dentro de la pantalla


pg.quit()