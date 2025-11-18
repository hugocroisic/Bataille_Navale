from src.bnav.bateau import PorteAvion, Croiseur, Torpilleur, SousMarin
import random

def placer_aleatoire(grille, BateauType):
    while True:
        vertical = random.choice([True, False])

        # on instancie juste pour connaître la longueur
        probe = BateauType(0, 0, vertical=vertical)
        L = probe.longueur

        if vertical:
            max_l = grille.n_ligne - L
            max_c = grille.n_colonne - 1
        else:
            max_l = grille.n_ligne - 1
            max_c = grille.n_colonne - L

        l = random.randint(0, max_l)
        c = random.randint(0, max_c)

        b = BateauType(l, c, vertical=vertical)
        if grille.ajoute(b):
            return b

def generer_flotte(grille):
    flotte = []
    for BT in (PorteAvion, Croiseur, Torpilleur, SousMarin):
        flotte.append(placer_aleatoire(grille, BT))
    return flotte