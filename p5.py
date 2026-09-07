num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("The number is divisible by both 3 and 5")

elif num % 3 == 0:
    print("The number is divisible by 3")

elif num % 5 == 0:
    print("The number is divisible by 5")

else:
    print("The number is divisible by neither 3 nor 5")