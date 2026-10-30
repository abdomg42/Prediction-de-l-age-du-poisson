# Exemple : on projette une image 3x3 puis on la reconstruit

from projection import transformee_mojette
from katz import katz_ok
from reconstruction import reconstruire


image = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
directions = [(0, 1), (1, 1), (-1, 1)]

print("Image de départ :")
for ligne in image:
    print(ligne)

projections = transformee_mojette(image, directions)
print("\nProjections :")
for d, proj in projections.items():
    print(d, {b: proj[b] for b in sorted(proj)})

print("\nKatz OK :", katz_ok(directions, 3, 3))

print("\nReconstruction :")
resultat = reconstruire(projections, 3, 3)

print("\nImage retrouvée :")
for ligne in resultat:
    print(ligne)
print("\nMême image :", resultat == image)