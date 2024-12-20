# Ask user for their name
# Remove whitespace from input and use title case
name = input("What's your name? ").strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")

# Say hello to user
#print("Hello, " + name + "!")

#print("hello, ", name, "!", sep="")

#print("Hello, ", end="")
#print(name, "!", sep="")

#print(f"Hello, {name}!")

print(f"Hello, {first}!")