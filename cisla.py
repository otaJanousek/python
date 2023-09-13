import random

c = 0
x = input ("V jakém rozsahu chcete hádat? Vložte nejprve dolní hranici ")
y = input("Vložte horní hranici ")
a = (random.randrange(int(x), int(y)))
while c == 0:
    b = input ("Hádejte číslo mezi " + x + " a "+ y+" ")
    if a == b:
        print ("správně, hledané číslo bylo"+ a)
        c = 1
    else:
        print("kreténe")
