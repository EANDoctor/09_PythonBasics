"""
Ha a bavitt szám kisebb, mint 0, ha a bevitt szám nagyobb, mint 0: pozitív
"""

# szam = int(input("Adj meg egy számot!"))

# if szam < 0:
#     print("Ez egy negatív szám.")
# elif szam > 0:
#     print("Ez a szám pozitív.")
# else:
#     print("Nulla")

"""
Páros számra írja ki a program azt, hogy páros
"""

szam = int(input("Adj meg egy számot."))

if szam % 2 == 0 and szam != 0:
    print("A megadott szám páros.")
elif szam == 0:
    print("NULLLLLA")
else:
    print("A megadott szám páratlan.")

