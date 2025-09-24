"""
1. Feladat
Készíts egy rövid programot, amely 1 és 3 között generál véletlenszámot, majd összehasonlítja ezt a felhasználó által megadott, szintén ebbe a tartományba eső számmal! Az összehasonlítás eredményéről tájékoztassa a felhasználót! 
"""

import random

random_number = random.randint(1, 3)
user_szam = int(input("Adj meg egy számot! [1-3]:"))

if user_szam > 3:
    print("Túl nagy a szám.")
    quit()

if random_number == user_szam:
    print("Kitaláltad! :)")
elif random_number < user_szam:
    print("Ez sajnos túl nagy lett.")
else:
    print("Nagyobb szám fog kellni ide.")
