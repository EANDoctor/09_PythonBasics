"""
B csoport:
Készítsünk programot, amely segíti a burkoló mesterek munkáját.
A szükséges csempe mennyiségének a kiszámításához a program kérje be a terület szélességét és a magasságát centiméterben,
valamint, hogy hány darab csempét vásároltunk már, majd számolja ki a területét (a*b), és
hogy a 20cm*20cm méretű csempék esetén hány darabra van szükség a munka elvégzéséhez (a plusz 10%-ot az illesztések miatt illik rászámolnunk).
A program azt is állapítsa meg, és közölje a felhasználóval, hogy kell-e még vásárolnunk csempét!
"""

a = int(input("Add meg a terület szélességét cm-ben:"))
b = int(input("Add meg a terület magasságát cm-ben:"))
csempe_mennyisege = int(input("Mennyi csempénk van ?"))

terulet = a * b 
csempe_terulete = 20 * 20
csempe_szukseglet = (terulet / csempe_terulete) * 1.1

if csempe_szukseglet <= csempe_mennyisege:
    print("Minden rendben több csempénk van.")
else:
    print("Baj van kell még csempe.")