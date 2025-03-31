import pygame
import echiquier

# Initialisation
pygame.init()

# Constantes
BLANC = (238, 238, 210)
VERT = (118, 150, 86)
TAILLE_ECHIQUIER = 8
TAILLE_CASE = 70

# creer un echiquier
ec = echiquier.echiquier(TAILLE_ECHIQUIER,TAILLE_CASE, BLANC, VERT)
ec.dessiner_echiquier()



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
