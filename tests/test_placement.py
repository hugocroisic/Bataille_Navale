from src.bnav.grille import Grille
from src.bnav.placement import placer_aleatoire, generer_flotte
from src.bnav.bateau import PorteAvion, Croiseur, Torpilleur, SousMarin

def test_placer_aleatoire_un():
    g = Grille(8, 10)
    b = placer_aleatoire(g, PorteAvion)
    # les cases du PA sont bien marquées
    for (l, c) in b.positions:
        assert g.grille[g._index(l, c)] == '🚢'

def test_generer_flotte():
    g = Grille(8, 10)
    flotte = generer_flotte(g)
    assert len(flotte) == 4
    # aucune case bateau ne doit se chevaucher (ajoute l'assure)
    # contrôle basique : somme des longueurs = nb de cases != '∿' et != 'x'
    total_longueurs = sum(b.longueur for b in flotte)
    nb_cases_bateaux = sum(1 for ch in g.grille if ch not in ('∿', 'x'))
    assert nb_cases_bateaux == total_longueurs
