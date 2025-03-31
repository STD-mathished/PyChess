import pygame
class piece:
    def __init__(self,nom, couleur,posX,posY, img):
        self.nom = nom
        self.couleur = couleur
        self.posX = posX
        self.posY = posY
        self.img = img

    def load_img(self):
        self.loaded_img = pygame.image.load(self.img)

