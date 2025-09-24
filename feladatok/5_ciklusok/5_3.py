"""
3. Feladat
Írj egy programot, amely kiírja a páratlan számokat csökkenő sorrendben 1 és 10 között! 
"""

szam = 10
while szam >= 0:
    if szam % 2 == 1:
        print(szam)
    szam = szam - 1
print("program vége")