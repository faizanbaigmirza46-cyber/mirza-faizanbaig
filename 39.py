hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

if hours > 40:
    overtime = hours - 40
    salary = (40 * rate) + (overtime * rate * 1.5)
else:
    salary = hours * rate

print("Salary =", salary)
