"""
2. Feladat
A program a pénzfeldobást modellezi. Kérdezze meg a felhasználótól a választását (fej vagy írás), majd adjon tájékoztatást, hogy eltalálta-e! 
"""

import random

penzdobas = input("fej vagy írás?: ")
fej = 1
iras = 2
gep = random.randint(1,2)

if  penzdobas == "fej" and gep == fej:
    print("Nyertél")
elif penzdobas == "iras" and gep == iras:
    print("Nyertél")
elif penzdobas == "iras" and gep == fej:
    print("Nem nyert")
elif penzdobas == "fej" and gep == iras:
    print("Nem nyert")