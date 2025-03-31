import pygame


# Constantes
#TAILLE_CASE = 70
#TAILLE_ECHIQUIER = 8


class echiquier:
    def __init__(self, taille_echiquier, taille_case,couleur_a, couleur_b):
        #initialisation des attributs
        self.taille_echiquier = taille_echiquier
        self.taille_case = taille_case
        self.couleur_a = couleur_a
        self.couleur_b = couleur_b
        self.largeur = self.taille_case * self.taille_echiquier
        self.hauteur= self.taille_case * self.taille_echiquier


    def dessiner_echiquier(self):

        # Création de la fenetre
        fenetre = pygame.display.set_mode(size=(self.largeur, self.hauteur))
        pygame.display.set_caption("échiquier")

        """Dessiner l'échiquier"""
        for ligne in range(self.taille_echiquier):
            for colonne in range(self.taille_echiquier):
                couleur = self.couleur_a if (ligne + colonne) % 2 == 0 else self.couleur_b
                pygame.draw.rect(fenetre, couleur,
                                 (colonne * self.taille_case, ligne * self.taille_case, self.taille_case, self.taille_case))