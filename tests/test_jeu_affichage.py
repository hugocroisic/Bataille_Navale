from src.bnav.grille import Grille
from src.bnav.bateau import Croiseur
from src.bnav.placement import generer_flotte
from src.bnav.jeu import tirer_avec_retour

def test_affichage_masque_et_coule():
    g = Grille(5, 7)
    b = Croiseur(1, 2, vertical=False)
    assert g.ajoute(b)
    flotte = [b]

    # début : bateau caché
    s0 = g.afficher_publique(flotte)
    assert '⛴' not in s0

    # on touche une case du bateau -> 💣
    statut, _ = tirer_avec_retour(g, flotte, 1, 3)
    assert statut == "touché"
    s1 = g.afficher_publique(flotte)
    assert '💣' in s1
    assert '⛴' not in s1

    # on finit de le couler : il faut toucher TOUTES ses cases
    _ , _ = tirer_avec_retour(g, flotte, 1, 2)  # << manquait dans ton test
    statut, _ = tirer_avec_retour(g, flotte, 1, 4)
    assert statut == "coulé"

    # affichage public : révélé en ⛴, état interne : 'x'
    s2 = g.afficher_publique(flotte)
    lines = s2.splitlines()
    for (l, c) in b.positions:
        assert lines[l][c] == '⛴'
        assert g.grille[g._index(l, c)] == 'x'
