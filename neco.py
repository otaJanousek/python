a, b, c = 1, 2, -3
#a = int(input(Zadejte a:)
b = int(input(Zadejte b:)
c = int(input(Zadejte c:) #

D = (pow(b, 2) - 4 * a * c)
if D == 0:
    print("1:", -b / (2 * a))
elif D > 0:
    print("1: ", (-b + (pow (D, 0,5))) / (2 * a),
          "2: ", (-b - (pow(D, 0,5))) / (2 * a))
else:
    print("Rovnice nemá kořen")
