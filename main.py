# main.py
from src.bnav.grille import Grille
from src.bnav.placement import generer_flotte
from src.bnav.jeu import tirer_avec_retour

def parse_coord(s: str):
    """Accepte 'l c' ou 'l,c' et renvoie (l, c) en int."""
    s = s.strip().replace(',', ' ')
    parts = [p for p in s.split() if p]
    if len(parts) != 2:
        raise ValueError("Format attendu : 'ligne colonne'")
    return int(parts[0]), int(parts[1])

def tout_coule(grille, flotte):
    return all(b.coule(grille) for b in flotte)

def main():
    L, C = 8, 10
    g = Grille(L, C)
    flotte = generer_flotte(g)

    coups = 0
    print("🎮 Bataille navale — . Tape 'q' pour quitter.\n")

    while True:
        print(g.afficher_publique(flotte))
        raw = input("\nTir ? (ex: 2 3) > ").strip()
        if raw.lower() in {"q", "quit", "exit"}:
            print("À bientôt !")
            break

        try:
            l, c = parse_coord(raw)
            statut, b = tirer_avec_retour(g, flotte, l, c)

            # On compte un coup seulement si ce n'était pas une case déjà tirée
            if statut != "déjà tiré":
                coups += 1

            if statut == "raté":
                print("➡️  Plouf ! (raté)")
            elif statut == "touché":
                print("💣 Touché !")
            elif statut == "coulé":
                print(f"🔥 Coulé ! {b.marque} (longueur {b.longueur})")
            elif statut == "déjà tiré":
                print("↩️  Tu as déjà tiré ici.")

            if tout_coule(g, flotte):
                print("\n" + g.afficher_publique(flotte))
                print(f"\n🏁 Victoire ! Tous les bateaux sont coulés en {coups} coup(s).")
                break

        except ValueError as e:
            print(f"⚠️  Entrée invalide : {e}")
        except IndexError:
            print("⚠️  Coordonnées hors grille.")

        print()

if __name__ == "__main__":
    main()
