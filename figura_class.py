class Rectangulo:
    def __init__(self, posX, posY, color=(255,255,255), w=20, h=20, vx=1, vy=1):
        self.posX = posX
        self.posY = posY
        self.color = color
        self.w = w
        self.h = h
        self.vx = vx
        self.vy = vy

    def mover(self, xMax, yMax):
        self.posX += self.vx
        self.posY += self.vy
 
        if self.posX == xMax or self.posX == 0:
            self.vx = self.vx*-1
        if self.posY == yMax or self.posY == 0:
            self.vy = self.vy*-1