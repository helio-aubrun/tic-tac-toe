import pygame
import sys
import ia
pygame.init()
largeur, hauteur = 600, 600
taille_case = 200
couleur_fond = (200, 200, 200)
couleur_ligne = (255, 255, 255)
couleur_signe = (255, 0, 0)
couleur_texte = (0,0,0)
taille_police = 50
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Tic Tac Toe")
tableau = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
tour_joueur = 1
derniere_case = None
partie_gagnee = False
ligne_gagnante = None
level=0

def afficher_debut():
    font = pygame.font.Font(None, 30)
    texte = font.render("Combien de joueur ? Appuyez sur 1 ou 2", True, couleur_texte)
    ecran.blit(texte, (largeur // 6, hauteur // 2))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 1
                elif event.key == pygame.K_2:
                    return 2
                
def dessiner_grille():
    for i in range(1, 3):
        pygame.draw.line(ecran, couleur_ligne, (i * taille_case, 0), (i * taille_case, hauteur), 5)
        pygame.draw.line(ecran, couleur_ligne, (0, i * taille_case), (largeur, i * taille_case), 5)

def deffinir_level(diff):
    ecran.fill(couleur_fond)
    dessiner_grille()
    font = pygame.font.Font(None, 30)
    texte = font.render("Quelle niveau de difficulté ? Appuyez sur 1, 2 ou 3", True, couleur_texte)
    ecran.blit(texte, (largeur // 6, hauteur // 2))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        diff = 1
                        return diff
                    if event.key == pygame.K_2:
                        diff = 2
                        return diff
                    if event.key == pygame.K_3:
                        diff = 3
                        return diff

def afficher_fin(message):
    font = pygame.font.Font(None, taille_police)
    texte = font.render(message, True, couleur_texte)
    ecran.blit(texte, (largeur // 6, hauteur // 2))
    pygame.display.flip()
    pygame.time.wait(1000)
    font_petite = pygame.font.Font(None, 30)
    rejouer_texte = font_petite.render("Appuyez sur ESPACE pour rejouer.", True, couleur_texte)
    ecran.blit(rejouer_texte, (largeur // 6, hauteur // 1.5))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    global tableau, tour_joueur, derniere_case, partie_gagnee, ligne_gagnante
                    tableau = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                    tour_joueur = 2
                    derniere_case = None
                    partie_gagnee = False
                    ligne_gagnante = None
                    return

ecran.fill(couleur_fond)
dessiner_grille()
nombre_joueurs = afficher_debut()
level = deffinir_level(level)
while True:
    ecran.fill(couleur_fond)
    dessiner_grille()
    if nombre_joueurs == 2 :
        for i in range(3):
            for j in range(3):
                if tableau[i][j] == 1:
                    pygame.draw.line(ecran, couleur_signe, (j * taille_case, i * taille_case),
                                     ((j + 1) * taille_case, (i + 1) * taille_case), 5)
                    pygame.draw.line(ecran, couleur_signe, (j * taille_case, (i + 1) * taille_case),
                                     ((j + 1) * taille_case, i * taille_case), 5)
                elif tableau[i][j] == 2:
                    pygame.draw.circle(ecran, couleur_signe, (j * taille_case + taille_case // 2,
                                                          i * taille_case + taille_case // 2),
                                   taille_case // 2 - 5, 5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not partie_gagnee:
                x, y = event.pos
                ligne = y // taille_case
                colonne = x // taille_case
                if tableau[ligne][colonne] == 0:
                    tableau[ligne][colonne] = tour_joueur
                    derniere_case = (ligne, colonne)
                    for i in range(3):
                        if all(tableau[i][j] == tour_joueur for j in range(3)):
                            for i in range(3):
                                for j in range(3):
                                    if tableau[i][j] == 1:
                                        pygame.draw.line(ecran, couleur_signe, (j * taille_case, i * taille_case),
                                                    ((j + 1) * taille_case, (i + 1) * taille_case), 5)
                                        pygame.draw.line(ecran, couleur_signe, (j * taille_case, (i + 1) * taille_case),
                                                    ((j + 1) * taille_case, i * taille_case), 5)
                                    elif tableau[i][j] == 2:
                                        pygame.draw.circle(ecran, couleur_signe, (j * taille_case + taille_case // 2,
                                                                              i * taille_case + taille_case // 2),
                                                       taille_case // 2 - 5, 5)
                            ligne_gagnante = [(i, j) for j in range(3)]
                            if tour_joueur==1:
                                afficher_fin(f"Le joueur X a gagné !")
                            elif tour_joueur==2:
                                afficher_fin(f"Le joueur O a gagné !")
                        if all(tableau[j][i] == tour_joueur for j in range(3)):
                            for i in range(3):
                                for j in range(3):
                                    if tableau[i][j] == 1:
                                        pygame.draw.line(ecran, couleur_signe, (j * taille_case, i * taille_case),
                                                    ((j + 1) * taille_case, (i + 1) * taille_case), 5)
                                        pygame.draw.line(ecran, couleur_signe, (j * taille_case, (i + 1) * taille_case),
                                                    ((j + 1) * taille_case, i * taille_case), 5)
                                    elif tableau[i][j] == 2:
                                        pygame.draw.circle(ecran, couleur_signe, (j * taille_case + taille_case // 2,
                                                                              i * taille_case + taille_case // 2),
                                                       taille_case // 2 - 5, 5)
                            ligne_gagnante = [(j, i) for j in range(3)]
                            if tour_joueur==1:
                                afficher_fin(f"Le joueur X a gagné !")
                            elif tour_joueur==2:
                                afficher_fin(f"Le joueur O a gagné !")
                    if all(tableau[i][i] == tour_joueur for i in range(3)):
                        for i in range(3):
                            for j in range(3):
                                if tableau[i][j] == 1:
                                    pygame.draw.line(ecran, couleur_signe, (j * taille_case, i * taille_case),
                                                    ((j + 1) * taille_case, (i + 1) * taille_case), 5)
                                    pygame.draw.line(ecran, couleur_signe, (j * taille_case, (i + 1) * taille_case),
                                                    ((j + 1) * taille_case, i * taille_case), 5)
                                elif tableau[i][j] == 2:
                                    pygame.draw.circle(ecran, couleur_signe, (j * taille_case + taille_case // 2,
                                                                              i * taille_case + taille_case // 2),
                                                       taille_case // 2 - 5, 5)
                        ligne_gagnante = [(i, i) for i in range(3)]
                        if tour_joueur==1:
                                afficher_fin(f"Le joueur X a gagné !")
                        elif tour_joueur==2:
                                afficher_fin(f"Le joueur O a gagné !")
                    if all(tableau[i][2 - i] == tour_joueur for i in range(3)):
                        for i in range(3):
                            for j in range(3):
                                if tableau[i][j] == 1:
                                    pygame.draw.line(ecran, couleur_signe, (j * taille_case, i * taille_case),
                                                    ((j + 1) * taille_case, (i + 1) * taille_case), 5)
                                    pygame.draw.line(ecran, couleur_signe, (j * taille_case, (i + 1) * taille_case),
                                                    ((j + 1) * taille_case, i * taille_case), 5)
                                elif tableau[i][j] == 2:
                                    pygame.draw.circle(ecran, couleur_signe, (j * taille_case + taille_case // 2,
                                                                              i * taille_case + taille_case // 2),
                                                       taille_case // 2 - 5, 5)
                        ligne_gagnante = [(i, 2 - i) for i in range(3)]
                        if tour_joueur==1:
                                afficher_fin(f"Le joueur X a gagné !")
                        elif tour_joueur==2:
                                afficher_fin(f"Le joueur O a gagné !")
                    if all(tableau[i][j] != 0 for i in range(3) for j in range(3)):
                        for i in range(3):
                            for j in range(3):
                                if tableau[i][j] == 1:
                                    pygame.draw.line(ecran, couleur_signe, (j * taille_case, i * taille_case),
                                                    ((j + 1) * taille_case, (i + 1) * taille_case), 5)
                                    pygame.draw.line(ecran, couleur_signe, (j * taille_case, (i + 1) * taille_case),
                                                    ((j + 1) * taille_case, i * taille_case), 5)
                                elif tableau[i][j] == 2:
                                    pygame.draw.circle(ecran, couleur_signe, (j * taille_case + taille_case // 2,
                                                                              i * taille_case + taille_case // 2),
                                                       taille_case // 2 - 5, 5)
                        afficher_fin("Match nul !")
                tour_joueur = 2 if tour_joueur == 1 else 1
    elif nombre_joueurs==1:
        for i in range(3):
            for j in range(3):
                if tableau[i][j] == 1:
                    pygame.draw.line(ecran, couleur_signe, (j * taille_case, i * taille_case),
                                     ((j + 1) * taille_case, (i + 1) * taille_case), 5)
                    pygame.draw.line(ecran, couleur_signe, (j * taille_case, (i + 1) * taille_case),
                                     ((j + 1) * taille_case, i * taille_case), 5)
                elif tableau[i][j] == 2:
                    pygame.draw.circle(ecran, couleur_signe, (j * taille_case + taille_case // 2,
                                                          i * taille_case + taille_case // 2),
                                   taille_case // 2 - 5, 5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not partie_gagnee:
                x, y = event.pos
                ligne = y // taille_case
                colonne = x // taille_case
                if tableau[ligne][colonne] == 0:
                    tableau[ligne][colonne] = tour_joueur
                    derniere_case = (ligne, colonne)
                    for i in range(3):
                        if all(tableau[i][j] == tour_joueur for j in range(3)):
                            for i in range(3):
                                for j in range(3):
                                    if tableau[i][j] == 1:
                                        pygame.draw.line(ecran, couleur_signe, (j * taille_case, i * taille_case),
                                                    ((j + 1) * taille_case, (i + 1) * taille_case), 5)
                                        pygame.draw.line(ecran, couleur_signe, (j * taille_case, (i + 1) * taille_case),
                                                    ((j + 1) * taille_case, i * taille_case), 5)
                                    elif tableau[i][j] == 2:
                                        pygame.draw.circle(ecran, couleur_signe, (j * taille_case + taille_case // 2,
                                                                              i * taille_case + taille_case // 2),
                                                       taille_case // 2 - 5, 5)
                            ligne_gagnante = [(i, j) for j in range(3)]
                            if tour_joueur==1:
                                afficher_fin(f"Le joueur X a gagné !")
                            elif tour_joueur==2:
                                afficher_fin(f"Le joueur O a gagné !")
                        if all(tableau[j][i] == tour_joueur for j in range(3)):
                            for i in range(3):
                                for j in range(3):
                                    if tableau[i][j] == 1:
                                        pygame.draw.line(ecran, couleur_signe, (j * taille_case, i * taille_case),
                                                    ((j + 1) * taille_case, (i + 1) * taille_case), 5)
                                        pygame.draw.line(ecran, couleur_signe, (j * taille_case, (i + 1) * taille_case),
                                                    ((j + 1) * taille_case, i * taille_case), 5)
                                    elif tableau[i][j] == 2:
                                        pygame.draw.circle(ecran, couleur_signe, (j * taille_case + taille_case // 2,
                                                                              i * taille_case + taille_case // 2),
                                                       taille_case // 2 - 5, 5)
                            ligne_gagnante = [(j, i) for j in range(3)]
                            if tour_joueur==1:
                                afficher_fin(f"Le joueur X a gagné !")
                            elif tour_joueur==2:
                                afficher_fin(f"Le joueur O a gagné !")
                    if all(tableau[i][i] == tour_joueur for i in range(3)):
                        for i in range(3):
                            for j in range(3):
                                if tableau[i][j] == 1:
                                    pygame.draw.line(ecran, couleur_signe, (j * taille_case, i * taille_case),
                                                    ((j + 1) * taille_case, (i + 1) * taille_case), 5)
                                    pygame.draw.line(ecran, couleur_signe, (j * taille_case, (i + 1) * taille_case),
                                                    ((j + 1) * taille_case, i * taille_case), 5)
                                elif tableau[i][j] == 2:
                                    pygame.draw.circle(ecran, couleur_signe, (j * taille_case + taille_case // 2,
                                                                              i * taille_case + taille_case // 2),
                                                       taille_case // 2 - 5, 5)
                        ligne_gagnante = [(i, i) for i in range(3)]
                        if tour_joueur==1:
                                afficher_fin(f"Le joueur X a gagné !")
                        elif tour_joueur==2:
                                afficher_fin(f"Le joueur O a gagné !")
                    if all(tableau[i][2 - i] == tour_joueur for i in range(3)):
                        for i in range(3):
                            for j in range(3):
                                if tableau[i][j] == 1:
                                    pygame.draw.line(ecran, couleur_signe, (j * taille_case, i * taille_case),
                                                    ((j + 1) * taille_case, (i + 1) * taille_case), 5)
                                    pygame.draw.line(ecran, couleur_signe, (j * taille_case, (i + 1) * taille_case),
                                                    ((j + 1) * taille_case, i * taille_case), 5)
                                elif tableau[i][j] == 2:
                                    pygame.draw.circle(ecran, couleur_signe, (j * taille_case + taille_case // 2,
                                                                              i * taille_case + taille_case // 2),
                                                       taille_case // 2 - 5, 5)
                        ligne_gagnante = [(i, 2 - i) for i in range(3)]
                        if tour_joueur==1:
                                afficher_fin(f"Le joueur X a gagné !")
                        elif tour_joueur==2:
                                afficher_fin(f"Le joueur O a gagné !")
                    if all(tableau[i][j] != 0 for i in range(3) for j in range(3)):
                        for i in range(3):
                            for j in range(3):
                                if tableau[i][j] == 1:
                                    pygame.draw.line(ecran, couleur_signe, (j * taille_case, i * taille_case),
                                                    ((j + 1) * taille_case, (i + 1) * taille_case), 5)
                                    pygame.draw.line(ecran, couleur_signe, (j * taille_case, (i + 1) * taille_case),
                                                    ((j + 1) * taille_case, i * taille_case), 5)
                                elif tableau[i][j] == 2:
                                    pygame.draw.circle(ecran, couleur_signe, (j * taille_case + taille_case // 2,
                                                                              i * taille_case + taille_case // 2),
                                                       taille_case // 2 - 5, 5)
                        afficher_fin("Match nul !")
                tour_joueur = 2 if tour_joueur == 1 else 1
                ligne, colonne = ia.ia(tableau, tour_joueur, level)
                if tableau[ligne][colonne] == 0:
                    tableau[ligne][colonne] = tour_joueur
                    derniere_case = (ligne, colonne)
                    for i in range(3):
                        if all(tableau[i][j] == tour_joueur for j in range(3)):
                            for i in range(3):
                                for j in range(3):
                                    if tableau[i][j] == 1:
                                        pygame.draw.line(ecran, couleur_signe, (j * taille_case, i * taille_case),
                                                    ((j + 1) * taille_case, (i + 1) * taille_case), 5)
                                        pygame.draw.line(ecran, couleur_signe, (j * taille_case, (i + 1) * taille_case),
                                                    ((j + 1) * taille_case, i * taille_case), 5)
                                    elif tableau[i][j] == 2:
                                        pygame.draw.circle(ecran, couleur_signe, (j * taille_case + taille_case // 2,
                                                                              i * taille_case + taille_case // 2),
                                                       taille_case // 2 - 5, 5)
                            ligne_gagnante = [(i, j) for j in range(3)]
                            if tour_joueur==1:
                                afficher_fin(f"Le joueur X a gagné !")
                            elif tour_joueur==2:
                                afficher_fin(f"Le joueur O a gagné !")
                        if all(tableau[j][i] == tour_joueur for j in range(3)):
                            for i in range(3):
                                for j in range(3):
                                    if tableau[i][j] == 1:
                                        pygame.draw.line(ecran, couleur_signe, (j * taille_case, i * taille_case),
                                                    ((j + 1) * taille_case, (i + 1) * taille_case), 5)
                                        pygame.draw.line(ecran, couleur_signe, (j * taille_case, (i + 1) * taille_case),
                                                    ((j + 1) * taille_case, i * taille_case), 5)
                                    elif tableau[i][j] == 2:
                                        pygame.draw.circle(ecran, couleur_signe, (j * taille_case + taille_case // 2,
                                                                              i * taille_case + taille_case // 2),
                                                       taille_case // 2 - 5, 5)
                            ligne_gagnante = [(j, i) for j in range(3)]
                            if tour_joueur==1:
                                afficher_fin(f"Le joueur X a gagné !")
                            elif tour_joueur==2:
                                afficher_fin(f"Le joueur O a gagné !")
                    if all(tableau[i][i] == tour_joueur for i in range(3)):
                        for i in range(3):
                            for j in range(3):
                                if tableau[i][j] == 1:
                                    pygame.draw.line(ecran, couleur_signe, (j * taille_case, i * taille_case),
                                                    ((j + 1) * taille_case, (i + 1) * taille_case), 5)
                                    pygame.draw.line(ecran, couleur_signe, (j * taille_case, (i + 1) * taille_case),
                                                    ((j + 1) * taille_case, i * taille_case), 5)
                                elif tableau[i][j] == 2:
                                    pygame.draw.circle(ecran, couleur_signe, (j * taille_case + taille_case // 2,
                                                                              i * taille_case + taille_case // 2),
                                                       taille_case // 2 - 5, 5)
                        ligne_gagnante = [(i, i) for i in range(3)]
                        if tour_joueur==1:
                                afficher_fin(f"Le joueur X a gagné !")
                        elif tour_joueur==2:
                                afficher_fin(f"Le joueur O a gagné !")
                    if all(tableau[i][2 - i] == tour_joueur for i in range(3)):
                        for i in range(3):
                            for j in range(3):
                                if tableau[i][j] == 1:
                                    pygame.draw.line(ecran, couleur_signe, (j * taille_case, i * taille_case),
                                                    ((j + 1) * taille_case, (i + 1) * taille_case), 5)
                                    pygame.draw.line(ecran, couleur_signe, (j * taille_case, (i + 1) * taille_case),
                                                    ((j + 1) * taille_case, i * taille_case), 5)
                                elif tableau[i][j] == 2:
                                    pygame.draw.circle(ecran, couleur_signe, (j * taille_case + taille_case // 2,
                                                                              i * taille_case + taille_case // 2),
                                                       taille_case // 2 - 5, 5)
                        ligne_gagnante = [(i, 2 - i) for i in range(3)]
                        if tour_joueur==1:
                                afficher_fin(f"Le joueur X a gagné !")
                        elif tour_joueur==2:
                                afficher_fin(f"Le joueur O a gagné !")
                    if all(tableau[i][j] != 0 for i in range(3) for j in range(3)):
                        for i in range(3):
                            for j in range(3):
                                if tableau[i][j] == 1:
                                    pygame.draw.line(ecran, couleur_signe, (j * taille_case, i * taille_case),
                                                    ((j + 1) * taille_case, (i + 1) * taille_case), 5)
                                    pygame.draw.line(ecran, couleur_signe, (j * taille_case, (i + 1) * taille_case),
                                                    ((j + 1) * taille_case, i * taille_case), 5)
                                elif tableau[i][j] == 2:
                                    pygame.draw.circle(ecran, couleur_signe, (j * taille_case + taille_case // 2,
                                                                              i * taille_case + taille_case // 2),
                                                       taille_case // 2 - 5, 5)
                        afficher_fin("Match nul !")
                tour_joueur = 2 if tour_joueur == 1 else 1
    pygame.display.flip()