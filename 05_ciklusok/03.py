
folytatja = True
while folytatja:
    print('Vidd ki a szemetet!')
    valasz = input('Mondjam még egyszer? (i/n)')
    if valasz == 'n':
        folytatja = False
    elif valasz == 'igen' or 'nem':
        print("Csak röviden! [i/n]")
print('>> Program vége! <<')