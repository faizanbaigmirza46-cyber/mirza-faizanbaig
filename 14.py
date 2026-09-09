n = int(input("Enter number: "))
k = int(input("Enter bit position k: "))

if n & (1 << k):
    print("Kth bit is SET")
else:
    print("Kth bit is NOT SET")
