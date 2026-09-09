import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d = b**2 - 4*a*c

if d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)

    print("Roots are real and different")
    print("Root 1 =", root1)
    print("Root 2 =", root2)

elif d == 0:
    root = -b / (2*a)

    print("Roots are real and equal")
    print("Root 1 = Root 2 =", root)

else:
    real = -b / (2*a)
    imaginary = math.sqrt(-d) / (2*a)

    print("Roots are imaginary")
    print("Root 1 =", real, "+", imaginary, "i")
    print("Root 2 =", real, "-", imaginary, "i")
