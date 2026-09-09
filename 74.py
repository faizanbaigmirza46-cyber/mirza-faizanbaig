x = float(input("Enter x: "))
n = int(input("Enter number of terms: "))

sum = 0
factorial = 1
power = 1

for i in range(n):
    # Calculate factorial of (2i + 1)
    factorial = 1

    for j in range(1, power + 1):
        factorial = factorial * j

    term = (x ** power) / factorial

    if i % 2 == 0:
        sum = sum + term
    else:
        sum = sum - term

    power = power + 2

print("Sum =", sum)
