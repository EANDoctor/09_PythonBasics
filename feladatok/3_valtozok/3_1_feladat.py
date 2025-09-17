"""
3. Feladat
Készíts egy programot! A gép "gondol" egy számra 1 és 5 között, vagyis egy változóban tárolj egy ilyen számot! Azután a program bekér egy számot a felhasználótól, majd kiírja, hogy ez a szám egyenlő-e a gép által "gondolt" számmal, vagy annál kisebb, illetve nagyobb. 
"""

# Egy kicsi segítséggel a sulipy.hu ról de megvan a random

import random
gondolt_szam = random.randint(1, 5)
megadott_szam = int(input("Adj meg egy számot 1 és 5 között: "))
if megadott_szam < gondolt_szam:
    print("A megadott szám kisebb, mint a gondolt szám.")
elif megadott_szam > gondolt_szam:
    print("A megadott szám nagyobb, mint a gondolt szám.")
else:
    print("A megadott szám egyenlő a gondolt számmal.")