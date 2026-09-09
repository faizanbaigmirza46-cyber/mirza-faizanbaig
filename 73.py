count = 0
sum = 0

while True:
    n = int(input("Enter a number (-1 to stop): "))

    if n == -1:
        break

    sum = sum + n
    count = count + 1

if count > 0:
    average = sum / count
    print("Count =", count)
    print("Average =", average)
else:
    print("No numbers entered")
