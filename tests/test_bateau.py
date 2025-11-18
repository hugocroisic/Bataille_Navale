from src.bnav.grille import Grille
from src.bnav.bateau import Bateau, chevauchent
from src.bnav.bateau import PorteAvion, Croiseur, Torpilleur, SousMarin

def test_bateau_defaut():
    b = Bateau(2, 3)
    assert b.ligne == 2
    assert b.colonne == 3
    assert b.longueur == 1
    assert b.vertical is False

def test_positions_horizontales():
    b = Bateau(2, 3, longueur=3)
    assert b.positions == [(2, 3), (2, 4), (2, 5)]

def test_positions_verticales():
    b = Bateau(2, 3, longueur=3, vertical=True)
    assert b.positions == [(2, 3), (3, 3), (4, 3)]

def test_chevauchent_vrai():
    b1 = Bateau(2, 3, longueur=3)
    b2 = Bateau(2, 4, longueur=2)
    assert chevauchent(b1, b2) is True

def test_chevauchent_faux():
    b1 = Bateau(0, 0, longueur=2)
    b2 = Bateau(3, 3, longueur=2)
    assert chevauchent(b1, b2) is False

def test_coule():
    g = Grille(5, 5)
    b = Bateau(1, 1, longueur=3, vertical=False)
    g.ajoute(b)

    # au début : pas coulé
    assert b.coule(g) is False

    # on touche partiellement
    g.tirer(1, 1)
    g.tirer(1, 2)
    assert b.coule(g) is False

    # on touche la dernière case
    g.tirer(1, 3)
    assert b.coule(g) is True

def test_ajoute_types_bateaux():
    g = Grille(8, 10)

    b1 = PorteAvion(0, 0)
    b2 = Croiseur(2, 0)
    b3 = Torpilleur(4, 0)
    b4 = SousMarin(6, 0)

    assert g.ajoute(b1)
    assert g.ajoute(b2)
    assert g.ajoute(b3)
    assert g.ajoute(b4)

    for (l, c) in b1.positions:
        assert g.grille[g._index(l, c)] == '🚢'
    for (l, c) in b2.positions:
        assert g.grille[g._index(l, c)] == '⛴'