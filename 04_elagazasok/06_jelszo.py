"""
6 Egyszerű jelszóellenőrző
Kérj be egy jelszót, és ha megegyezik a „titok” szóval, írd ki: „Belépés engedélyezve!”, különben „Helytelen jelszó!”.
"""

password = input("Adja meg a jelszót!")

if password == "titok":
    print("Belépés engedélyezve!")
else:
    print("Helytelen jelszó")