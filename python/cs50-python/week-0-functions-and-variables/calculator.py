# Allows user to perform various mathematical operations by inputting two ints
# and/or floats and get back the result as an int

# You can nest functions (Python looks at the innermost function first and
# passes that return value to the next outermost function) 


# Add 
# x = float(input("What's x? "))
# y = float(input("What's y? "))

# z = round(x + y)

# print(f"{z:,}")


# Divide
x = float(input("What's x? "))
y = float(input("What's y? "))

# The two print statements below result in things being rounded to 2 decimal
# places
# z = round(x / y, 2)
# print(z)

z = x / y
print(f"{z:.2f}")