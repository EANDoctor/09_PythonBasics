"""
1.1 Feladat
Készíts egy programot, amely megkérdezi a felhasználótól, hogy jó napja van-e! A válasz kétféle lehet: igen vagy nem. A választól függően írjon ki üzenetet a gép! 
"""

valasz = input("Jó napod van? [igen/nem]")

if valasz == "igen":
    print("Örülök neki.")
elif valasz == "nem":
    print("Sajnálom.")