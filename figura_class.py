import pygame as pg

class Figura:
    def __init__(self, posX, posY, color=(255,255,255), vx=1, vy=1, w=20, h=20, radio=10):
        self.posX = posX
        self.posY = posY
        self.color = color
        self.vx = vx
        self.vy = vy
        self.w = w
        self.h = h
        self.radio = radio

    def mover(self, xMax, yMax):
        self.posX += self.vx
        self.posY += self.vy
        if self.posX == xMax or self.posX == 0:
            self.vx = self.vx*-1
        if self.posY == yMax or self.posY == 0:
            self.vy = self.vy*-1

    def dibujarCirculo(self, pantalla):
        pg.draw.circle(pantalla, self.color, (self.posX, self.posY), self.radio)

    def dibujarRectangulo(self, pantalla):
        pg.draw.rect(pantalla, self.color, (self.posX, self.posY, self.h, self.w))