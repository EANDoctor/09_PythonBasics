"""
1. Feladat
Thonny fejlesztői környezetben készíts egy rövid programot, amely

    kommentként tartalmazza a program funkciójának leírását,
    konstansként tárolja PI értékét,
    egy másik változóban tárolja egy kör sugarának nagyságát (cm-ben megadva),
    kiszámolja és a képernyőre kiírja a kör kerületét és területét!

[Megjegyzés] A szorzás jele: * 
"""

PI = 3.14
sugar = 5 #cm

kerulet = 2 * PI * sugar
terulet = PI * sugar * sugar

print("A kör kerülete:", kerulet, "cm")
print("A kör területe:", terulet, "cm²")