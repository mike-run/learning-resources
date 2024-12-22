# This program prompts the user for an arithmetic expression and then 
# calculates and outputs the result as a floating-point value
# formatted to one decimal place

x, y, z = input("Expression: ").split(" ")

if y == "+":
    expression = float(x) + float(z)
elif y == "-":
    expression = float(x) - float(z)
elif y == "*":
    expression = float(x) * float(z)
elif y == "/":
    expression = float(x) / float(z)
else:
    expression = "Please enter a valid expression"

print(f"{expression:.1f}")