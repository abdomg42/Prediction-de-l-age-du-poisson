# Transformée de Mojette inverse : des projections vers l'image

from projection import numero_de_bin


def reconstruire(projections, nb_colonnes, nb_lignes):
    # on travaille sur une copie, les valeurs vont diminuer au fil des étapes
    reste = {d: dict(proj) for d, proj in projections.items()}
    image = [[None] * nb_colonnes for _ in range(nb_lignes)]

    # pour chaque bin, la liste des pixels qu'on ne connaît pas encore
    inconnus = {}
    for (p, q) in reste:
        for l in range(nb_lignes):
            for k in range(nb_colonnes):
                b = numero_de_bin(p, q, k, l)
                inconnus.setdefault(((p, q), b), []).append((k, l))

    nb_a_trouver = nb_colonnes * nb_lignes
    etape = 0

    while nb_a_trouver > 0:
        trouve = False

        for (direction, b), pixels in inconnus.items():
            # s'il ne reste qu'un pixel dans ce bin, sa valeur est le reste du bin
            if len(pixels) == 1:
                k, l = pixels[0]
                valeur = reste[direction][b]
                image[l][k] = valeur
                nb_a_trouver -= 1
                etape += 1
                print(f"Étape {etape} : bin {b} de la direction {direction}, "
                      f"pixel ({k}, {l}) = {valeur}")

                # on retire ce pixel de toutes les projections
                for (p, q) in reste:
                    bb = numero_de_bin(p, q, k, l)
                    reste[(p, q)][bb] -= valeur
                    inconnus[((p, q), bb)].remove((k, l))

                trouve = True
                break

        if not trouve:
            raise ValueError("Impossible de continuer, il manque des projections.")

    return image