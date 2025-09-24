"""
1. Feladat
Írj egy programot, amely kiírja a páros számokat 1 és 10 között! 
"""

szam = 0
while szam <= 10:
    if szam % 2 == 0:
        print(szam)
    szam = szam + 1
print("program vége")