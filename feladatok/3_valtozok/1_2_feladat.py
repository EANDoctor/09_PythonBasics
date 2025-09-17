"""
1.2 Feladat
Fejleszd tovább az első feladat programját úgy, hogy amennyiben a felhasználó nem a két lehetséges válasz (igen/nem) közül ad meg egyet, a gép kiírja: "Sajnos nem értem a válaszodat!"
"""

valasz = input("Jó napod van? [igen/nem]")

if valasz == "igen":
    print("Örülök neki.")
elif valasz == "nem":
    print("Sajnálom.")
else:
    print("Sajnos nem értem a válaszodat!")