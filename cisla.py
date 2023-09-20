import random

c = 0
typ= input("Chcete-li jrát proti počítači, napište 1. Pokud chcete hrát ve dvou, napište 2)")
if typ = 1:
    print("Zvolili jste hru proti počítači")
    x = input ("V jakém rozsahu chcete hádat? Vložte nejprve dolní hranici ")
    y = input("Vložte horní hranici ")
    pokus = int(input("Vložte počet pokusů, který chcete mít:"))
    a = (random.randrange(int(x), int(y)))
    while c == 0:
        b = int(input ("Hádejte číslo mezi " + x + " a "+ y+" "))
        if a == b :
            print ("správně, hledané číslo bylo", a)
            c = 1
        else:
            print("Špatně zkuste znovu")
else:
    z = input("Vložte myšlené číslo: ")

    
