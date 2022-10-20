import cmath
a = int(input("Valor de A: "))
b = int(input("Valor de B: "))
c = int(input("Valor de C: "))

delta = b**2-4*a*c

if delta > 0:
    r1 = (-b + delta**0.5)/(a*2)
    r2 = (-b - delta**0.5)/(a*2)
    print("Xn = C1( " + str(r1) + " )^n C2( " + str(r2) + " )^n")
elif delta == 0:
    r1 = (-b + 0)/(a*2)
    print("Xn = C1( " + str(r1) + " )^n C2 n( " + str(r1) + " )^n" )
elif delta < 0: 
    print("Xn = C1 * (" + str(-b) + " +i√" + str(-1*delta) + " / " + str(2*a) + " )^n " + " + C2 * (" + str(-b) + " -i√" + str(-1*delta) + " / " + str(2*a) + ")^n")




