import pygame
import piece as pi

# Constantes


class echiquier:
    def __init__(self, taille_echiquier, taille_case,couleur_a, couleur_b):
        self.pieces_noires = []
        self.pieces_blanches = []
        #initialisation des attributs
        self.taille_echiquier = taille_echiquier
        self.taille_case = taille_case
        self.couleur_a = couleur_a
        self.couleur_b = couleur_b
        self.largeur = self.taille_case * self.taille_echiquier
        self.hauteur= self.taille_case * self.taille_echiquier


    def dessiner_echiquier(self, fenetre):

        # Création de la fenetre

        pygame.display.set_caption("échiquier")

        """Dessiner l'échiquier"""
        for ligne in range(self.taille_echiquier):
            for colonne in range(self.taille_echiquier):
                couleur = self.couleur_a if (ligne + colonne) % 2 == 0 else self.couleur_b
                pygame.draw.rect(fenetre, couleur,
                                 (colonne * self.taille_case, ligne * self.taille_case, self.taille_case, self.taille_case))


    def ajouter_piece(self, piece):
        if isinstance(piece, piece):
            if piece.couleur == "black": # on presume que c'est soit black soit white
                self.pieces_noires.append(piece)
            elif piece.couleur == "white":
                self.pieces_blanches.append(piece)

    def test(self):
        print(self.pieces_noires + "\n" +self.pieces_blanches)

    def init_pieces(self):
        print("Initialisation des pieces sur l'echiquier")
        #for piece in :
            #piece_img  =

        """king_img = "img/white/white-king.png"
            king = piece.piece("roi_b", "blanc", 3 * TAILLE_CASE, 0 * TAILLE_CASE, king_img)  # Colonne 3, ligne 0
            king.load_img()
            king.loaded_img = pygame.transform.scale(king.loaded_img, (TAILLE_CASE, TAILLE_CASE))
            fenetre.blit(king.loaded_img, (king.posX, king.posY))"""
