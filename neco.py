
a = int(input("Zadejte a:"))
b = int(input("Zadejte b:"))
c = int(input("Zadejte c:"))

print("Řeším rovnici: ",a,"x2 *",b,"x *",c)
if a != 0:
    D = (pow(b, 2) - 4 * a * c)
    print(D)
    if D == 0:
        x = (-b / (2 * a))
        print("1:", x )

    elif D > 0:
        x1 = (-b + (pow (D, 0,5))) / (2 * a)
        x2 = (-b - (pow(D, 0,5))) / (2 * a)
        print("1: ", x1,
              "2: ", x2)
    else:
        print("Rovnice nemá kořen")
elif a == 0:
    print("1: ", (-b/c))
#nefunguje to :(
