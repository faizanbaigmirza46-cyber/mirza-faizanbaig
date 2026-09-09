a=int(input("enter first side"))
b=int(input("enter second side"))
c=int(input("enter third side"))
if a+b>c and b+c>a and a+c>b:
    print("valid triangle")
else:
    print("invalid triangle")