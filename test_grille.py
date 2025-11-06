from grille import Grille

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
