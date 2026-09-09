def product_digits(n):
    if n < 10:
        return n
    return (n % 10) * product_digits(n // 10)

n = int(input("Enter a number: "))

n = abs(n)

print("Product of digits =", product_digits(n))
