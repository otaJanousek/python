import random

z = 0
while z ==0:
    x = input ("V jakém rozsahu chcete hádat? Vložte nejprve dolní hranici ")
    y = input("Vložte horní hranici ")
    if int(x) < int(y):
        z = 1
    else:
        print("Dolní hranice musí být menší než horní hranice, zopakujte proces")
a = random.randrange( int(x), int(y))
while z == 1:
    b = input ("Hádejte číslo mezi " +  x +  " a "  + y +  " ")
    if int(x) <= int(b) <= int(y):
        if a == int(b):
            print ("Správně, hledané číslo bylo", a, "a hra končí")
            z = 2
        else:
            print("Špatně, zkuste znovu")
    else:
        print("Vámi hádané číslo nebylo v zadaném rozsahu, zopakujte proces")