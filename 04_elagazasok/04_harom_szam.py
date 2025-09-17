"""
4️ Három szám közül a legnagyobb
Kérj be három egész számot, és írd ki, melyik a legnagyobb.

"""

first_num = int(input("Írj be az első számot!"))
second_num = int(input("Írj be a második számot!"))
third_num = int(input("Írj be a harmadik számot!"))

if first_num > second_num and first_num > third_num:
    print(f"Biggest number is: {first_num}")
elif second_num > first_num and second_num > third_num:
    print(f"Biggest number is: {second_num}")
else:
    print(f"Biggest number is: {third_num}")