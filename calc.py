a = float(input("Enter no1:"))
b = float(input("Enter no2:"))
op = input("Enter operator (+, -, *, /):")

if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    result = a / b

print(result)
