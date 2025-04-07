import pygame
class piece:
    def __init__(self,nom, couleur,pos_x,pos_y, img):
        self.nom = nom
        self.couleur = couleur
        self.posX = pos_x
        self.posY = pos_y
        self.img = img

    def load_img(self):
        self.loaded_img = pygame.image.load(self.img)

