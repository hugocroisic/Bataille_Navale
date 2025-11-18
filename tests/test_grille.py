from src.bnav.grille import Grille
from src.bnav.bateau import Bateau

def test_constructeur():
    g = Grille(5, 8)
    assert len(g.grille) == 5 * 8
    assert set(g.grille) == {'∿'}

def test_tirer():
    g = Grille(5, 8)
    g.tirer(1, 2)
    assert g.grille[g._index(1, 2)] == 'x'

def test_tirer_hors_grille():
    g = Grille(5, 8)
    try:
        g.tirer(10, 10)
        assert False, "IndexError attendu"
    except IndexError:
        pass

def test_str():
    g = Grille(2, 3)
    assert str(g) == "∿∿∿\n∿∿∿"
    g.tirer(1, 1)
    assert str(g) == "∿∿∿\n∿x∿"

def test_ajoute_bateau_ok():
    g = Grille(2, 3)
    b = Bateau(1, 0, longueur=2, vertical=False)
    ok = g.ajoute(b)
    assert ok is True
    assert g.grille == ['∿', '∿', '∿', '⛵', '⛵', '∿']

def test_ajoute_bateau_hors_grille():
    g = Grille(2, 3)
    b1 = Bateau(1, 0, longueur=2, vertical=True)   
    b2 = Bateau(1, 0, longueur=4, vertical=True)   

    etat_initial = g.grille.copy()

    assert g.ajoute(b1) is False
    assert g.grille == etat_initial

    assert g.ajoute(b2) is False
    assert g.grille == etat_initial
