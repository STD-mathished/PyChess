import pygame
import echiquier
import piece

# Initialisation
pygame.init()

# Constantes
BLANC = (238, 238, 210)
VERT = (118, 150, 86)
TAILLE_ECHIQUIER = 8
TAILLE_CASE = 70


#variables
HAUTEUR = LARGEUR = TAILLE_CASE * TAILLE_ECHIQUIER

#fenetre
fenetre = pygame.display.set_mode(size=(LARGEUR,HAUTEUR))


# creer un echiquier
ec = echiquier.echiquier(TAILLE_ECHIQUIER,TAILLE_CASE, BLANC, VERT)
ec.dessiner_echiquier(fenetre)


#afficher une piece
"""king_img = "img/white/white-king.png"
king = piece.piece("roi_b", "blanc", 3 * TAILLE_CASE, 0 * TAILLE_CASE, king_img)  # Colonne 3, ligne 0
king.load_img()
king.loaded_img = pygame.transform.scale(king.loaded_img, (TAILLE_CASE, TAILLE_CASE))
fenetre.blit(king.loaded_img, (king.posX, king.posY))"""

#initialisation des pieces
ec.init_pieces()

#test
p = piece("black-king", "black")

# Boucle principale
running = True
while running:
    # Gestion des events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Mise à jour de l'affichage
    pygame.display.update()

# Quitter
pygame.quit()
